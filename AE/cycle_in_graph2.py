def cycleInGraph(edges):
    # Write your code here.
    for i in range(len(edges)):
        if dfs_find_cycle(edges, i):
            return True
    return False


def dfs_find_cycle(edges, target):
    stack = [target]
    seen = set()
    while stack:
        curr = stack.pop()
        if target in edges[curr]:
            return True
        seen.add(curr)

        for child in edges[curr]:
            if child not in seen:
                stack.append(child)

    return False


inputx = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]

print(cycleInGraph(inputx))
