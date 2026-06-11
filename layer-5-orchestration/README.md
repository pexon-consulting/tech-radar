# Layer 5 — AI Agent Hub & MCP Registry

> Provides the central nervous system for multi-agent AI systems. The Agent Hub
> routes requests to the right agent, manages agent lifecycle, and produces the
> audit trail required for EU AI Act compliance. The MCP Registry is the governed
> catalog of all tools agents are permitted to use.

---

## Cluster lead

| Scope | Lead | Contact |
|---|---|---|
| All Layer 5 components | Patricia Berger | `@patricia-berger` |

PRs are reviewed and merged by Patricia Berger,
as defined in [`CODEOWNERS`](../../.github/CODEOWNERS).

---

## Components

| Component | Path | Description |
|---|---|---|
| AI Agent Hub | `agent-hub/` | Central routing, lifecycle management, and audit logging for all agents |
| MCP Registry | `mcp-registry/` | Governed catalog of available MCP tools with versioning and compliance tiers |

---

## When to use this layer

| Scenario | Component |
|---|---|
| Multiple agents need to coordinate on a task | Agent Hub — routing engine |
| Human approval required before an agent takes an action | Agent Hub — human-in-the-loop workflow |
| EU AI Act traceability is required (high-risk use case) | Agent Hub — audit log |
| A new tool should be made available to all agents | MCP Registry — tool onboarding |
| Different tools allowed for different compliance tiers | MCP Registry — tier-based access control |
| Agent tool usage needs governance and review | MCP Registry — approval workflow |

---

## General knowledge

### Agent orchestration patterns

**Single agent** — one LLM with a set of tools. Sufficient for most departmental use cases.
Use the MCP Registry to control which tools are available; no Hub routing needed.

**Multi-agent (sequential)** — Agent A produces output that Agent B consumes.
The Hub manages handoff, retries, and failure handling between agents.

**Multi-agent (parallel)** — multiple agents work concurrently on subtasks; results
are aggregated. The Hub handles fan-out and fan-in, and enforces timeout policies.

**Supervisor / subagent** — a supervisor agent decomposes tasks and delegates to
specialist subagents. The Hub enforces that subagents only access tools in their
assigned tier.

Framework comparison:

| Framework | Pattern support | Language | Notes |
|---|---|---|---|
| LangGraph | All patterns | Python | Graph-based, good for complex flows; stateful |
| AutoGen | Multi-agent | Python | Strong for research / code generation agents |
| CrewAI | Sequential, parallel | Python | Higher-level abstraction; faster to prototype |
| Semantic Kernel | Single + multi | Python, C#, Java | Strong Azure / Microsoft ecosystem integration |

### Agent lifecycle management

An agent's lifecycle in the Hub:

1. **Registration** — agent metadata, allowed tools (MCP Registry tier), model, and system prompt
   are declared and versioned
2. **Invocation** — Hub receives a task, selects the appropriate agent, and passes context
3. **Execution** — agent runs; all tool calls are logged with input/output and latency
4. **Human-in-the-loop** — if configured, Hub pauses execution and awaits human approval
   before a high-risk action (e.g. writing to a production system)
5. **Completion / failure** — result returned; full trace stored in audit log
6. **Deregistration / deprecation** — agent version marked inactive; traces retained per policy

### EU AI Act audit requirements

For high-risk AI systems (Annex III of the EU AI Act), the audit log must capture:

- Identity of the system and model version used
- Input data and context provided to the model
- All tool calls made, with inputs and outputs
- Human oversight interactions (who approved, when)
- Final output and confidence indicators where applicable
- Timestamps accurate to the second, tamper-evident storage

The Agent Hub audit log schema in this layer is designed to satisfy these requirements.
For non-high-risk use cases, logging can be reduced to invocation metadata only.

Reference: [EU AI Act full text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689)

### MCP Registry governance

Every tool available to agents must be registered in the MCP Registry before use.
The registration process ensures:

- Tool schema is documented and versioned
- Tool is assigned a **compliance tier** (see below)
- Tool has a named owner responsible for availability and updates
- Breaking changes follow the deprecation policy (min. 30-day notice)

**Compliance tiers:**

| Tier | Description | Example tools |
|---|---|---|
| Standard | No special restrictions | Web search, calculator, document reader |
| Sensitive | Requires audit logging; data classification | CRM query, HR data lookup |
| KRITIS | Restricted to KRITIS-approved agents; enhanced logging | SCADA system write, energy grid query |
| Write-protected | Requires human-in-the-loop approval before execution | Send email, create ticket, write to production DB |

---

## Internal / company-specific

> **Access:** Content described here lives in `_internal/layer-5/` and is restricted
> to `@pexon-consulting/internal`. Request access via `#stack-repo-access`.

### What is stored internally

**Agent Hub (`_internal/layer-5/agent-hub/`)**  
Maintained by Patricia Berger

- Pexon Agent Hub routing engine configuration with RBAC and multi-tenancy
- Audit log schema used for EU AI Act traceability (validated with legal team 2025-Q3)
- Tested agent topologies per use-case type:
  - RAG chatbot (single agent, retrieval + generation)
  - Document processing pipeline (sequential multi-agent)
  - Research assistant (parallel multi-agent with supervisor)
  - Service desk automation (human-in-the-loop on write actions)
- Human-in-the-loop approval workflow configs used in Banking and Manufacturing deployments

**MCP Registry (`_internal/layer-5/mcp-registry/`)**  
Maintained by Patricia Berger

- Pexon tool catalog schema with compliance tier assignments
- Approved tool list per compliance tier as used in current engagements
- Tool onboarding governance checklist (security review, schema validation, tier assignment)
- Deprecation notice templates and communication process

### Maintenance schedule

| Artefact | Review frequency | Owner |
|---|---|---|
| Audit log schema | Per EU AI Act guidance updates | Patricia Berger |
| Tool compliance tier assignments | Quarterly | Patricia Berger |
| Agent topology templates | Per new use-case type delivered | Patricia Berger |
| Tool onboarding checklist | Per MCP spec update | Patricia Berger |

---

## Prerequisites

### Agent Hub

- Kubernetes cluster (from Layer 3) with AI platform deployed
- LiteLLM gateway running (Layer 3 — `ai-platform/`)
- PostgreSQL for agent registry and audit log persistence
- Redis for in-flight agent state (optional for stateless single-agent use)
- MCP Registry reachable from Hub (in-cluster service)

### MCP Registry

- Kubernetes cluster
- PostgreSQL for tool catalog persistence
- Access credentials with write permissions for tool owners onboarding new tools

---

## Quick start

### Deploy the Agent Hub

```bash
cd layer-5-orchestration/agent-hub

cp helm/values.yaml helm/values.local.yaml
# Configure: litellm_url, database_url, redis_url, mcp_registry_url

helm upgrade --install agent-hub ./helm \
  -f helm/values.local.yaml \
  --namespace ai-orchestration \
  --create-namespace
```

### Deploy the MCP Registry

```bash
cd layer-5-orchestration/mcp-registry

helm upgrade --install mcp-registry ./helm \
  -f helm/values.yaml \
  --namespace ai-orchestration
```

### Register an agent

```bash
# Register a new agent via the Hub API
curl -X POST http://agent-hub.ai-orchestration.svc.cluster.local/agents \
  -H "Content-Type: application/json" \
  -d '{
    "name": "document-analyst",
    "model": "azure/gpt-4o",
    "system_prompt": "You are a document analyst...",
    "allowed_tools": ["document_reader", "vector_search"],
    "compliance_tier": "sensitive",
    "audit_level": "full"
  }'
```

### Register a tool in the MCP Registry

```bash
curl -X POST http://mcp-registry.ai-orchestration.svc.cluster.local/tools \
  -H "Content-Type: application/json" \
  -d @tool-manifests/vector_search.json
```

---

## Related layers

- **Layer 3** (`layer-3-platform-engineering/ai-platform/`) — LiteLLM gateway
  that the Agent Hub routes model calls through
- **Layer 4** (`layer-4-data-platform/mcp-integration/`) — MCP tool
  implementations that are registered in the Registry here
- **Layer 6** (`layer-6-applications/`) — applications invoke the Agent Hub
  to run agents; they do not call models or tools directly
- **Security** (`security-governance/`) — RBAC and audit schemas that govern
  agent and tool access across this layer

---

*Layer owner: Patricia Berger · Last reviewed: 2026-05*
