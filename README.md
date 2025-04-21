![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg) ![crewai](https://img.shields.io/badge/crewai-%3E%3D0.83.0-ff69b4) ![OpenAI Whisper](https://img.shields.io/badge/openai-whisper-green) ![Gmail API](https://img.shields.io/badge/gmail%20api-v1-yellow)

# meeting_minutes

A GenAI-based toolkit for automating meeting transcription, summarization, sentiment analysis,
action-item extraction, and follow-up email drafting via configurable agent workflows.

---

## Overview

- Transcribe audio meetings into text using OpenAI Whisper
- Summarize transcripts, extract action items, and analyze sentiment
- Generate polished Markdown meeting minutes
- Draft follow-up emails via Gmail API
- Configure agents and tasks through simple YAML files
- Extend functionality with custom tools under `src/meeting_minutes/tools`

---

## Features

| Feature                         | Details                                                                                   |
|---------------------------------|-------------------------------------------------------------------------------------------|
| Transcription                   | Chunk-based WAV processing + Whisper API for crisp, readable transcripts                  |
| Summarization                   | Multi-agent summarizer writes: <ul><li>Concise summary</li><li>Action items</li><li>Sentiment analysis</li></ul> |
| Meeting Minutes Generation      | Seamlessly merges summary, action items & sentiment into a polished Markdown document     |
| Email Drafting                  | GmailTool creates HTML drafts with Markdown-to-HTML conversion                            |
| Config-Driven                   | YAML-based agent & task definitions — tweak prompts & workflows in seconds                |
| Extensibility                   | Drop in custom tools under `src/meeting_minutes/tools` to enhance capabilities            |
| Dev-Friendly                    | Pydantic models, Python 3.10+, pre-configured CLI via `crewai run`                       |

---

## Tech Stack

| Technology          | Purpose                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Python 3.10+        | Core language                                                          |
| crewAI              | Agent orchestration & workflow management                               |
| OpenAI Whisper API  | High-quality audio transcription                                        |
| pydub               | Audio chunking & processing                                             |
| Pydantic            | Data validation & state management                                      |
| Google Gmail API    | Programmatic email drafting                                             |
| YAML                | Agent & Task configuration                                               |

---

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/tanny1412/meeting_minutes_crewai.git
cd meeting_minutes

# 2. Install dependencies
pip install uv crewai[tools] pydub openai google-api-python-client

# 3. Set up credentials
# - Add your OPENAI_API_KEY to a .env file.
# - Place Gmail OAuth credentials.json in src/meeting_minutes/crews/gmailcrew/tools/

# 4. Run!
crewai run
```

Generated outputs will appear:
- `summary.txt` — meeting summary  
- `action_items.txt` — bulletized tasks  
- `sentiment.txt` — tone analysis  
- Draft email ID in console log  

---

## Configuration

1. **Agents**: `src/meeting_minutes/crews/*/config/agents.yaml`  
2. **Tasks**: `src/meeting_minutes/crews/*/config/tasks.yaml`  
3. **Flow Logic**: `src/meeting_minutes/main.py`  
4. **Custom Tools**: add modules under `src/meeting_minutes/tools/`  
5. **Prompts**: Tune in YAML to adapt roles, goals, and backstories  

---

## How It Works

```mermaid
flowchart TD
    A[Load audio file] --> B[Chunk audio (1 min)]
    B --> C[Transcribe with Whisper]
    C --> D[Summarize transcript]
    D --> E[Save summary, actions, sentiment]
    E --> F[Generate Markdown minutes]
    F --> G[Draft email via Gmail]
```

---

## Use Cases

- Automated stand-up recap for remote teams  
- Investor call summarization & follow-up  
- Customer support call analytics  
- Podcast transcription & highlight reel generation  

---

## Contributing

1. Fork the repo & create a feature branch  
2. Add or update tools/agents/tasks  
3. Run `pre-commit run --all-files`  
4. Submit a PR with detailed description  

Contributions welcome.
---
