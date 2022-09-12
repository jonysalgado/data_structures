from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def BFS(root:Node, target:Node) -> int:

    step = 0
    queue = deque()
    visited = set() # to avoid infinite recursion
    queue.append(root)
    visited.add(root)

    while len(queue) > 0:
        
        size = len(queue)
        for _ in range(size):
            cur = queue.popleft()
            if cur == target:
                return step
            if cur.left not in visited:
                queue.append(cur.left)
                visited.add(cur.left)
            if cur.right not in visited:
                queue.append(cur.right)
                visited.add(cur.right)
        
        step += 1


    return -1