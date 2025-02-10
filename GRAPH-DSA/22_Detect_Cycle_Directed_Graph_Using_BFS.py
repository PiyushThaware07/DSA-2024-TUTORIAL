from common.graph import Graph

# Implement Toposort Kahns for it.
class Solution:
    def detectCycle(self,matrix):
        indegree = {node:0 for node in matrix}
        # Step-1 : generate indegree for all the node of a matrix.
        for node in  matrix:
            for neighbor in matrix[node]:
                indegree[neighbor] += 1
        
        # step-2 : push all the node having indegree 0 push them to queue
        queue = []
        for node in matrix:
            if indegree[node] == 0:
                queue.append(node)
        
        # Step-3 : pop the current node and print it or store to result and check for its neighbor and if it have neighbor just decrement there indegree if there indegree=0 then just add them to queue for futher processing.
        result = []
        while queue:
            currentNode = queue.pop(0)
            result.append(currentNode)
            for neighbor in matrix[currentNode]:
                indegree[neighbor] = indegree[neighbor] - 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(result) == len(matrix):
            print("no cycle found!")
        else:
            print("cycle found!")
                    
                


g = Graph()
g.addVertice("A")
g.addVertice("B")
g.addVertice("C")
g.addVertice("D")
g.addVertice("E")
g.addVertice("F")
g.addVertice("G")
g.addEdge("A","B","directed")
g.addEdge("B","C","directed")
g.addEdge("C","D","directed")
g.addEdge("B","E","directed")
g.addEdge("E","F","directed")
g.addEdge("F","G","directed")
g.addEdge("G","E","directed")

sol = Solution()
sol.detectCycle(g.graph)