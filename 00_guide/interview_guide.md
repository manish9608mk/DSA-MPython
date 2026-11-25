# Interview Guide: how to prepare for today's tech industry

DSA gets you through the coding rounds. Getting hired also needs **communication, behavioral stories, a credible portfolio and (for your goal) cloud/infra skills**.
Nobody can guarantee a result. This guide is built to raise your odds and to keep you employable even if one interview goes badly.

## 1. What the process usually looks like

| Stage | What happens | How to prepare |
|---|---|---|
| Resume / referral | a human or a tool screens you | one page, measurable projects, working links; a referral helps a lot |
| Online assessment (OA) | 60 to 120 minutes, usually 2 to 3 coding problems, sometimes MCQs or a work-style / situational section | timed practice on Easy/Medium, `PRACTICE_TRACKER.md` ⭐ list |
| Phone / video screen | 45 to 60 minutes, 1 to 2 problems live | think aloud, clarify, test |
| Final loop | 2 to 5 rounds: coding, behavioral, sometimes design or debugging | mocks, story bank, fundamentals |

Formats change by company, role, country and year. **Always follow the recruiter's email and the company's official pages.**

## 2. Suppose, If you are applying to Amazon (your internship application)

- Amazon states on its own careers site that it uses an **online assessment** for software roles. Read the official preparation page (search "Amazon online assessment prep for SDE roles" on amazon.jobs) and your invitation email for the exact format and time limits.
- **Candidate reports** (not official, they vary by year and country) usually describe: an OA with **coding problems** (LeetCode Easy/Medium style), a **work-style / behavioral** part, then one or more interviews with **coding + Leadership Principles questions**.
- Your role is "Programmer Analyst Intern", which can differ from the "SDE Intern" process people write about. Do not assume; read your email.
- **Leadership Principles (LPs):** Amazon behavioral questions are built around them. Learn the current list on amazon.jobs (it has 16 principles, for example Customer Obsession, Ownership, Dive Deep, Bias for Action, Deliver Results, Learn and Be Curious, Earn Trust, Have Backbone; Disagree and Commit).
- Build a **story bank of 6 to 8 stories** from your own work (projects, college, teamwork). Each story should be tellable in 2 minutes and fit 2 or 3 LPs. Use your real projects (for example MurphAI) with real numbers. Do not invent anything: interviewers dig into details.

## 3. The online assessment: a strategy

1. **Read all problems first** (3 to 5 minutes). Start with the one you are most sure of.
2. **Budget time:** about 25 to 30 minutes per problem, leave 10 minutes at the end to re-test.
3. For each problem: examples → brute force → optimized → code → test the **edge cases** (empty, one element, duplicates, large values).
4. **Partial credit counts.** A correct brute force that passes some tests beats a half-written optimal solution.
5. Watch the constraints (`n ≤ 10⁵` means O(n log n)). See `PATTERN_CHEATSHEET.md`.
6. Use only the language features you know well. Standard imports (`heapq`, `collections`, `bisect`) are usually allowed.
7. Practice in the **same kind of editor** (no autocomplete, no internet). Do 3 full mock OAs before the real one.

## 4. How to solve a problem live (use this order every time)

1. **Clarify:** input size, duplicates, negatives, sorted?, empty?, return type.
2. **Examples:** write one normal and one edge case.
3. **Brute force:** say it and its complexity.
4. **Optimize:** name the pattern and why it fits.
5. **Code:** clear names, small functions, no silent assumptions.
6. **Test:** walk through your example, then edge cases.
7. **Complexity:** time and space, and what you would improve with more time.

Example of speaking (Two Sum): "Brute force checks every pair, O(n²). For each number I need its complement, so I store seen numbers in a hash map: one pass, O(n) time, O(n) space. Edge cases: duplicates, no answer, negative numbers."

Interviewers grade **communication and reasoning** as much as the final code. A correct answer in silence scores lower than a nearly correct answer with clear thinking. If you are stuck, say what you tried and what you suspect: that is a signal, not a weakness.

## 5. Behavioral rounds (STAR)

**S**ituation (1 sentence), **T**ask (what you were responsible for), **A**ction (what **you** did, 60% of the story), **R**esult (numbers, and what you learned).

Prepare stories for: a hard technical problem, a failure, disagreeing with someone, taking initiative without being asked, a tight deadline, learning something quickly, helping a teammate, a decision with incomplete information.

Common mistakes: saying "we" for everything, no result, no numbers, a story with no obstacle, blaming others.

## 6. Debugging and code-reading rounds

Some interviews give you broken code. Habit: **reproduce → read the error → form a hypothesis → check with a print/test → fix → re-run all tests**. Read the whole function before changing it. Say your hypothesis aloud.

## 7. Using AI tools in this era

- Many people use AI assistants daily and interviews keep adapting. **Policies vary by company and by round: follow the instructions you are given and never use hidden help.**
- The valuable skill is **understanding**: explain why a solution works, find a bug, adapt it when requirements change. AI makes writing code cheaper, so reasoning, debugging, design and communication matter more.
- Use AI to **learn faster**: quiz you, explain a mistake, generate edge cases, review your complexity analysis, give a hint without the answer. Do **not** paste a problem and copy the answer: that trains dependence, which is the opposite of your goal.
- Good prompt: "Here is my solution to LC 560 and my reasoning. Find the weakest point in my explanation and give me 3 edge cases that could break it. Do not rewrite the code."


## 8. Your GitHub as a portfolio

- Solutions with approach, complexity and tests show communication. 
- Never list tools or skills on the resume that you cannot discuss for 5 minutes.

## 9. A 30-day checklist before an interview window

- Week 1 to 2: finish the ⭐ list for arrays, strings, hashing, two pointers, sliding window, binary search.
- Week 3: trees, graphs (BFS/DFS), linked list, stack; one full mock OA.
- Week 4: DP basics, heap, greedy; two mock interviews aloud; story bank ready; resume proofread.
- Day before: sleep, light revision of `PATTERNS.md`, set up the editor and internet, read the invite again.
- After each interview: write down the questions and what went wrong (feeds the error log).

## 10. Habits that decide results

1. **Consistency over intensity:** 2 focused hours daily beat a 12-hour weekend.
2. **Blind practice:** "I understand the solution" is not "I can solve it".
3. **Write the explanation** after every problem.
4. **Mock interviews:** at least 4 before real ones. Speaking is a separate skill.
5. **Sleep and breaks.** Tired practice teaches bad habits.
6. **Apply early and often.** Rejections are data, not verdicts.
7. **Stay current:** tools change, fundamentals (data structures, complexity, systems thinking) do not.

## 11. Revision - Speak it

For every blind problem explain in this order: clarify, example, brute force, optimization, complexity, edge cases, code. Record yourself once a week. Speaking is a separate skill from coding.

## 12. Beyond DSA for your goal (Cloud → DevOps → Platform/SRE)

| Area | What to learn and show |
|---|---|
| Linux and shell | processes, files, permissions, `grep`/`awk`/`sed`, bash scripting, systemd |
| Networking | TCP/IP, DNS, HTTP/HTTPS, TLS, load balancers, ports |
| Git and CI/CD | branching, pull requests, GitHub Actions |
| Containers | Docker, then Kubernetes basics (pods, services, deployments) |
| One cloud deeply | AWS (EC2, S3, IAM, VPC, RDS, Lambda) or the GCP/Azure equivalents |
| Infrastructure as code | Terraform (and Ansible) |
| Observability | logs, metrics, tracing, Prometheus/Grafana, alerts, SLI/SLO, incident response |
| Python for automation | scripts, APIs, `requests`, `argparse`, testing with `pytest` |
| Databases | SQL basics, indexes, transactions; caching (Redis) |
| System design basics | scaling, caching, queues, replication, consistency, rate limiting |

DSA that matters most for infrastructure roles: hashing, arrays/strings, graphs (dependency graphs, topological sort), heaps/scheduling, queues, caches (LRU/LFU), rate limiters, trees (file systems), basic DP. `24_design_problems` covers LRU/LFU, rate limiter, consistent hashing.

**Show it:** 2 or 3 real projects: a containerized app with a CI/CD pipeline, deployed on a cloud free tier, with monitoring. A README with an architecture diagram beats ten tutorial copies.

## 12A. Beyond DSA for an AI Engineer (building products with LLMs)

**What the role is:** an AI Engineer is a software engineer who **builds products on top of existing models** (prompts, retrieval, tools, agents, evaluation) and ships them reliably. An ML Engineer (next section) mostly **trains and ships models**. Titles are inconsistent: the same job may be called AI Engineer, GenAI Engineer, Applied AI Engineer or LLM Engineer. At a small startup one person does both; at a large company they are separate teams. **Read the job description, not the title.**

**How it connects to your current path:** cloud, Docker, CI/CD, FastAPI and observability are exactly what AI products need in production (often called **LLMOps** or AI platform work). Your cloud track is not wasted: it is the foundation here.

| Area | What to learn and show |
|---|---|
| Strong Python + backend | FastAPI, async, REST, auth (JWT), databases, queues, tests with `pytest` (you already have much of this) |
| LLM APIs | chat/completions, **structured output** (JSON schema), **tool / function calling**, streaming, retries, rate limits, timeouts |
| Prompt design | clear instructions, examples, constraints, system vs user messages, versioning prompts like code |
| **RAG** | embeddings, chunking strategies, vector search (FAISS, pgvector, Qdrant, etc.), hybrid search, reranking, answers **grounded with citations** |
| Agents | tool use, planning loops (ReAct style), tool integrations (for example MCP-style servers), memory, human-in-the-loop, failure handling and step limits |
| **Evaluation** | golden datasets, offline evals, regression tests for prompts, LLM-as-judge **with its limits**, human review, measuring retrieval quality and answer quality separately |
| LLMOps and observability | tracing each step, logging prompts and outputs, token/cost/latency dashboards, caching, A/B tests, rollbacks |
| Safety and security | prompt injection, data leakage, PII handling, permissions for tools, output validation, guardrails |
| Fine-tuning basics | when to fine-tune vs prompt vs RAG; LoRA/QLoRA idea; data quality matters more than quantity |
| Cost and serving | model routing (small vs large models), batching, caching, context-window management, quantization (concept) |

**The key judgment interviewers look for:** *when to use prompting, RAG or fine-tuning, and when not to use an LLM at all.* Explain trade-offs in terms of **quality, latency and cost**.

**What the interview loop usually contains (reports vary by company):**

| Round | What is tested |
|---|---|
| Coding | LeetCode-style DSA and Python, sometimes with an AI flavour (this is why your DSA work still matters) |
| LLM / ML fundamentals | transformers and attention (idea level), embeddings, tokens, hallucinations, sampling parameters |
| **AI system design** | design a document Q&A / RAG system, a support agent, a code assistant: data flow, retrieval, evaluation, cost, latency, safety |
| Project deep-dive | your real project, your decisions, your numbers |
| Take-home | build a small RAG or agent app in 1 to 7 days, and explain it |
| Behavioral | ownership in ambiguous work (use the STAR stories from section 5) |

**Questions to practice answering aloud:**
1. Design a RAG system for company documents. How do you choose chunk size? How do you know retrieval works?
2. How would you evaluate an LLM feature before and after launch?
3. How do you reduce hallucinations?
4. RAG vs fine-tuning: when would you choose each?
5. How do you control cost and latency for 1 million requests a day?
6. What is prompt injection and how do you defend against it?
7. How would you design an agent that can call tools safely? What are its failure modes?
8. How do embeddings and vector search work? What is approximate nearest neighbour search?

**DSA links that actually help here:** hash maps (caching, deduplication), heaps (top-k retrieval), tries (prefix search), graphs (workflow/agent DAGs, dependency ordering), queues and rate limiters (`24_design_problems`), and LRU/LFU caches.

**Three portfolio projects (build them in this order):**
1. **RAG over your own documents** with a small **evaluation harness** (a test set, retrieval hit-rate, answer quality checks) and citations. Deploy it on a cloud free tier.
2. **A tool-using agent** with a small, safe tool set, step limits, tracing/logging and an eval suite that catches regressions.
3. **An LLM-backed API** with FastAPI, Docker and CI, a cost/latency dashboard, and prompt-injection tests. Put **numbers** in the README (latency, cost per request, eval scores).

**A 12-week path (about 10 hours per week, alongside DSA):**

| Weeks | Focus |
|---|---|
| 1 to 2 | LLM API basics, structured outputs, tool calling; build a small CLI assistant |
| 3 to 5 | embeddings, vector search, chunking, RAG; project 1 |
| 6 to 7 | evaluation: build the eval harness, compare prompt/retrieval variants with numbers |
| 8 to 9 | agents and tool integrations; project 2 |
| 10 to 11 | serving, observability, caching, security; project 3 |
| 12 | AI system design practice, mock interviews, polish READMEs |

**Resources (check for the current version of each):** the documentation and prompt/tool-use guides of the major model providers, the Hugging Face courses, DeepLearning.AI short courses, and the book *AI Engineering* by Chip Huyen.

**Common mistakes:** collecting frameworks instead of understanding the ideas (tools change every few months, the fundamentals do not), building demos with **no evaluation**, ignoring cost and latency, claiming results you did not measure, and never reading what the model actually received (always log prompts and retrieved context).

## 12B. Beyond DSA for an AI / ML Engineer (training and shipping models)

**What the role is:** an ML Engineer builds, evaluates and deploys **models trained on data**: problem framing, data pipelines, features, training, evaluation, serving and monitoring. It sits between software engineering and applied data science. **Research scientist** roles usually need deeper math and often a graduate degree; **ML engineer** and **applied scientist** roles value strong engineering plus solid fundamentals.

**What you already have:** from your GitHub skills (Python, scikit-learn, Pandas, NumPy, MLflow, FastAPI, Docker, GitHub Actions, GCP/Vertex AI) you already have a base for **MLOps**. Your gaps are mostly **math depth, deep learning in PyTorch, ML system design and evaluation rigor**.

| Area | What to learn and show |
|---|---|
| Math | linear algebra (vectors, matrices, eigenvalues idea), probability, statistics (distributions, hypothesis tests), calculus for gradients, optimization (gradient descent and variants) |
| Python data stack and SQL | NumPy, Pandas, Matplotlib, **strong SQL** (joins, window functions, aggregations); SQL carries weight in ML interviews |
| Classical ML | linear/logistic regression, decision trees, random forest, **gradient boosting** (XGBoost/LightGBM), k-means, PCA; bias-variance, regularization (L1/L2), cross-validation |
| Evaluation | precision, recall, F1, ROC-AUC vs PR-AUC, calibration, regression metrics; **choosing the metric that matches the business problem**; data leakage; imbalanced classes |
| Deep learning | backpropagation, optimizers, initialization, normalization, CNN/RNN basics, **transformers and attention**, embeddings; writing a PyTorch training loop |
| NLP / LLM basics | tokenization, pre-training vs fine-tuning, LoRA/PEFT idea, evaluating language models |
| Recommenders, ranking, time series | basic ideas, because many interview cases come from these |
| Experimentation | A/B test design, metrics, sample size intuition, pitfalls |
| Data and feature pipelines | feature engineering, train/serve consistency, data validation, versioning |
| **MLOps** | experiment tracking (MLflow), model registry, CI/CD for ML, batch vs real-time serving, monitoring and **drift detection**, retraining, Docker/Kubernetes, Vertex AI / SageMaker |
| Scale basics | GPUs, mixed precision, data/model parallelism (concept level) |
| Responsible ML | bias and fairness, privacy, explainability basics |

**What the interview loop usually contains (reports vary):**

| Round | What is tested |
|---|---|
| Coding | LeetCode-style DSA, plus ML coding in NumPy (for example k-means, logistic regression, gradient descent from scratch, metric functions) |
| ML fundamentals | bias-variance, regularization, overfitting, metrics, optimization, how a model works inside |
| **Applied ML case** | "design a fraud / churn / recommendation model": problem framing, data, features, baseline, model, metric, validation, deployment, monitoring |
| ML system design | training and serving pipeline, feature store, latency, retraining, monitoring |
| SQL / data | queries and data-cleaning tasks |
| Project deep-dive and behavioral | your decisions, mistakes, numbers |

**Questions to practice answering aloud:**
1. Explain bias vs variance. How do you detect and fix overfitting?
2. How do you handle an imbalanced dataset? Which metric do you report and why?
3. What is data leakage? Give an example and how to prevent it.
4. L1 vs L2 regularization: effects and when to use each.
5. Explain gradient descent. What changes with momentum or Adam?
6. How does attention work, at idea level?
7. How do you monitor a deployed model? What is drift and how do you detect it?
8. A model has great offline metrics but fails in production. What do you check?

**Four portfolio projects:**
1. **End-to-end tabular ML:** proper train/validation/test split, a **baseline first**, error analysis, MLflow tracking, FastAPI serving, Docker, CI, and a monitoring plan.
2. **A PyTorch project:** for example fine-tune a small text classifier, compare it with a classical baseline and report the difference honestly.
3. **From-scratch implementations:** logistic regression, a small neural network, k-means (NumPy only). This proves you understand the maths, not just the library.
4. **A competition or dataset write-up:** problem framing, mistakes and what you would do next.

**A 6-month path (about 10 hours per week, alongside DSA):**

| Months | Focus |
|---|---|
| 1 | math refresh + NumPy/Pandas + SQL |
| 2 to 3 | classical ML with scikit-learn, evaluation, project 1 |
| 3 to 4 | deep learning with PyTorch, project 2 and the from-scratch notebooks |
| 5 | NLP, transformers, fine-tuning basics |
| 6 | MLOps and ML system design, mock interviews, polish READMEs |

**Resources (check for the current version of each):** Andrew Ng's Machine Learning and Deep Learning specializations, fast.ai, Andrej Karpathy's *Neural Networks: Zero to Hero* lectures, the Hugging Face courses, Google's Machine Learning Crash Course, the books *Hands-On Machine Learning* (Aurelien Geron) and *Designing Machine Learning Systems* (Chip Huyen), and the Stanford CS229 / CS224n lectures.

**Common mistakes:** jumping to deep learning before understanding baselines and evaluation, reporting accuracy on imbalanced data, data leakage in cross-validation, notebooks that only run on your laptop (no pipeline, no serving), no error analysis, and copying tutorials without changing the problem.

### Choosing your track (Cloud/DevOps/SRE vs AI Engineer vs ML Engineer)

| Track | Core strength it needs | Typical first target role | Best bridge from your current work |
|---|---|---|---|
| Cloud / DevOps / SRE (section 12) | Linux, networking, cloud, IaC, observability | Cloud or DevOps engineer | what you are already doing |
| AI Engineer (12A) | backend + LLM application skills + evaluation | AI/GenAI engineer, backend with AI | your FastAPI + cloud + Docker work |
| ML Engineer (12B) | math, ML fundamentals, deep learning, MLOps | ML engineer, applied scientist | your scikit-learn + MLflow + Vertex AI work |
| **MLOps / ML platform engineer** | cloud + DevOps + ML basics | MLOps / ML platform engineer | combines section 12 and 12B |

**Practical advice:** keep **DSA, Python and one cloud** as the common base for all tracks. Spend about 70% of your extra time on one primary track and 30% on a second, then decide after your first real projects and interviews. Interviews for all three still include coding rounds, so your DSA work is never wasted. Because the AI field changes quickly, prefer **fundamentals, evaluation and working systems** over memorizing tool names.
