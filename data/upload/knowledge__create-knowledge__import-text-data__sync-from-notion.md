# Sync Data from Notion

Dify datasets support importing from Notion and setting up **synchronization** so that data updates in Notion are automatically synced to Dify.

> **Info**
>
> Notion is connected through Dify's pre-configured integration. Authorize your workspace once and you're ready to import; no Notion app setup required.

### Authorization Verification

1. When creating a dataset and selecting the data source, click **Sync from Notion Content -- Bind Now** and follow the prompts to complete the authorization verification.
2. Alternatively, you can go to **Settings -- Data Sources -- Add Data Source**, click on the Notion source **Bind**, and complete the authorization verification.

### Import Notion Data

After completing the authorization verification, go to the create dataset page, click **Sync from Notion Content**, and select the authorized pages you need to import.

### Chunking and Cleaning

Next, choose a [chunking mode](https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/chunking-and-cleaning-text) and [indexing method](https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/setting-indexing-methods) for your knowledge base, then save it and wait for the automatically processing. Dify not only supports importing standard Notion pages but can also consolidate and save page attributes from database-type pages.

> **Note**
>
> Images and files cannot be imported, and data from tables will be converted to text.

### Synchronize Notion Data

If your Notion content has been updated, you can sync the changes by clicking the **Sync** button for the corresponding page in the document list of your knowledge base. Syncing involves an embedding process, which will consume tokens from your embedding model.
