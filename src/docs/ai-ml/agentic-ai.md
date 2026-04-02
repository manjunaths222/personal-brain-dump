---
title: "Agentic Ai"
---

Multi-Agent Systems
CHAPTER 21
1. Why Multi-Agent Systems Exist (First Principles)
A single LLM agent has hard limits:
* One context window
* One perspective
* One objective at a time
* One failure mode
Real problems require:
* decomposition
* specialization
* verification
* negotiation
* parallelism
Core Insight
Instead of making one model smarter,
use multiple models that are simpler â€” but coordinated.
________________


2. What Is an â€œAgentâ€ (Precise Definition)
An agent is not just an LLM call.
An agent has:
1. Goal (what it tries to achieve)
2. State (memory / context)
3. Tools (actions it can take)
4. Policy (how it decides next steps)
5. Communication interface
Mental Model
An agent is an LLM wrapped in intent, memory, and actions.
________________


3. Single Agent vs Multi-Agent (Key Shift)
Single Agent
User â†’ LLM â†’ Answer


Works for:
* Q&A
* summarization
* simple reasoning
________________


Multi-Agent System
User
 â†“
Planner Agent
 â”œâ”€â†’ Research Agent
 â”œâ”€â†’ Reasoning Agent
 â”œâ”€â†’ Validator Agent
 â””â”€â†’ Execution Agent
        â†“
     Final Answer


This is distributed cognition.
________________


4. Multi-Agent Architecture (High-Level)
               â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
User â”€â”€â”€â”€â”€â”€â”€â”€â”€â–¶ â”‚ Orchestratorâ”‚
                â””â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”˜
                       â”‚
        â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
        â”‚              â”‚              â”‚
 â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
 â”‚ Agent A     â”‚ â”‚ Agent B     â”‚ â”‚ Agent C     â”‚
 â”‚ (Research)  â”‚ â”‚ (Reasoning) â”‚ â”‚ (Validation)â”‚
 â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
        â”‚              â”‚              â”‚
        â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                       â†“
                 Aggregation / Decision


The orchestrator can be:
* a rule engine
* another LLM
* deterministic code
________________


5. Why Multiple Agents Work (Cognitive Intuition)
Humans do this naturally:
* one person researches
* another critiques
* another executes
* another verifies
LLMs trained on human text inherit this structure.
Multi-agent systems externalize it.
________________


6. Agent-to-Agent (A2A) Communication
6.1 What A2A Communication Is
Agents must:
* exchange intermediate results
* ask each other questions
* pass partial state
This is not chat â€” itâ€™s protocol-driven communication.
________________


6.2 A2A Communication Patterns
Pattern 1: Requestâ€“Response
Agent A â†’ Question â†’ Agent B
Agent B â†’ Answer â†’ Agent A


Used for:
* delegation
* expertise lookup
________________


Pattern 2: Broadcast
Agent A â†’ Message â†’ All Agents


Used for:
* shared context
* global updates
________________


Pattern 3: Debate / Consensus
Agent A â†’ Proposal
Agent B â†’ Critique
Agent C â†’ Counter-proposal


Used for:
* reasoning
* validation
* safety
________________


7. A2A Communication Architecture
Agent
 â”œâ”€ State
 â”œâ”€ Policy
 â”œâ”€ Tools
 â””â”€ Communication Layer
        â†“
   Message Bus / Protocol
        â†“
   Other Agents


Communication must be:
* structured
* inspectable
* bounded
________________


8. Example 1: Research + Answer + Validator Agents
Problem
â€œExplain how chunk size affects hallucinations in RAG.â€
________________


Agent Roles
* Research Agent â†’ retrieves documents
* Reasoning Agent â†’ synthesizes explanation
* Validator Agent â†’ checks claims vs context
________________


Flow
User
 â†“
Research Agent â†’ chunks
 â†“
Reasoning Agent â†’ draft answer
 â†“
Validator Agent â†’ flags unsupported claims
 â†“
Final Answer


________________


Why This Works
Hallucinations often happen because:
* generation is unchecked
Validation agent breaks the loop.
________________


9. Sample Code (Conceptual Multi-Agent Flow)
research = ResearchAgent()
reasoner = ReasoningAgent()
validator = ValidatorAgent()


docs = research.run(query)
draft = reasoner.run(query, docs)
final = validator.verify(draft, docs)


Notice:
* agents are independent
* each has a clear contract
________________


10. Example 2: Plannerâ€“Executor Pattern
Problem
â€œDeploy a RAG system on AWS.â€
________________


Agents
* Planner â†’ decomposes task
* Executor â†’ runs steps
* Observer â†’ checks results
________________


Flow Diagram
Planner
 â†“
Step 1 â†’ Executor â†’ Result
 â†“
Step 2 â†’ Executor â†’ Result
 â†“
Observer validates


This avoids:
* long context
* tangled reasoning
* prompt collapse
________________


11. Example 3: Competitive Agents (Debate)
Setup
Two agents answer the same question.
A third agent judges.
Agent A â†’ Answer A
Agent B â†’ Answer B
Judge â†’ Picks / Merges


This improves:
* reasoning quality
* factual accuracy
* robustness
Used in:
* safety
* legal analysis
* architecture reviews
________________


12. Failure Modes of Multi-Agent Systems (Important)
Multi-agent systems can fail badly if misdesigned.
Common Failures
1. Infinite loops
2. Agents amplifying each otherâ€™s errors
3. Context explosion
4. Cost runaway
5. No termination criteria
________________


Core Rule
Agents must have bounded scope and explicit stopping conditions.
________________


13. Control vs Autonomy (Key Trade-off)
Design
	Pros
	Cons
	High autonomy
	Flexible
	Unpredictable
	High control
	Safe
	Less powerful
	Enterprise systems bias toward control.
________________


14. MCP Ecosystems (Model Context Protocol)
Now letâ€™s place MCP in this picture.
________________


15. What MCP Actually Is (Clarified)
MCP (Model Context Protocol) is:
* a standardized interface
* for exposing tools, data, and actions
* to LLM agents
Mental Model
MCP is to agents what HTTP is to services.
________________


16. Why MCP Exists
Without MCP:
* each agent integrates tools differently
* brittle, custom glue code
* no portability
MCP standardizes:
* tool discovery
* invocation
* schema
* permissions
________________


17. MCP Architecture
Agent
  â†“
MCP Client
  â†“
MCP Server
  â†“
Tool / DB / API


Multiple agents can share the same MCP server.
________________


18. MCP in a Multi-Agent System
Agents
 â”œâ”€ Research Agent
 â”œâ”€ Planner Agent
 â”œâ”€ Executor Agent
 â””â”€ Validator Agent
        â†“
      MCP
        â†“
 Databases / APIs / Filesystems


This ensures:
* consistent access
* auditability
* security boundaries
________________


19. Example: MCP-Backed RAG Agent
Flow
1. Agent queries MCP vector store
2. MCP returns chunks
3. Agent reasons
4. Validator agent checks grounding
________________


Conceptual Code
chunks = mcp.query(
    tool="vector_search",
    input={"query": user_query}
)


answer = llm.generate(context=chunks)


Agent does not care how retrieval works.
________________


20. Why MCP Matters for Enterprise Agentic AI
MCP enables:
* multi-agent coordination
* tool governance
* observability
* replaceable components
Without MCP:
multi-agent systems turn into spaghetti.
________________


21. When to Use Multi-Agent Systems (Decision Guide)
Use multi-agents when:
* tasks are multi-step
* correctness matters
* validation is required
* workflows cross domains
Do not use them for:
* simple Q&A
* summarization
* low-latency chat
________________


22. Core Intuitions to Lock In
* Agents are LLMs with goals and tools
* Intelligence scales via specialization
* Communication must be structured
* Orchestration matters more than prompts
* MCP standardizes agentâ€“tool interaction
* Control > autonomy in production
* Most failures are coordination failures
________________


23. Why This Chapter Completes the Picture
With this chapter, you now understand:
* LLMs (decoder-only)
* RAG (grounding)
* Evaluation (truth)
* Retrieval (knowledge access)
* Agents (reasoning & action)
* MCP (infrastructure)
This is full-stack GenAI architecture.




Agentic AI Details
CHAPTER 22
1. What Is Agentic AI? (From First Principles)
1.1 The Core Definition
Agentic AI refers to systems where LLMs are embedded inside goal-directed loops that can:
* decide next actions
* use tools
* maintain state
* coordinate with other agents
* stop when objectives are met
The key word is agency.
An agent does not just respond â€” it acts.
________________


2. Chatbots vs Workflows vs Agentic Systems
Letâ€™s clearly separate these â€” this is where confusion starts.
________________


2.1 Chatbots (Reactive Systems)
User â†’ Prompt â†’ LLM â†’ Response


Properties:
* single turn or short memory
* no long-term goal
* no self-initiated action
* no planning
Example:
â€œExplain RAGâ€
The system is purely reactive.
________________


2.2 Workflows (Deterministic Automation)
Input
 â†“
Step 1 â†’ Step 2 â†’ Step 3
 â†“
Output


Properties:
* fixed sequence
* deterministic
* predictable
* brittle to new situations
Example:
* document ingestion pipeline
* ETL jobs
Workflows execute, but they do not reason.
________________


2.3 Agentic Systems (Goal-Oriented Intelligence)
Goal
 â†“
Reason
 â†“
Act
 â†“
Observe
 â†“
Reason (loop)


Properties:
* dynamic planning
* conditional branching
* tool usage
* self-correction
* termination conditions
Agentic AI decides what to do next.
________________


Mental Model (Critical)
System
	Control
	Flexibility
	Chatbot
	User
	Low
	Workflow
	Engineer
	Medium
	Agentic AI
	System
	High
	________________


3. Why Agentic AI Is Needed
LLMs are powerful, but:
* context windows are finite
* prompts are brittle
* one-shot reasoning collapses
* complex tasks exceed single responses
Agentic AI exists because:
Complex problems require multiple reasoning and action steps.
________________


4. Why LangChain + LangGraph? (Design Motivation)
Agentic systems need infrastructure, not just prompts.
________________


4.1 What LangChain Solves
LangChain provides:
* abstractions for LLM calls
* tools
* memory
* prompt templates
It helps you compose reasoning blocks.
But LangChain alone is:
* linear
* fragile for loops
* hard to visualize
________________


4.2 What LangGraph Adds
LangGraph introduces:
* explicit state
* graphs, not chains
* branching
* cycles
* termination conditions
________________


Mental Model
LangChain = logic blocks
LangGraph = control plane
________________


5. Agentic Architecture (High-Level)
User Goal
   â†“
Agent (LLM + Policy)
   â†“
Decision Node
   â”œâ”€ Tool A
   â”œâ”€ Tool B
   â”œâ”€ Ask Another Agent
   â””â”€ Stop


This loop continues until:
* goal is satisfied
* max steps reached
* supervisor intervenes
________________


6. How LLM Internals Shape Agent Design
Agentic AI must respect how LLMs actually work.
________________


6.1 Tokens and Context Window
LLMs:
* process tokens
* have finite context
* forget beyond the window
Implication:
* agents must externalize memory
* summarize state
* store plans outside prompts
________________


6.2 Why Agents Need Memory
Without memory:
* agents repeat themselves
* replan endlessly
* loop
Memory types:
* short-term (current task)
* long-term (external store)
* episodic (summaries)
________________


7. Prompt Engineering for Agents (Not Chatbots)
Agent prompts are policies, not questions.
________________


7.1 System vs User Prompts (Critical)
System prompt:
* defines identity
* defines constraints
* defines goals
User prompt:
* provides input
* should not override policy
________________


Example
System:
You are a planning agent.
You must decompose tasks into steps.
You may call tools.
Stop when task is complete.


User:
Deploy a RAG system on AWS.


________________


Mental Model
System prompt = constitution
User prompt = request
Agentic systems must protect system prompts.
________________


8. Determinism, Temperature, Top-p (Agent Stability)
8.1 Why Determinism Matters for Agents
Agents loop.
Randomness compounds across steps.
High temperature leads to:
* unpredictable plans
* divergence
* infinite loops
________________


Recommended Settings
* temperature â†’ low (0â€“0.3)
* top-p â†’ moderate
* consistent outputs > creativity
Agents need reliability, not poetry.
________________


9. Real-World Agentic Use Cases
Now letâ€™s ground this.
________________


9.1 RAG Agents (Knowledge-Driven Agents)
Instead of:
Query â†’ Retrieve â†’ Generate


We do:
Agent
 â”œâ”€ Reformulate query
 â”œâ”€ Retrieve
 â”œâ”€ Check coverage
 â”œâ”€ Retrieve again (if needed)
 â”œâ”€ Generate answer


________________


Architecture
User Question
   â†“
RAG Agent
   â”œâ”€ Vector Search
   â”œâ”€ Re-ranking
   â”œâ”€ Faithfulness Check
   â””â”€ Final Answer


This reduces hallucinations dramatically.
________________


9.2 Tool-Using Agents
Tools:
* APIs
* databases
* search
* code execution
________________


Example: Tool Agent
Goal: Find recent incidents
 â†“
Agent decides:
 â†’ Query logs
 â†’ Parse results
 â†’ Summarize


________________


Conceptual Code
while not done:
    action = agent.decide(state)
    result = tools.execute(action)
    state.update(result)


The agent chooses when to use tools.
________________


9.3 Autonomous Workflows
Autonomous agents:
* run with minimal human input
* handle long tasks
* recover from errors
Examples:
* CI/CD troubleshooting
* incident response
* data pipeline repair
________________


10. Orchestration vs Autonomy (Key Trade-off)
This is the central design decision.
________________


Orchestrated Agents
* predefined flow
* safe
* predictable
Supervisor â†’ Agent A â†’ Agent B â†’ Stop


________________


Autonomous Agents
* self-directed
* flexible
* risky
Agent â†’ Decide â†’ Act â†’ Repeat


________________


Rule of Thumb
Enterprise systems bias toward orchestration.
Research systems bias toward autonomy.
________________


11. Centralized vs Decentralized Agents
11.1 Centralized (Supervisor-Led)
Supervisor
 â”œâ”€ Agent A
 â”œâ”€ Agent B
 â””â”€ Agent C


Pros:
* control
* visibility
* safety
Cons:
* bottleneck
________________


11.2 Decentralized (Peer-to-Peer)
Agent A â†” Agent B â†” Agent C


Pros:
* scalable
* resilient
Cons:
* coordination failures
* deadlocks
________________


12. Deadlocks & Infinite Loops (Why Agents Fail)
This is where most demos collapse.
________________


Common Causes
* unclear termination conditions
* conflicting goals
* excessive randomness
* no step limit
________________


Example Loop
Agent: Need more info
Agent: Retrieve
Agent: Still insufficient
(repeat forever)


________________


Mitigations
* max step count
* confidence thresholds
* explicit â€œstopâ€ criteria
* supervisor intervention
________________


13. Role of Supervisors (Non-Optional in Production)
Supervisors are:
* control agents
* evaluators
* safety layers
________________


Supervisor Responsibilities
* monitor agent actions
* validate outputs
* stop runaway loops
* enforce policies
________________


Architecture
User
 â†“
Supervisor
 â”œâ”€ Worker Agent 1
 â”œâ”€ Worker Agent 2
 â””â”€ Validator Agent


Supervisor may itself be:
* rules-based
* LLM-based
* hybrid
________________


14. Example: Supervisor-Controlled RAG Agent
Flow:
1. Agent retrieves context
2. Generates answer
3. Supervisor checks faithfulness
4. If failure â†’ retry or stop
This mirrors human review.
________________


15. Minimal LangGraph-Style Mental Model
Node: Reason
 â†“
Node: Act
 â†“
Node: Observe
 â†º (loop)
 â†“
Node: Stop


LangGraph makes this explicit and debuggable.
________________


16. Core Intuitions to Lock In
* Agentic AI is about goals, not responses
* LLMs are reasoning engines, not controllers
* Memory must be external
* Prompts define policy
* Determinism beats creativity
* Orchestration > autonomy in production
* Supervisors are mandatory
* Most failures are control failures, not model failures
________________


17. Why This Chapter Matters (Career Perspective)
If you understand this chapter deeply:
* you can design real agentic systems
* you can explain why agents fail
* you can defend architectural choices
* you stand out instantly in Staff / Principal / Architect interviews




Foundations
MODULE 1: Foundations of Agentic AI
1. Introduction to Agentic AI
1.1 What is Agentic AI?
Letâ€™s start with intuition.
Most people today interact with chatbots:
* You ask a question
* Model responds
* Conversation ends (or continues linearly)
Thatâ€™s not Agentic AI.
Mental Model Shift
Traditional Chatbot
	Agentic AI
	Responds to input
	Acts toward a goal
	Single turn or chat
	Multi-step reasoning
	No memory or planning
	Memory, planning, decision-making
	No tools
	Uses tools, APIs, DBs
	Stateless
	Stateful
	ğŸ‘‰ Agentic AI = LLM + Reasoning + Memory + Tools + Control Flow
An agent is not just answering â€” it is:
* deciding what to do next
* calling tools
* evaluating results
* looping until a goal is achieved
________________


1.2 Chatbots vs Workflows vs Agents
Chatbot
User â†’ LLM â†’ Response


Example:
â€œWhat is Kubernetes?â€
Good for:
* Q&A
* explanations
* content generation
Limitations:
* No actions
* No persistence
* No autonomy
________________


Workflow-based AI
User â†’ Step 1 â†’ Step 2 â†’ Step 3 â†’ Output


Example:
* Upload PDF
* Extract text
* Summarize
* Save to DB
Pros:
* Deterministic
* Easy to debug
Cons:
* Rigid
* Cannot adapt
* No reasoning
________________


Agentic AI
Goal â†’ Think â†’ Act â†’ Observe â†’ Decide â†’ Loop


Example:
â€œAnalyze this document, check latest policies online, summarize risks, and email stakeholders.â€
Here the agent:
1. Understands the goal
2. Chooses tools (search, email, DB)
3. Evaluates intermediate results
4. Decides next steps dynamically
âœ… This is where LangChain + LangGraph shine
________________


1.3 Why LangChain + LangGraph?
LangChain
Best for:
* LLM abstraction
* Prompts
* Tools
* Memory
* RAG pipelines
Think of it as:
â€œThe plumbing for LLM applicationsâ€
________________


LangGraph
Best for:
* Multi-agent systems
* Cyclic workflows
* State machines
* Human-in-the-loop
* Long-running agents
Think of it as:
â€œAirflow / Temporal for Agentsâ€
________________


High-level Architecture
User
 â†“
Agent (LLM)
 â†“
Decision Layer (LangGraph)
 â”œâ”€ Tool A (Search)
 â”œâ”€ Tool B (DB)
 â”œâ”€ Tool C (API)
 â†“
Memory / State
 â†“
Final Output


LangChain handles capabilities
LangGraph handles control flow
________________


1.4 Real-World Use Cases
1. RAG Agents (Retrieval-Augmented Generation)
Problem
LLMs hallucinate and donâ€™t know your private data.
Solution
Agent decides:
* when to search
* what to retrieve
* how to answer
Flow
User Question
 â†’ Agent decides: "Need knowledge?"
 â†’ Vector DB Search
 â†’ Retrieved docs
 â†’ LLM synthesizes answer


WhyAgentic RAG > Simple RAG
* Multi-step retrieval
* Query reformulation
* Confidence checking
* Follow-up questions
________________


2. Tool-Using Agents
Examples:
* GitHub issue triaging
* Jira ticket estimation
* Cloud cost analysis
* Data quality checks
Adnt reasoning example
Thought: I need repo data
Action: Call GitHub API
Observation: Found 120 commits
Thought: Analyze patterns
Action: Run statistics tool


________________


3. Autonomous Workflows
Examples:
* Resume screening agent
* Incident response agent
* AI PM / Tech lead agent
* Research agent
These systems:
* Run for minutes or hours
* Maintain state
* Make decisions dynamically
________________


1.5 Course Architecture & Expectations
By the end of this course, learners will:
* Understand agent internals
* Build production-grade agents
* Design agent architectures
* Debug agent failures
* Add safety & evaluation
You are not just teaching â€œhow to use LangChainâ€ â€”
you're teaching how to think like an AI systems architect.
________________
________________


2. LLM & Prompting Essentials (Quick but Solid)
This section builds intuition, not theory overload.
________________


2.1 How LLMs Work (Intuition First)
Tokens
LLMs donâ€™t read words â€” they read tokens.
Example:
"ChatGPT is powerful"
â†’ ["Chat", "GPT", " is", " powerful"]


Why this matters:
* Cost = tokens
* Context window = tokens
* Chunking strategies depend on tokens
________________


Context Window
The LLM can only â€œrememberâ€ a limited number of tokens at a time.
Implications:
* Long chats lose earlier context
* RAG must be smart
* Memory is external, not inside the model
________________


2.2 Prompt Engineering Essentials
A good prompt has:
1. Role
2. Task
3. Context
4. Constraints
5. Output format
Example (Bad)
Summarize this document


Example (Good)
You are a senior cloud architect.
Summarize the document focusing on security risks.
Limit to 5 bullet points.


________________


2.3 System vs User Prompts
System Prompt
Defines who the model is.
Example:
You are an expert backend architect.
You must respond with structured JSON.


Stable, long-lived, foundational.
________________


User Prompt
Defines what to do now.
Example:
Analyze this API design.


Dynamic, task-specific.
________________


2.4 Determinism: Temperature & Top-P
Parameter
	Effect
	Temperature
	Creativity vs consistency
	Top-P
	Token diversity cutoff
	Rule of Thumb
* Agents â†’ low temperature (0â€“0.3)
* Creative writing â†’ higher (0.7+)
Why?
Agents must be:
* predictable
* debuggable
* repeatable
________________


2.5 Why Prompts Alone Are NOT Enough
Letâ€™s be honest.
Prompt engineering:
* âŒ breaks with scale
* âŒ fails on long tasks
* âŒ cannot loop
* âŒ cannot call tools reliably
Example problem:
â€œKeep trying until you find the correct answer.â€
LLM:
* Canâ€™t retry
* Canâ€™t evaluate
* Canâ€™t decide next step
________________


This is where Agents come in
Agents add:
* Planning
* Tool invocation
* Memory
* Feedback loops
________________


2.6 First Taste: Simple Agent Code (LangChain)
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI


def search_tool(query: str) -> str:
    return f"Search results for {query}"


tools = [
    Tool(
        name="Search",
        func=search_tool,
        description="Useful for searching information"
    )
]


llm = OpenAI(temperature=0)


agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description"
)


agent.run("Find latest trends in Agentic AI")


Whatâ€™s happening internally:
1. LLM reasons
2. Chooses a tool
3. Executes it
4. Observes result
5. Continues or stops
________________


2.7 Conceptual Agent Loop (Core Intuition)
while not goal_met:
    thought = llm(reasoning)
    action = choose_tool(thought)
    observation = execute(action)
    update_state(observation)


ğŸ‘‰ LangGraph will formalize this loop later


LangChain â€“ Core Building Blocks
MODULE 2: LangChain â€“ Core Building Blocks
3. LangChain Architecture Overview
3.1 Why LangChain Exists
Before LangChain, building LLM apps looked like this:
response = openai.chat.completions.create(
    model="gpt-4",
    messages=[...]
)


Problems at scale:
* Prompt logic scattered everywhere
* No standard way to call tools
* No memory abstraction
* Hard to debug multi-step flows
* Zero reusability
LangChain exists to solve software engineering problems, not AI problems.
LangChain = SDK for building LLM-powered systems, not just prompts
________________


3.2 Core Design Philosophy
LangChain is built on composability.
Small blocks â†’ combined into bigger systems.
Think Unix philosophy for LLM apps.
________________


3.3 Core Abstractions (Mental Model)
Input
 â†“
Prompt â†’ LLM
 â†“
Chain (or Agent)
 â†“
Tools / Memory / RAG
 â†“
Output


Each abstraction does one thing well.
________________


3.4 Core Abstractions Explained
1. LLMs
Wrapper around:
* OpenAI
* HuggingFace
* Local models (Ollama, vLLM, llama.cpp)
LangChain standardizes:
* .invoke()
* streaming
* retries
* callbacks
________________


2. Prompts
Templates, not strings.
Why?
* Dynamic inputs
* Reusability
* Partial filling
________________


3. Chains
Deterministic pipelines:
* Prompt â†’ LLM â†’ Output
* Or multi-step logic
Chains are not agents.
________________


4. Tools
Bridges to the real world:
* APIs
* Databases
* Files
* Calculations
________________


5. Memory
External state:
* Chat history
* Summaries
* Context windows
LLMs are stateless â€” memory lives outside.
________________


3.5 LangChain Ecosystem Overview
LangChain Core
 â”œâ”€ Models
 â”œâ”€ Prompts
 â”œâ”€ Chains
 â”œâ”€ Memory
 â”œâ”€ Tools
 â”‚
 â”œâ”€ LangSmith (debugging, evals)
 â””â”€ LangGraph (agents, workflows)


Rule of thumb:
* LangChain â†’ building blocks
* LangGraph â†’ orchestration
________________
________________


4. Models & Prompts in LangChain
4.1 Integrating LLMs
LangChain lets you swap models without rewriting logic.
________________


OpenAI Example
from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


llm.invoke("Explain Agentic AI in one paragraph")


________________


HuggingFace Example
from langchain_huggingface import HuggingFacePipeline


llm = HuggingFacePipeline.from_model_id(
    model_id="google/flan-t5-base",
    task="text2text-generation"
)


________________


Local Model (Ollama)
from langchain_community.llms import Ollama


llm = Ollama(model="llama3")


ğŸ‘‰ Same interface, different engines
________________


4.2 PromptTemplate (Why It Matters)
Bad:
prompt = f"Summarize {text}"


Good:
from langchain.prompts import PromptTemplate


prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text:\n{text}"
)


Why?
* Validation
* Reusability
* Composition
________________


4.3 Few-Shot Prompts (Teaching by Example)
from langchain.prompts import FewShotPromptTemplate


examples = [
    {"input": "AWS", "output": "Cloud platform"},
    {"input": "Kafka", "output": "Distributed streaming system"},
]


prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=PromptTemplate(
        input_variables=["input", "output"],
        template="Input: {input}\nOutput: {output}"
    ),
    suffix="Input: {term}\nOutput:",
    input_variables=["term"]
)


Use when:
* You want consistent formatting
* You want behavior shaping, not rules
________________


4.4 Prompt Composition (Advanced but Crucial)
Prompts can be layered.
System Prompt
 + Task Prompt
 + Formatting Prompt


base_prompt = PromptTemplate(...)
format_prompt = PromptTemplate(...)


final_prompt = base_prompt + format_prompt


This enables:
* Role separation
* Prompt reuse across agents
________________


4.5 Dynamic Prompts
Prompts that change based on:
* user role
* time
* memory
* retrieved docs
def build_prompt(user_type):
    if user_type == "beginner":
        return "Explain simply"
    return "Explain technically"


________________


Hands-on: Reusable Prompt Pipeline
prompt = PromptTemplate(
    input_variables=["topic", "audience"],
    template="""
    You are an expert educator.
    Explain {topic} for a {audience}.
    """
)


chain = prompt | llm
chain.invoke({"topic": "LangChain", "audience": "backend engineer"})


________________
________________


5. Chains in Depth
5.1 What is a Chain?
A Chain is:
A deterministic sequence of operations involving LLMs and transformations
Not autonomous. No looping.
________________


5.2 LLMChain (Basic Unit)
from langchain.chains import LLMChain


chain = LLMChain(
    llm=llm,
    prompt=prompt
)


Good for:
* Single task
* Simple generation
* Controlled outputs
________________


5.3 Sequential Chains
Input â†’ Step 1 â†’ Step 2 â†’ Output


from langchain.chains import SequentialChain


Example:
1. Extract key points
2. Summarize them
________________


5.4 Router Chains (Decision Making)
LLM decides which chain to use.
Example:
* Technical question â†’ Tech chain
* Business question â†’ Business chain
This is proto-agent behavior.
________________


5.5 Transform Chains
Used for:
* Pre-processing
* Post-processing
* Validation
* Cleaning
No LLM needed sometimes.
________________


5.6 When NOT to Use Chains
âŒ Long-running tasks
âŒ Conditional loops
âŒ Retry logic
âŒ Tool-heavy flows
ğŸ‘‰ Use Agents / LangGraph instead
________________


Hands-on: Multi-step Text Pipeline
extract_chain = LLMChain(...)
summarize_chain = LLMChain(...)


pipeline = SequentialChain(
    chains=[extract_chain, summarize_chain],
    input_variables=["text"],
    output_variables=["summary"]
)


________________
________________


6. Memory in LangChain
6.1 Why Memory Matters
LLMs forget everything after each call.
Memory solves:
* Context continuity
* User personalization
* Multi-turn reasoning
________________


6.2 ConversationBufferMemory
Stores everything.
Pros:
* Simple
* Accurate
Cons:
* Token explosion
________________


6.3 Window Memory
Keeps last N messages.
Best for:
* Chatbots
* Cost control
________________


6.4 Summary Memory
Older chats â†’ summarized.
Best for:
* Long conversations
* Agents
________________


6.5 Trade-offs & Limitations
Memory Type
	Accuracy
	Cost
	Scale
	Buffer
	High
	High
	Low
	Window
	Medium
	Medium
	Medium
	Summary
	Medium
	Low
	High
	________________


6.6 Memory vs RAG
Memory
	RAG
	Short-term
	Long-term
	Conversation state
	Knowledge
	Personal
	Global
	They complement, not replace each other.
________________


Hands-on: Stateful Chatbot
from langchain.memory import ConversationBufferMemory


memory = ConversationBufferMemory()


chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory
)


________________
________________


7. Tools & Function Calling
7.1 What are Tools?
Tools let LLMs act.
Without tools:
LLM is a brain in a jar
With tools:
LLM becomes an operator
________________


7.2 Tool Schema (Contract)
Each tool has:
* name
* description
* input schema
* function
________________


7.3 LLM Function Calling (Key Idea)
LLM outputs:
{
  "name": "search",
  "arguments": {"query": "LangChain"}
}


System executes â†’ feeds result back.
________________


7.4 Custom Tool Creation
from langchain.tools import tool


@tool
def calculator(a: int, b: int) -> int:
    return a + b


________________


7.5 Tool Categories
* API tools (GitHub, Jira)
* DB tools (SQL)
* File tools (PDF, CSV)
* Computation tools
________________


Hands-on: Tool-Using Assistant
from langchain.agents import initialize_agent


tools = [calculator]
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="openai-functions"
)


agent.run("What is 45 + 67?")




RAG with LangChain
MODULE 3: Retrieval-Augmented Generation (RAG) with LangChain
8. Retrieval-Augmented Generation (RAG)
8.1 Why RAG Beats Fine-Tuning (Most of the Time)
Letâ€™s kill a very common myth early:
â€œIf the model doesnâ€™t know my data, I should fine-tune it.â€
In practice, RAG is usually the better default.
________________


Fine-Tuning: What Itâ€™s Actually Good For
* Style adaptation (tone, format)
* Domain phrasing
* Behavioral alignment
Fine-Tuning: What Itâ€™s Bad At
* Large private knowledge bases
* Frequently changing data
* Explainability
* Cost + iteration speed
________________


RAG: The Core Idea
Instead of forcing knowledge into the model:
Bring knowledge to the model at runtime
LLM remains:
* small
* generic
* replaceable
Knowledge remains:
* external
* updatable
* auditable
________________


Decision Rule (Very Practical)
Use Case
	Prefer
	Private docs
	RAG
	FAQs / manuals
	RAG
	Constantly changing data
	RAG
	Writing style change
	Fine-tuning
	Reasoning improvement
	Agents, not FT
	________________


8.2 RAG Architecture (Core Mental Model)
High-Level Architecture
               â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                â”‚ Documents  â”‚
                â””â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”˜
                      â”‚
                [Chunking]
                      â”‚
                [Embeddings]
                      â”‚
                â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                â”‚ Vector DB  â”‚
                â””â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”˜
                      â”‚
User Query â†’ [Embed] â†’ Similarity Search
                      â”‚
                Retrieved Chunks
                      â”‚
                Prompt + Context
                      â”‚
                     LLM
                      â”‚
                   Answer


Key idea:
LLM never â€œknowsâ€ your data â€” it only sees relevant slices
________________


8.3 Query â†’ Retrieve â†’ Generate (The RAG Loop)
Letâ€™s break it down.
1. Query
User asks:
â€œWhat are the security risks in our Kubernetes setup?â€
2. Retrieve
* Query is embedded
* Vector DB finds closest chunks
* Optional filtering (metadata)
3. Generate
LLM receives:
* Question
* Retrieved context
* Instructions to only use that context
________________


Why This Works
* Limits hallucinations
* Improves factual grounding
* Enables citations
* Makes system debuggable
________________


9. Document Loaders & Text Splitters
9.1 Document Loaders (Getting Data In)
LangChain provides loaders to normalize data into a standard format:
Document(
  page_content="text",
  metadata={...}
)


________________


PDF Loader
from langchain.document_loaders import PyPDFLoader


loader = PyPDFLoader("policy.pdf")
docs = loader.load()


________________


Markdown Loader
from langchain.document_loaders import TextLoader


loader = TextLoader("README.md")
docs = loader.load()


________________


Web Page Loader
from langchain.document_loaders import WebBaseLoader


loader = WebBaseLoader("https://example.com")
docs = loader.load()


________________


9.2 Why Chunking Matters (Very Important)
LLMs:
* have limited context windows
* perform poorly with long text
* retrieve chunks, not documents
________________


Chunking Intuition
Bad chunk:
Entire 30-page PDF
Good chunk:
Small, coherent semantic unit
________________


9.3 Chunking Strategies
Fixed-Size Chunking
* Simple
* Fast
* Risk: broken sentences
from langchain.text_splitter import RecursiveCharacterTextSplitter


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)


________________


Semantic Chunking
* Better retrieval quality
* Slower
* Complex
________________


9.4 Chunk Overlap Trade-offs
Overlap
	Pros
	Cons
	Low
	Less cost
	Context loss
	High
	Better continuity
	Token explosion
	Rule of thumb:
10â€“20% overlap
________________


10. Embeddings & Vector Stores
10.1 Embeddings (Explained Simply)
Embeddings convert text into numbers such that:
* Similar meaning â†’ closer vectors
* Different meaning â†’ farther vectors
Think:
Meaning â†’ Coordinates in space
________________


10.2 Embedding Example
from langchain_openai import OpenAIEmbeddings


embeddings = OpenAIEmbeddings()
vector = embeddings.embed_query("Kubernetes security best practices")


________________


10.3 Vector Databases (Why Not SQL?)
SQL:
* exact match
Vector DB:
* semantic similarity
________________


10.4 FAISS (Local, Fast, Simple)
from langchain.vectorstores import FAISS


db = FAISS.from_documents(docs, embeddings)


Best for:
* POCs
* Local experiments
* Offline use
________________


10.5 Chroma (Local + Persistent)
from langchain.vectorstores import Chroma


db = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="./chroma_db"
)


________________


10.6 Pinecone (Conceptual)
Used when:
* Large scale
* Multi-tenant
* Cloud-native
Conceptually same API:
* Upsert vectors
* Query top-k
* Filter metadata
________________


10.7 Similarity Search
results = db.similarity_search(
    "container hardening practices",
    k=3
)


Each result:
* chunk text
* metadata
* similarity score
________________


Hands-on: End-to-End RAG Pipeline
from langchain.chains import RetrievalQA


qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(),
    chain_type="stuff"
)


qa_chain.run("What are key Kubernetes security risks?")


What happens internally:
1. Embed query
2. Retrieve chunks
3. Inject into prompt
4. Generate answer
________________


11. Advanced RAG Patterns (Where Production Lives)
11.1 Multi-Query Retrieval
Problem:
* User asks vague questions
Solution:
* LLM rewrites query into multiple variants
Original â†’ Query 1
         â†’ Query 2
         â†’ Query 3


Retrieval improves recall dramatically.
________________


11.2 Parent-Child Documents
Problem:
* Small chunks lose context
Solution:
* Embed small chunks
* Retrieve larger parent doc
Chunk â†’ Parent Section â†’ Answer


Best for:
* Manuals
* Legal docs
* Policies
________________


11.3 Metadata Filtering
Filter by:
* date
* document type
* user role
db.similarity_search(
    query,
    filter={"department": "security"}
)


________________


11.4 Hybrid Search
Combine:
* Keyword search (BM25)
* Vector similarity
Why?
* Keywords catch exact terms
* Vectors catch semantics
This solves:
* IDs
* Error codes
* Proper nouns
________________


11.5 Context Compression
Problem:
* Retrieved chunks too large
Solution:
* LLM summarizes or filters context before final prompt
Retrieve â†’ Compress â†’ Generate


________________


Hands-on: Production-Ready RAG Agent
Architecture
User Query
 â†“
Query Rewriter (LLM)
 â†“
Retriever (Vector DB + Filters)
 â†“
Context Compressor
 â†“
Answer Generator
 â†“
Confidence / Source Attribution


________________


Agent-style RAG Code (Simplified)
from langchain.retrievers.multi_query import MultiQueryRetriever


retriever = MultiQueryRetriever.from_llm(
    retriever=db.as_retriever(),
    llm=llm
)


________________


Common RAG Failure Modes (Critical Section)
âŒ Poor chunking
âŒ Over-retrieval
âŒ Irrelevant context
âŒ Prompt not grounding answers
âŒ Treating RAG as â€œset and forgetâ€
________________


Module 3 Outcome
After this module, learners can:
* Design RAG systems confidently
* Choose correct chunking strategies
* Debug retrieval failures
* Build production-grade pipelines
* Extend RAG into agentic systems


LangGraph
MODULE 4: LangGraph â€“ Stateful & Controlled Agents


LangSmith Studio - Docs by LangChain




LangGraph overview - Docs by LangChain




Deep Agents overview - Docs by LangChain
12. Why LangGraph?
12.1 The Problem with Classic Agents
Classic LangChain agents look magical in demos:
Thought â†’ Action â†’ Observation â†’ Thought â†’ â€¦


But in real systems, they break fast.
________________


Problems Youâ€™ll Face in Production
âŒ Stateless Execution
Each agent run:
* forgets previous runs
* has no durable state
* cannot resume after failure
If the process crashes:
âŒ everything is lost
________________


âŒ Uncontrolled Loops
* Infinite tool calls
* Repeating the same reasoning
* No guarantees of termination
________________


âŒ Hard to Debug
* Reasoning hidden inside LLM text
* No visibility into steps
* No replay or inspection
________________


âŒ No Human Control
* No approvals
* No checkpoints
* No overrides
________________


12.2 Stateless vs Stateful Execution (Critical Intuition)
Stateless Agent (Classic)
Input â†’ Agent â†’ Output


* One-shot
* No memory across executions
* No recovery
________________


Stateful Agent (LangGraph)
State â†’ Node â†’ State â†’ Node â†’ â€¦


State is:
* explicit
* inspectable
* persisted
LangGraph treats agents like workflows with memory
________________


12.3 Why LangGraph Exists (Core Idea)
LangGraph answers one question:
â€œHow do we build long-running, reliable, inspectable agent systems?â€
It gives you:
* Cycles
* Branching
* State persistence
* Deterministic execution paths
* Human-in-the-loop
* Multi-agent coordination
________________


12.4 LangGraph Mental Model
Think of LangGraph as:
Tool
	Analogy
	LangChain
	SDK
	LangGraph
	State machine / workflow engine
	Airflow
	For data
	Temporal
	For services
	LangGraph
	For agents
	________________


13. LangGraph Core Concepts
13.1 The Graph Abstraction
At its core, LangGraph is a directed graph.
Nodes = functions
Edges = transitions
State = shared memory


________________


13.2 State (The Most Important Concept)
State is a typed object that flows through the graph.
Example state:
{
  "input": "...",
  "messages": [...],
  "decision": None,
  "result": None
}


Rules:
* Every node receives state
* Every node returns state (or part of it)
* State evolves step by step
LLMs donâ€™t â€œrememberâ€ â€” state does
________________


13.3 Nodes
A node is just a Python function.
def analyze(state):
    ...
    return {"analysis": "..."}


Nodes can:
* call LLMs
* call tools
* update state
* make decisions
________________


13.4 Edges
Edges define what runs next.
analyze â†’ decide â†’ act


Edges can be:
* static
* conditional
* cyclic
________________


13.5 Entry & Exit Points
Every graph has:
* entry point â†’ where execution starts
* finish point(s) â†’ where execution ends
This gives:
* predictability
* termination guarantees
________________


13.6 Conditional Routing (Decision Making)
Instead of:
â€œLet the LLM decide everythingâ€
We do:
â€œLLM decides, code routesâ€
Example:
if state["decision"] == "approve":
    go_to("approved")
else:
    go_to("rejected")


This is controlled autonomy.
________________


Hands-on 1: Simple Graph-Based Workflow
Goal
Classify input and respond differently.
________________


Graph Design
       â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”
        â”‚  Start â”‚
        â””â”€â”€â”€â”€â”¬â”€â”€â”€â”˜
             â†“
       â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
       â”‚ Classify â”‚
       â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”˜
        yes  â”‚  no
             â†“
   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
   â”‚ Tech Reply â”‚   â”‚ Biz Reply  â”‚
   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜


________________


Code (Simplified)
from langgraph.graph import StateGraph


class State(dict):
    pass


def classify(state):
    text = state["input"]
    if "API" in text:
        return {"type": "tech"}
    return {"type": "biz"}


def tech_reply(state):
    return {"output": "Technical response"}


def biz_reply(state):
    return {"output": "Business response"}


graph = StateGraph(State)


graph.add_node("classify", classify)
graph.add_node("tech", tech_reply)
graph.add_node("biz", biz_reply)


graph.set_entry_point("classify")


graph.add_conditional_edges(
    "classify",
    lambda s: s["type"],
    {
        "tech": "tech",
        "biz": "biz"
    }
)


graph.set_finish_point("tech")
graph.set_finish_point("biz")


app = graph.compile()
app.invoke({"input": "Explain this API"})


________________


14. Building Stateful Agent Workflows
14.1 Human-in-the-Loop (Why This Matters)
In real systems:
* AI should propose
* Humans should approve
Examples:
* Sending emails
* Deploying infra
* Publishing content
* Legal summaries
________________


Human-in-the-Loop Pattern
LLM â†’ Proposal â†’ WAIT
                 â†“
           Human Approves?
                 â†“
              Continue


________________


14.2 Multi-Step Reasoning Flows
Instead of:
â€œAnswer everything in one promptâ€
We do:
1. Analyze
2. Plan
3. Execute
4. Validate
This reduces hallucinations drastically.
________________


14.3 Tool Invocation in Graphs
Unlike classic agents:
* tool calls are explicit
* retries are controlled
* failures are handled
Node example:
def call_api(state):
    try:
        result = api_call(state["query"])
        return {"api_result": result}
    except Exception as e:
        return {"error": str(e)}


________________


14.4 Error Handling & Retries
Classic agents:
âŒ crash or loop
LangGraph:
âœ… retry, branch, or stop
Tool Failed?
  â”œâ”€ retry
  â”œâ”€ fallback
  â””â”€ escalate to human


________________


Hands-on 2: Approval-Based Agent Workflow
Use Case
An agent drafts a response, waits for approval, then sends it.
________________


Graph Design
Start
 â†“
Draft Response
 â†“
WAIT (Human)
 â†“
Approved?
 â”œâ”€ Yes â†’ Send
 â””â”€ No â†’ Revise


________________


Key Insight
LangGraph lets you pause execution and resume later â€” this is impossible with classic agents.
________________


15. Multi-Agent Systems with LangGraph
15.1 When to Use Multiple Agents
Use multiple agents when:
* Tasks require different expertise
* Reasoning is complex
* Outputs need cross-validation
________________


Single Agent vs Multi-Agent
Single Agent
	Multi-Agent
	Simple tasks
	Complex workflows
	Faster
	More robust
	Harder to debug
	Clear responsibilities
	________________


15.2 Role-Based Agents
Each agent has:
* role
* prompt
* responsibility
Example roles:
* Researcher
* Planner
* Writer
* Reviewer
________________


15.3 Supervisor-Agent Pattern (Very Important)
One agent:
* plans
* delegates
* validates
Other agents:
* execute tasks
Supervisor
 â”œâ”€ Research Agent
 â”œâ”€ Writer Agent
 â””â”€ Reviewer Agent


Supervisor decides what runs next.
________________


15.4 Collaboration vs Competition
Collaboration
Agents share state.
Competition
Agents produce alternatives â†’ best one chosen.
This improves:
* quality
* robustness
* confidence
________________


Hands-on 3: Research Agent + Writer Agent
Use Case
Generate a blog post with sources.
________________


Architecture
User Topic
 â†“
Research Agent â†’ Notes
 â†“
Writer Agent â†’ Draft
 â†“
Reviewer Agent â†’ Improve


________________


State Example
{
  "topic": "...",
  "sources": [],
  "notes": "",
  "draft": "",
  "final": ""
}


________________


Key Learning
* Each agent is just a node
* Coordination happens via state
* No hidden magic
________________


Common LangGraph Design Mistakes
âŒ Putting all logic in LLM prompts
âŒ Not defining state clearly
âŒ No termination conditions
âŒ Overusing agents for simple chains
âŒ No human checkpoints






Agentic AI
MODULE 5: Agentic AI â€“ The Real Value
16. Agent Design Principles
16.1 What Makes an Agent â€œAgenticâ€?
An agent is not:
* a chatbot
* a chain
* a single LLM call
* a fancy prompt
An agent is a system that can:
Perceive â†’ Decide â†’ Act â†’ Observe â†’ Adapt
Minimal Definition
An agent is an AI system that:
* pursues a goal
* operates over multiple steps
* decides what to do next
* can act on the environment
* adapts based on outcomes
________________


Agent vs Non-Agent (Clear Contrast)
Property
	LLM Call
	Chain
	Agent
	Goal-oriented
	âŒ
	âŒ
	âœ…
	Multi-step
	âŒ
	âœ… (fixed)
	âœ… (dynamic)
	Decision making
	âŒ
	âŒ
	âœ…
	Tool usage
	âŒ
	Limited
	âœ…
	Adaptation
	âŒ
	âŒ
	âœ…
	Autonomy
	âŒ
	âŒ
	âœ…
	________________


16.2 Autonomy vs Control (The Central Tension)
This is the core design challenge of Agentic AI.
* Too little autonomy â†’ glorified workflow
* Too much autonomy â†’ chaos, hallucinations, risk
Bad Extremes
âŒ â€œLet the LLM decide everythingâ€
âŒ â€œHardcode everything and call it an agentâ€
Good Agents
Autonomy inside guardrails
________________


Controlled Autonomy Architecture
       â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
        â”‚   Goal     â”‚
        â””â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”˜
              â†“
        â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
        â”‚  Reasoning â”‚  â† LLM autonomy
        â””â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”˜
              â†“
     â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
     â”‚ Decision Boundaryâ”‚  â† code control
     â””â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
              â†“
        â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
        â”‚   Action   â”‚  â† tools / APIs
        â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜


Key idea:
* LLM reasons
* Code decides what is allowed
________________


16.3 The Agent Loop (Fundamental Pattern)
All agents reduce to this loop:
while not goal_met:
    think()
    decide()
    act()
    observe()


More explicitly:
Thought â†’ Action â†’ Observation â†’ Thought â†’ ...


This is not a prompt â€” itâ€™s a system loop.
________________


16.4 The ReAct Pattern (Reason + Act)
The ReAct pattern is foundational.
Concept
* LLM explains why it acts
* LLM chooses what action to take
* System executes action
* Result fed back
________________


ReAct Trace Example
Thought: I need current data
Action: search("LangGraph state persistence")
Observation: Retrieved article...
Thought: Now summarize findings
Action: summarize(text)


Why this matters:
* Transparency
* Debuggability
* Reduced hallucinations
ReAct is the backbone of tool-using agents.
________________


17. Types of Agents (Design Taxonomy)
There is no â€œone agent.â€
There are agent archetypes.
________________


17.1 Tool-Using Agents
What They Do
* Decide which tool to call
* Execute it
* Use results to respond
Architecture
User Query
 â†“
LLM (Reason)
 â†“
Tool Selection
 â†“
Tool Execution
 â†“
LLM (Synthesize)


Use Cases
* Search assistants
* Calculators
* API orchestration
* DevOps assistants
Example (LangChain-style)
from langchain.agents import initialize_agent


agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="openai-functions",
    verbose=True
)


agent.run("Find AWS EC2 pricing and summarize")


________________


17.2 Planning Agents
What They Do
* Decompose a goal into steps
* Execute step-by-step
Architecture
Goal
 â†“
Planner (LLM)
 â†“
Step 1 â†’ Step 2 â†’ Step 3


This is not ReAct â€” itâ€™s plan-first.
________________


Planning Example
Goal: Write a technical blog
Plan:
1. Research topic
2. Outline sections
3. Write draft
4. Review


Planning reduces:
* chaos
* repetition
* shallow answers
________________


17.3 Reflex Agents
What They Do
* Immediate response
* No planning
* Rule-like behavior
If condition â†’ action


Use Cases
* Moderation
* Validation
* Monitoring
* Alerting
These agents trade intelligence for speed and reliability.
________________


17.4 Autonomous Task Agents
What They Do
* Accept a goal
* Run for minutes or hours
* Decide when they are â€œdoneâ€
Architecture
Goal
 â†“
Plan
 â†“
Execute
 â†“
Evaluate
 â†“
Repeat


Examples:
* Research agents
* Code refactoring agents
* Incident analysis agents
These require:
* state
* memory
* checkpoints
* termination logic
________________


17.5 Workflow Agents
These are agent + workflow hybrids.
* Fixed stages
* Flexible decisions within stages
Stage 1 (fixed)
 â†“
Agent decides
 â†“
Stage 2 (fixed)


This is often the sweet spot for production.
________________


18. Agent Memory & Planning
18.1 Short-Term vs Long-Term Memory
Short-Term Memory
* Recent messages
* Current context
* Stored in prompts or buffers
Long-Term Memory
* Knowledge
* Past experiences
* Stored externally (DB, vector store)
________________


Memory Spectrum
Prompt Context
 â†’ Buffer Memory
 â†’ Summary Memory
 â†’ Episodic Memory
 â†’ Knowledge Store


________________


18.2 Episodic Memory (Very Important)
Episodic memory = memory of past agent runs.
Example:
â€œLast time I tried this API, it failed with a timeout.â€
This enables:
* learning
* adaptation
* reduced repetition
Stored as:
* logs
* embeddings
* structured records
________________


18.3 Planning Strategies
1. Static Planning
* One plan, executed sequentially
* Simple, brittle
2. Dynamic Planning
* Plan updated after each step
* More robust
3. Hierarchical Planning
* High-level plan
* Subplans per step
This mirrors how humans plan complex tasks.
________________


18.4 Task Decomposition (Critical Skill)
Bad agent:
â€œAnswer everything at onceâ€
Good agent:
â€œBreak problem â†’ solve parts â†’ synthesizeâ€
________________


Hands-on: Task-Planning Agent (Conceptual Code)
def planner(state):
    plan = llm.invoke(
        f"Break this task into steps: {state['goal']}"
    )
    return {"plan": plan}


def executor(state):
    current_step = state["plan"].pop(0)
    result = llm.invoke(f"Execute: {current_step}")
    return {"results": state["results"] + [result]}


This is the core of autonomous agents.
________________


19. Evaluating & Guarding Agents (Non-Negotiable)
If you donâ€™t do this:
Your agent will fail in production
________________


19.1 Hallucinations
Why Agents Hallucinate More
* Longer runtimes
* Multiple steps
* Tool chaining
Mitigations
* RAG grounding
* Tool result verification
* â€œI donâ€™t knowâ€ paths
* Confidence scoring
________________


19.2 Tool Misuse
Agents may:
* Call wrong tools
* Use wrong arguments
* Over-call tools
Guards
* Strict schemas
* Tool-level validation
* Cost budgets
* Rate limits
________________


19.3 Infinite Loops
Classic failure mode:
Thought: Try again
Action: Same tool
Observation: Same error
Thought: Try again


Prevention
* Max step limits
* Loop detection
* State change checks
________________


19.4 Safety & Guardrails
Guardrails operate at multiple layers:
Layer
	Guard
	Prompt
	Role & constraints
	Tool
	Schema validation
	Runtime
	Step limits
	Output
	Moderation
	System
	Human approval
	________________


19.5 Observability & Logging
You must log:
* agent steps
* tool calls
* state changes
* failures
Without observability:
You cannot debug agents
This is why LangSmith + LangGraph matter.
________________


Agent Failure Modes (Real World)
âŒ Over-autonomy
âŒ No termination condition
âŒ Hidden state
âŒ No retries / fallbacks
âŒ No human checkpoints


Production & Real-World Concerns
MODULE 6: Production & Real-World Concerns
20. Agent Evaluation & Metrics
20.1 Why Traditional NLP Metrics Fail for Agents
Classic NLP metrics:
* BLEU
* ROUGE
* METEOR
* Accuracy / F1
These assume:
* single input
* single output
* fixed reference answer
ğŸ‘‰ Agents break all three assumptions.
________________


WhyAgents Are Hard to Evaluate
Agents:
* take multiple steps
* use tools
* make decisions
* may reach the goal via different paths
* may partially succeed
Example:
â€œInvestigate production incident and summarize root cause.â€
Two agents may:
* use different logs
* call different tools
* still produce valid answers
âŒ BLEU canâ€™t score this
âŒ Accuracy is meaningless
âŒ One â€œcorrect answerâ€ doesnâ€™t exist
________________


2ŒˆÚ]ÙHXİX[H]˜[X]H[ˆYÙ[ÂYÙ[]˜[X][Ûˆ\[œÈ]][\H^Y\œÎ‚‘ÛØ[XÚY]™[Y[ˆ8¥'8¥ İ]]]X[]Bˆ8¥'8¥ ÛÛ\ØYÙHÛÜœ™Xİ™\ÜÂˆ8¥'8¥ ™X\ÛÛš[™È]ˆ8¥'8¥ ÛÜİ	ˆ][˜ŞBˆ8¥%8¥ ØY™]B‚‚—×××××××××××××××Â‚‚ŒŒŒÈQÈ]˜[X][Ûˆ˜\ÚXÜÂ”QÈ[›ÙXÙ\ÈÜ›İ[™[™ËÛÈÙHØ[ˆ]˜[X]N‚’Ù^HQÈY]šXÜÂ“Y]šXÂ‚UÚ]]YX\İ\™\Â‚PÛÛ^™XÚ\Ú[Û‚‚T™]šY]™YÚ[šÜÈ™[]˜[˜ÙB‚PÛÛ^™XØ[‚SZ\ÜÚ[™È™[]˜[[™›Â‚Q˜Z][™\ÜÂ‚P[œİÙ\ˆÜ›İ[™Y[ˆÛÛ^‚P[œİÙ\ˆ™[]˜[˜ÙB‚U\Ù\ˆ[[[YÛ›Y[‚U\È\ÈÚ\™HQĞ\Ë\İ[HY]šXÜÈš]ÛÛ˜Ù\X[K‚—×××××××××××××××Â‚‚”QÈ]˜[X][Ûˆ›İÂ”]Y\Bˆ8¡¤Â”™]šY]™YÚ[šÜÂˆ8¡¤Â[œİÙ\‚ˆ8¡¤ÂÛÛ\\™N‚ˆH[œİÙ\ˆœÈÛÛ^ˆHÛÛ^œÈÛÛØÜÂ‚‚‘]™[ˆÚ]İ]›Ü›X[ÛÛ[™ËHÛÛ˜Ù\X]\œË‚—×××××××××××××××Â‚‚ŒŒYÙ[İXØÙ\ÜÈY]šXÜÈ
˜XİXØ[
B‘›Ü™Ù]\™™Xİ[Ûˆ8 %›Øİ\ÈÛˆİ]ÛÛY\Ë‚ÛÛ[[ÛˆYÙ[Y]šXÜÂŠˆ\ÚÈÛÛ\][Ûˆ˜]BŠˆ\X[İXØÙ\ÜÈ˜]BŠˆÛÛ˜Z[\™H˜]BŠˆ™]HÛİ[Šˆ[X[ˆİ™\œšYH˜]BŠˆÛÜİ\ˆ\ÚÂŠˆ[YHÈÛÛ\][Û‚—×××××××××××××××Â‚‚‘^[\Nˆİ\ÜYÙ[Y]šXÜÂ•\ÚÜÈÛÛ\]YˆL‰B’[X[ˆ\ØØ[][ÛœÎˆ‰B]™ÈÛÜİ\ˆXÚÙ]ˆ	ŒN]™È][˜ŞNˆŒœÂ‚‚•\ÙHY]šXÜÈX]\ˆ[Ü™H[ˆ“ÕQÑH]™\ˆÚ[‚—×××××××××××××××Â‚‚ŒŒH[X[ˆ™YY˜XÚÈÛÜÈ
›Û‹SÜ[Û˜[
B’[X[œÈ›İšYN‚ŠˆÛÜœ™Xİ™\ÜÈ˜[Y][Û‚Šˆ™Y™\™[˜ÙHÚYÛ˜[ÂŠˆØY™]HÚXÚÜÂ‘™YY˜XÚÈØ[ˆ™N‚Šˆš[˜\H
\›İ™KÜ™Z™Xİ
BŠˆØÛÜ™Y
x $ÍJBŠˆœ™YK]^•\È™YYÎ‚Šˆ›Û\[š[™ÂŠˆYÙ[›İ][™ÂŠˆÛÛÛÛœİ˜Z[Â—×××××××××××××××Â‚‚ŒŒKˆ\™›Ü›X[˜ÙH	ˆÛÜİÜ[Z^˜][Û‚•\È\ÈÚ\™HYÙ[Ş\İ[\È˜Z[Ú[[K‚—×××××××××××××××Â‚‚ŒŒKŒHÚÙ[ˆÜ[Z^˜][Ûˆ
šYÙÙ\İÛÜİ]™\ŠB•ÚÙ[œÈH[Û™^H
È][˜ŞK‚•Ú\™HÚÙ[œÈ\™HØ\İYŠˆÛ™ÈŞ\İ[H›Û\ÂŠˆ[Ú]\İÜBŠˆİ™\‹\™]šY]˜[[ˆQÂŠˆ™\X][™È[œİXİ[ÛœÂŠˆ™\˜›ÜÙHÛÛİ]]Â—×××××××××××××××Â‚‚•ÚÙ[ˆÜ[Z^˜][Ûˆİ˜]YÚY\ÂŒKˆ›Û\ÛÛ\™\ÜÚ[Û‚Šˆ™[[İ™H™Y[™[[œİXİ[ÛœÂŠˆ[İ™H[˜\šX[ÈÈŞ\İ[K[]™[›Û\ÂŒ‹ˆÛÛ^Ú[™İÈÛÛ›ÛŠˆÚ[™İÈY[[ÜH[œİXYÙˆ[Y™™\‚Šˆİ[[X\š^™HÛİ]BŒËˆQÈ\ØÚ\[™BŠˆ™]Ù\ˆÚ[šÜÂŠˆÛX[\ˆÚ[šÜÂŠˆ™]\ˆ™]šY]™\œÂ—×××××××××××××××Â‚‚ŒŒKŒˆØXÚ[™È
X\ÜÚ]™HÚ[ŠB“X[HYÙ[Ø[È\™N‚Šˆ™\X]YŠˆÚ[Z[\‚Šˆ]\›Z[š\İXÂØXÚHÚ]ÂŠˆH™\ÜÛœÙ\ÂŠˆ[X™Y[™ÜÂŠˆÛÛ™\İ[ÂŠˆ[›š[™Èİ]]Â—×××××××××××××××Â‚‚ØXÚ[™È\˜Ú]Xİ\™B”™\]Y\İˆ8¡¤ÂØXÚOÂˆ8¥'8¥ ]8¡¤ˆ™]\›‚ˆ8¥%8¥ Z\ÜÈ8¡¤ˆ^Xİ]HYÙ[8¡¤ˆİÜ™B‚‚•\ÈØ[ˆ™YXÙHÛÜİHL8 $Î	H[ˆ™X[Ş\İ[\Ë‚—×××××××××××××××Â‚‚ŒŒKŒÈ\˜[[^Xİ][Û‚Û\ÜÚXÈYÙ[È\™HÙ\]Y[X[‚•[šÈ8¡¤ˆXİ8¡¤ˆØœÙ\™H8¡¤ˆ™\X]‚‚]X[H\ÚÜÈØ[ˆ™H\˜[[^™Y‚‘^[\BŠˆ™]ÚÙÜÂŠˆ™]ÚY]šXÜÂŠˆ™]ÚÛÛ™šYÜÂ•\ÙHØ[ˆ[ˆÛÛ˜İ\œ™[K‚—×××××××××××××××Â‚‚”\˜[[YÙ[\˜Ú]Xİ\™B•\ÚÂˆ8¡¤Â”\˜[[ÛÛÂˆ8¥'8¥ ÛÛBˆ8¥'8¥ ÛÛ‚ˆ8¥'8¥ ÛÛÂˆ8¡¤ÂYÙÜ™YØ]H8¡¤ˆXÚYB‚‚•\È˜[X]XØ[H[\›İ™\È][˜ŞK‚—×××××××××××××××Â‚‚ŒŒK\Ş[˜ÈYÙ[È
Üš]XØ[›ÜˆØØ[JB”Ş[˜Ú›Û›İ\ÈYÙ[Î‚Šˆ›ØÚÈ™XYÂŠˆÛ¸ &]ØØ[B\Ş[˜ÈYÙ[Î‚Šˆ[™HX[H\ÚÜÂŠˆØZ]ÛˆKÓÈY™šXÚY[B“[Ù\›ˆYÙ[˜XÚÙ[™È]\İ™H\Ş[˜ËYš\œİ‚—×××××××××××××××Â‚‚ŒŒKHÛÜİœÈ[[YÙ[˜ÙH˜YK[Ù™‚“[Ü™H]]Û›Û^H8¢h™]\ˆŞ\İ[K‚’[˜Ü™X\ÙB‚T™\İ[‚S[Ü™Hİ\Â‚RYÚ\ˆÛÜİ‚S[Ü™HÛÛÂ‚S[Ü™H˜Z[\™HÚ[Â‚S\™Ù\ˆÛÛ^‚TÛİÙ\ˆ
È^[œÚ]™B‚T›ÙXİ[ÛˆYÙ[ÈÜ[Z^™H›Ü‚¸ 'ÛÛÙ[›İYÚ˜\İ[™ÚX\¸ 'B—×××××××××××××××Â‚‚ŒŒ‹ˆ\ŞZ[™ÈYÙ[XÈŞ\İ[\ÂŒŒ‹ŒH\Ş[Y[\È›İ8 '[ˆ\ÈØÜš\8 'B[ˆYÙ[\ÈH˜XÚÙ[™Ş\İ[K›İH›İX›ÛÚË‚‘\Ş[Y[ÛÛ˜Ù\›œÎ‚Šˆ™\œÚ[Ûš[™ÂŠˆØœÙ\˜Xš[]BŠˆ›Û˜XÚÂŠˆØØ[[™ÂŠˆÙXİ\š]B—×××××××××××××××Â‚‚ŒŒ‹ŒˆTKP˜\ÙY\Ş[Y[
[ÜİÛÛ[[ÛŠBYÙ[È\™H^ÜÙY\ÈT\Ë‚ÛY[ˆ8¡¤ÂYÙ[TBˆ8¡¤ÂYÙ[[[YBˆ8¡¤Â“\ÈÈÛÛÂ‚‚™\İ›Ü‚ŠˆÙXˆ\ÂŠˆ[\›˜[ÛÛÂŠˆ[YÜ˜][ÛœÂ—×××××××××××××××Â‚‚ŒŒ‹ŒÈ˜XÚÙ[™[YÜ˜][Û‚YÙ[È˜\™[H]™H[Û™K‚•^H[YÜ˜]HÚ]‚Šˆ]][XØ][Û‚Šˆ]X˜\Ù\ÂŠˆ]Y]Y\ÂŠˆ]™[Ş\İ[\Â‘]™[Qš]™[ˆYÙ[]\›‚‘]™[
XÚÙ]Ü™X]Y
Bˆ8¡¤ÂYÙ[šYÙÙ\™Yˆ8¡¤Â[˜[\Ú\Âˆ8¡¤ÂXİ[Ûˆ
ÛÛ[Y[È\ØØ[][ÛŠB‚‚—×××××××××××××××Â‚‚ŒŒ‹RH[YÜ˜][Ûˆ
Y[ˆÛÛ\^]JB•RHÚ[[™Ù\Î‚Šˆİ™X[Z[™È™\ÜÛœÙ\ÂŠˆ\X[™\İ[ÂŠˆİ]\È\]\ÂŠˆ[X[ˆ\›İ˜[ÂYÙ[ÈÚİ[^ÜÙN‚Šˆİ\İ]\ÂŠˆ[\›YYX]Hİ]]ÂŠˆ›ÙÜ™\ÜÈ[™XØ]ÜœÂ—×××××××××××××××Â‚‚ŒŒ‹HÒKĞÑ›ÜˆYÙ[XÈŞ\İ[\Â•\È\ÈÚ\™HX[\È˜Z[\™\İ‚YÙ[È™YY‚Šˆ›Û\™\œÚ[Ûš[™ÂŠˆÛÛÛÛ˜Xİ\İÂŠˆ™YÜ™\ÜÚ[ÛˆØÙ[˜\š[ÜÂŠˆ]˜[X][Ûˆ]\Ù]Â—×××××××××××××××Â‚‚YÙ[ÒKĞÑ\[[™BÛÙHÚ[™ÙBˆ8¡¤Â”›Û\˜[Y][Û‚ˆ8¡¤Â•ÛÛÛÛ˜Xİ\İÂˆ8¡¤Â‘ÛÛ[ˆ\ÚÈ]˜[X][Û‚ˆ8¡¤Â‘\ŞB‚‚•™X]YÙ[ÈZÙHÛÙØ\™K›İ^\š[Y[Ë‚—×××××××××××××××Â‚‚ŒŒ‹ˆ™\œÚ[Ûš[™ÈYÙ[Â–[İH]\İ™\œÚ[Û‚Šˆ›Û\ÂŠˆÛÛÂŠˆ›İ][™ÈÙÚXÂŠˆ]˜[X][ÛˆÜš]\šXB•ÚOÂ–[İHÚ[™YYÈ^Z[ˆÚHHYÙ[™Z]™YHÙ\Z[ˆØ^H\İ[Û‚—×××××××××××××××Â‚‚ÛÛ[[Ûˆ›ÙXİ[Ûˆ˜Z[\™H[Ù\È
™X[UÛÜ›
B¸§cYÙ[ÈÛÜ[™È[™\ÜÛB¸§cÛÜİÈ^Ù[™ÈÚ[[B¸§c][˜ŞHÜZÙ\È[™\ˆØY¸§cÛÛ˜Z[\™\ÈØ\ØØY[™Â¸§c›ÈØ^HÈXYÈ\İ[œÂ¸§c›È›Û˜XÚÈ]—×××××××××××××××Â‚‚”›ÙXİ[Û‹QÜ˜YHYÙ[\˜Ú]Xİ\™H
[™]ËQ[™
BÛY[ÈRBˆ8¡¤ÂTHØ]]Ø^Bˆ8¡¤ÂYÙ[[[YBˆ8¥'8¥ ØXÚ[™Âˆ8¥'8¥ ˜]H[Z]Âˆ8¥'8¥ İX\™˜Z[Âˆ8¡¤Â“\ÈÈQÈÈÛÛÂˆ8¡¤Â“ÙÜÈ	ˆY]šXÜÂˆ8¡¤Â’[X[ˆ™YY˜XÚÂ‚‚•\È\È›Û‹[Ü[Û˜[›ÜˆÙ\š[İ\ÈŞ\İ[\Ë‚‚‚‘ÛÛÙÛHYÙ[]™[ÜY[Ú]
QÊB“SÑSHˆÛÛÙÛHYÙ[]™[ÜY[Ú]
QÊB‚‚šÎ‹ËÙÛÛÙÛK™Ú]X‹š[ËØYËYØÜËÂ‚‚‚‚Œˆ[›ÙXİ[ÛˆÈÛÛÙÛHQÂŒŒHÚ]\ÈÛÛÙÛHQÏÂ‘ÛÛÙÛHYÙ[]™[ÜY[Ú]
QÊH\ÈÛÛÙÛx &\È[\œš\ÙKYÜ˜YHœ˜[Y]ÛÜšÈ›ÜˆZ[[™Ë\ŞZ[™Ë[™Ûİ™\›š[™ÈRHYÙ[ÈÛˆ™\^RK‚•[šÈÙˆQÈ\Î‚¸ 'İÈÛÛÙÛHØ[ÈYÙ[ÈÈ™HZ[[ˆ›ÙXİ[Û‹¸ 'B’Ù^HÚ\˜Xİ\š\İXÜÎ‚ŠˆYÙ[È\™Hš\œİXÛ\ÜÈŞ\İ[HÛÛ\Û™[ÂŠˆİ›Û™ÈY˜][È›ÜˆØY™]K]\›Z[š\ÛKØœÙ\˜Xš[]BŠˆY\[YÜ˜][ÛˆÚ]™\^RKÙX\˜ÚPSK[Ûš]Üš[™ÂŠˆ\ÚYÛ™Y›Üˆ™Yİ[]Y\™ÙK\ØØ[H[š\›Û›Y[Â—×××××××××××××××Â‚‚ŒŒˆÚHÛÛÙÛHZ[QÈ
H™X[[İ]˜][ÛŠB‘VHYÙ[İXÚÜÈ
[™ĞÚZ[ˆ
È[™ÑÜ˜\
ÈÛÛÊH\™HİÙ\™[8 %][\œš\Ù\È]Ø[Î‚”›Ø›[\ÈÚ]VHYÙ[ÂŠˆ[˜ÛÛœÚ\İ[\˜Ú]Xİ\™\ÈXÜ›ÜÜÈX[\ÂŠˆ[˜ÛX\ˆ™\ÜÛœÚXš[]H›İ[™\šY\ÂŠˆÛÛXØÙ\ÜÈš\ÚÜÂŠˆ\™]ËY[™›Ü˜ÙHÛXÚY\ÂŠˆY™šXİ[]Y]È[™ÛÛ\X[˜ÙBŠˆœ˜YÚ[H™]H	ˆ\œ›Üˆ[™[™ÂŠˆYZØÈY[[ÜH[™İ]B‘[\œš\Ù\ÈÛ¸ &]\ÚÎ‚¸ 'Ø[ˆÙHZ[\Ïø 'B•^H\ÚÎ‚¸ 'Ø[ˆÙHÜ\˜]H\ÈØY™[H›ÜˆYX\œÏø 'B—×××××××××××××××Â‚‚ŒŒÈQÈœÈ[™ĞÚZ[ˆœÈ[™ÑÜ˜\‘[Y[œÚ[Û‚‚S[™ĞÚZ[‚‚S[™ÑÜ˜\‚QÛÛÙÛHQÂ‚Q›Øİ\Â‚PZ[[™È›ØÚÜÂ‚Tİ]Y[Ü˜Ú\İ˜][Û‚‚Q[\œš\ÙHYÙ[]›Ü›B‚Q›^Xš[]B‚U™\HYÚ‚RYÚ‚SYY][H
Ü[š[Û˜]Y
B‚Q]\›Z[š\ÛB‚SİÂ‚SYY][B‚RYÚ‚TØY™]HY˜][Â‚SZ[š[X[‚SYY][B‚Tİ›Û™Â‚S][KXYÙ[‚SX[X[‚Q^XÚ]‚PZ[Z[ˆ]\›œÂ‚QÛİ™\›˜[˜ÙB‚QVB‚QVB‚Qš\œİXÛ\ÜÂ‚U\™Ù]\Ù\œÂ‚Q]™[Ü\œÂ‚TŞ\İ[H\ÚYÛ™\œÂ‚Q[\œš\Ù\Â‚RÙ^H[œÚYÚ‚“[™ĞÚZ[‹Ó[™ÑÜ˜\Ü[Z^™H›Üˆ]™[Ü\ˆİÙ\‚QÈÜ[Z^™\È›ÜˆÜ™Ø[š^˜][Û˜[ØY™]H[™ØØ[B—×××××××××××××××Â‚‚ŒÚ[ˆÈ\ÙHQÈœÈÜ[‹TÛİ\˜ÙB•\ÙHQÈÚ[‚Šˆ[\œš\ÙH]BŠˆ™Yİ[]YÛXZ[œÂŠˆÛX\ˆİÛ™\œÚ\›İ[™\šY\ÂŠˆ]Y]Xš[]HX]\œÂŠˆ™\^RH\È[™XYHİ[™\™•\ÙH[™ĞÚZ[‹Ó[™ÑÜ˜\Ú[‚Šˆ˜\Y^\š[Y[][Û‚Šˆ™\ÙX\˜ÚŞ\İ[\ÂŠˆİ\İÛHYÙ[™Z]š[ÜœÂŠˆ[Ù[Ü›İšY\ˆ›^Xš[]B—×××××××××××××××Â‚‚ŒHQÈ\˜Ú]Xİ\™Hİ™\šY]Â’YÚS]™[\˜Ú]Xİ\™BÛY[È\ˆ8¡¤ÂˆQÈYÙ[[[YBˆ8¡¤ÂˆYÙ[Yš[š][Û‚ˆ8¥'8¥ ÚÚ[Âˆ8¥'8¥ ÛÛÂˆ8¥'8¥ ÛXÚY\Âˆ8¥'8¥ Y[[ÜBˆ8¡¤Âˆ™\^RH
\ÊBˆ8¡¤Âˆ[\œš\ÙHŞ\İ[\Âˆ
ÙX\˜ÚœËT\ÊB‚‚QÈYÙ[È]™H[œÚYHHĞÔXÛÜŞ\İ[K›İİ]ÚYH]‚—×××××××××××××××Â‚‚ŒKˆÛÜ™HÛÛ˜Ù\ÈÙˆÛÛÙÛHQÂŒKŒHYÙ[È\Èš\œİPÛ\ÜÈÚ]^™[œÂ’[ˆQÎ‚ŠˆYÙ[È\™H^XÚ][]Y\ÂŠˆ^H]™N‚ˆ
ˆY[]Bˆ
ˆ\›Z\ÜÚ[ÛœÂˆ
ˆY™XŞXÛBˆ
ˆ]Y]˜Z[•\È\È˜YXØ[HY™™\™[œ›ÛN‚¸ '\İH[˜İ[ÛˆØ[[™È[ˆx 'B—×××××××××××××××Â‚‚ŒKŒˆ\ÚÜÈ	ˆÛØ[ÂQÈÙ\\˜]\Î‚Šˆ\ÚÈYš[š][Ûˆ
Ú]ÈÊBŠˆ^Xİ][Ûˆİ˜]YŞH
İÈÈÈ]
B•\È]›ÚYÈYÙ[È8 'Ø[™\š[™ø 'K‚‘^[\N‚•\ÚÎˆ[˜[^™Hİ\İÛY\ˆÛÛ\Z[Â‘ÛØ[ˆ›ÙXÙHš\ÚÈİ[[X\BÛÛœİ˜Z[Îˆ›ÈRHXZØYÙB‚‚—×××××××××××××××Â‚‚ŒKŒÈÛÛÈ	ˆXİ[ÛœÂ’[ˆQÎ‚ŠˆÛÛÈ\™H\›İ™YØ\Xš[]Y\ÂŠˆYÙ[ÈØ[››İ[™[ÛÛÂŠˆÛÛÈ\™H\›Z\ÜÚ[Û™Y•\È\È™\›Ë]\İH\ÚYÛ‹‚—×××××××××××××××Â‚‚ŒKYÙ[Y™XŞXÛB’[š]X[^™Bˆ8¡¤ˆÛÛ^Ù]\ˆ8¡¤ˆ\ÚÈ\ÜÚYÛ›Y[ˆ8¡¤ˆ^Xİ][Û‚ˆ8¡¤ˆ˜[Y][Û‚ˆ8¡¤ˆÛÛ\][ÛˆÈ\ØØ[][Û‚‚‚YÙ[ÈÈ›İÛÜ[™\ÜÛH[›\ÜÈ[İÙY‚—×××××××××××××××Â‚‚ŒKH]\›Z[š\İXÈ^Xİ][ÛˆœÈ]]Û›Û^BQÈ[X™\˜][H[Z]È˜]È]]Û›Û^K‚\ÜXİ‚PQÈ\›ØXÚ‚T[›š[™Â‚PÛÛœİ˜Z[™Y‚UÛÛXØÙ\ÜÂ‚UÚ][\İY‚T™]šY\Â‚PZ[Z[‚‚SÛÜÂ‚P›İ[™Y‚R[X[ˆ™]šY]Â‚Qš\œİXÛ\ÜÂ‚PQÈ\È\ÚYÛ™Y›ÜˆØY™H]]Û›Û^K›İX^[X[]]Û›Û^K‚—×××××××××××××××Â‚‚Œ‹ˆQÈYÙ[\˜Ú]Xİ\™BŒ‹ŒHYÙ[Yš[š][Û‚[ˆQÈYÙ[\ÈYš[™YN‚Šˆ\œÜÙBŠˆÚÚ[ÂŠˆ[İÙYÛÛÂŠˆÛXÚY\ÂŠˆY[[ÜHÛÛ™šYİ\˜][Û‚ÛÛ˜Ù\X[N‚YÙ[
ˆ˜[YOH”š\ÚĞ[˜[\Ú\ĞYÙ[‹ˆÚÚ[ÏVÔİ[[X\š^˜][Û‹Û\ÜÚYšXØ][Û—KˆÛÛÏVÔÙX\˜ÚÛÛ•ÛÛKˆÛXÚY\ÏVÓ›ÔRK™XYÛ›PXØÙ\Ü×BŠB‚‚—×××××××××××××××Â‚‚Œ‹ŒˆÚÚ[P˜\ÙY\ÚYÛ‚”ÚÚ[È\™H™]\ØX›HØ\Xš[]Y\Ë›İ›Û\Ë‚‘^[\\Î‚Šˆİ[[X\š^™HØİ[Y[ÂŠˆÛ\ÜÚYHÙ[[Y[Šˆ^˜Xİ[]Y\ÂŠˆÙ[™\˜]H™\ÜÂ•\È›Û[İ\Î‚Šˆ™]\ÙBŠˆÛÛœÚ\İ[˜ŞBŠˆ\İ[™Â—×××××××××××××××Â‚‚Œ‹ŒÈÛÛÜ˜Ú\İ˜][Û‚QÈÜ˜Ú\İ˜]\ÈÛÛÈÙ[˜[N‚Šˆ›È\™XİTHØ[Èœ›ÛHBŠˆ[Ø[ÈÛÈ›İYÚÙXİ\™H^Xİ]ÜœÂYÙ[ˆ8¡¤ÂXİ[Ûˆ™\]Y\İˆ8¡¤Â•ÛÛÜ˜Ú\İ˜]Ü‚ˆ8¡¤Â‘[\œš\ÙHŞ\İ[B‚‚—×××××××××××××××Â‚‚Œ‹^Xİ][Ûˆ›İÂ•\ÚÈ\ÜÚYÛ™Yˆ8¡¤Â”ÚÚ[Ù[Xİ[Û‚ˆ8¡¤Â•ÛÛ[›ØØ][Ûˆ
Yˆ[İÙY
Bˆ8¡¤Â”™\İ[˜[Y][Û‚ˆ8¡¤Â‘š[˜[İ]]‚‚—×××××××××××××××Â‚‚Œ‹H\œ›Üˆ[™[™È	ˆ™]šY\È
Z[Z[ŠB•[›ZÙHVHYÙ[Î‚Šˆ™]šY\È\™Hİ[™\™^™YŠˆ˜[˜XÚÈİ˜]YÚY\È\™H[™›Ü˜ÙYŠˆ\œ›ÜœÈ\™HÙÙÙYÙ[˜[B•\È\ÈYÙH›ÜˆÜÈX[\Ë‚—×××××××××××××××Â‚‚’[™Ë[Ûˆ˜\ÚXÈQÈYÙ[
ÛÛ˜Ù\X[
B˜YÙ[HYÙ[
ˆ˜[YOH”İ\ÜYÙ[‹ˆ\ÚÏH”İ[[X\š^™Hİ\ÜXÚÙ]È‹ˆÚÚ[ÏVÈœİ[[X\š^™H—KˆÛÛÏVÈ™[\œš\ÙWÜÙX\˜Ú—BŠB‚‚œ™\ÜÛœÙHHYÙ[œ[Š[œ]Ù]JB‚‚‘›Øİ\Î‚ŠˆÛ\š]BŠˆ]\›Z[š\ÛBŠˆ˜XÙXXš[]B—×××××××××××××××Â‚‚ŒËˆÛÛËXİ[ÛœÈ	ˆ[YÜ˜][ÛœÂŒËŒHYš[š[™ÈÛÛÈ[ˆQÂ•ÛÛÈ\™H^XÚ]ÛÛ˜XİÎ‚Šˆ[œ]ØÚ[XBŠˆİ]]ØÚ[XBŠˆ\›Z\ÜÚ[ÛœÂ“›È8 'HXÚY\È\™İ[Y[Èœ™Y[x 'K‚—×××××××××××××××Â‚‚ŒËŒˆZ[Z[ˆœÈİ\İÛHÛÛÂ•ÛÛ\B‚Q^[\\Â‚PZ[Z[‚‚TÙX\˜ÚİÜ˜YÙKšYÔ]Y\B‚Pİ\İÛB‚R[\›˜[T\Â‚T™\İšXİY‚Qš[˜[˜ÚX[ˆŞ\İ[\Â‚W×××××××××××××××Â‚‚ŒËŒÈÙXİ\™HÛÛ^Xİ][Û‚”ÙXİ\š]H™X]\™\Î‚ŠˆPSH[™›Ü˜Ù[Y[Šˆ›ÛKX˜\ÙYXØÙ\ÜÂŠˆØÛÜYÜ™Y[X[ÂŠˆ]Y]ÙÜÂ—×××××××××××××××Â‚‚’[™Ë[ÛˆÛÛQ[˜X›Y[\œš\ÙHYÙ[YÙ[ˆš[˜[˜ÙP\ÜÚ\İ[•ÛÛÎ‚ˆH™XY[Û›HYÙ\ˆTBˆH[˜[]XÜÈ‚”ÛXÚY\Î‚ˆH›ÈÜš]HXØÙ\ÜÂˆH›È^\›˜[Ø[Â‚‚—×××××××××××××××Â‚‚Œˆ][KPYÙ[Ş\İ[\ÈÚ]QÂŒŒHYÙ[ÛÛX›Ü˜][Ûˆ]\›œÂQÈİ\ÜÎ‚Šˆ[YØ][Û‚Šˆ\˜[[^Xİ][Û‚Šˆİ\\š\ÛÜˆİ™\œÚYÚ—×××××××××××××××Â‚‚ŒŒˆİ\\š\ÛÜˆYÙ[Â”İ\\š\ÛÜ‚Šˆ\ÜÚYÛœÈ\ÚÜÂŠˆ˜[Y]\Èİ]]ÂŠˆ\ØØ[]\È\ÜİY\Â”İ\\š\ÛÜ‚ˆ8¥'8¥ [˜[\Ú\ÈYÙ[ˆ8¥'8¥ ™]šY]˜[YÙ[ˆ8¥%8¥ ™\ÜYÙ[‚‚—×××××××××××××××Â‚‚ŒŒÈÛÛ›ÛY]]Û›Û^BYÙ[Î‚ŠˆØ[››İÜ]ÛˆYÙ[Èœ™Y[BŠˆ]\İ›ÛİÈYš[™YÛÜšÙ›İÜÂ•\È™]™[Î‚Šˆ[˜]Ø^HÛÜİÂŠˆ[œ™YXİX›H™Z]š[Ü‚—×××××××××××××××Â‚‚’[™Ë[Ûˆ][KPYÙ[ÛÜšÙ›İÂİ\İÛY\ˆ]Y\Bˆ8¡¤Â”İ\\š\ÛÜ‚ˆ8¡¤Â”™]šY]™\ˆ
È[˜[^™\ˆ
\˜[[
Bˆ8¡¤Â”Ş[\Ú^™\‚‚‚—×××××××××××××××Â‚‚ŒKˆY[[ÜKÛÛ^	ˆİ]H[ˆQÂŒKŒHÛÛ^X[˜YÙ[Y[QÈÛÛ›ÛÎ‚ŠˆÚ]ÛÛ^\È[š™XİYŠˆÚ]\È\œÚ\İYŠˆÚ]\È\ØØ\™Y—×××××××××××××××Â‚‚ŒKŒˆÚÜU\›HœÈ\œÚ\İ[Y[[ÜB•\B‚U\ÙB‚TÚÜ]\›B‚PÛÛ™\œØ][Û‚‚T\œÚ\İ[‚RÛ›İÛYÙK\İÜB‚Q^\›˜[‚Q[\œš\ÙH]B‚W×××××××××××××××Â‚‚ŒKŒÈ[\œš\ÙH]HXØÙ\ÜÈ]\›œÂQÈ]›ÚYÎ‚¸ '[\[\™Hˆ[È›Û\8 'B’[œİXY‚ŠˆØÛÜY™]šY]˜[ŠˆÛXŞKXÚXÚÙYXØÙ\ÜÂŠˆ]Y]X›H]Y\šY\Â—×××××××××××××××Â‚‚ŒÌˆQÈÚ]ÛÛÙÛHQÈ	ˆ™\^RBŒÌŒH™\^RHÙX\˜Ú‘ÛÛÙÛK[˜]]™HQÎ‚Šˆ[\œš\ÙHÛÛ›™XİÜœÂŠˆXØÙ\ÜÈÛÛ›ÛÂŠˆœ™\Ú™\ÜÈİX\˜[Y\Â—×××××××××××××××Â‚‚ŒÌŒˆ[X™Y[™ÜÈ[ˆĞÔŠˆ™\^RH[X™Y[™ÜÂŠˆX[˜YÙYØØ[[™ÂŠˆÙXİ\™HİÜ˜YÙB—×××××××××××××××Â‚‚ŒÌŒÈÙXİ\™H[\œš\ÙHQÈ\˜Ú]Xİ\™B‘ØÜÈ8¡¤ˆ[™Ù\İ[Ûˆ\[[™Bˆ8¡¤ˆ™\^RHÙX\˜Úˆ8¡¤ˆQÈYÙ[ˆ8¡¤ˆÛXŞHÚXÚÂˆ8¡¤ˆB‚‚—×××××××××××××××Â‚‚’[™Ë[Ûˆ[\œš\ÙHQÈYÙ[YÙ[
ˆ˜[YOH”ÛXŞP\ÜÚ\İ[‹ˆ]WÜÛİ\˜ÙOH•™\^RTÙX\˜Ú‹ˆÛXÚY\ÏVÈ“›Ò[XÚ[˜][Ûˆ‹Ú]TÛİ\˜Ù\È—BŠB‚‚—×××××××××××××××Â‚‚ŒÌKˆ]˜[X][Û‹ØY™]H	ˆİX\™˜Z[ÂŒÌKŒHZ[Z[ˆ]˜[X][Û‚QÈİ\ÜÎ‚Šˆİ]]˜[Y][Û‚ŠˆÛÛœÚ\İ[˜ŞHÚXÚÜÂŠˆ™YÜ™\ÜÚ[Ûˆ\İ[™Â—×××××××××××××××Â‚‚ŒÌKŒˆØY™]Hš[\œÂŠˆÛÛ[[Ù\˜][Û‚Šˆ]HXZØYÙH™]™[[Û‚ŠˆÛXZ[ˆ™\İšXİ[ÛœÂ—×××××××××××××××Â‚‚ŒÌKŒÈÛÛXØÙ\ÜÈÛÛ›ÛYÙ[Î‚ŠˆÛ›HÙYH[İÙYÛÛÂŠˆØ[››İ\\ÜÈPSB—×××××××××××××××Â‚‚ŒÌK[X[‹Z[‹]KSÛÜ“X[™]ÜH›Ü‚ŠˆÙ[œÚ]]™Hİ]]ÂŠˆ^\›˜[Xİ[ÛœÂŠˆ\œ™]™\œÚX›Hİ\Â—×××××××××××××××Â‚‚ŒÌ‹ˆ\Ş[Y[	ˆØØ[[™ÈÚ]QÂŒÌ‹ŒH[›š[™ÈYÙ[ÈÛˆ™\^RBŠˆX[˜YÙY^Xİ][Û‚Šˆ]]Ë\ØØ[[™ÂŠˆ™YÚ[Û˜[ÛÛ\X[˜ÙB—×××××××××××××××Â‚‚ŒÌ‹Œˆ[Ûš]Üš[™È	ˆÙÙÚ[™ÂŠˆÙ[˜[^™YÙÜÂŠˆ˜XÙ\È\ˆYÙ[ŠˆÛÜİ]šX][Û‚—×××××××××××××××Â‚‚ŒÌ‹ŒÈÛÜİÜ[Z^˜][Û‚ŠˆÛÛYÙ]ÂŠˆÚÙ[ˆØ\ÂŠˆ^Xİ][Ûˆ[Z]Â‚‚‚‚‚‚“[™ĞÚZ[ˆœÈ[™ÑÜ˜\œÈÛÛÙÛHQÂ“SÑSHÎˆ[™ĞÚZ[ˆœÈ[™ÑÜ˜\œÈÛÛÙÛHQÂŒŒË˜Hœ˜[Y]ÛÜšÈÛÛ\\š\ÛÛˆ8 $ÈY\]™B“]8 &\ÈÛÈ^Y\ˆH^Y\‹›İ\İÚ]HX›K‚—×××××××××××××××Â‚‚“Y[[[Ù[š\œİ
™Y›Ü™HHX›JB“[™ĞÚZ[‚¸ 'Ú]™HYHİÙ\™[YÛÈ›ØÚÜËˆx &[\ÜÙ[X›H^HİÛˆŞ\İ[K¸ 'B“[™ÑÜ˜\¸ 'Ú]™HYHHİ]HXXÚ[™HÛÈHØ[ˆÛÛ›ÛYÙ[^Xİ][Û‹¸ 'B‘ÛÛÙÛHQÂ¸ 'Ú]™HYHHÛİ™\›™Y]›Ü›HÛÈ^HÜ™Ø[š^˜][ÛˆØ[ˆÛY\]šYÚ¸ 'B—×××××××××××××××Â‚‚’YÚS]™[\˜Ú]Xİ\˜[ÛÛ\\š\ÛÛ‚“[™ĞÚZ[‚\ÛÙBˆ8¡¤Â”›Û\ÈÈÚZ[œÈÈÛÛÂˆ8¡¤Â“B‚‚ŠˆYÚÙZYÚŠˆ›^X›BŠˆZ[š[X[Ü˜Ú\İ˜][Û‚Šˆ[İHİÛˆ]™\][™Â—×××××××××××××××Â‚‚“[™ÑÜ˜\\ÛÙBˆ8¡¤Â”İ]HÜ˜\
›Ù\È
ÈYÙ\ÊBˆ8¡¤ÂÛÛ›ÛYYÙ[^Xİ][Û‚ˆ8¡¤Â“\ÈÈÛÛÂ‚‚Šˆ^XÚ]İ]BŠˆ]\›Z[š\İXÈ›İÜÂŠˆ™XÛİ™\˜X›H^Xİ][Û‚Šˆ]™[Ü\‹XÛÛ›ÛYÜ˜Ú\İ˜][Û‚—×××××××××××××××Â‚‚‘ÛÛÙÛHQÂÛY[ÈÙ\šXÙBˆ8¡¤ÂQÈ[[YBˆ8¡¤ÂYÙ[Yš[š][Û‚ˆ8¥'8¥ ÚÚ[Âˆ8¥'8¥ ÛXÚY\Âˆ8¥'8¥ ÛÛÂˆ8¥'8¥ Y[[ÜBˆ8¡¤Â•™\^RH
È[\œš\ÙHŞ\İ[\Â‚‚Šˆİ›Û™ÈÛİ™\›˜[˜ÙBŠˆÜ[š[Û˜]YY˜][ÂŠˆZ[Z[ˆØY™]H	ˆÜÂŠˆX[˜YÙY^Xİ][Û‚—×××××××××××××××Â‚‚‘œ˜[Y]ÛÜšÈÛÛ\\š\ÛÛˆX›H
^[™Y	ˆ^Z[™Y
B\ÜXİ‚S[™ĞÚZ[‚‚S[™ÑÜ˜\‚QÛÛÙÛHQÂ‚Q›^Xš[]B‚x«d8«d8«d8«d8«d‚x«d8«d8«d8«d‚x«d8«d8«d‚PÛÛ›Û‚x«d8«d8«d‚x«d8«d8«d8«d8«d‚x«d8«d8«d8«d8«d‚Tİ]Y[™\ÜÂ‚UÙXZÂ‚Tİ›Û™Â‚Tİ›Û™Â‚PYÙ[Ü˜Ú\İ˜][Û‚‚P˜\ÚXÂ‚Q^XÚ]‚PZ[Z[‚‚Q\œ›Üˆ[™[™Â‚QVB‚Q^XÚ]‚PZ[Z[‚‚R[X[‹Z[‹[ÛÜ‚SX[X[‚S˜]]™B‚S˜]]™B‚T›ÙXİ[Ûˆ™XY[™\ÜÂ‚SYY][B‚RYÚ‚U™\HYÚ‚Q[\œš\ÙHÙXİ\š]B‚SİÂ‚SYY][B‚U™\HYÚ‚SØœÙ\˜Xš[]B‚SÜ[Û˜[‚Tİ›Û™Â‚Qš\œİXÛ\ÜÂ‚U™[™ÜˆØÚËZ[‚‚S›Û™B‚S›Û™B‚RYÚ‚SX\›š[™Èİ\™B‚SİÂ‚SYY][B‚RYÚ‚W×××××××××××××××Â‚‚•Ú]\ÙH˜][™ÜÈXİX[HYX[‚‘›^Xš[]BŠˆ[™ĞÚZ[ˆ]È[İHÈ[][™ÂŠˆQÈ™\İšXİÈ[İHÛˆ\œÜÙBŠˆ™\İšXİ[ÛœÈ\™HÛÛÙ[ˆ™Yİ[]Y[š\›Û›Y[ÂÛÛ›ÛŠˆ[™ĞÚZ[ˆHXÚY\È[Üİ[™ÜÂŠˆ[™ÑÜ˜\ˆ[İHXÚYH^Xİ][Û‚ŠˆQÎˆ]›Ü›HXÚY\ÈİX\™˜Z[Â”›ÙXİ[Ûˆ™XY[™\ÜÂŠˆ[™ĞÚZ[ˆ™\]Z\™\È\ØÚ\[™BŠˆ[™ÑÜ˜\[™›Ü˜Ù\ÈİXİ\™BŠˆQÈ[™›Ü˜Ù\ÈÛÛ\X[˜ÙB—×××××××××××××××Â‚‚‘œ˜[Y]ÛÜšÜÈH›Ø›[H\H
™\H˜XİXØ[
B—×××××××××××××××Â‚‚Ø\ÙHNˆÚ[\HRH™X]\™H
İ\\ÈU”
B‘^[\B¸ 'YHÛX\TH›İÈİ\ˆ›ÙXİ¸ 'B™\İÚÚXÙNˆ[™ĞÚZ[‚•ÚN‚Šˆ˜\İ\İÈZ[ŠˆZ[š[X[İ™\šXYŠˆX\ŞH]\˜][Û‚‘^[\H
[™ĞÚZ[ŠB˜ÚZ[ˆH›Û\B˜ÚZ[‹š[›ÚÙJÈœ]Y\İ[Ûˆˆ•Ú]\È[İ\ˆ™Y[™ÛXŞOÈŸJB‚‚•\Ú[™È[™ÑÜ˜\ÜˆQÈ\™HÛİ[™Hİ™\šÚ[‚—×××××××××××××××Â‚‚Ø\ÙHˆQËP˜\ÙYÛ›İÛYÙH\ÜÚ\İ[
Ü›İÚ[™È›ÙXİ
B‘^[\B¸ '[\›˜[Øİ[Y[][Ûˆ\ÜÚ\İ[›Üˆ[™Ú[™Y\œË¸ 'B™\İÚÚXÙNˆ[™ĞÚZ[ˆ8¡¤ˆ[™ÑÜ˜\”İ\Ú]‚Šˆ[™ĞÚZ[ˆQÈ\[[™B‘]›Û™HÎ‚Šˆ[™ÑÜ˜\›Üˆ™]šY\Ë[X[ˆ™]šY]Ë™]\ˆÛÛ›Û•ÚH›İQÈY]ÂŠˆÛÈX\›BŠˆÛİÜÈ]\˜][Û‚ŠˆØÚËZ[ˆš\ÚÂ—×××××××××××××××Â‚‚Ø\ÙHÎˆÛ™ËT[›š[™ÈYÙ[
™\ÙX\˜ÚÈÜÊB‘^[\B¸ '[™\İYØ]H[˜ÚY[ËØ]\ˆÙÜËİ[[X\š^™H›ÛİØ]\ÙK¸ 'B™\İÚÚXÙNˆ[™ÑÜ˜\•ÚN‚Šˆ][K\İ\Šˆ™YYÈİ]BŠˆ™YYÈ™]šY\ÂŠˆ™YYÈ]\ÙKÜ™\İ[YB“[™ÑÜ˜\ÚÙ]Ú”İ\ˆ8¡¤ÂÛÛXİÙÜÂˆ8¡¤Â[˜[^™Bˆ8¡¤Â’[X[ˆ™]šY]ÏÂˆ8¡¤Â‘š[˜[^™B‚‚“[™ĞÚZ[ˆYÙ[ÈÚ[‚ŠˆÛÜŠˆ˜Z[Ú[[BŠˆ™H[\ÜÜÚX›HÈXYÂ—×××××××××××××××Â‚‚Ø\ÙHˆ[\œš\ÙHRH\ÜÚ\İ[
™Yİ[]Y]JB‘^[\B¸ 'ˆ\ÜÚ\İ[XØÙ\ÜÚ[™È[\ŞYYH™XÛÜ™Ë¸ 'B™\İÚÚXÙNˆÛÛÙÛHQÂ•ÚN‚ŠˆPSBŠˆ]Y][™ÂŠˆÛÛ™\İšXİ[ÛœÂŠˆÛÛ\X[˜ÙBŠˆÙ[˜[Ûİ™\›˜[˜ÙB’Ù^H[œÚYÚ•\È\È›İ[ˆRH›Ø›[H8 %]8 &\ÈHš\ÚÈX[˜YÙ[Y[›Ø›[K‚—×××××××××××××××Â‚‚ŒŒË˜ˆÚÛÜÚ[™ÈHšYÚœ˜[Y]ÛÜšÈ
XÚ\Ú[Ûˆ[œÊB“]8 &\Èœ™XZÈ\ÈİÛˆH™X[]ÛÜ›ÛÛœİ˜Z[Ë‚—×××××××××××××××Â‚‚”İ\\ÈœÈ[\œš\Ù\Â”İ\\ÂŠˆÜYYˆÛİ™\›˜[˜ÙBŠˆ›^Xš[]Hˆİ[™\™^˜][Û‚ŠˆÛÜİÙ[œÚ]]š]B¸§!H[™ĞÚZ[‚¸§!H[™ÑÜ˜\
]\ŠB—×××××××××××××××Â‚‚‘[\œš\Ù\ÂŠˆÛÛ\X[˜ÙHˆÜYYŠˆİ[™\™^˜][Ûˆˆ›^Xš[]BŠˆ]Y]Xš[]Hˆ^\š[Y[][Û‚¸§!HÛÛÙÛHQÂ—×××××××××××××××Â‚‚”›İİ\[™ÈœÈ›ÙXİ[Û‚”›İİ\[™ÂŠˆÚ[™ÙH›Û\ÈZ[BŠˆœ™XZÈ[™ÜÈÙ[‚ŠˆX\›ˆ˜\İ•\ÙN‚Šˆ[™ĞÚZ[‚—×××××××××××××××Â‚‚”›ÙXİ[Û‚ŠˆİXš[]HX]\œÂŠˆ™YXİXš[]HX]\œÂŠˆ˜Z[\™\È\™H^[œÚ]™B•\ÙN‚Šˆ[™ÑÜ˜\
Ü[‹\Ûİ\˜ÙJBŠˆQÈ
X[˜YÙY
B—×××××××××××××××Â‚‚“Ü[‹TÛİ\˜ÙHœÈX[˜YÙY“Ü[‹TÛİ\˜ÙH
[™ĞÚZ[ˆÈ[™ÑÜ˜\
B”›ÜÎ‚Šˆ›ÈØÚËZ[‚Šˆ[ÛÛ›ÛŠˆ[Ù[XYÛ›ÜİXÂÛÛœÎ‚Šˆ[İHİÛˆÜÂŠˆ[İHİÛˆÙXİ\š]BŠˆ[İHİÛˆ˜Z[\™\Â—×××××××××××××××Â‚‚“X[˜YÙY
ÛÛÙÛHQÊB”›ÜÎ‚ŠˆZ[Z[ˆØY™]BŠˆZ[Z[ˆÜÂŠˆZ[Z[ˆØØ[[™ÂÛÛœÎ‚Šˆ™[™ÜˆØÚËZ[‚Šˆ\ÜÈ›^Xš[]BŠˆYÚ\ˆ˜\ÙHÛÜİ—×××××××××××××××Â‚‚ÛÜİ	ˆØÚËR[ˆÛÛœÚY\˜][ÛœÈ
™\H[\Ü[
B’Y[ˆÛÜİÈÙˆÜ[‹TÛİ\˜ÙBŠˆ[™Ú[™Y\š[™È[YBŠˆØœÙ\˜Xš[]BŠˆİX\™˜Z[ÂŠˆÙXİ\š]H™]šY]ÜÂ’Y[ˆÛÜİÈÙˆX[˜YÙYŠˆ]›Ü›H™Y\ÂŠˆ™[™Üˆ\[™[˜ŞBŠˆZYÜ˜][ÛˆY™šXİ[B•HÚX\\İœ˜[Y]ÛÜšÈ\ÈHÛ™H]˜Z[ÈHX\İ[ˆ[İ\ˆÛÛ^‚—×××××××××××××××Â‚‚”ÚYKXKTÚYNˆØ[YHYÙ[[ˆÈœ˜[Y]ÛÜšÜÂ‘ÛØ[¸ 'İ[[X\š^™H\ØYYØİ[Y[Ë¸ 'B—×××××××××××××××Â‚‚“[™ĞÚZ[ˆ
˜\İ\İ
BœXHH™]šY]˜[PK™œ›ÛWØÚZ[—İ\J‹‹ŠBœXKœ[Š]Y\JB‚‚—×××××××××××××××Â‚‚“[™ÑÜ˜\
ÛÛ›ÛY
B”İ\8¡¤ˆ™]šY]™H8¡¤ˆİ[[X\š^™H8¡¤ˆ[™‚‚‘^XÚ]İ]K™]HÙÚXË[œÜXİX›H›İË‚—×××××××××××××××Â‚‚‘ÛÛÙÛHQÈ
Ûİ™\›™Y
B•\ÚÈYš[™Yˆ8¡¤ˆÚÚ[[›ÚÙYˆ8¡¤ˆÛÛ^Xİ]Yˆ8¡¤ˆÛXŞHÚXÚÙYˆ8¡¤ˆ™\İ[ÙÙÙY‚‚—×××××××××××××××Â‚‚’Ù^H\ÚYÛˆ[œÚYÚ
\È\ÈHZÙX]Ø^JB•\ÙHœ˜[Y]ÛÜšÜÈ\™H›İÛÛ\]]ÜœÈ8 %^H\™H^Y\œÈÙˆX]\š]K‚•\XØ[]›Û][Û‚“[™ĞÚZ[‚ˆ8¡¤ˆ[™ÑÜ˜\ˆ8¡¤ˆÛÛÙÛHQÂ‚‚\Î‚ŠˆX[HÚ^™HÜ›İÜÂŠˆš\ÚÈ[˜Ü™X\Ù\ÂŠˆŞ\İ[H™XÛÛY\ÈÜš]XØ[—×××××××××××××××Â‚‚ÛÛ[[ÛˆZ\İZÙ\ÈÈ]›ÚY¸§c\Ú[™ÈQÈ›ÜˆXÚØ]ÛœÂ¸§c\Ú[™È[™ĞÚZ[ˆYÙ[È›Üˆ[\œš\ÙHÜÂ¸§cÚÚ\[™È[™ÑÜ˜\›ÜˆÛ™Ë\[›š[™ÈYÙ[Â¸§cİ™\‹[Ü[Z^š[™Èœ˜[Y]ÛÜšÈÚÚXÙHÛÈX\›B¸§cYÛ›Üš[™È]\™HZYÜ˜][ÛˆÛÜİ