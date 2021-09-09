from copy import deepcopy
import sys

cost = None
dp = None
tree = None
INF = sys.maxsize

sales, links = 	[14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
answer = 0
sales = [-1] + sales
cost = sales
print(cost, '코스트임')

tree = [ [] for _ in range(len(sales))]
dp = [[-1, -1] for _ in range(len(sales))]

for p, c in links:
    tree[p].append(c)

print(tree)
print(dp)

# 선택이 됐을 때, 안됐을 때 나눠서 해야대나

def dfs(n, include):
    if dp[n][include] != -1:
        return dp[n][include]

    ret = 0
    if include: # 선발된 경우,
        ret = cost[n] # 비용 대입
        for child in tree[n]:
            c_cost = min(dfs(child, 0), dfs(child, 1)) # 해당 노드의 자식이 선발이되건 안되건 최소값을 선택한다.
            ret += c_cost # 더해줌
        print(n, include, ret, '쳌')
        dp[n][include] = ret
        return dp[n][include]
    else: #선발되지 않았을 경우, 내 자식들중 하나는 무적권 포함되어야 함. (한팀당 한명 차출 필수)
        ans = 0
        diff = 0 if len(tree[n]) == 0 else INF # 자식이 없으면 0 있으면 무한대
        
        # 자식들이 참여안하면 flag = False
        flag = False

        for child in tree[n]:
            cost1 = dfs(child, 1)
            cost2 = dfs(child, 0)

            # 방문코스트가 방문안한 코스트보다 작다 = 자식들중 누군가가 참여했었다.
            if cost1 < cost2:
                flag = True
            else: 
                diff = min(cost1 - cost2, diff)

            ans += min(cost1, cost2)
        ret = ans if flag else diff + ans
        dp[n][include] = ret
        return dp[n][include]

print(min(dfs(1,1), dfs(1,0)))




