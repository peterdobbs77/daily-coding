# Agentic AI

"agentic" was invented as a word to avoid the debate over what is an agent

## Why Agentic AI?

Agentic AI is an expansion on zero-shot Generative AI. More than just leveraging the memory of a Generative AI model, Agentic AI provides a network of operational components that can be combined and evolved to accomplish a task (or set of tasks).

Agentic AI can make decisions without user input

## Reflection

__Reflection__ benefits greatly from additional input from external sources. In addition to providing the response of another model to the reflection step, feed in the result of executing on that response. For example, in the case of reflecting on a SQL query generated to answer some question posed by the user, provide the result of that SQL query as an input to the reflection step.

## Tool Use

__Tools__ provide additional functionality to LLMs, creating powerful agents that can perform advanced calculations, author custom code, manage emails and tasks, provide customer support, perform market research, interact with MCP servers, and more!

## Evaluation ("evals")

End-to-end Evaluation techniques and examples
| - | code (objective) | LLM Judge (subjective) |
| --- | --- | --- |
| Per-example\n ground truth    | ex: invoice date extraction | ex: count gold-standard talking points |
| No per-example\n ground truth | ex: copy length within acceptable bounds | ex: standard rubic for visualizatons |

Error analysis is a critical step in the iterative development of Agentic AI. Starting from as early as a prototype, reviewing Traces (end-to-end eval) and Spans (individual component-level eval) will allow a developer to detect problem areas or bottlenecks. (see OpenTelemetry's [Observability primer](https://opentelemetry.io/docs/concepts/observability-primer/))

Sample "Span" (component-level) evaluation method...using the example of a research agent
1. Create gold standard ground truth web resources
2. Write comparison code between ground truth and actual results at each component (e.g., [F-score](https://en.wikipedia.org/wiki/F-score))
3. Track as you vary hyperparameters (e.g., search engine, number of results, dates)

## Improving non-LLM component performance
(e.g., web search, text retrieval for RAG, code execution, trained ML model)

* Tune hyper parameters of component (web search: # results, date range; RAG: change similarity metric, chunk size; ML models: detection threshold)
* Replace component (the power of MODULARITY)

## Improving LLM component performance

* Improve prompts -- more explicit instructions, provide concrete examples ("few-shot" prompting)
* Try a new/different model -- use evals to select the most appropriate
* Split up the step -- task decomposition is critical!
* Fine-tune a model -- tune on internal data to improve performance (complex, so often reserved for improving over the final 5%)

## Develop intuition for model intelligence
* Play with models often
    * make personal set of evals
    * read other people's prompts
* Use different models in agentic workflows
    * which models work for which types of tasks?
    * [aisuite](https://github.com/andrewyng/aisuite) makes it easy to swap out models

## Optimizing: latency and cost

After first optimizing for output quality, you'll want to ship your agentic workflow to production. At that point (maybe a bit before), you must consider latency and cost as metrics for user experience and financial efficiency.

Costing/pricing your workflow
* LLM steps = pay per token
* Any API-calling tools = pay per API call
* Compute steps = server capacity / cost

## Autonomous Agentic Workflows: Planning

Though currently experimental, planning workflows are a huge step in autonomous agentic ai. Rather than hard-coding an full agentic workflow, a developer would provide a Planner agent with a set of tools to accomplish a scope of work and then instruct an LLM to execute the resulting Plan from that Planner agent.

Recommendation (pass this as requirements to the system prompt): Format plan as JSON

Example system prompt
```
You have access to the following tools:
{list of tools and descriptions of the tools}

Create a step-by step plan in JSON format.

Each step should have the following items: step number, description, tool name, and args. 
```

Planning with tools is pretty neat, but it is overly restrictive (brittle, inefficient, continuously dealing with edge cases not covered by tools). Instead, you could **plan with code execution**!

## Multi-agent Workflows

Each agent can focus on one capability at a time. Teams/developers can focus on improving individual agents, which can help with task allocation at a company.

Planning with multiple agents does not _have_ to be completed linearly. It can be advantageous to have an orchestrator (or manager) agent that decides how the agents coordinate to accomplish a given assignment.

## Communication patterns for multi-agent systems

### Linear

results are passed directly from one agent to the next (and possibly even further down the pipeline)

### Hierarchical / Orchestrated

results passed up the hierarchy before moving along to the next step

### Deeper Hierarchy

agents have sub-agents for refinement/reflection or other agentic tooling

### All-to-all (peer-to-peer)

all agents have all intermediate and final outputs from other agents

# Idea:

optimize an agentic planning workflow with cached responses to FAQ based on similarity threshold.

web-hosted agentic workflow that can access a research database of anonymized (de-identified) patient records to provide intelligence about various diseases