<h1 align="center">⚡ OmniPulse (Agent Reach)</h1>

<p align="center">
  <strong>Give your AI Agent one-click access to the entire live internet</strong>
</p>

<p align="center">
  The unbannable, zero-auth multi-platform intelligence and ingestion engine for AI Agents (Claude Desktop, Cursor, OpenClaw, AutoGPT, and Local LLMs).
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-green.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="https://github.com/mradulsinghal/omnipulse"><img src="https://img.shields.io/badge/Maintained%20by-Mradul%20Singhal-blueviolet?style=for-the-badge" alt="Maintained by Mradul Singhal"></a>
</p>

---

## 🚀 Why OmniPulse?

AI Agents are cognitively brilliant, but sensorially blind when dealing with dynamic live data:

- 🐦 **Twitter / X:** Expensive paywalled APIs ($100–$200/mo) or blocked bots.
- 📖 **Reddit:** Cloudflare & Datadome 403 blocks on server IPs.
- 💼 **LinkedIn:** Strict login walls and ban risks for automated accounts.
- 📺 **YouTube & Media:** Captions and audio difficult to ingest cleanly.
- 🌐 **Dynamic Web:** Cluttered HTML tags instead of token-efficient Markdown.

**OmniPulse solves this with a unified, multi-backend stealth routing engine.**

---

## 🌟 Key Architecture & Capabilities

```text
┌─────────────────────────────────────────────────────────────┐
│                      OMNIPULSE ENGINE                       │
│           (Universal Multi-Platform Ingestion)              │
└──────────────────────────────┬──────────────────────────────┘
                               │
   ┌────────────────┬──────────┴─────┬────────────────┐
   ▼                ▼                ▼                ▼
[Twitter / X]    [Reddit]       [LinkedIn]       [Web & Docs]
• Live tweets    • Subreddits   • Public posts   • Dynamic JS
• Topic trends   • Global search• Author takes   • Clean Markdown
• No API keys    • Real upvotes • Zero login     • Deep Crawler
```

1. **Multi-Backend Fallback Routing:** Automatic failover across primary and stealth secondary endpoints.
2. **Decoupled Client Identity:** 0% account ban risk with zero personal cookie exports.
3. **Model Context Protocol (MCP) Native:** Integrates directly with Claude Desktop, Cursor, and IDEs via JSON-RPC stdio.
4. **Token-Efficient Clean Output:** Strips noise, ads, scripts, and navigation boilerplates for LLM context windows.

---

## ⚡ Quickstart

### 1. Installation
```bash
git clone https://github.com/mradulsinghal/omnipulse.git
cd omnipulse
pip install -e .
```

### 2. Verify Your Environment
Run the built-in diagnostic tool:
```bash
python3 -m agent_reach doctor
```

### 3. CLI Ingestion Commands
```bash
# Search live Twitter / X discussions
python3 -m agent_reach x "DeepSeek V3"

# Fetch top discussions from Reddit
python3 -m agent_reach reddit startups --timeframe week

# Ingest YouTube video transcript
python3 -m agent_reach youtube <VIDEO_URL>

# Crawl dynamic webpage to Markdown
python3 -m agent_reach web https://example.com
```

---

## 🤖 Connect to Claude Desktop & Cursor (MCP Setup)

Add the following to your Claude Desktop config file (`~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "omnipulse": {
      "command": "python3",
      "args": ["-m", "agent_reach", "mcp"],
      "cwd": "/path/to/omnipulse"
    }
  }
}
```

---

## 🛡️ Security & Privacy

- **Local Execution:** All requests and local configurations remain strictly on your machine.
- **Open Source:** 100% transparent codebase licensed under the MIT License.

---

## 📜 Acknowledgements & License

- Built & Maintained by **[Mradul Singhal](https://github.com/mradulsinghal)**.
- Licensed under the **MIT License**.
- Built on top of open-source research and contributions from the Agent Reach community.
