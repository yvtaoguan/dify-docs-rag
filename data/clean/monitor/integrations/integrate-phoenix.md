# Integrate with Phoenix

### What is Phoenix

[Arize Phoenix](https://arize.com/phoenix/) is the open-source, OpenTelemetry-based platform from [Arize AI](https://arize.com/?utm_source=dify-docs&utm_medium=partner&utm_campaign=partner-docs&utm_content=integrate-phoenix) for observability, evaluation, prompt engineering, and experimentation with LLM workflows and agents.

Use Arize's hosted [Phoenix Cloud](#how-to-configure-phoenix-cloud), or self-host Phoenix on your own infrastructure (a single container is enough to start). Dify sends traces server-side, so a self-hosted endpoint must be reachable from the internet.

If you need the full-featured platform built for production teams, AI-native companies, and enterprises, set up [Arize AX](https://arize.com/products/ax/) through the [Arize integration](https://docs.dify.ai/en/cloud/use-dify/monitor/integrations/integrate-arize) instead.

Once traces are flowing, see Arize's [agent evaluation guide](https://arize.com/guides/ai-agent-handbook/agent-evaluation/) and [LLM evaluation guide](https://arize.com/resources/llm-evaluation/) for how to use them to debug failures, evaluate agent behavior, and monitor model quality.

### How to Configure Phoenix

#### 1. Register/Login to [Phoenix](https://app.arize.com/auth/phoenix/signup)

#### 2. Get your Phoenix API Key

Retrieve your Phoenix API Key from the user menu at the top-right. Click on **API Key**, then on the API Key to copy it:

#### 3. Integrate Phoenix with Dify

Configure Phoenix in the Dify application. Open the application you need to monitor, open **Monitoring** in the side menu, and select **Tracing app performance** on the page.

After clicking configure, paste the **API Key** and **project name** created in Phoenix into the configuration and save.

Once successfully saved, you can view the monitoring status on the current page.

### How to Configure Phoenix Cloud

#### 1. Register/Login to [Phoenix Cloud](https://app.arize.com/auth/phoenix/signup)

#### 2. Create your Phoenix Space

You can create your Phoenix Space from the user menu at the top-right. Click on **Create Space**, then provide a unique URL identifier for your space:

Once successfully saved, you can view the space status on the overview page.

#### 3. Create your Phoenix API Key

After launching your space, you can create your Phoenix API Key from the **Settings** option in the user menu at the bottom-left. Click on **System Key**, then provide a name for your Phoenix API Key:

#### 4. Integrate Phoenix Cloud with Dify

Configure Phoenix in the Dify application. Open the application you need to monitor, open **Monitoring** in the side menu, and select **Tracing app performance** on the page.

After clicking configure, paste the **API Key** and **project name** along with **Space Hostname** created in Phoenix Cloud into the configuration and save.

Once successfully saved, you can view the monitoring status on the current page.

### Monitoring Data List

#### **Workflow/Chatflow Trace Information**

**Used to track workflows and chatflows**

      Workflow
      Phoenix Trace

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
      Phoenix LLM

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
      Phoenix Tool

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
      Phoenix LLM

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
      Phoenix Retriever

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
      Phoenix Tool

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
      Phoenix Tool

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
