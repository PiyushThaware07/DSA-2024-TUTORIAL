# PROBLEM STATEMENT : It determines if there is a cycle in an undirected graph starting from a given node.


def detect_cycle(grid,start):
    queue = [(start,-1)]                        # (node,parent)
    visited = {node:False for node in grid}     # create a visited hashmap to track visiting of nodes
    while queue:
        node,parent = queue.pop(0)
        if visited[node]:
            print("Cycle Found!")
            return
        visited[node] = True
        for neighbor in grid[node]:
            if neighbor != parent:              # visit non-parent nodes.
                queue.append((neighbor,node))
    print("Cycle Not Found!")
    return
grid = {
    1 : [2],
    2 : [1,3],
    3 : [2,4,5],
    4 : [3,5],
    5 : [3,4]
}
detect_cycle(grid,1)