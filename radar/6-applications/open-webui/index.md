---
name: Open WebUI
layer: 6-applications
ring: trial
tags: [chat-ui, self-hosted, private-ai, sso]
champions: []
since: 2026-06
ring_history:
  - { ring: trial, date: 2026-06, reason: "Added from blog coverage — our most-written-about chat frontend for private AI stacks" }
articles:
  - { title: "Open WebUI SSO mit Azure Entra ID einrichten", url: "https://pexon-consulting.de/blog/open-webui-sso-entra-id-einrichten/", date: 2026-04 }
  - { title: "Open WebUI vs. Onyx (Danswer): Welcher KI-Chat passt zu Ihrem Unternehmen?", url: "https://pexon-consulting.de/blog/open-webui-vs-onyx-danswer-vergleich/", date: 2026-04 }
  - { title: "Open-Source KI-Stack für Unternehmen: OpenWebUI, LiteLLM, Milvus und n8n im Praxiseinsatz", url: "https://pexon-consulting.de/blog/open-source-ki-stack-unternehmen/", date: 2026-04 }
  - { title: "LibreChat vs Open WebUI: Self-Hosted KI-Chat im Vergleich", url: "https://pexon-consulting.de/blog/librechat-vs-open-webui/", date: 2026-03 }
  - { title: "Open WebUI Guide: Die beste Benutzeroberfläche für lokale KI-Modelle einrichten", url: "https://pexon-consulting.de/blog/private-ai-ollama-open-webui-ubuntu-installieren/", date: 2026-03 }
  - { title: "Open Source AI Chatbot: 5 Plattformen im Enterprise-Vergleich", url: "https://pexon-consulting.de/blog/open-source-ai-chatbot/", date: 2026-01 }
---

## What is it?

Self-hosted chat frontend for LLMs — the standard UI of our open-source/private-AI stack, with SSO (Entra ID), RBAC and multi-model support via gateways like LiteLLM.

## Why this ring?

Six blog posts deep, it's our default answer for "private ChatGPT" requests: pairs with LiteLLM (gateway) and vLLM/Ollama (models) into a fully self-hosted stack. Trial until a named production deployment is referenced here.

## When to use it — and when not?

- **Use** as the chat frontend for private-AI stacks where data must stay in the client's perimeter.
- **Don't** force it where the client lives in M365 and Copilot fits the bill, or where a custom product UI is the deliverable (→ Next.js).

## Client projects & references

| Client | Project | Period | Internal contact |
|---|---|---|---|
|  |  |  |  |

## Lessons learned

-

## Resources

- https://github.com/open-webui/open-webui
