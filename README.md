# 🔎 InsightCrew — Multi-Agent AI Research & Decision Intelligence System

An **AI-powered multi-agent research and decision intelligence system** built using **CrewAI, Python, Ollama, Llama 3.2, Tavily, and YAML-based agent configuration**.

InsightCrew uses multiple specialized AI agents to research a given topic, analyze the collected information, identify important trends and risks, and generate a structured decision-oriented report.

## 🚀 Features

- 🤖 Multi-agent AI architecture using CrewAI
- 🔎 Web-based research using Tavily
- 🌐 Access to current and relevant information
- 📊 Automated data and trend analysis
- 📝 Structured decision report generation
- 🧠 Local LLM inference using Ollama
- 🦙 Llama 3.2 support
- 🔗 Sequential multi-agent workflow
- ⚙️ YAML-based agent and task configuration
- 🔐 Environment variable support for API keys
- 💻 Interactive command-line interface
- 📌 Specialized agents with different responsibilities
- 🔄 Agent-to-agent task flow

---

## 🏗️ System Architecture

```text
                         User
                           │
                           ▼
                    Enter Topic
                           │
                           ▼
                  ┌─────────────────┐
                  │  Research Agent │
                  └────────┬────────┘
                           │
                           ▼
                    Tavily Web Search
                           │
                           ▼
                 Research Findings
                           │
                           ▼
                 ┌──────────────────┐
                 │  Data Analyst    │
                 │      Agent       │
                 └────────┬─────────┘
                          │
                          ▼
                  Data & Trend Analysis
                          │
                          ▼
                 ┌──────────────────┐
                 │   Report Agent   │
                 └────────┬─────────┘
                          │
                          ▼
                 Final Decision Report
```

---

## 🔄 Agent Workflow

```text
User Topic
    │
    ▼
Research Agent
    │
    ├── Web Search
    ├── Current Information
    ├── Facts
    ├── Opportunities
    └── Challenges
    │
    ▼
Data Analyst Agent
    │
    ├── Numbers
    ├── Trends
    ├── Comparisons
    ├── Risks
    └── Insights
    │
    ▼
Report Agent
    │
    ├── Executive Summary
    ├── Research Findings
    ├── Data & Trends
    ├── Opportunities
    ├── Risks
    ├── Insights
    └── Recommendation
    │
    ▼
Final Report
```

---

## 🤖 AI Agents

### 🔎 1. Research Agent

The Research Agent is responsible for collecting relevant information about the given topic.

**Responsibilities:**

- Search the web for current information
- Collect important facts
- Identify recent developments
- Find opportunities
- Identify challenges
- Organize research findings

The agent uses the **Tavily Web Search Tool** to access online information.

---

### 📊 2. Data Analyst Agent

The Data Analyst Agent analyzes the findings collected by the Research Agent.

**Responsibilities:**

- Identify important numbers
- Analyze statistics
- Detect trends and patterns
- Perform comparisons
- Identify opportunities
- Identify risks
- Generate analytical insights

---

### 📝 3. Report Agent

The Report Agent converts the research and analysis into a professional decision-oriented report.

The final report contains:

1. Executive Summary
2. Topic Overview
3. Key Research Findings
4. Data and Trends
5. Opportunities
6. Risks and Challenges
7. Final Insights
8. Recommendation

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| CrewAI | Multi-agent AI orchestration |
| Ollama | Local LLM runtime |
| Llama 3.2 | Local language model |
| Tavily | Web search and information retrieval |
| PyYAML | Agent and task configuration |
| python-dotenv | Environment variable management |
| uv | Python dependency and project management |

---

## 📂 Project Structure

```text
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
├── .env.example
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

> The `.env` file contains private API keys and should never be committed to GitHub.

---

## 🔍 Web Search Tool

InsightCrew uses **Tavily** to provide the Research Agent with web search capabilities.

The Research Agent can search for:

- Current market information
- Recent developments
- Statistics
- Companies
- Technologies
- Competitors
- Industry information
- Other information requiring up-to-date research

The tool returns:

```text
Title
Content
Source URL
```

The Research Agent then uses these results to prepare its research findings.

---

## ⚙️ How It Works

### 1. User Provides a Topic

The user enters a topic through the command-line interface.

Example:

```text
Should a startup invest in India's EV charging market in 2027?
```

---

### 2. Research Agent Performs Web Search

The Research Agent receives the topic and uses the Tavily Web Search Tool.

```text
User Topic
     ↓
Research Agent
     ↓
Tavily Web Search
     ↓
Search Results
     ↓
Research Findings
```

---

### 3. Data Analyst Processes the Research

The research findings are passed to the next task.

The Data Analyst Agent examines the information and identifies:

```text
Numbers
Trends
Patterns
Comparisons
Opportunities
Risks
Insights
```

---

### 4. Report Agent Generates Final Report

The final agent combines the research and analysis.

```text
Research Findings
        +
Data Analysis
        ↓
   Report Agent
        ↓
 Final Decision Report
```

---

## 🧠 CrewAI Process

The current system uses a **sequential process**.

```text
Research Agent
       ↓
Data Analyst Agent
       ↓
Report Agent
```

Each task is completed before the next task begins.

The workflow is configured using:

```python
Process.sequential
```

---

## 📋 Agent Configuration

Agents are defined in:

```text
src/insight_crew/config/agents.yaml
```

Example:

```yaml
research_agent:
  role: >
    Research Specialist

  goal: >
    Conduct thorough research on the given topic and collect
    relevant, reliable, and useful information.

data_analyst_agent:
  role: >
    Data Analysis Specialist

  goal: >
    Analyze the research findings and identify important
    data, trends, patterns, and insights.

report_agent:
  role: >
    Senior Decision Report Analyst

  goal: >
    Combine research and data analysis into a clear,
    structured, evidence-based final report.
```

---

## 📝 Task Configuration

Tasks are defined in:

```text
src/insight_crew/config/tasks.yaml
```

The main tasks are:

```text
research_task
      ↓
data_analysis_task
      ↓
report_task
```

The topic is dynamically passed to the system using:

```python
inputs = {
    "topic": user_topic
}
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
OLLAMA_BASE_URL=http://localhost:11434
TAVILY_API_KEY=your_tavily_api_key
```

Never upload your actual `.env` file or API keys to GitHub.

Create a `.env.example` file:

```env
OLLAMA_BASE_URL=http://localhost:11434
TAVILY_API_KEY=your_tavily_api_key_here
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Shreya9996/insight-crew.git
```

### 2. Navigate to the Project

```bash
cd insight-crew
```

### 3. Install Dependencies

This project uses `uv` for dependency management.

```bash
uv sync
```

---

## 🦙 Setup Ollama

Install Ollama and make sure it is running locally.

Check Ollama:

```bash
ollama list
```

Download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

You can also test the model:

```bash
ollama run llama3.2
```

The project uses:

```text
Model: llama3.2
Base URL: http://localhost:11434
```

---

## 🔐 Configure Tavily

Create a Tavily API key and add it to your `.env` file.

```env
TAVILY_API_KEY=your_tavily_api_key
```

The Research Agent uses this key to perform web searches.

---

## ▶️ Run the Application

Start the CrewAI application using:

```bash
crewai run
```

The application will ask for a topic.

Example:

```text
======================================
   AI Research & Insight System
======================================

Enter Your Topic :
```

Enter:

```text
Should a startup invest in India's EV charging market in 2027?
```

---

## 💬 Example

### User Input

```text
Enter Your Topic :
Should a startup invest in India's EV charging market in 2027?
```

### Research Agent

```text
Researching the Indian EV charging market...

Searching for:
- EV adoption
- Charging infrastructure
- Market growth
- Government policies
- Investment opportunities
- Industry challenges
```

### Data Analyst

```text
Analyzing research findings...

Identifying:
- Market trends
- Important statistics
- Growth opportunities
- Risks
- Industry patterns
```

### Report Agent

```text
Generating final decision report...
```

### Final Output

```text
======================================
           FINAL REPORT
======================================

Executive Summary

Topic Overview

Key Research Findings

Data and Trends

Opportunities

Risks and Challenges

Final Insights

Recommendation
```

---

## 🎯 Example Use Cases

InsightCrew can be used for decision-oriented research such as:

```text
Should a startup invest in India's EV charging market in 2027?

Should a company enter the AI healthcare market?

Should a startup build an AI-powered education platform?

Is a particular technology suitable for a new business?

Which market provides better investment opportunities?

What are the major risks in a particular industry?

Which technology should a startup adopt?
```

---

## 🌟 Key Features

### Multi-Agent Architecture

Instead of asking one AI agent to perform everything, InsightCrew divides the problem into specialized responsibilities.

```text
Research
   ↓
Analysis
   ↓
Decision Report
```

### Tool-Enabled Agent

The Research Agent has access to an external web search tool.

```text
Research Agent
      ↓
Web Search Tool
      ↓
Tavily
      ↓
Internet Search Results
```

### Local LLM

The project uses Ollama to run the Llama 3.2 model locally.

```text
CrewAI
   ↓
Ollama
   ↓
Llama 3.2
```

### YAML-Based Configuration

Agent roles, goals, backstories, and tasks are separated from Python logic.

```text
agents.yaml
     ↓
Agent Configuration

tasks.yaml
     ↓
Task Configuration
```

---

## 🔮 Future Improvements

- [ ] Add Competitor Analysis Agent
- [ ] Add Fact Checker Agent
- [ ] Add source credibility scoring
- [ ] Add citation generation
- [ ] Add advanced web search tools
- [ ] Add multiple research sources
- [ ] Add RAG-based knowledge retrieval
- [ ] Add vector database support
- [ ] Add long-term agent memory
- [ ] Add conversational memory
- [ ] Add human approval workflow
- [ ] Add decision scoring system
- [ ] Add FastAPI backend
- [ ] Add React frontend
- [ ] Add report export to PDF
- [ ] Add structured JSON output
- [ ] Add authentication
- [ ] Deploy the application as a web service

---

## 🛡️ Security

API keys and environment variables should never be committed to GitHub.

The `.gitignore` file should include:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
*.log
.vscode/
.idea/
```

Use `.env.example` to document the required environment variables without exposing actual credentials.

---

## ⚠️ Current Limitations

The current version has some limitations:

- The system currently uses three agents.
- Research quality depends on web search results.
- Search results may contain irrelevant or low-quality sources.
- The system does not yet have a dedicated fact-checking agent.
- The system does not yet perform advanced source credibility scoring.
- The system does not maintain long-term memory.
- The application currently runs through the command line.
- The final report is generated as text and is not yet exported automatically to PDF.
- The system currently uses a sequential workflow.

---

## 🧩 Planned Architecture

The future version can expand the current architecture into a more advanced decision intelligence system.

```text
                         User
                           │
                           ▼
                     Manager Agent
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
        Research       Data Analyst   Competitor
          Agent           Agent        Agent
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                    Fact Checker
                           │
                           ▼
                  Decision Agent
                           │
                           ▼
                   Report Generator
                           │
                           ▼
                     Final Report
```

---

## 📚 Learning Outcomes

This project helped implement and understand:

- Multi-agent AI systems
- CrewAI framework
- Agent and task design
- Sequential agent workflows
- Tool-enabled AI agents
- Web search integration
- Local LLM integration
- Ollama
- Llama 3.2
- YAML-based configuration
- Prompt engineering
- Agent-to-agent task flow
- Environment variable management
- AI-based decision intelligence

---

## 🎓 Project Goal

The main goal of InsightCrew is to demonstrate how multiple specialized AI agents can collaborate to solve a complex research and decision-making problem.

Instead of:

```text
User
  ↓
Single AI Agent
  ↓
Answer
```

InsightCrew follows:

```text
User
  ↓
Research Agent
  ↓
Data Analyst Agent
  ↓
Report Agent
  ↓
Decision-Oriented Report
```

This architecture can later be extended into a more advanced **Agentic AI system** with memory, RAG, additional tools, human approval, APIs, and a web interface.

---

## 👩‍💻 Author

**Shreya Patil**

B.Tech Computer Science Engineering Student

Interested in:

**Data Science • Machine Learning • Generative AI • Agentic AI • Automation**

---

## ⭐ Acknowledgement

This project was developed as a practical implementation of **Multi-Agent AI systems using CrewAI**, with local LLM inference through **Ollama** and web research capabilities through **Tavily**.

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is intended for **educational, learning, and research purposes**.
