---
marp: true
theme: dracula
paginate: true
---

<style>
.bottom {
  position: absolute;
  bottom: 3em;
  left: 3em;
}
.center {
  position: absolute;
  bottom: 8em;
  left: 3em;
}
.smaller {
  font-size: .6em;
  line-height: 1.3;
}
.compact {
  font-size: .8em;
  line-height: 1.2;
}
pre {
  font-size: 1.0em !important;
  line-height: 1.4 !important;
}
code {
  font-size: 1.0em !important;
  line-height: 1.4 !important;
}
</style>

![bg right 80%](assets/undraw_ai-agent_pdkp.svg)

<div class="center">

# AI Developer Day

</div>

---

<div class="center">

# AI Developer Day
<br><br>

</div>

![bg right 80%](./assets/undraw_vibe-coding_mjme.svg)

<div class="bottom">

**Instructors:**
Patrick O'Connor
Garrett Smith
</div>


---

# Reminder

Today's class is intended for developers. We'll provide support along the way, but expect all attendees to be able to:
* **Run commands in terminal/command line** - Navigate directories, execute scripts, and use basic shell commands
* **Write and understand code** - Comfortable with at least one programming language (Python or TypeScript/JavaScript)
* **Use Git/GitLab/GitHub** - Clone repositories, create branches, and make commits  

---

## Today's Agenda

![bg right:40% fit](./assets/undraw_schedule_ry1w.svg)

* **Session 1:** Setup & Environment
* **Session 2:** Vibe Coding Fundamentals
* **Session 3:** Advanced Techniques
* **Session 4:** MCP Ecosystem

---

# Survey

![bg right 80%](./assets/qr-survey.png)

Scan the QR code or visit:


[https://forms.office.com/r/iX1MDRW50E](https://forms.office.com/r/iX1MDRW50E)</div>


---

# Session 1: Setup & Environment

![bg right:40% fit](./assets/undraw_dev-environment_n5by.svg)

- Environment setup & validation
- AI development assistants comparison
- Getting started with Cursor 2.0

---

## Getting Started

![bg right:40% fit](./assets/undraw_preparation_59f0.svg)

Welcome to Cursor!
Your account has been provisioned!

Follow the Cursor setup in the email labeled `Action Required`

---

## Lab Resources
We've compiled slides, documentation, and code for labs into a workshop repository.

Please choose either Gitlab or Github:
- [github.disney.com/ai-workshops/ai-developer-day](https://github.disney.com/ai-workshops/ai-developer-day)
- [gitlab.disney.com/ai-workshops/ai-developer-day](https://gitlab.disney.com/ai-workshops/ai-developer-day)
---

## Environment Validation

![bg right:40% fit](./assets/undraw_correct-answer_vjt7.svg)

**Test your setup via Cursor:**

- Ask Cursor to help you create a simple script (e.g. fizzbuzz in bash or powershell)
- Test basic file operations (read, write, edit)
- Verify Cursor can execute bash commands

---

## AI Development Tools Comparison

![bg right:40% fit](./assets/undraw_choose-card_es1o.svg)

- **Cursor 2.0** vs **Claude** vs <br/>**Q-Developer** vs **GitHub Copilot**
- Same models, different developer experience
- Understanding strengths of each tool

---

# Session 2: Vibe Coding Fundamentals

![bg right:40% fit](./assets/undraw_lightbulb-moment_16av.svg)

Master the art of collaborating effectively with AI development tools

---

## Context in AI Development

![bg right:30% fit](./assets/undraw_chat-with-ai_ir62.svg)

Providing the right context:
- **Errors** and stack traces
- **Browser interactions**
- **Images** and screenshots
- **Data** and schemas
- **Documentation** and standards
---

## Exercise

![bg right:40% fit](./assets/undraw_add-file_lf11.svg)

Providing the right context:

- **Docs** - [Wiz AI secure rules](https://github.com/wiz-sec-public/secure-rules-files)

- **Images** - drag and drop to chat

---


## Context Management

![bg right:40% fit](./assets/undraw_our-solution_qv3b.svg)

- Context approaches evolve (large conversation vs targeted)
- Cursor 2.0 maintains context within chat sessions
- Context tied to conversations
- Chat history automatically preserved

---

## Exercise: Context Exploration

![bg right:40% fit](./assets/undraw_settings_2quf.svg)

- Close and reopen Cursor 2.0
- Access previous chat conversations from history
- Explore chat panel management (sidebar navigation)

💭 Question: When does Cursor's context gets truncated/summarized?

---

## Composer: Cursor's Proprietary Model

![bg right:20% fit](./assets/undraw_multiple-choice_9n00.svg)

- **Composer** - Agentic coding model (4x faster, tasks in <30s)
- **200,000 token context** (~15,000 lines of code)
- Trained on real-world software engineering challenges
- Optimized for interactive development workflows

---

## Model Selection Options

![bg right:30% fit](./assets/undraw_settings_2quf.svg)
- **Auto** - Cursor selects optimal premium model automatically
- **Frontier models** - GPT-5, Claude
- **Max Mode** - Extended context window (slower, higher cost)
- Balance speed, intelligence, and cost per use case

---


## Handling Inconsistency

![bg right:40% fit](./assets/undraw_brainstorming_gny9.svg)

**Interactive Exercise in Composer Mode (`Cmd+I` / `Ctrl+I`):**

*"How would you build a simple script that finds all available pets in the swagger petstore api, and how would you test it works?"*

---

## Rules and Project Guidelines

![bg right:30% fit](./assets/undraw_text-files_tqjw.svg)

**Rules provide consistency:**
- *"Our APIs are built with language X, framework Y, using testing approach Z"*
- Configured via `.cursor/rules/` directory with `.mdc` files
- Project-specific rules with multiple files for organization

---

## Exercise: Creating Rules

![bg right:30% fit](./assets/undraw_add-file_lf11.svg)

- Navigate to **Cursor Settings > Rules**
- Creates `.mdc` files in `.cursor/rules/` directory
- Add project rules and guidelines
- Rerun previous development plan with rules
- Compare results with and without constraints

---

## Memory Management

![bg right:30% fit](./assets/undraw_mind-map_i9bv.svg)

**Cursor 2.0 Memories**
- **Auto-saved memories** - Cursor learns from your corrections and preferences
- **Manual memories** - Add explicit facts, constraints, or context
- **Smart context attachment** - Memories automatically included when relevant

---

## Exercise: Adding Memory

![bg right:20% fit](./assets/undraw_my-files_1xwx.svg)

Add tribal knowledge via Cursor Rules

**Configuration options:**
- Creates `.mdc` files in `.cursor/rules/` directory
- Include project-specific guidelines and patterns
- Rule types: Always, Auto Attached, Agent Requested, Manual

---

## Core Tools Overview

![bg right:40% fit](./assets/undraw_web-app_141a.svg)


- **Read and write files** in your codebase
- **Search through code** to find relevant functions or patterns
- **Run shell commands** to test code or install packages
- **Access documentation** or **search the web** for current information
- Check for errors by **running linters or tests**


---

### Hands-on Lab: First Vibe Coding

![bg right:30% fit](./assets/undraw_preparation_59f0.svg)

**Getting Started:**
- Create new repository/folder (e.g.,`ai-day-lab`)
- Open Cursor in that folder
- Open Composer mode in Cursor (`Cmd+I` / `Ctrl+I`)
- Ready to vibe!

---

## Lab Prompt

![bg right:40% fit](./assets/undraw_got-an-idea_1z3i.svg)

<div class="center">

**Your Mission:** Create a simple website to demonstrate the API at:
https://github.com/cheatsnake/emojihub

</div>

---

## Lab: Development Phase

![bg right:40% fit](./assets/undraw_developer-activity_4zqd.svg)

- Plan out the work
- Use Chat mode for iterative development (`Cmd+L` / `Ctrl+L`)
- Build with Cursor's guidance
- Watch the magic happen!

<div class="compact">
<div class="bottom">

Your Mission: Create a simple website to demonstrate the API at:
https://github.com/cheatsnake/emojihub

</div></div>

---

## Lab: Finishing Strong

![bg right:40% fit](./assets/undraw_proud-designer_1rcm.svg)

- Test thoroughly
- Run and see your creation
- Celebrate success!
- Incorporate into SDLC (commits, issues, MR/PR)

---

# Break

![bg right:40% fit](./assets/undraw_vibe-coding_mjme.svg)

---

# Session 3: Advanced Techniques

![bg right:40% fit](./assets/undraw_vibe-coding_mjme.svg)

Level up your AI development skills

---

## Token Usage Monitoring

![bg right:40% fit](./assets/undraw_progress-indicator_c14b.svg)

- **Usage dashboard** → Monitor token usage (Settings)
- **Optimization Strategies** → Rules, Project Requirements, Documentation

---

## Optimizing Token Usage

![bg right:40% fit](./assets/undraw_loading_3kqt.svg)

- **Limit data/queries** → Reduce costs
- **Scoped Development** → Stay focused
- **Local DB caching** → Speed + savings
- **ASCII mockup planning** → Cost effective and quick

---

## Exercise: UI Refactoring

![bg right:40% fit](./assets/undraw_in-the-zone_07y7.svg)

- Return to your lab repo project
- Propose UI refactor in Browser Tab Mode
- Provide feedback before Cursor builds

---

## Advanced Lab Setup

![bg right:30% fit](./assets/undraw_setup-wizard_wzp9.svg)

- **Lab Setup** → [Lab Setup Docs](./instructions/lab-repos-setup.md)
- **Docker Desktop** → [Docker Setup Docs](./instructions/docker-setup.md)

---

## Planning Strategies

![bg right:40% fit](./assets/undraw_idea_hz8b.svg)

- **Plan Mode** → Think before coding (multi-file edits)
- **Chat Mode** → Iterative development and Q&A
- **Spec Files** → Clear requirements
- Break work into manageable pieces

---

## Exercise: Project Documentation

![bg right:40% fit](./assets/undraw_to-do-list_o3jf.svg)

Create markdown documents for a project pivot:

- Product Requirements Document
- Epic Spec
- Feature breakdown
- Story format

---

## Multi-Agent Systems Introduction

![bg right:30% fit](./assets/undraw_visionary-technology_f6b3.svg)

- Multiple AI agents with specialized roles
- Like a dev team: frontend, backend, QA, DevOps
- Specialized agents focus on their strengths
- Workspace setup

---

## Multi-Agent Use Cases

![bg right:40% fit](./assets/undraw_working-together_r43a.svg)

- **Code review workflows**: Writer + reviewer agents
- **Complex systems**: UI + API + database agents
- **Testing scenarios**: Generation + execution + analysis
- **Documentation**: Code + docs + review agents

---

## Agent Coordination Strategies

![bg right:29% fit](./assets/undraw_deliveries_qutl.svg)

#### Coordination Patterns

- **Sequential**: Agent A → Agent B → Agent C
- **Parallel**: Multiple agents simultaneously
- **Hierarchical**: Supervisor managing workers

---

## Benefits & Considerations

![bg right:20% fit](./assets/undraw_ideation_r1g5.svg)

**Benefits:**

- Specialization and focused expertise
- Parallel Development

**Considerations:**

- Coordination complexity
- Communication overhead

---

## Multi - Agent Labs

![bg right:30% fit](./assets/undraw_work-in-progress_m95a.svg)

Apply multi-agent concepts to enhance your project:

- Agent creation and coordination
- Planning phase with multiple perspectives
- Development
- QA Testing

---

## Lab: Agent Setup

![bg right:30% fit](./assets/undraw_master-plan_m8ym.svg)

Ask agent to create an AGENTS.md file for the following agent personas:

- Planning Agent: writes clear product requirements for each agent.
- Developer Agent: writes code based on product requirements.
- QA Agent: Writes tests and verifies functionality of code based on product requirements.

---

## Lab: Put The Agents to Work

![bg right:30% fit](./assets/undraw_firmware_3fxd.svg)

Enhancement Request: 

**Implement a "list all movies" endpoint with filters for each field and fuzzy search capabilities.**

---
# Break

![bg right:40% fit](./assets/undraw_vibe-coding_mjme.svg)


__MCP labs will require `node` specifically `npx`. We will show this, but if you want to do this yourself, use the break to get setup (optional)__

---

# Session 4: MCP Ecosystem

![bg right:40% fit](./assets/undraw_chat-with-ai_ir62.svg)

Explore the Model Context Protocol

---

## What is Model Context Protocol?

![bg right:40% fit](./assets/undraw_chat-with-ai_ir62.svg)

**MCP** is an open protocol connecting AI applications to data sources and systems

**Learn more:** [modelcontextprotocol.io](https://modelcontextprotocol.io)

---

## How MCP Works

![bg right:40% fit](./assets/undraw_working-together_r43a.svg)

- **Client** → AI application (Cursor, Claude, VS Code, etc.)
- **Server** → Data source or tool integration
- **Protocol** → Standard communication layer

**Result:** AI gets live access to your tools and data

---

## Why MCP?

![bg right:40% fit](./assets/undraw_lightbulb-moment_16av.svg)

**The Problem:**
- AI models have static, outdated data

**The Solution:**
- Live connections to your tools and data

---

## MCP Ecosystem

![bg right:40% fit](./assets/undraw_deliveries_qutl.svg)

- **9** Official SDKs
- **1000+** Available Servers
- **70+** Compatible Clients

---

## MCP Use Cases

![bg right:40% fit](./assets/undraw_dev-productivity_5wps.svg)

- **Development** → Code repos, databases, APIs
- **Productivity** → Calendar, email, tasks
- **Analysis** → Real-time metrics, logs, monitoring
- **Creative** → Design tools, asset libraries, CMS

---

## Off-the-Shelf MCP Servers

![bg right:40% fit](./assets/undraw_file-search_cbur.svg)

**Playwright** - Browser automation
**Context7** - Up-to-date software documentation

---

## MCP Protocols

![bg right:40% fit](./assets/undraw_progressive-app_9517.svg)

**Three transport protocols:**
- **STDIO** - Standard input/output (local)
- **HTTP** - RESTful communication (remote)
- **SSE** - Server-sent events (streaming)

---

## Why MCP vs CLI/REST?

![bg right:40% fit](./assets/undraw_questions_g2px.svg)

**Advantages:**
- Standardized protocol for AI tools
- Built-in schema validation
- Better context management
- Native AI tool integration

---

## Building Custom MCP Servers

![bg right:29% fit](./assets/undraw_typing-code_6t2b.svg)

**Create servers that expose:**
- **Tools** - Functions AI can call
- **Resources** - Data AI can access
- **Prompts** - Reusable prompt templates

---

## MCP Building Tools

![bg right:35% fit](./assets/undraw_the-search_cjxa.svg)

**MCP Inspector**
- Local testing and debugging
- Interactive tool testing
- Schema validation

[github.com/modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)

---

## Hands-on Lab: Build Your MCP Server

![bg right:30% fit](./assets/undraw_work-in-progress_m95a.svg)

**What We'll Build:**
- Custom MCP server with multiple tools
- Local testing with MCP Inspector
- Cursor 2.0 integration
- Choose Python or TypeScript

**Time:** ~45 minutes

---

## Lab Exercise Structure

![bg right:30% fit](./assets/undraw_ideation_r1g5.svg)

1. **Setup** (5 min) - Environment and dependencies
2. **Basic Server** (15 min) - On Movie API Repo
3. **Add Tools** (20 min) - Add Movie MCP
4. **Test** (10 min) - MCP Inspector testing
5. **Integrate** (10 min) - Add to Cursor 2.0

---

## Group Discussion and Q&A

![bg right:40% fit](./assets/undraw_chat-bot_c8iw.svg)

- Share experiences
- Address challenges
- Best practices discussion

---

## Thank You

![bg right:40% fit](./assets/undraw_going-upwards_0y3z.svg)

**Next Steps:**

- Apply learned concepts
- Experiment with different approaches
- Build custom MCP servers
- Share knowledge with your teams

---

## Resources

![bg right:40% fit](./assets/undraw_bookmarks_i66k.svg)

- **Cursor 2.0 Docs**: [docs.cursor.com](https://docs.cursor.com)
- **MCP Protocol**: [modelcontextprotocol.io](https://modelcontextprotocol.io)
- **Workshop Repo**: Internal GitLab/GitHub
- **Setup Guide**: [MCP-Setup.md](./MCP-Setup.md)
