#A program to implement Alpha beta search 


tree = [[5, 5, 1, 2], [8, 8, -4, 9], [[9, 4, 5], [-1, 4, 3]]]
pruned = 0 

def alphabeta(node, depth, alpha, beta, maximizingPlayer):
    global pruned

    # If node is a leaf node (no children)
    if type(node) is not list:
        return node

    if maximizingPlayer:
        maxEval = float('-inf')
        for child in node:
            eval = alphabeta(child, depth + 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                pruned += 1
                break  # Beta cut-off
        return maxEval
    else:
        minEval = float('inf')
        for child in node:
            eval = alphabeta(child, depth + 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                pruned += 1
                break  # Alpha cut-off
        return minEval


def run_alphabeta():
    global pruned
    pruned = 0
    result = alphabeta(tree, 0, float('-inf'), float('inf'), True)
    print("Final Result:", result)
    print("Times pruned:", pruned)


if __name__ == "__main__":
    run_alphabeta()