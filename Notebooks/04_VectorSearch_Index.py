# Databricks notebook source
# MAGIC %sql
# MAGIC /*
# MAGIC This code queries a Databricks Vector Search index to find the three most relevant documents for the question: “Where can I find Accountease Pro Documentation?”
# MAGIC
# MAGIC --->This code implements the retrieval step (R) in RAG — Retrieval-Augmented Generation. It retrieves relevant documentation from a Vector Search index. An LLM can then use the retrieved documents to generate a grounded answer for the user.
# MAGIC
# MAGIC */

# COMMAND ----------

# WorkspaceClient: Connects to your Databricks workspace.
# vectorsearch: Provides Vector Search configuration classes, including reranker settings.
from databricks.sdk import WorkspaceClient
from databricks.sdk.service import vectorsearch

# Creates a workspace client using the available Databricks authentication configuration.
w = WorkspaceClient()

#index_name: Specifies the Vector Search index containing your product documentation.
# columns: Returns the document text (indexed_doc) and its product ID (product_id).
# query_text: The user's natural-language question.
# query_type="HYBRID": Combines semantic vector search with keyword-based search to find relevant documents.#num_results=3: Retrieves the top three matching results.

results = w.vector_search_indexes.query_index(
    index_name="agentic_catalog.agentic_schema.product_docs_index",
    columns=["indexed_doc", "product_id"],
    query_text="where can I find Accountease Pro Documentation",
    query_type="HYBRID",
    num_results=3,
    # Reranker requires workspace admin to enable access to the reranker model.
    # Uncomment the following once access is granted:
    # reranker=vectorsearch.RerankerConfig(
    #     model="databricks_reranker",
    #     parameters=vectorsearch.RerankerConfigRerankerParameters(
    #         columns_to_rerank=["indexed_doc"]
    #     )
    # )
)
#Loops through the search results and prints each matching document record.
for doc in results.result.data_array:
    print(doc)