# MCP Library — Exhaustive Claude Code Arsenal

> **Auto-updated every Monday at 00:00 UTC** from community sources including [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers), [PulseMCP](https://www.pulsemcp.com/servers), and [mcp.so](https://mcp.so).
>
> Last updated: <!-- LAST_UPDATED -->2026-04-13<!-- /LAST_UPDATED -->

This library is referenced by `~/.claude/CLAUDE.md` so every Claude Code session can pick the optimal MCP stack for any project. Claude reads this at session start and selects the best MCPs based on the task at hand.

---

## Quick Selection Guide

| I need to... | Use these MCPs |
|---|---|
| Build a full-stack web app | GitHub + Context7 + Supabase/PostgreSQL + Playwright + Vercel + Sentry |
| Design UI components | 21st.dev Magic + shadcn/ui + Figma + Pencil |
| Automate workflows | n8n + Composio + Zapier + Sequential Thinking |
| Debug production issues | Sentry + PostgreSQL + Sequential Thinking + GitHub |
| Research & gather data | Exa + Tavily + Firecrawl + Context7 + OmniSearch |
| Manage DevOps / infra | Terraform + Kubernetes + Prometheus + GitHub + Sentry |
| Multi-agent orchestration | Rowboat + Sequential Thinking + mem0 + GitHub |
| Firebase project | GitHub + Context7 + Firebase + Playwright + Sentry |
| E-commerce app | Stripe + Supabase + Vercel + GitHub + Context7 |
| API integrations | Composio + Context7 + GitHub + Postman/Apidog |
| Anything (baseline) | **GitHub + Context7 — always active** |

---

## Categories

- [Core / Always-On](#core--always-on)
- [UI & Design Generation](#ui--design-generation)
- [Browser & Automation](#browser--automation)
- [Web Research & Search](#web-research--search)
- [Databases](#databases)
- [DevOps & Cloud Infrastructure](#devops--cloud-infrastructure)
- [Communication & Productivity](#communication--productivity)
- [Memory & Knowledge](#memory--knowledge)
- [Reasoning & Planning](#reasoning--planning)
- [Automation & Integration Hubs](#automation--integration-hubs)
- [Code Execution & Filesystem](#code-execution--filesystem)
- [Testing & QA](#testing--qa)
- [Finance & Commerce](#finance--commerce)
- [Monitoring & Observability](#monitoring--observability)
- [MCP Chains by Workflow](#mcp-chains-by-workflow)

---

## Core / Always-On

These two MCPs should be active in **every** Claude Code session without exception.

| Name | Install | What It Does | Free? |
|------|---------|-------------|-------|
| **GitHub MCP** | `npx @modelcontextprotocol/server-github` | PR creation, issue triage, branch ops, code review, commit history. Official Anthropic reference server. | ✅ Free |
| **Context7 MCP** | `npx @context7/mcp-server` | Live, version-accurate framework docs fetched at query time. Eliminates hallucinated APIs. Use before implementing any library. | ✅ Free |

---

## UI & Design Generation

| Name | Install | What It Does | Free? |
|------|---------|-------------|-------|
| **21st.dev Magic MCP** | `npx @21st-dev/magic-mcp` | Like v0.dev inside your IDE. Type `/ui [description]` to generate polished React/Tailwind/shadcn components with multiple variants. Free during beta. Requires API key from 21st.dev/magic/console. | ✅ Free (beta) |
| **shadcn/ui MCP** (official) | `npx shadcn@latest mcp` | Browse, search, and install shadcn/ui v4 components. Supports React, Svelte, Vue, React Native. Integrated into the shadcn CLI. | ✅ Free |
| **Figma Dev Mode MCP** (official) | Figma plugin | Exposes selected Figma layers as structured JSON. Generates pixel-accurate code from live designs instead of screenshots. | ✅ Free (Dev tier) |
| **Pencil MCP** | Built into Claude Code | Native .pen file design tooling inside Claude sessions. Create and edit UI mockups without leaving the IDE. | ✅ Free |
| **v0 MCP** (Vercel) | `npx @vercel/v0-mcp` | Vercel's generative UI — produces Next.js + shadcn output from natural language prompts. | ✅ Free tier |
| **Magic Patterns MCP** | `npx @magic-patterns/mcp` | AI-generated UI pattern library for rapid wireframing and prototyping. | ✅ Free tier |
| **Svelte MCP** (official) | `npx svelte-mcp` | Official Svelte tooling — component scaffolding, docs, and AI-enhanced DX. | ✅ Free |

---

## Browser & Automation

| Name | Install | What It Does | Free? |
|------|---------|-------------|-------|
| **Playwright MCP** (Microsoft official) | `npx @microsoft/playwright-mcp` | E2E browser automation via accessibility snapshots. Faster and more reliable than visual analysis for AI tasks. Screenshots, form fills, scraping. | ✅ Free |
| **Stagehand / Browserbase MCP** | `npx @browserbase/mcp-server-browserbase` | AI-powered cloud browser built on Stagehand v3. Natural language web actions, 20–40% faster than Playwright for AI workflows. | Freemium |
| **Desktop Commander MCP** | `npx @wonderwhy-er/desktop-commander-mcp` | Full terminal control, file system search, diff-based surgical editing. Best for long-running shell tasks and background processes. | ✅ Free |
| **Puppeteer MCP** (official) | `npx @modelcontextprotocol/server-puppeteer` | Headless Chrome — screenshots, PDFs, web scraping. Official Anthropic reference server. | ✅ Free |
| **Claude in Chrome MCP** | Browser extension | Control the active Chrome tab, read DOM, fill forms, execute JS, read console/network. | ✅ Free |

---

## Web Research & Search

| Name | Install | What It Does | Free? |
|------|---------|-------------|-------|
| **Exa MCP** | `npx exa-mcp-server` | Neural/semantic search — surfaces conceptually relevant sources. Best for deep research where keyword search fails. | Freemium |
| **Tavily MCP** (official) | `npx @tavily/mcp-server` | AI-optimized search purpose-built for LLM research workflows. Fast and accurate. | Freemium |
| **Firecrawl MCP** (official) | `npx firecrawl-mcp` | Fastest web scraper/extractor (avg 7s). Converts any URL to clean markdown. 83% accuracy in 2026 benchmarks. | Freemium |
| **Crawl4AI MCP** | `npx crawl4ai-mcp` | Open-source crawler outputting clean markdown. Fully self-hostable. No API key needed. | ✅ Free |
| **OmniSearch MCP** | `npx mcp-omnisearch` | Unified interface: Tavily + Brave + Kagi + Perplexity + Jina AI through a single MCP. Best all-in-one option. | ✅ Free |
| **Brave Search MCP** (official) | `npx @modelcontextprotocol/server-brave-search` | Brave's independent search index. No Google dependency. Official reference server. | Freemium |
| **Fetch MCP** (official) | `npx @modelcontextprotocol/server-fetch` | Simple URL fetching + HTML-to-markdown. Lightweight for single-page reads. | ✅ Free |
| **Kagi Search MCP** | `npx mcp-kagi` | Premium ad-free search. High signal-to-noise ratio for research. | Paid |

---

## Databases

| Name | Install | What It Does | Free? |
|------|---------|-------------|-------|
| **PostgreSQL MCP** (official) | `npx @modelcontextprotocol/server-postgres` | Natural language queries, schema inspection, migration helpers. Official reference server. | ✅ Free |
| **SQLite MCP** (official) | `npx @modelcontextprotocol/server-sqlite` | Same for SQLite. Great for local dev, data modeling, and embedded databases. | ✅ Free |
| **Supabase MCP** (official) | `npx @supabase/mcp-server-supabase` | Design schemas, write migrations, generate TypeScript types, manage auth, Storage, and Edge Functions. | ✅ Free tier |
| **Neon MCP** (official) | `npx @neondatabase/mcp-server-neon` | Serverless Postgres. Create DB branches per PR for isolated testing. Instant clones. | ✅ Free tier |
| **MySQL MCP** | `npx mysql-mcp-server` | Full MySQL interaction — queries, schema management, index analysis. | ✅ Free |
| **MongoDB MCP** | `npx @mongodb-js/mongodb-mcp-server` | CRUD, aggregations, index management, Atlas integration. | ✅ Free |
| **Redis MCP** | `npx @modelcontextprotocol/server-redis` | Key inspection, pub/sub monitoring, cache debugging, cluster management. | ✅ Free |
| **PlanetScale MCP** | `npx planetscale-mcp` | MySQL-compatible serverless DB with database branching model. | Freemium |
| **Astra DB MCP** | `npx @datastax/astra-db-mcp` | DataStax Cassandra-backed NoSQL for vector + document workloads. | Freemium |

---

## DevOps & Cloud Infrastructure

| Name | Install | What It Does | Free? |
|------|---------|-------------|-------|
| **Terraform MCP** (HashiCorp official) | `npx @hashicorp/terraform-mcp-server` | Query Terraform Registry, inspect workspace state, trigger runs with human approval. Enterprise-backed, production-ready. | ✅ Free |
| **Kubernetes MCP** | `npx @kubernetes/mcp-server` | Manage clusters, diagnose crashlooping pods, pull logs and events in real time. Community-maintained. | ✅ Free |
| **Docker MCP** | `npx docker-mcp` | `docker ps`, `docker logs`, `docker inspect`, `docker exec` via natural language. | ✅ Free |
| **AWS MCP** (awslabs official) | `npx @aws/mcp-server` | S3, Lambda, EC2, CloudFormation, Cost Explorer, IAM via natural language. Official AWS Labs. | ✅ Free |
| **Vercel MCP** (official) | `npx @vercel/mcp-adapter` | Deploy projects, check logs, manage env vars, compare preview vs production. | ✅ Free |
| **Cloudflare MCP** (official) | `npx @cloudflare/mcp-server-cloudflare` | Workers, KV, R2, D1, Pages — manage the full Cloudflare stack. | ✅ Free |
| **Firebase MCP** (official) | Built into `firebase-tools` | Firestore, Auth, Storage, Hosting, Functions — full Firebase project management. | ✅ Free tier |
| **Azure DevOps MCP** | `npx azure-devops-mcp` | Pipelines, work items, repos, boards, artifact management. | ✅ Free tier |
| **Heroku MCP** (official) | `npx @heroku/mcp-server` | App management, dyno scaling, logs, add-ons. Official Heroku server. | Freemium |

---

## Communication & Productivity

| Name | Install | What It Does | Free? |
|------|---------|-------------|-------|
| **Slack MCP** (official) | `npx @modelcontextprotocol/server-slack` | Read channels, post messages, search conversations, manage workspaces. Official reference server. | ✅ Free |
| **Notion MCP** (official) | `npx @notionhq/notion-mcp-server` | Read/write pages, query databases, sync specs and docs into context. Official Notion server. | ✅ Free |
| **Linear MCP** (official) | `npx @linear/mcp-server` | Issue tracking, project management, sprint planning, cycle management. | ✅ Free |
| **Jira MCP** | `npx @atlassian/jira-mcp` | Create/update issues, query sprints, link PRs to tickets, roadmap planning. | Freemium |
| **Google Drive MCP** (official) | `npx @modelcontextprotocol/server-gdrive` | Search, read, and manage Drive files — Docs, Sheets, Slides — from Claude. | ✅ Free |
| **Gmail MCP** | `npx gmail-mcp-server` | Read, send, search, label, and draft emails. | ✅ Free |
| **Google Calendar MCP** | `npx google-calendar-mcp` | Schedule events, check availability, manage meetings, set reminders. | ✅ Free |
| **Discord MCP** | `npx discord-mcp-server` | Read channels, post messages, manage servers and roles. | ✅ Free |
| **Airtable MCP** | `npx airtable-mcp-server` | Query and update Airtable bases, manage records and views. | Freemium |

---

## Memory & Knowledge

| Name | Install | What It Does | Free? |
|------|---------|-------------|-------|
| **Memory MCP** (official) | `npx @modelcontextprotocol/server-memory` | Persistent knowledge graph across sessions stored as JSON. The official Anthropic memory solution. | ✅ Free |
| **mem0 MCP** | `npx mem0-mcp` | Semantic cross-session memory with vector search. Store and retrieve architectural decisions by meaning. | Freemium |
| **Pieces MCP** | Pieces Desktop app | Code snippet retrieval and reusable pattern recall mid-session. Works offline. | ✅ Free |
| **Knowledge Graph MCP** | `npx knowledge-graph-mcp` | Entities, relations, and observations stored persistently in a graph structure. | ✅ Free |

---

## Reasoning & Planning

| Name | Install | What It Does | Free? |
|------|---------|-------------|-------|
| **Sequential Thinking MCP** (official) | `npx @modelcontextprotocol/server-sequential-thinking` | Structured multi-step reasoning. Forces chain-of-thought for architecture decisions. Official reference server. | ✅ Free |
| **Thinking Claude MCP** | `npx thinking-claude-mcp` | Extended thinking mode wrapper. Great for complex debugging and system design. | ✅ Free |

---

## Automation & Integration Hubs

| Name | Install | What It Does | Free? |
|------|---------|-------------|-------|
| **n8n MCP** | `npx n8n-mcp` | Trigger self-hosted n8n workflows. Pairs with n8n's 400+ node library for any automation. | ✅ Free (self-hosted) |
| **Composio MCP** | `npx composio-core mcp` | 500+ app integrations (Slack, Jira, Gmail, Stripe, HubSpot, Salesforce...) via one install. Best when no dedicated MCP exists. | ✅ Free tier |
| **Zapier MCP** | `npx @zapier/mcp-server` | Trigger Zapier zaps, connect 7,000+ apps. | Freemium |
| **Make MCP** | `npx make-mcp-server` | Visual workflow automation with 1,000+ app integrations. | Freemium |

---

## Code Execution & Filesystem

| Name | Install | What It Does | Free? |
|------|---------|-------------|-------|
| **Filesystem MCP** (official) | `npx @modelcontextprotocol/server-filesystem` | Secure local file read/write/search with granular permission controls. Official reference server. | ✅ Free |
| **Git MCP** (official) | `npx @modelcontextprotocol/server-git` | Git history, diffs, branch management, commit inspection from Claude. | ✅ Free |
| **Desktop Commander MCP** | `npx @wonderwhy-er/desktop-commander-mcp` | Terminal control + file ops + diff editing. See also: Browser & Automation. | ✅ Free |
| **Jupyter MCP** | `npx jupyter-mcp-server` | Execute code cells in Jupyter notebooks, read outputs, iterate on analyses. | ✅ Free |
| **Code Interpreter MCP** | `npx code-interpreter-mcp` | Run Python, JS, bash in a sandboxed environment. | ✅ Free |

---

## Testing & QA

| Name | Install | What It Does | Free? |
|------|---------|-------------|-------|
| **Playwright MCP** | `npx @microsoft/playwright-mcp` | E2E tests, browser automation, accessibility testing. See also: Browser & Automation. | ✅ Free |
| **Postman MCP** | `npx postman-mcp-server` | Execute API collections, validate responses, manage environments. | Freemium |
| **Apidog MCP** | `npx apidog-mcp-server` | Work with API specs, generate request code, mock responses. | Freemium |

---

## Finance & Commerce

| Name | Install | What It Does | Free? |
|------|---------|-------------|-------|
| **Stripe MCP** (official) | `npx @stripe/mcp-server` | Query customers, subscriptions, invoices, payments, refunds. Official Stripe server. | ✅ Free |
| **Coinbase MCP** | `npx coinbase-mcp` | Crypto prices, wallet operations, transaction history. | Freemium |

---

## Monitoring & Observability

| Name | Install | What It Does | Free? |
|------|---------|-------------|-------|
| **Sentry MCP** (official) | `npx @sentry/mcp-server` | Pull full error context, stack traces, correlate with releases, create issues. | ✅ Free tier |
| **Prometheus MCP** | `npx prometheus-mcp-server` | Natural language PromQL queries against live metrics. CPU, memory, latency at query time. | ✅ Free |
| **Datadog MCP** | `npx datadog-mcp-server` | Logs, traces, dashboards, monitors, SLOs. | Freemium |
| **Grafana MCP** | `npx grafana-mcp` | Query dashboards, panels, explore metrics and logs. | ✅ Free |
| **PagerDuty MCP** | `npx pagerduty-mcp-server` | Incident management, escalations, on-call schedules, post-mortems. | Freemium |

---

## MCP Chains by Workflow

```
Research:       Sequential Thinking → Context7 → Exa/Tavily → Notion/mem0
Build:          Context7 → 21st.dev Magic → GitHub → Supabase → Playwright → Vercel
UI/Design:      Figma → 21st.dev Magic → shadcn/ui → Context7 → GitHub
Debug:          Sentry → PostgreSQL/SQLite → Sequential Thinking → GitHub
Deploy:         GitHub → Vercel/Cloudflare → n8n → Composio (Slack notify)
Data pipeline:  PostgreSQL/Supabase → Jupyter → Sequential Thinking → Grafana
Infra:          Terraform → Kubernetes → Prometheus → PagerDuty → GitHub
E-commerce:     Stripe → Supabase → Vercel → Sentry → GitHub
Research bot:   Exa → Tavily → Firecrawl → mem0 → Notion
```

---

## Directories & Further Reading

- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) — Community curated list
- [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) — Additional curated list
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — Official reference implementations
- [PulseMCP](https://www.pulsemcp.com/servers) — 8,600+ servers, updated daily
- [mcp.so](https://mcp.so) — 17,000+ servers marketplace
- [mcp-awesome.com](https://mcp-awesome.com) — 1,200+ quality-verified servers

---

*Auto-updated by `.github/workflows/update.yml`. To add a server: open a PR to this repo.*
