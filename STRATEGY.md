# MCP Selection Strategy — God Mode Protocol

## The Algorithm (Run at Session Start)

1. **Identify project type** from the table below
2. **Activate baseline**: GitHub + Context7 — always, no exceptions
3. **Layer task-specific MCPs** for the current work
4. **Declare active MCPs** in your plan: `Using: GitHub, Context7, Supabase, Playwright`
5. **Pre-fetch docs** via Context7 for every library before writing any code
6. **Store decisions** in mem0 at session end

---

## By Project Type

| Type | Activate |
|------|---------|
| Full-stack web app | GitHub, Context7, Supabase/PostgreSQL, Playwright, Vercel, Sentry |
| Firebase app | GitHub, Context7, Firebase, Playwright, Sentry |
| Mobile app | GitHub, Context7, Supabase, Playwright, Sequential Thinking |
| Data pipeline | PostgreSQL, SQLite, Sequential Thinking, Filesystem, Jupyter |
| Automation bot | n8n, Composio, GitHub, Sequential Thinking, mem0 |
| DevOps / infra | Terraform, Kubernetes, Prometheus, GitHub, Sentry, PagerDuty |
| Design-to-code | Figma, 21st.dev Magic, shadcn/ui, Context7, GitHub |
| Research project | Exa, Tavily, Firecrawl, Context7, Notion, mem0, Sequential Thinking |
| API integration | Composio, Context7, GitHub, Postman/Apidog |
| E-commerce | Stripe, Supabase, Vercel, GitHub, Context7, Sentry |
| Multi-agent work | Rowboat, Sequential Thinking, mem0, GitHub |

---

## By Task Type (Within a Session)

| Task | MCPs to Activate |
|------|-----------------|
| Implementing a new feature | Context7 (fetch docs) + GitHub |
| Designing a UI | 21st.dev Magic + shadcn/ui + Figma |
| Writing a DB schema | Supabase/PostgreSQL + Sequential Thinking |
| Debugging a bug | Sentry + PostgreSQL + Sequential Thinking |
| Writing E2E tests | Playwright + GitHub |
| Deploying | Vercel/Cloudflare + GitHub |
| Researching a library | Context7 + Exa |
| Sending notifications | Composio (Slack/email) or n8n |
| Tracking tasks | Linear or Jira |

---

## MCP Chains

```
Research chain:
  Sequential Thinking → Context7 → Exa/Tavily → Notion/mem0

Build chain:
  Context7 → 21st.dev Magic → GitHub → Supabase → Playwright → Vercel

UI/Design chain:
  Figma → 21st.dev Magic → shadcn/ui → Context7 → GitHub

Debug chain:
  Sentry → PostgreSQL/SQLite → Sequential Thinking → GitHub

Deploy chain:
  GitHub → Vercel/Cloudflare → n8n → Composio (Slack notify)

Infra chain:
  Terraform → Kubernetes → Prometheus → PagerDuty → GitHub

Research bot chain:
  Exa → Tavily → Firecrawl → mem0 → Notion
```

---

## Free vs Paid

All MCPs marked ✅ Free in README.md work with no credit card. Freemium tools have
generous free tiers sufficient for most solo and small-team projects.

Key fully-free stacks:
- **Full-stack (free)**: GitHub + Context7 + Supabase (free tier) + Vercel (hobby) + Playwright + Sentry (free)
- **Design (free)**: 21st.dev Magic (beta) + shadcn/ui + Figma (dev) + GitHub
- **Research (free)**: OmniSearch + Context7 + Crawl4AI + Memory MCP + Notion

---

## God Mode Checklist (Start of Every Project)

- [ ] Run `/gsd:new-project` to scaffold `.planning/`
- [ ] Write `.planning/PRD.md`
- [ ] Write `.planning/FLOW.md`
- [ ] Write `.planning/TECH.md`
- [ ] Run `/gsd:plan-phase 1`
- [ ] Identify active MCPs → write `.planning/TOOLS.md`
- [ ] Pre-fetch all library docs via Context7
- [ ] Set up Vibe Kanban board
- [ ] Declare active MCPs in first response of every session
