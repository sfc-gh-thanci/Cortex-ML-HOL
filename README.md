# Topdanmark on-site Snowflake day - Cortex Demo (HOL)

## Overview

This repo is created to provide what you need to run the updated version of the demo which has been presented in Data for Breakfast event. In the event we have demostrated the solution and we haven't run the setup. But for this Hands on Lab, we will also spend time together to setup the demo environment where we will tocuh the ML functions.
## Prerequisites

You must have access to a Snowflake account where Snowflake Cortex ([check availability regions](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions#label-cortex-llm-availability)) and Snowflake Notebooks are enabled. 


## General Setup

- Run SQL statements in [setup.sql](src/setup.sql) to create various objects (including db, schema, warehouse, tables, etc.) and load data using Snowsight using the provided .csv files (see setup.sql for details).

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

