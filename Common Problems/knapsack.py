#recursive only approach
def recursive_knapsack(weight_capacity, items, index):
    if index < 0:
        return 0
    elif items[index][0] > weight_capacity:
        return recursive_knapsack(weight_capacity, items, index - 1)
    else:
        return max(recursive_knapsack(weight_capacity, items, index - 1), recursive_knapsack(weight_capacity - items[index][0], items, index - 1) + items[index][1])

#recursive with memoization
def recursive_memo_knapsack(weight_capacity, items, index, memo):
    if index < 0:
        return 0
    elif items[index][0] > weight_capacity:
        return recursive_memo_knapsack(weight_capacity, items, index - 1, memo)
    elif memo[index][weight_capacity] != -1:
        return memo[index][weight_capacity]
    else:
        memo[index][weight_capacity] = max(recursive_memo_knapsack(weight_capacity, items, index - 1, memo), recursive_memo_knapsack(weight_capacity - items[index][0], items, index - 1, memo) + items[index][1])
        return memo[index][weight_capacity]