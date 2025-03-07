class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        queue = [root]
        height = 0
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode = queue.pop(0)
                if currentNode.children:
                    queue.extend(currentNode.children)
            height += 1
        return height

# Example Usage
if __name__ == "__main__":
    # Constructing an N-ary tree
    root = Node(1, [
        Node(2),
        Node(3, [Node(5), Node(6)]),
        Node(4)
    ])

    solution = Solution()
    print("Maximum Depth:", solution.maxDepth(root))  # Output: 3
