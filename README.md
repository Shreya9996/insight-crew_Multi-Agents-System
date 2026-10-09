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


# 🔍 InsightCrew — Multi-Agent AI Research & Decision Intelligence System

An AI-powered multi-agent research system built using **CrewAI** and **Google Gemini** that researches a given topic, analyzes competitors, evaluates evidence, fact-checks claims, and generates a structured research report to support better decision-making.

## 🚀 Overview

InsightCrew automates the research and analysis process using multiple specialized AI agents. Each agent performs a specific task and contributes to a final research report.

Instead of relying on a single AI agent, InsightCrew divides the workflow into specialized roles to improve research organization, evidence evaluation, and decision support.

## ✨ Key Features

* 🤖 **Multi-Agent Architecture** — Multiple specialized AI agents collaborate on one research task.
* 🔎 **Web Research** — Searches the web for relevant information and sources.
* 🏢 **Competitor Analysis** — Identifies competitors and compares their offerings.
* 📊 **Data Analysis** — Organizes available findings and identifies useful insights.
* ✅ **Fact Checking** — Reviews claims and distinguishes verified facts from uncertain information.
* 🧠 **Decision Intelligence** — Generates recommendations based on collected evidence.
* 📝 **Automated Report Generation** — Produces a structured report in Markdown format.
* 🔗 **Source-Based Research** — Aims to include source URLs to support findings.

## 🏗️ System Architecture

InsightCrew uses a sequential multi-agent workflow.

```text
                 ┌──────────────────────┐
                 │    Research Topic    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Research Agent     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Competitor Agent     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Data Analyst Agent   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Fact Checker Agent   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Decision Agent       │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    Report Agent      │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ output/output.md     │
                 └──────────────────────┘
```

## 👥 AI Agents

| Agent              | Responsibility                                                         |
| ------------------ | ---------------------------------------------------------------------- |
| Research Agent     | Collects background information and relevant research findings.        |
| Competitor Agent   | Identifies competitors and compares products, services, or strategies. |
| Data Analyst Agent | Organizes research findings and analyzes available information.        |
| Fact Checker Agent | Evaluates claims and checks supporting evidence.                       |
| Decision Agent     | Develops insights and recommendations from the findings.               |
| Report Agent       | Compiles the final findings into a structured Markdown report.         |

## 🛠️ Technology Stack

* **Python** — Core programming language
* **CrewAI** — Multi-agent orchestration framework
* **Google Gemini** — Large language model for AI agent reasoning
* **DuckDuckGo Search** — Web search through the configured search tool
* **uv** — Python dependency and project management
* **Markdown** — Research report output format

## 📁 Project Structure

```text
insight_crew/
│
├── src/
│   └── insight_crew/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       │
│       ├── tools/
│       │   └── web_search_tool.py
│       │
│       ├── crew.py
│       └── main.py
│
├── output/
│   └── output.md
│
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Shreya9996/insight-crew_Multi-Agents-System.git
```

### 2. Navigate to the Project Directory

```bash
cd insight-crew_Multi-Agents-System
```

### 3. Install Python

Use Python **3.11** for the development environment described in this project.

Check your Python version:

```bash
python --version
```

### 4. Install uv

If `uv` is not installed, install it using:

```bash
pip install uv
```

Verify the installation:

```bash
uv --version
```

### 5. Install Project Dependencies

```bash
uv sync
```

If you encounter environment issues, create a fresh virtual environment and install dependencies there.

### 6. Configure Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with your actual Google Gemini API key.

**Important:** Never commit your `.env` file or expose your API key on GitHub.

### 7. Run the Project

Run the CrewAI project using the project's configured entry point:

```bash
uv run run_crew
```

If your environment is already activated and the project environment needs to be explicitly selected, use:

```powershell
uv run --active --project "C:\path\to\insight_crew" run_crew
```

Enter your research topic when prompted:

```text
Enter Your Topic: Impact of Generative AI on Data Science Careers
```

The agents will process the topic according to their configured tasks.

## 📄 Output

The generated research report is saved at:

```text
output/output.md
```

The report can contain sections such as:

* Research overview
* Competitor analysis
* Data-driven findings
* Fact-checking results
* Decision insights
* Recommendations
* Supporting source URLs

The exact report structure depends on the agent and task configurations.

## 🔄 Workflow

1. The user provides a research topic.
2. The Research Agent collects relevant information.
3. The Competitor Agent analyzes the competitive landscape.
4. The Data Analyst Agent organizes and evaluates available findings.
5. The Fact Checker Agent reviews claims and supporting evidence.
6. The Decision Agent develops recommendations.
7. The Report Agent compiles the findings into `output/output.md`.

## 🔐 Environment Variables

| Variable         | Purpose                                  |
| ---------------- | ---------------------------------------- |
| `GEMINI_API_KEY` | Authenticates requests to Google Gemini. |

Keep all API credentials private. Add `.env` to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
```

## ⚠️ Limitations

* AI-generated findings may contain inaccuracies and must be verified.
* Web search results depend on source availability and search quality.
* Source URLs should be checked to confirm that they support the associated claims.
* Recommendations depend on the quality and completeness of the collected information.
* Fact-checking by an AI agent does not guarantee that every claim is correct.

## 🔮 Future Enhancements

* Better source validation and citation handling
* Improved research quality evaluation
* Structured report export to PDF
* User-configurable research depth
* Enhanced competitor comparison
* More robust error handling and retry mechanisms
* Additional data sources and research tools



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
