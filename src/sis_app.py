import streamlit as st
import altair as alt
import pandas as pd
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

st.set_page_config(layout='wide')
session = get_active_session()

supported_languages = {'German':'de','French':'fr','Korean':'ko','Portuguese':'pt','English':'en','Italian':'it','Russian':'ru','Swedish':'sv','Spanish':'es','Japanese':'ja','Polish':'pl'}

@st.cache_data()
def load_historic_daily_calls():
    df_historic_daily_calls = session.table('DAILY_CALL_VOLUME').with_column_renamed('TOTAL_CALLS','HISTORIC_VALUE').to_pandas()
    return df_historic_daily_calls
    
def forecast():
    # Load total calls from the past
    df_historic_daily_calls = load_historic_daily_calls()
    with st.container():
        st.header("Forecast Call Volume With Snowflake Cortex")
        forecasting_period = st.slider(label='Select Forecast Period (in days)', min_value=7, max_value=60, value=14, step=7)
        st.caption(f"Forecast Call Volume for {forecasting_period} days")

        # Generate forecast values based on the user selected period
        df_forecast = session.sql(f"call d4b_model!FORECAST(FORECASTING_PERIODS => {forecasting_period})").collect()
        df_forecast = pd.DataFrame(df_forecast)

        # Merge actuals and forecast dataframes so we get FORECAST,LOWER_BOUND,UPPER_BOUND,HISTORIC_VALUE values for each day
        df = pd.merge(df_forecast,df_historic_daily_calls,left_on=df_forecast['TS'].apply(lambda x: (x.month, x.day)),
         right_on=df_historic_daily_calls['DATE'].apply(lambda y: (y.month, y.day)),
         how='outer')[['TS','FORECAST','LOWER_BOUND','UPPER_BOUND','HISTORIC_VALUE']]
        df = df[~df['TS'].isnull()]

        # Unpivot our dataframe from wide to long format so it works better with altair
        df = pd.DataFrame(df).melt('TS', var_name='Value Type', value_name='Number of Calls')
        
        line_chart = (
            alt.Chart(
                data=df
            )
            .mark_line(point=True)
            .encode(
                x=alt.X("TS:T",axis=alt.Axis(title="Date")),
                y=alt.Y("Number of Calls:Q"),
                color=alt.Color('Value Type')
            )
        )
        st.altair_chart(line_chart,use_container_width=True)

def translate():
    with st.container():
        st.header("Translate With Snowflake Cortex")
        col1,col2 = st.columns(2)
        with col1:
            from_language = st.selectbox('From',dict(sorted(supported_languages.items())))
        with col2:
            to_language = st.selectbox('To',dict(sorted(supported_languages.items())))
        entered_text = st.text_area("Enter text",label_visibility="hidden",height=300,placeholder='For example: call transcript')
        if entered_text:
          entered_text = entered_text.replace("'", "\\'")
          cortex_response = session.sql(f"select snowflake.cortex.translate('{entered_text}','{supported_languages[from_language]}','{supported_languages[to_language]}') as response").to_pandas().iloc[0]['RESPONSE']
          st.write(cortex_response)

def sentiment():
    with st.container():
        st.header("Sentiment Analysis With Snowflake Cortex")
        # Sample transcript
        # Customer: Hello! Agent: Hello! I hope you're having a great day. To best assist you, can you please share your first and last name and the company you're calling from? Customer: Sure, I'm Michael Green from SnowSolutions. Agent: Thanks, Michael! What can I help you with today? Customer: We recently ordered several DryProof670 jackets for our store, but when we opened the package, we noticed that half of the jackets have broken zippers. We need to replace them quickly to ensure we have sufficient stock for our customers. Our order number is 60877. Agent: I apologize for the inconvenience, Michael. Let me look into your order. It might take me a moment. Customer: Thank you. Agent: Michael, I've confirmed your order and the damage. Fortunately, we currently have enough stock to replace the damaged jackets. We'll send out the replacement jackets immediately, and they should arrive within 3-5 business days. Customer: That's great to hear! How should we handle returning the damaged jackets? Agent: We will provide you with a return shipping label so that you can send the damaged jackets back to us at no cost to you. Please place the jackets in the original packaging or a similar box. Customer: Sounds good! Thanks for your help. Agent: You're welcome, Michael! We apologize for the inconvenience, and thank you for your patience. Please don't hesitate to contact us if you have any further questions or concerns. Have a great day! Customer: Thank you! You too.
        entered_transcript = st.text_area("Enter call transcript",label_visibility="hidden",height=400,placeholder='Enter call transcript')
        entered_transcript = entered_transcript.replace("'", "\\'")
        if entered_transcript:
          cortex_response = session.sql(f"select snowflake.cortex.sentiment('{entered_transcript}') as sentiment").to_pandas()
          st.caption("Score is between -1 and 1; -1 = Most negative, 1 = Positive, 0 = Neutral")  
          st.write(cortex_response)

def latest_call_summary():
    with st.container():
        st.header("Latest Call Summary From Dynamic Table")
        df_latest_call_summary = session.table('CUSTOMER_LATEST_CALL_SUMMARY').sort(col("Call Date")).select("Customer ID","Call Sentiment Score","Months As Customer","Lifetime Value")
        df_call_sentiments_sql = 'SELECT count(*) as "Total Calls", case when "Call Sentiment Score" = 1 then \'Positive\' when "Call Sentiment Score" = -1 then \'Most Negative\' when "Call Sentiment Score" = 0 then \'Neutral\' end as "Sentiment" from CUSTOMER_LATEST_CALL_SUMMARY where "Call Sentiment Score" in (-1,0,1) group by "Sentiment"'
        df_call_sentiments = session.sql(df_call_sentiments_sql).collect()
    
        df_latest_call_summary = df_latest_call_summary.to_pandas()
        df_latest_call_summary['Customer ID'] = df_latest_call_summary['Customer ID'].apply(str)
        st.dataframe(df_latest_call_summary,use_container_width=True)

        st.subheader("Aggregated Call Sentiments")
        st.bar_chart(df_call_sentiments, x="Sentiment", y="Total Calls",use_container_width=True)
    
page_names_to_funcs = {
    "Sentiment Analysis": sentiment,
    "Latest Call Summary": latest_call_summary,
    "Forecast Call Volume": forecast,
    "Translate Call Summary": translate
}

selected_page = st.sidebar.selectbox("Select", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
