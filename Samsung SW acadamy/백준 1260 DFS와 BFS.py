import sys

sys.stdin = open("input.txt", "r")

n, m, v = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
#print(matrix)

for _ in range(m):
    start, end = map(int,input().split())
    # Matrix connect
    matrix[start][end] = 1
    matrix[end][start] = 1

def DFS(root, visited):
    visited += [root]
    for i in range(len(matrix[root])): # 시작 노드의 자식 노드길이만큼 DFS
        if matrix[root][i] == 1 and i not in visited: # 연결된 노드가 있으며, visited 하지 않았다면 자식노드로 DFS 수행
            DFS(i, visited)

    return visited


def BFS(root):
    visited = [root]
    queue = [root]

    while queue:
        node = queue.pop(0)
        for i in range(len(matrix[root])): # 똑같이 시작 노드의 자식 길이만큼 BFS.
            if matrix[node][i] == 1 and i not in visited:
                visited.append(i)
                queue.append(i)
    return visited

print(*DFS(v,[]))
print(*BFS(v))