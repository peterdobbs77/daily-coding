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