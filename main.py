
# BINARY TREE - JUAREZ

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree
root = Node("J")
root.left = Node("U")
root.right = Node("A")
root.left.left = Node("R")
root.left.right = Node("E")
root.right.left = Node("Z")


# Breadth-First Search (BFS)
def bfs(root):
    queue = [root]

    print("BFS:", end=" ")

    while queue:
        current = queue.pop(0)
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)


# Depth-First Search (DFS)
def dfs(root):
    if root is None:
        return

    print(root.data, end=" ")
    dfs(root.left)
    dfs(root.right)


print("BINARY TREE - JUAREZ")

bfs(root)

print("\nDFS:", end=" ")
dfs(root)

print()
