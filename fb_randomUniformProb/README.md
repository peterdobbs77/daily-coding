# randomElement_UniformProb

## Prompt

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

## Implementation

Reservoir Sampling! We need to choose a simple random sample (without replacement) with probability `1/n` of `k = 1` items from a population of unknown size `n` in a single pass.