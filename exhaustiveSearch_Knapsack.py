# EXHAUSTIVE SEARCH / OPTIMIZATIONM, KNAPSACK
'''

#! EXHAUSTIVE SEARCH pseudocode:
best = None
for candidate in gen_candidates(instances):
    if verify(instance, candidate):
        if best is None or better(candidate, best):
            best = candidate
return best
Key Patterns: 
1. Find any solution
'''

'''
#! EXHAUSTIVE OPTIMIZATION PSEUDOCODE:
def exhaustive_optimize(instance):
    best = None
    for candidate in gen_candidates(instance):
        if verify(instance, candidate):
            if best is None or better(candidate, best):
                best = candidate
    return best
KEY PATTERNS:
1. find best solution
examples: TSP (minimize cost) , knapsack (maximize value)
'''

'''
#! KNAPSACK PROBLEM: 
given: set of items with weights wt[], values val[],
Knapsack with capacity W.
GOAL: Select a subset of items to maximie value without exceeding cap

DYNAMIC PROGRAMMING SOLUTION (efficient):
1. Create a 2D table dp[i][w] -> max value using first i itmes with cap w
2. Base case: dp[0][w] = 0 for all w (no items, no value)
Recursive relation: dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w-wt[i-1]])
if wt[i-1] <= w
dp[i-1][w] otherwise
Time & space complexity = O(n * W)
'''

'''
GCD: Optimization, Exhaustive optimize, O(min(a,b))
Powerset: Search/opt, Exhaustive search, O(2^n)
Circuit-SAT, search, exhaustive search, O(2^n * n)
TSP Optimization, exhaustive optimize, O(n!)
Knapsack Optimization, exhaustive optimize, O(2^n)
'''