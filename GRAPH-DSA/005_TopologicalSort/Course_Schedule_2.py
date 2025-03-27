'''
Problem Statement : 
You are tasked with developing a system to determine the order in which a student can complete their courses, given a list of prerequisites. 
Each course is assigned a unique integer from 0 to numCourses - 1. The prerequisites are provided as a list of pairs, where each pair [a, b]
indicates that course b must be completed before course a.

Your goal is to return a valid order of courses such that all prerequisites are satisfied. If there are multiple valid orders, return any of them.
If it is impossible to complete all courses, return an empty list.
'''

class Solution:
    def findOrder_CourseSchedule(self,numCourses,prerequisites):
        # Create adjacency list
        adjList = {node: [] for node in range(numCourses)}

        # Build the graph with correct edge direction
        for dest, src in prerequisites:
            adjList[src].append(dest)

        # Calculate indegrees
        indegree = {node: 0 for node in adjList}
        for node in adjList:
            for neighbor in adjList[node]:
                indegree[neighbor] += 1

        # Initialize the queue with nodes having indegree 0
        queue = []
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)

        # Perform topological sorting
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current)
            for neighbor in adjList[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Check if we have a valid topological order
        if len(result) == numCourses:
            print(result)
            return 
        else:
            print([])
            return []
        
        




# Example 01
numCourses = 2
prerequisites = [[1,0]]

# Example 02
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

# Usage
sol = Solution()
sol.findOrder_CourseSchedule(numCourses,prerequisites)