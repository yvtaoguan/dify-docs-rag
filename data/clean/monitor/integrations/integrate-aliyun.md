# Integrate with Alibaba Cloud Monitor

## What is Alibaba Cloud Monitor

Alibaba Cloud provides a fully managed, maintenance-free observability platform that enables one-click monitoring, tracing, and evaluation of Dify applications.

> **Info**
>
> Alibaba Cloud Monitor natively supports Python/Golang/Java applications through [LoongSuite](https://github.com/alibaba/loongsuite-python-agent) agents and open-source OpenTelemetry agents. In addition to one-click monitoring of Dify LLM applications, it also supports end-to-end observability of Dify components and their upstream and downstream dependencies through non-invasive agents.
>
>   For more details, please refer to the [Cloud Monitor documentation](https://www.alibabacloud.com/help/en/cms/cloudmonitor-1-0/product-overview/what-is-cloudmonitor?spm=a3c0i.63551.2277339270.1.76c7112eeKEvSr).

## How to Configure Alibaba Cloud Monitor

### 1. Get Alibaba Cloud Endpoint and License Key

1. Log in to the [ARMS console](https://account.alibabacloud.com/login/login.htm?spm=5176.12901015-2.0.0.68d74b84XRatpU), and click **Integration Center** in the left navigation bar.
2. In the **Server-side Applications** area, click the **OpenTelemetry** card.
3. In the **OpenTelemetry** panel that appears, select **gRPC** as the export protocol, and select the connection method and region according to your actual deployment.

4. Save the **Public Endpoint** and **Authentication Token (License Key)**.

> **Note**
>
> The Endpoint does not include a port number, for example `http://tracing-cn-heyuan.arms.aliyun.com`.

### 2. Configure Cloud Monitor in Dify

1. Log in to the Dify console and navigate to the application you want to monitor.
2. Open **Monitoring** in the left navigation bar.
3. Click **Tracing app performance**, then click **Configure** in the **Cloud Monitor** area.

4. In the dialog that appears, enter the **License Key** and **Endpoint** obtained in step 1, and customize the **App Name** (the application name displayed in the ARMS console), then click **Save & Enable**.

## View Monitoring Data in Alibaba Cloud Monitor

After configuration, debug or production data from applications in Dify can be monitored in Cloud Monitor.

### Method 1: Jump to ARMS Console from Dify Application

In the Dify console, select an application with tracing enabled, go to **Tracing Configuration**, and click **View** in the **Cloud Monitor** area.

### Method 2: View Directly in ARMS Console

Go to the corresponding Dify application in the **LLM Application Monitoring > Application List** page of the ARMS console.

## Access More Data

Cloud Monitor provides multi-language non-invasive agents that support accessing various components of the Dify cluster to achieve end-to-end tracing.

| Dify Component | Agent | Details |
|----------------|-------|---------|
| Nginx | OpenTelemetry Agent | [Use OpenTelemetry for Nginx Tracing](https://www.alibabacloud.com/help/en/opentelemetry/user-guide/use-opentelemetry-to-perform-tracing-analysis-on-nginx?spm=a2c63.l28256.help-menu-search-90275.d_1) |
| API | LoongSuite-Python Agent | [loongsuite-python-agent](https://github.com/alibaba/loongsuite-python-agent/blob/main/README.md) |
| Sandbox | LoongSuite-Go Agent | [loongsuite-go-agent](https://github.com/alibaba/loongsuite-go-agent/blob/main/README.md) |
| Worker | OpenTelemetry Agent | [Submit Python Application Data via OpenTelemetry](https://www.alibabacloud.com/help/en/opentelemetry/user-guide/use-managed-service-for-opentelemetry-to-submit-the-trace-data-of-python-applications?spm=a2c63.p38356.help-menu-90275.d_2_0_5_0.18ee53a4EGoGuS) |
| Plugin-Daemon | LoongSuite-Go Agent | [loongsuite-go-agent](https://github.com/alibaba/loongsuite-go-agent/blob/main/README.md) |

## Monitoring Data List

Cloud Monitor supports collecting data from Dify's Workflow/Chatflow/Chat/Agent applications, including execution details of workflows and workflow nodes, covering model calls, tool calls, knowledge retrieval, execution details of various process nodes, as well as metadata such as conversations and user information.

### Workflow/Chatflow Trace Information

      Workflow
      Alibaba Cloud Monitor Trace

      workflow\_id
      Unique identifier of the Workflow

      conversation\_id
      Conversation ID

      workflow\_run\_id
      ID of this run

      tenant\_id
      Tenant ID

      elapsed\_time
      Duration of this run

      status
      Run status

      version
      Workflow version

      total\_tokens
      Total tokens used in this run

      file\_list
      List of processed files

      triggered\_from
      Source that triggered this run

      workflow\_run\_inputs
      Input data for this run

      workflow\_run\_outputs
      Output data for this run

      error
      Errors that occurred during this run

      query
      Query used during runtime

      workflow\_app\_log\_id
      Workflow application log ID

      message\_id
      Associated message ID

      start\_time
      Run start time

      end\_time
      Run end time

**Workflow Trace Metadata**

* workflow\_id - Unique identifier of the Workflow
* conversation\_id - Conversation ID
* workflow\_run\_id - ID of this run
* tenant\_id - Tenant ID
* elapsed\_time - Duration of this run
* status - Run status
* version - Workflow version
* total\_tokens - Total tokens used in this run
* file\_list - List of processed files
* triggered\_from - Trigger source

### Message Trace Information

      Message
      Alibaba Cloud Monitor Trace

      message\_id
      Message ID

      message\_data
      Message data

      user\_session\_id
      User's session\_id

      conversation\_model
      Conversation model

      message\_tokens
      Number of tokens in the message

      answer\_tokens
      Number of tokens in the answer

      total\_tokens
      Total tokens in message and answer

      error
      Error information

      inputs
      Input data

      outputs
      Output data

      file\_list
      List of processed files

      start\_time
      Start time

      end\_time
      End time

      message\_file\_data
      File data associated with the message

      conversation\_mode
      Conversation mode

**Message Trace Metadata**

* conversation\_id - ID of the conversation to which the message belongs
* ls\_provider - Model provider
* ls\_model\_name - Model ID
* status - Message status
* from\_end\_user\_id - ID of the sending user
* from\_account\_id - ID of the sending account
* agent\_based - Whether it is agent-based
* workflow\_run\_id - Workflow run ID
* from\_source - Message source
* message\_id - Message ID

### Dataset Retrieval Trace Information

      Dataset Retrieval
      Alibaba Cloud Monitor Trace

      message\_id
      Message ID

      inputs
      Input content

      documents
      Document data

      start\_time
      Start time

      end\_time
      End time

      message\_data
      Message data

**Dataset Retrieval Trace Metadata**

* message\_id - Message ID
* ls\_provider - Model provider
* ls\_model\_name - Model ID
* status - Message status
* from\_end\_user\_id - ID of the sending user
* from\_account\_id - ID of the sending account
* agent\_based - Whether it is agent-based
* workflow\_run\_id - Workflow run ID
* from\_source - Message source

### Tool Trace Information

      Tool
      Alibaba Cloud Monitor Trace

      message\_id
      Message ID

      tool\_name
      Tool name

      start\_time
      Start time

      end\_time
      End time

      tool\_inputs
      Tool inputs

      tool\_outputs
      Tool outputs

      message\_data
      Message data

      error
      Error information (if any)

      inputs
      Input content of the message

      outputs
      Answer content of the message

      tool\_config
      Tool configuration

      time\_cost
      Time cost

      tool\_parameters
      Tool parameters

      file\_url
      URL of associated file

**Tool Trace Metadata**

* message\_id - Message ID
* tool\_name - Tool name
* tool\_inputs - Tool inputs
* tool\_outputs - Tool outputs
* tool\_config - Tool configuration
* time\_cost - Time cost
* error - Error information
* tool\_parameters - Tool parameters
* message\_file\_id - Message file ID
* created\_by\_role - Creator role
* created\_user\_id - Creator user ID
