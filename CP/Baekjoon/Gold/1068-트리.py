import sys

n = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
delete = int(sys.stdin.readline())

def dfs(del_node):
    tree[del_node] = -2
    for i in range(n):
        if del_node == tree[i]:
            dfs(i)

dfs(delete)

res = 0
for i in range(n):
    if tree[i] != -2 and i not in tree:
        res += 1

print(res)