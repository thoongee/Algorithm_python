# 음료수 얼려먹기 문제랑 조금 유사함.

def solution(n, computers):
    def dfs(start):
        stack = [start]
        while stack:
            j = stack.pop()
            if not visited[j]: # visited[j] = False 이면,
                visited[j] = True
                for i in range(n):
                    if computers[j][i] == 1 and not visited[i]:
                        stack.append(i)

    networks = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            networks += 1  # 새로운 네트워크 발견

    return networks