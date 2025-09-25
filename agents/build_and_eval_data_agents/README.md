# Data Agents

Data Agents are a stateful (memory-retaining) combination of assistant agents capable of coordinating and executing on an action plan related to data analysis.

# Evals

## "RAG Triad"

1. Query
2. Context
3. Response

Evals
* Context Relevance (Query ^ Context)
* Groundedness (Context ^ Response)
* Answer Relevance (Response ^ Query)

## GPA = Goal, Plan, Act

Evals
* Plan Quality (G ^ A)
* Plan Adherence (P ^ A)
* Execution Efficiency (A ^ G)
* Logical Consistency (G ^ P ^ A)

True lense = opensource trace for agents

## Improvement patterns

1. Find Failure Modes (use tracing)
2. Identify improvements
    1. Adjust prompts
    2. Inline evaluation
    3. Tune Retriever
    4. Tune specialized agent nodes
    5. Test different models
3. Validate improvements

# Resources

* OpenAI API
* Tavily API

# References

Based on lessons from the "Building and Evaluating Data Agents" course on [DeepLearning.AI](https://www.deeplearning.ai/).