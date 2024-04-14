# Data For Breakfast (D4B) 2024 Keynote Demo

## Overview

This repo contains everything you need to know about the [Data For Breakfast](https://www.snowflake.com/events/data-for-breakfast/) keynote demo.

## Prerequisites

You must have access to a Snowflake account where Snowflake Cortex ([check availability regions](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions#label-cortex-llm-availability)) and Snowflake Notebooks are enabled. To learn more, check pinned message(s) in ***#feat-cortex-llm*** and ***#notebooks*** Slack channels.

***IMPORTANT***: Please go through setup instructions outlined in **General Setup** section below <ins>at least a couple of days before you are scheduled to perform the live demo</ins>. This will help you prepare and get ready ahead of time. And after your practice / dry runs, remember to delete the dynamic table by executing `DROP DYNAMIC TABLE CUSTOMER_LATEST_CALL_SUMMARY;` so that the refresh history looks cleaner during the live demo.

If you have any questions, please reach out to [Dash](dash.desai@snowflake.com) and also checkout ***#d4b-presenters-fy25*** channel.

## General Setup

- Run SQL statements in [setup.sql](src/setup.sql) to create various objects (including db, schema, warehouse, tables, etc.) and load data using Snowsight using the provided .csv files (see setup.sql for details).

- If your version of Snowflake Notebooks supports **Import .ipynb** feature, then import [snowflake_cortex.ipynb](src/snowflake_cortex.ipynb). Otherwise, copy-paste SQL cell code snippets from [snowflake_cortex.txt](src/snowflake_cortex.txt) into your Snowflake Notebook. ***IMPORTANT***: Create your notebook in the following location DASH_D4B_DB > DASH_D4B_SCHEMA

- Create Streamlit application in your Snowflake account using the code provided in [sis_app.py](src/sis_app.py).

## Demos

The demo section of the D4B is broken down into three parts and the demo talking points/script can be [found here](https://docs.google.com/document/d/1OvWqKP2IaxAYBOWbKEOCwQ_t4vQSQ-Ra-8_0-7OWACA/edit). If you don't have access to the doc or if you have questions related to the script, please reach out to [Suha Saya](suha.saya@snowflake.com).

***IMPORTANT***: Before you start demo'ing, make sure you have all demo parts open in different browser tabs for faster transition.

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

Copy-paste this sample call transcript. If you're on Mac, you can also create a "shortcut" via text replacement. For example, when you type "s1" in the textarea it can replace it with the transcript -- here's how System Setting >> Keyboard >> Text Input >> Text Replacements.

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

***Common errors:***

> * If you get this error `Uncaught exception of type 'STATEMENT_ERROR' on line 7 at position 2 : No active warehouse selected in the current session. Select an active warehouse with the 'use warehouse' command.`, then execute this statement in your deployment `alter account XXXXXXX unset STREAMLIT_CHILD_JOB_WAREHOUSE_INVOCATION_RIGHTS;`.

> * If you get this error `KeyError: 'TS'`, then it means that you trained the forecast model without first loading the data in DASH_D4B_DB.DASH_D4B_SCHEMA.DAILY_CALL_VOLUME table. So go back to [setup.sql](src/setup.sql) and repeat the last couple of steps.


![Demo3.3](assets/demo3.3.png)

## Cleanup

After your practice / dry runs and live demo, delete the dynamic table by executing `DROP DYNAMIC TABLE CUSTOMER_LATEST_CALL_SUMMARY;`

## Questions

If you have any questions, please reach out to [Dash](dash.desai@snowflake.com) and also checkout ***#d4b-presenters-fy25*** channel.
