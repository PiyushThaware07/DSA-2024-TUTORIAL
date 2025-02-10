'''
When a node is visited, it is marked as visited to prevent revisiting the same node.
If a node is already visited (but not the immediate parent of the current node), it means we have encountered a back edge, indicating a cycle.
'''
def dfs(node, parent, visited, grid):
    visited[node] = True
    for neighbor in grid[node]:
        if not visited[neighbor]: 
            if dfs(neighbor, node, visited, grid):
                return True
        elif neighbor != parent:
            return True
    return False

def cycle_detect(grid):
    visited = {node: False for node in grid}
    for node in grid:
        if not visited[node]:
            if dfs(node, -1, visited, grid):
                print("Cycle Found!")
                return
    print("Cycle Not Found!")

grid = {
    1: [2],
    2: [1,3],
    3: [2,4,5],
    4 : [3,5],
    5 : [3,4]
}

cycle_detect(grid)
