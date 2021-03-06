# sum_check_k

I'm sure there's a better way to describe this kind of problem than "sum check k" but that's what I'm going with. *So get over it already*

## Prompt
Given a list of numbers and a number `k`, return whether any two numbers from the list add up to `k`.

For example, given `[10, 15, 3, 7]` and `k` of `17`, return true since `10 + 7` is `17`.

Bonus: Can you do this in one pass?

## Implementation
According to my stop-watch, I finished in **27:06.40**. A lot of that time was spent setting up my debug environment, since VSCode was acting up, and correcting syntax because I get mixed up between *R*, *Matlab*, and *Python*. *__sigh__ such is the life of a grad student*

I saw <quote> one pass </quote> and interpreted that as the solution shouldn't perform the same sum twice. So, I did a nested loop with bounds that advance through the list, avoiding the duplicated sum. I'm probably over-thinking it, but I feel like there might be a better way? I started to go down the rabbit hole of [Faulhaber's formula](https://en.wikipedia.org/wiki/Faulhaber's_formula), but stopped myself when I saw how much time I had spent on that page.
