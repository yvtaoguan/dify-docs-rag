# Integrate with Opik

### What is Opik

Opik is an open-source platform designed for evaluating, testing, and monitoring large language model (LLM) applications. Developed by Comet, it aims to facilitate more intuitive collaboration, testing, and monitoring of LLM-based applications.

> **Info**
>
> For more details, please refer to [Opik](https://www.comet.com/site/products/opik/).

---

### How to Configure Opik

#### 1. Register/Login to [Opik](https://www.comet.com/signup?from=llm)

#### 2. Get your Opik API Key

Retrieve your Opik API Key from the user menu at the top-right. Click on **API Key**, then on the API Key to copy it:

#### 3. Integrate Opik with Dify

Configure Opik in the Dify application. Open the application you need to monitor, open **Monitoring** in the side menu, and select **Tracing app performance** on the page.

After clicking configure, paste the **API Key** and **project name** created in Opik into the configuration and save.

Once successfully saved, you can view the monitoring status on the current page.

### View Monitoring Data in Opik

Once configured, you can debug or use the Dify application as usual. All usage history can be monitored in Opik.

When you switch to Opik, you can view detailed operation logs of Dify applications in the dashboard.

Detailed LLM operation logs through Opik will help you optimize the performance of your Dify application.

### Monitoring Data List

#### **Workflow/Chatflow Trace Information**

**Used to track workflows and chatflows**

      Workflow
      Opik Trace

      workflow_app_log_id/workflow_run_id
      id

      user_session_id
      - placed in metadata

      {"workflow_{id}"}
      name

      start_time
      start_time

      end_time
      end_time

      inputs
      inputs

      outputs
      outputs

      Model token consumption
      usage_metadata

      metadata
      metadata

      error
      error

      \[workflow]
      tags

      "conversation_id/none for workflow"
      conversation_id in metadata

**Workflow Trace Info**

- workflow_id - Unique identifier of the workflow
- conversation_id - Conversation ID
- workflow_run_id - ID of the current run
- tenant_id - Tenant ID
- elapsed_time - Time taken for the current run
- status - Run status
- version - Workflow version
- total_tokens - Total tokens used in the current run
- file_list - List of processed files
- triggered_from - Source that triggered the current run
- workflow_run_inputs - Input data for the current run
- workflow_run_outputs - Output data for the current run
- error - Errors encountered during the current run
- query - Query used during the run
- workflow_app_log_id - Workflow application log ID
- message_id - Associated message ID
- start_time - Start time of the run
- end_time - End time of the run
- workflow node executions - Information about workflow node executions
- Metadata
  - workflow_id - Unique identifier of the workflow
  - conversation_id - Conversation ID
  - workflow_run_id - ID of the current run
  - tenant_id - Tenant ID
  - elapsed_time - Time taken for the current run
  - status - Run status
  - version - Workflow version
  - total_tokens - Total tokens used in the current run
  - file_list - List of processed files
  - triggered_from - Source that triggered the current run

#### **Message Trace Information**

**Used to track LLM-related conversations**

      Chat
      Opik LLM

      message_id
      id

      user_session_id
      - placed in metadata

      "llm"
      name

      start_time
      start_time

      end_time
      end_time

      inputs
      inputs

      outputs
      outputs

      Model token consumption
      usage_metadata

      metadata
      metadata

      \["message", conversation_mode]
      tags

      conversation_id
      conversation_id in metadata

**Message Trace Info**

- message_id - Message ID
- message_data - Message data
- user_session_id - User session ID
- conversation_model - Conversation mode
- message_tokens - Number of tokens in the message
- answer_tokens - Number of tokens in the answer
- total_tokens - Total number of tokens in the message and answer
- error - Error information
- inputs - Input data
- outputs - Output data
- file_list - List of processed files
- start_time - Start time
- end_time - End time
- message_file_data - File data associated with the message
- conversation_mode - Conversation mode
- Metadata
  - conversation_id - Conversation ID
  - ls_provider - Model provider
  - ls_model_name - Model ID
  - status - Message status
  - from_end_user_id - ID of the sending user
  - from_account_id - ID of the sending account
  - agent_based - Whether the message is agent-based
  - workflow_run_id - Workflow run ID
  - from_source - Message source

#### **Moderation Trace Information**

**Used to track conversation moderation**

      Moderation
      Opik Tool

      user_id
      - placed in metadata

      “moderation"
      name

      start_time
      start_time

      end_time
      end_time

      inputs
      inputs

      outputs
      outputs

      metadata
      metadata

      \["moderation"]
      tags

**Moderation Trace Info**

- message_id - Message ID
- user_id: User ID
- workflow_app_log_id - Workflow application log ID
- inputs - Moderation input data
- message_data - Message data
- flagged - Whether the content is flagged for attention
- action - Specific actions taken
- preset_response - Preset response
- start_time - Moderation start time
- end_time - Moderation end time
- Metadata
  - message_id - Message ID
  - action - Specific actions taken
  - preset_response - Preset response

#### **Suggested Question Trace Information**

**Used to track suggested questions**

      Suggested Question
      Opik LLM

      user_id
      - placed in metadata

      "suggested_question"
      name

      start_time
      start_time

      end_time
      end_time

      inputs
      inputs

      outputs
      outputs

      metadata
      metadata

      \["suggested_question"]
      tags

**Message Trace Info**

- message_id - Message ID
- message_data - Message data
- inputs - Input content
- outputs - Output content
- start_time - Start time
- end_time - End time
- total_tokens - Number of tokens
- status - Message status
- error - Error information
- from_account_id - ID of the sending account
- agent_based - Whether the message is agent-based
- from_source - Message source
- model_provider - Model provider
- model_id - Model ID
- suggested_question - Suggested question
- level - Status level
- status_message - Status message
- Metadata
  - message_id - Message ID
  - ls_provider - Model provider
  - ls_model_name - Model ID
  - status - Message status
  - from_end_user_id - ID of the sending user
  - from_account_id - ID of the sending account
  - workflow_run_id - Workflow run ID
  - from_source - Message source

#### **Dataset Retrieval Trace Information**

**Used to track knowledge base retrieval**

      Dataset Retrieval
      Opik Retriever

      user_id
      - placed in metadata

      "dataset_retrieval"
      name

      start_time
      start_time

      end_time
      end_time

      inputs
      inputs

      outputs
      outputs

      metadata
      metadata

      \["dataset_retrieval"]
      tags

      message_id
      parent_run_id

**Dataset Retrieval Trace Info**

- message_id - Message ID
- inputs - Input content
- documents - Document data
- start_time - Start time
- end_time - End time
- message_data - Message data
- Metadata
  - message_id - Message ID
  - ls_provider - Model provider
  - ls_model_name - Model ID
  - status - Message status
  - from_end_user_id - ID of the sending user
  - from_account_id - ID of the sending account
  - agent_based - Whether the message is agent-based
  - workflow_run_id - Workflow run ID
  - from_source - Message source

#### **Tool Trace Information**

**Used to track tool invocation**

      Tool
      Opik Tool

      user_id
      - placed in metadata

      tool_name
      name

      start_time
      start_time

      end_time
      end_time

      inputs
      inputs

      outputs
      outputs

      metadata
      metadata

      \["tool", tool_name]
      tags

#### **Tool Trace Info**

- message_id - Message ID
- tool_name - Tool name
- start_time - Start time
- end_time - End time
- tool_inputs - Tool inputs
- tool_outputs - Tool outputs
- message_data - Message data
- error - Error information, if any
- inputs - Inputs for the message
- outputs - Outputs of the message
- tool_config - Tool configuration
- time_cost - Time cost
- tool_parameters - Tool parameters
- file_url - URL of the associated file
- Metadata
  - message_id - Message ID
  - tool_name - Tool name
  - tool_inputs - Tool inputs
  - tool_outputs - Tool outputs
  - tool_config - Tool configuration
  - time_cost - Time cost
  - error - Error information, if any
  - tool_parameters - Tool parameters
  - message_file_id - Message file ID
  - created_by_role - Role of the creator
  - created_user_id - User ID of the creator

**Generate Name Trace Information**

**Used to track conversation title generation**

      Generate Name
      Opik Tool

      user_id
      - placed in metadata

      "generate_conversation_name"
      name

      start_time
      start_time

      end_time
      end_time

      inputs
      inputs

      outputs
      outputs

      metadata
      metadata

      \["generate_name"]
      tags

**Generate Name Trace Info**

- conversation_id - Conversation ID
- inputs - Input data
- outputs - Generated conversation name
- start_time - Start time
- end_time - End time
- tenant_id - Tenant ID
- Metadata
  - conversation_id - Conversation ID
  - tenant_id - Tenant ID
