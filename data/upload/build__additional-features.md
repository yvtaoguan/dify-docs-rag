# App Toolkit

Dify apps come with optional features you can enable to improve the end-user experience. Open the **Features** panel of the builder to see what's available for your app type.

> Image: Features Panel in Chatbots, Agents, and Text Generators

> Image: Features Panel in Chatflows

## Conversation Opener

Set an opening message that greets users at the start of each conversation, with optional suggested questions to guide them toward what the app does well.

You can insert variables into the opening message and suggested questions to personalize the experience.

- In the opening message, type `{` or `/` to insert variables from the picker.

- In suggested questions, type variable names manually in `{{variable_name}}` format.

> Image: Configuration

> Image: Web App

## Follow-up

When enabled, follow-up questions are generated after each response to help users continue the conversation.

Click **Settings** to pick the model that generates the questions, or write a custom prompt (up to 1,000 characters) to adjust the number, wording, or length of the questions.

## Text to Speech

Convert AI responses to audio. You can configure the language and voice to match your app's audience, and enable **Auto Play** to stream audio automatically as the AI responds.

> **Info**
>
> **Text to Speech** uses your workspace's text-to-speech model (set in **Integrations** > **Model Provider** > **Default Models**).
>
> The feature only appears in the **Features** panel when a default TTS model is configured.

## Speech to Text

Enable voice input for the chat interface. When enabled, your end users can dictate messages instead of typing by clicking the microphone button.

> **Info**
>
> **Speech to Text** uses your workspace's speech-to-text model (set in **Integrations** > **Model Provider** > **Default Models**).
>
> The feature only appears in the **Features** panel when a default STT model is configured.

## File Upload

Allow end users to send files at any point during a conversation. You can configure which file types to accept, the upload method, and the maximum number of files per message.

Per-file size limits:

- Images: 10 MB
- Documents: 15 MB
- Audio: 50 MB
- Video: 100 MB

## Citations and Attributions

Show the source documents behind AI responses. When enabled, responses that draw from a connected knowledge base display numbered citations linking back to the original documents and chunks.

## Content Moderation

Filter inappropriate content in user inputs, AI outputs, or both. Choose a moderation provider based on your needs:

- **OpenAI Moderation**: Use OpenAI's dedicated moderation model to detect harmful content across multiple categories.

- **Keywords**: Define a list of blocked terms. Any match triggers the preset response.

- **Custom Endpoint**: Connect a custom moderation endpoint for your own filtering logic.

When content is flagged, the app replaces it with a preset response that you define.

## Annotation Reply

Define curated Q&A pairs that take priority over LLM responses. When a user's query **semantically** matches an annotation above the score threshold (how closely a query must match), the curated answer is returned directly without calling the LLM.

You can configure the score threshold and the embedding model used for semantic matching.

To create and manage your annotations:

- Convert existing conversations into annotations directly from **Debug & Preview** or **Logs** by clicking the **Add annotation** icon on any LLM response.

    Once a message is annotated, the icon changes to **Edit**, so you can modify the annotation in place.

- In **Annotations**, manually add new Q&A pairs, manage existing annotations, and view hit history. Click `...` to bulk import or bulk export.

## More Like This

Generate alternative outputs for the same input. Once enabled, each generated result includes a button to produce a variation, so you can explore different responses without re-entering your query.

You can generate up to 2 variations per result. Each variation uses additional tokens.
