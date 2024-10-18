import math

# Alpha-Beta Pruning algorithm
def alpha_beta(depth, nodeIndex, isMaximizingPlayer, values, alpha, beta, maxDepth):
    # Terminal node (leaf nodes)
    if depth == maxDepth:
        print(f"Leaf node reached at depth {depth}, returning value: {values[nodeIndex]}")
        return values[nodeIndex]

    if isMaximizingPlayer:
        best = -math.inf

        # Maximizer's choice (MAX player)
        print(f"Maximizer at depth {depth}, alpha: {alpha}, beta: {beta}")
        for i in range(2):
            value = alpha_beta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, maxDepth)
            print(f"Maximizer at depth {depth}, comparing value: {value} with best: {best}")
            best = max(best, value)
            alpha = max(alpha, best)
            print(f"Maximizer at depth {depth}, updated alpha: {alpha}")
            if beta <= alpha:
                print(f"Pruning at depth {depth}, beta: {beta} <= alpha: {alpha}")
                break  # Beta cutoff
        print(f"Maximizer at depth {depth}, selected best: {best}")
        return best
    else:
        best = math.inf

        # Minimizer's choice (MIN player)
        print(f"Minimizer at depth {depth}, alpha: {alpha}, beta: {beta}")
        for i in range(2):
            value = alpha_beta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, maxDepth)
            print(f"Minimizer at depth {depth}, comparing value: {value} with best: {best}")
            best = min(best, value)
            beta = min(beta, best)
            print(f"Minimizer at depth {depth}, updated beta: {beta}")
            if beta <= alpha:
                print(f"Pruning at depth {depth}, beta: {beta} <= alpha: {alpha}")
                break  # Alpha cutoff
        print(f"Minimizer at depth {depth}, selected best: {best}")
        return best

# Test the Alpha-Beta Pruning algorithm
values = [3, 5, 6, 9, 1, 2, 0, -1]  # Example leaf nodes values
maxDepth = math.log2(len(values))  # Calculate the depth based on the values length

# Run the Alpha-Beta Pruning algorithm
start_depth = 0
start_index = 0
is_maximizing = True  # Start with the maximizer
alpha = -math.inf
beta = math.inf

best_value = alpha_beta(start_depth, start_index, is_maximizing, values, alpha, beta, int(maxDepth))
print("Optimal value found by Alpha-Beta Pruning:", best_value)
