# Databricks notebook source
# DBTITLE 1,Install openai
# MAGIC %pip install openai

# COMMAND ----------

# DBTITLE 1,programmatic way to ask query
from openai import OpenAI
import os

# How to get your Databricks token: https://docs.databricks.com/en/dev-tools/auth/pat.html
# DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')
# Alternatively in a Databricks notebook you can use this:
DATABRICKS_TOKEN = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()

client = OpenAI(
    api_key=DATABRICKS_TOKEN,
    base_url="https://dbc-631ed380-0cf3.cloud.databricks.com/ai-gateway/mlflow/v1"
)

response = client.chat.completions.create(
    model="system.ai.gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Why AI?"
        }
    ],
    max_tokens=5000
)

print(response.choices[0].message.content)

# COMMAND ----------

# DBTITLE 1,output is array of json
#All LLMs are desgined to output as markdown language.

print(response.choices[0].message.content[1].get("text"))

# COMMAND ----------

# DBTITLE 1,view the text
# copied markdown frm previous cell in text

# COMMAND ----------

# MAGIC %md
# MAGIC ### Output
# MAGIC In a nutshell: Why we build and use AI
# MAGIC
# MAGIC | **Goal** | **How AI helps** | **Typical examples** |
# MAGIC |----------|------------------|----------------------|
# MAGIC | **Automate repetitive work** | Learns patterns and executes tasks faster and without fatigue | Data entry bots, invoice processing, factory line quality‑inspection |
# MAGIC | **Extract insight from massive data** | Finds correlations, trends, and anomalies that humans would miss | Fraud detection, genomics research, recommendation engines |
# MAGIC | **Scale expertise** | Packs “expert knowledge” into a model that can be accessed by anyone, anywhere | Medical‑diagnosis assistants, legal‑research tools, language translators |
# MAGIC | **Augment human decision‑making** | Provides predictions, simulations, or “second opinions” while keeping the human in control | Financial‑risk scoring, climate‑model forecasting, medical‑image triage |
# MAGIC | **Enable new products and services** | Makes possible experiences that didn’t exist before | Voice assistants, self‑driving cars, AI‑generated art or code |
# MAGIC | **Reduce cost and time** | Cuts labor, speeds up R&D cycles, and optimizes resource allocation | Supply‑chain optimization, drug‑discovery pipelines, predictive maintenance |

# COMMAND ----------

# DBTITLE 1,Interacting with model using sql
# MAGIC %sql
# MAGIC
# MAGIC -- function: ai_query
# MAGIC -- 2 parameters: model name, user question
# MAGIC
# MAGIC select ai_query("system.ai.gpt-oss-120b","why AI" )