# 🔎 InsightCrew — Multi-Agent AI Research & Decision Intelligence System

> A multi-agent AI system that researches real-world topics using web search, analyzes the collected information, and generates a structured decision-oriented report.

InsightCrew is an AI-powered research and decision intelligence system built using **CrewAI**. It uses specialized AI agents that collaborate sequentially to transform a user's research question into a structured report.

The system combines **CrewAI multi-agent orchestration**, **Ollama local LLMs**, and **Tavily Web Search** to perform research using up-to-date web information.

---

## 🚀 Overview

Traditional AI assistants can answer questions, but complex research tasks often require multiple steps:

1. Finding relevant information
2. Collecting current data
3. Identifying trends and patterns
4. Analyzing opportunities and risks
5. Producing a structured conclusion

InsightCrew divides these responsibilities among specialized AI agents.

### Example Query

```text
Should a startup invest in India's EV charging market in 2027?


                    ┌─────────────────────┐
                    │        User         │
                    │   Research Query    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Research Agent    │
                    │                     │
                    │ Researches topic   │
                    │ using web search    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Tavily Web Search  │
                    │                     │
                    │ Current web data    │
                    │ and sources         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Data Analyst Agent  │
                    │                     │
                    │ Numbers             │
                    │ Trends              │
                    │ Patterns            │
                    │ Risks               │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Report Agent     │
                    │                     │
                    │ Combines research   │
                    │ and analysis        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Final Report      │
                    │                     │
                    │ Insights + Risks +  │
                    │ Recommendation      │
                    └─────────────────────┘


🤖 Multi-Agent Workflow

InsightCrew currently uses three specialized agents.

1. 🔎 Research Agent
Role

Research Specialist

Responsibilities
Understand the user's research topic
Search the web for relevant information
Collect recent facts and developments
Identify opportunities and challenges
Organize research findings
Tool

Tavily Web Search

The Research Agent can dynamically call the web search tool when external information is required.

2. 📊 Data Analyst Agent
Role

Data Analysis Specialist

Responsibilities
Analyze research findings
Identify important numbers and statistics
Find trends and patterns
Compare relevant information
Identify opportunities and risks
Convert research into useful analytical insights


3. 📝 Report Agent
Role

Senior Decision Report Analyst

Responsibilities :
Combine research and analysis
Organize findings into a professional report
Highlight opportunities and risks
Provide final insights
Generate a decision-oriented recommendation


🛠️ Tech Stack

Technology	Purpose
Python	Core programming language
CrewAI	Multi-agent orchestration
Ollama	Local LLM runtime
Llama 3.2	Local language model
Tavily	Web search and research
YAML	Agent and task configuration
UV	Python environment and dependency management


insight_crew/
│
├── src/
│   └── insight_crew/
│       │
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       │
│       ├── tools/
│       │   ├── __init__.py
│       │   └── web_search_tool.py
│       │
│       ├── __init__.py
│       ├── crew.py
│       └── main.py
│
├── tests/
│
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md


