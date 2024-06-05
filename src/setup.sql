USE ROLE ACCOUNTADMIN;

CREATE OR REPLACE WAREHOUSE DASH_D4B_WH;
CREATE OR REPLACE DATABASE DASH_D4B_DB;
CREATE OR REPLACE SCHEMA DASH_D4B_SCHEMA;

USE DATABASE DASH_D4B_DB;
USE SCHEMA DASH_D4B_SCHEMA;

-- Create tables and load data

-- Table STREAMING_CALLS_RAW
create or replace TABLE DASH_D4B_DB.DASH_D4B_SCHEMA.STREAMING_CALLS_RAW (
	RECORD_METADATA VARIANT COMMENT 'created by automatic table creation from Snowflake Kafka Connector',
	CUSTOMER_ID NUMBER(38,0) COMMENT 'column created by schema evolution from Snowflake Kafka Connector',
	CALL_DURATION NUMBER(38,0) COMMENT 'column created by schema evolution from Snowflake Kafka Connector',
	CALL_ID NUMBER(38,0) COMMENT 'column created by schema evolution from Snowflake Kafka Connector',
	SENTIMENT FLOAT COMMENT 'column created by schema evolution from Snowflake Kafka Connector'
);

-- Load data using Snowsight from streaming_calls_raw.csv
---- Header: Skip first line
---- Field optionally enclosed by: Double quotes

-- Table CALL_TRANSCRIPTS
create or replace TABLE DASH_D4B_DB.DASH_D4B_SCHEMA.CALL_TRANSCRIPTS (
	DATE_CREATED DATE,
	LANGUAGE VARCHAR(60),
	COUNTRY VARCHAR(60),
	PRODUCT VARCHAR(60),
	CATEGORY VARCHAR(60),
	DAMAGE_TYPE VARCHAR(90),
	TRANSCRIPT VARCHAR(16777216)
);

-- Load data using Snowsight from call_transcripts.csv
---- Header: Skip first line
---- Field optionally enclosed by: Double quotes

-- Table CUSTOMER_LTV
create or replace TABLE DASH_D4B_DB.DASH_D4B_SCHEMA.CUSTOMER_LTV (
	CUSTOMER_ID NUMBER(38,0),
	NUM_MONTHS_AS_CUSTOMER NUMBER(38,0),
	LTV FLOAT,
	WEEKS_SINCE_LAST_PURCHASE NUMBER(38,0)
);

-- Load data using Snowsight from customer_ltv.csv
---- Header: Skip first line

-- Table DAILY_CALL_VOLUME
create or replace TABLE DASH_D4B_DB.DASH_D4B_SCHEMA.DAILY_CALL_VOLUME (
	DATE TIMESTAMP_NTZ,
	TOTAL_CALLS NUMBER(38,0)
);

-- Load data using Snowsight from daily_call_column.csv
---- Header: Skip first line

-- Train Forecast Model d4b_model
/*create or replace SNOWFLAKE.ML.FORECAST d4b_model(
  INPUT_DATA => SYSTEM$REFERENCE('TABLE', 'DAILY_CALL_VOLUME'),
  TIMESTAMP_COLNAME => 'date',
  TARGET_COLNAME => 'total_calls'
);*/
