USE ROLE ACCOUNTADMIN;
USE DATABASE DASH_D4B_DB;
USE SCHEMA DASH_D4B_SCHEMA;

-- Let's preview the data
SELECT * from STREAMING_CALLS_RAW LIMIT 10;

-- Join the streaming data with Customer Lifetime Value static table
SELECT 
    a.customer_id as "Customer ID",
    a.sentiment as "Call Sentiment Score",
    b.num_months_as_customer as "Months As Customer",
    to_varchar(b.ltv,'$99,99,999.00') as "Lifetime Value"
FROM STREAMING_CALLS_RAW a 
INNER JOIN CUSTOMER_LTV b ON a.CUSTOMER_ID = b.CUSTOMER_ID
QUALIFY RANK() OVER(PARTITION BY a.customer_id ORDER BY a.RECORD_METADATA:CreateTime DESC) = 1
ORDER BY a.RECORD_METADATA:CreateTime;

-- Create the Dynamic Table using the same logic/SQL for incremental refreshes
CREATE or REPLACE DYNAMIC TABLE CUSTOMER_LATEST_CALL_SUMMARY
LAG = '1  minute'
WAREHOUSE = DASH_D4B_WH
AS
SELECT 
    a.customer_id as "Customer ID",
    a.sentiment as "Call Sentiment Score",
    b.num_months_as_customer as "Months As Customer",
    to_varchar(b.ltv,'$99,99,999.00') as "Lifetime Value",
    dateadd(MS, a.RECORD_METADATA:CreateTime, '1970-01-01') as "Call Date"
FROM STREAMING_CALLS_RAW a 
INNER JOIN CUSTOMER_LTV b ON a.CUSTOMER_ID = b.CUSTOMER_ID
QUALIFY RANK() OVER(PARTITION BY a.customer_id ORDER BY a.RECORD_METADATA:CreateTime DESC) = 1;

-- -- Preview DT data 
SELECT "Customer ID","Call Sentiment Score","Months As Customer","Lifetime Value" from CUSTOMER_LATEST_CALL_SUMMARY;
