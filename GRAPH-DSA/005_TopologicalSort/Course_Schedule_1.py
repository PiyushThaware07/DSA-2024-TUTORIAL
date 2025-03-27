'''
Problem Statement : Given numCourses and a list of prerequisites, determine if all courses can be finished. 
If there is a cycle in the course dependency graph, print "Cycle Found!"; otherwise, print "No Cycle Found!".
'''
class Solution:
    def canFinish_CourseSchedule(self,numCourses,prerequisites):
        # Build the adjacency list
        adjList = {node: [] for node in range(numCourses)}
        for destination,source in prerequisites:
            adjList[source].append(destination)
            
        # Calculate indegree for each node
        indegree = {node:0 for node in adjList}
        for node in adjList:
            for neighbor in adjList[node]:
                indegree[neighbor] += 1
        
        # Initialize the queue with nodes having indegree of 0
        queue = []
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
        
        # Perform Topological Sort using kahn algorithm
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current)
            # Decrease the indegree of neighbors
            for neighbor in adjList[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if a valid topological order exists
        if len(result) == numCourses:
            print("No Cycle Found!")     # All courses can be completed
            return
        else:
            print("Cycle Found!")        # There's a cycle in the graph
            return
                
        
        
        
        
    
# Example - 1
numCourses = 2
prerequisites = [[1,0]]

# Example - 2
numCourses = 2
prerequisites = [[1,0],[0,1]]

# Useage
sol = Solution()
sol.canFinish_CourseSchedule(numCourses,prerequisites)