  # Topdanmark on-site Snowflake day - Cortex Demo (HOL)

## Overview

This repo is created to provide what you need to run the updated version of the demo which has been presented in Data for Breakfast event. In the event we have demostrated the solution and we haven't run the setup. But for this Hands on Lab, we will also spend time together to setup the demo environment where we will tocuh the ML functions.
## Prerequisites

You must have access to a Snowflake account where Snowflake Cortex ([check available regions](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions#label-cortex-llm-availability)) and Snowflake Notebooks are enabled. We will use AWS Frankfurt region for this HOL, since the LLM functions we will be using are available in this region. Supposing that you have created a Trial account for AWS Frankfurt region, otherwise please create one via this [link](https://signup.snowflake.com/?utm_source=google&utm_medium=paidsearch&utm_campaign=em-dk-en-brand-trial-exact&utm_content=go-eta-evg-ss-free-trial&utm_term=c-g-snowflake%20trial-e&_bt=562156038952&_bk=snowflake%20trial&_bm=e&_bn=g&_bg=129534974844&gclsrc=aw.ds&gad_source=1&gclid=CjwKCAjwmYCzBhA6EiwAxFwfgCw9J9bW_ANxN7hSrOJeiF-sO7tFdSMyDKRrpNGWS6R9KLnfeJrvkBoC-tcQAvD_BwE).


## General Setup

- Create a new worksheet in Snowsight and copy SQL statements in [setup.sql](src/setup.sql) into the worksheet and run it to create various objects (including db, schema, warehouse, tables, etc.).
- Download data in .csv files from [here](https://github.com/sfc-gh-thanci/test/tree/main/data) and load data using Snowsight (see setup.sql for details).
**!!!DO NOT RUN last step (Train Forecast Model d4b_model) before loading data to the tables!!!**

- Using snowsigt load data to each of the tables by using the below options. (Snowsight leftpane menu -> Data -> Database -> DASH_D4B_DB -> DASH_D4B_SCHEMA -> TABLES -> Top right corner "Load" -> Browse -> Choose the related file)
Header: Skip first line
Field optionally enclosed by: Double quotes

<p align="center">
  <img src="assets/Load_Data.png" width=75% height=75% />
</p>

## Model Training
- **Option 1:** Create and train the model using Cortex ML Functions.

          Step 1
    create or replace SNOWFLAKE.ML.FORECAST d4b_model(
      INPUT_DATA => SYSTEM$REFERENCE('TABLE', 'DAILY_CALL_VOLUME'),
      TIMESTAMP_COLNAME => 'date',
      TARGET_COLNAME => 'total_calls'
    );

- **Option 2:** Use no-code UI Snowflake AI&ML Studio to create and train the model . Follow the screenshots.


Step 1:
<p align="center">
  <img src="assets/Studio_1.png" width=75% height=75% />
</p>
Step 2:
<p align="center">
  <img src="assets/Studio_2.png" width=75% height=75% />
</p>
Step 3:
<p align="center">
  <img src="assets/Studio_3.png" width=75% height=75% />
</p>
Step 4:
<p align="center">
  <img src="assets/Studio_4.png" width=75% height=75% />
</p>
Step 5:
<p align="center">
  <img src="assets/Studio_6.png" width=75% height=75% />
</p>
Step 6:
<p align="center">
  <img src="assets/Studio_7.png" width=75% height=75% />
</p>
Step 7:
<p align="center">
  <img src="assets/Studio_8.png" width=75% height=75% />
</p>
Step 8:
<p align="center">
  <img src="assets/Studio_9.png" width=75% height=75% />
</p>



- If your version of Snowflake Notebooks supports **Import .ipynb** feature, then import [snowflake_cortex.ipynb](src/snowflake_cortex.ipynb). Otherwise, copy-paste SQL cell code snippets from [snowflake_cortex.txt](src/snowflake_cortex.txt) into your Snowflake Notebook. ***IMPORTANT***: Create your notebook in the following location CORTEX_DEMO_DB > CORTEX_DEMO_SCHEMA

- Create Streamlit application in your Snowflake account using the code provided in [sis_app.py](src/sis_app.py).

## Demos

The demo section of the D4B is broken down into three parts.

### Demo 1: Snowflake Cortex

Open [Snowflake Coxtex Notebook](src/snowflake_cortex.ipynb) and follow the demo script to perform the live demo.

![Demo1](assets/demo1.1.png)

![Demo1](assets/demo1.2.png)

### Demo 2: Dynamic Tables

Open [dynamic_table_demo.sql](src/dynamic_table_demo.sql) SQL Worksheet and follow the demo script to perform the live demo.

![Demo2.1](assets/demo2.1.png)

![Demo2.2](assets/demo2.2.png)

### Demo 3: Streamlit in Snowflake (SiS) Application

Open [Streamlit](src/sis_app.py) app follow the demo script to perform the live demo for **Sentiment Analysis, Latest Call Summary, and Forecast Call Volume**.

#### 1. Sentiment Analysis

Copy-paste this sample call transcript. If you're on Mac, you can also create a "shortcut" via text replacement. For example, when you type "s1" in the text area it can replace it with the transcript -- here's how System Setting >> Keyboard >> Text Input >> Text Replacements.

```bash
Customer: Hello!
Agent: Hello! I hope you're having a great day. To best assist you, can you please share your first and last name and the company you're calling from?
Customer: Sure, I'm Michael Green from SnowSolutions.
Agent: Thanks, Michael! What can I help you with today?
Customer: We recently ordered several DryProof670 jackets for our store, but when we opened the package, we noticed that half of the jackets have broken zippers. We need to replace them quickly to ensure we have sufficient stock for our customers. Our order number is 60877.
Agent: I apologize for the inconvenience, Michael. Let me look into your order. It might take me a moment.
Customer: Thank you.
Agent: Michael, I've confirmed your order and the damage. Fortunately, we currently have enough stock to replace the damaged jackets. We'll send out the replacement jackets immediately, and they should arrive within 3-5 business days.
Customer: That's great to hear! How should we handle returning the damaged jackets?
Agent: We will provide you with a return shipping label so that you can send the damaged jackets back to us at no cost to you. Please place the jackets in the original packaging or a similar box.
Customer: Sounds good! Thanks for your help.
Agent: You're welcome, Michael! We apologize for the inconvenience, and thank you for your patience. Please don't hesitate to contact us if you have any further questions or concerns. Have a great day!
Customer: Thank you! You too. 
```

![Demo3.1](assets/demo3.1.png)

#### 2. Latest Call Summary

![Demo3.2](assets/demo3.2.png)

#### 3. Forecast Call Volume


![Demo3.3](assets/demo3.3.png)

## Cleanup

After your demo delete the dynamic table by executing `DROP DYNAMIC TABLE CUSTOMER_LATEST_CALL_SUMMARY;`

