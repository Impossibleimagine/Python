#使用0/1/2/3/4/5產出三位不同數字的三位數，印出並計算數量
list = ['0','1', '2', '3','4','5']
visited = [False] * 6
ans = [''] * 3

def dfs(layer):
    if layer == 3:
        print(*ans)
        return

    for i in range(6):
        if visited[i]: #用過
            continue
        visited[i] = True 
        ans[layer] = list[i]
        dfs(layer + 1)
        visited[i] = False

dfs(0)
