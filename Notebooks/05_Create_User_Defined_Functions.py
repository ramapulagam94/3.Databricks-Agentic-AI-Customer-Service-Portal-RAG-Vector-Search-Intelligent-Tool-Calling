# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# MAGIC %sql
# MAGIC /*
# MAGIC Unity Catalog knows that it is a function because of the CREATE OR REPLACE FUNCTION statement in your SQL code.
# MAGIC --you can find functions under catalog-->scehma-->functions
# MAGIC
# MAGIC The fully qualified function name is:
# MAGIC 1. agentic_catalog.agentic_schema.get_return_policy
# MAGIC
# MAGIC Unity Catalog doesn't identify the function by guessing from the code. The CREATE FUNCTION statement explicitly instructs Databricks to create and register a function object, and its metadata records that object as a function.
# MAGIC */

# COMMAND ----------

# DBTITLE 1,Unity Catalog SQL table-valued function
spark.sql(f"""
-- Create a function to retrieve company policy details
CREATE OR REPLACE FUNCTION agentic_catalog.agentic_schema.get_return_policy(
    policy_name STRING COMMENT 'Policy name to return. Example policies: Account Cancellation Policy, Exchange Policy, Refund Policy, Warranty Policy, Privacy Policy, Return Policy'
    )

    --defines the return structure, Unlike a scalar function that returns a single value, this function returns a table-shaped result.
    RETURNS TABLE (
    policy           STRING,
    policy_details   STRING,
    last_updated     DATE
    )

    --Stores a description of the function in its metadata so users can understand its purpose.
    COMMENT 'Returns the details of the Return Policy'

    --specify language
    LANGUAGE SQL

    --Define the query
    RETURN (
    SELECT
    policy,
    policy_details,
    last_updated
    FROM agentic_catalog.agentic_schema.policies
    WHERE policy = policy_name
    LIMIT 1
    );
    """)
####################################################################################

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from agentic_catalog.agentic_schema.policies

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from agentic_catalog.agentic_schema.get_return_policy("Return Policy")

# COMMAND ----------

# MAGIC %sql
# MAGIC /*
# MAGIC This code creates a Unity Catalog SQL table-valued function that retrieves a customer's service and return history using their email address.
# MAGIC
# MAGIC Unity Catalog SQL table-valued function that accepts a customer email, filters service records for that customer, groups them by issue category, and returns the record count and current date. The function makes the service-history logic reusable for customer-support applications and AI agents.”
# MAGIC */

# COMMAND ----------

####################################################################################
# Create two functions we will use later in the course
spark.sql(f"""
-- Create a function to get service history by user
CREATE OR REPLACE FUNCTION agentic_catalog.agentic_schema.get_service_history(
    user_email STRING COMMENT 'User email to retrieve order history'
    )
    
    RETURNS TABLE (
    returns_last_12_months INT,
    issue_category STRING, 
    todays_date DATE
    )

    COMMENT 'This takes the user_name of a customer as an input and returns the number of returns and the issue category'

    LANGUAGE SQL

    RETURN(
    SELECT count(*) as returns_last_12_months, issue_category, now() as todays_date
    FROM agentic_catalog.agentic_schema.cust_service_data 
    WHERE email = user_email
    GROUP BY issue_category
    );""")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from agentic_catalog.agentic_schema.cust_service_data 

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from agentic_catalog.agentic_schema.get_service_history("nicolas.pelaez@example.com")