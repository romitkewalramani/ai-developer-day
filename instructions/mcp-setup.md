# Model Context Protocol (MCP) Setup Guide

Set up MCP servers for Cursor 2.0: **Context7** (documentation) and **Playwright** (browser automation).

**MCP** connects AI applications to data sources and tools. [Learn more](https://modelcontextprotocol.io)

## Prerequisites

- **Node.js 18+** (verify with `node --version`)
- **Cursor 2.0** installed and configured
- **Internet access**

---

## Playwright MCP

Browser automation for testing, scraping, and web interaction.

### Installation

1. Open **Cursor Settings** (`Cmd+,` / `Ctrl+,`) → **Features** → **MCP**
2. Add this configuration to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    }
  }
}
```

3. **Restart Cursor 2.0**

### Test It

Ask Cursor: *"Navigate to https://example.com and take a screenshot"*

### Troubleshooting

- **Won't connect**: Check Node.js 18+, restart Cursor
- **Browser issues**: Run `npx playwright install`

---

## Context7 MCP

Access up-to-date documentation and code examples for programming libraries.

### Installation

1. Open **Cursor Settings** (`Cmd+,` / `Ctrl+,`) → **Features** → **MCP**
2. Add this configuration to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

3. **Restart Cursor 2.0**

### Test It

Ask Cursor: *"Get React documentation for useState hook"* or *"Show me Express.js routing examples"*

---

## Troubleshooting

**MCP server won't connect:**
- Verify Node.js 18+: `node --version`
- Test package: `npx @playwright/mcp@latest --help` or `npx @upstash/context7-mcp@latest --help`
- Restart Cursor completely
- Check JSON syntax in `~/.cursor/mcp.json`

**Tools not available:**
- Restart Cursor
- Verify configuration file syntax
- Ask Cursor explicitly to use the MCP tool

---

## Quick Reference

**Configuration file**: `~/.cursor/mcp.json`

**Both servers in one file:**
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"]
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

---

*This guide is part of Disney's AI Developer Day Workshop materials. For questions, contact the workshop instructors.*
