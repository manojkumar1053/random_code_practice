def cycleInGraph(edges):
    # Write your code here.
    number_of_nodes     = len(edges)
    visited             = [False for _ in range(number_of_nodes)]
    currently_in_stack  = [False for _ in range(number_of_nodes)]

    for node in range(number_of_nodes):
        if visited[node]:
            continue
        
        conatins_cycle = isNodeInCycle(node, edges, visited, currently_in_stack)
        if conatins_cycle:
            return True
    return False

def isNodeInCycle(node, edges, visited, currently_in_stack):
    visited[node]               = True
    currently_in_stack[node]    = True

    neighbors = edges[node]
    for neighbor in neighbors:
        if not visited[neighbor]:
            contains_cycle = isNodeInCycle(neighbor, edges, visited, currently_in_stack )
            if contains_cycle:
                return True
        elif currently_in_stack[neighbor]:
            return True

    currently_in_stack[node] = False
    return False
    

inputx = [[1, 3], [2, 3, 4], [0], [], [2, 5], []]

print(cycleInGraph(inputx))