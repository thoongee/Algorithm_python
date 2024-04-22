import sys
sys.setrecursionlimit(10**6)    #10^6으로 최대 재귀 깊이 설정
input = sys.stdin.readline

def star(l):
    if l == 1:
        return['*']

    Stars = star(l//3)
    L = []

    for s in Stars:
        L.append(s*3) # N/3 패턴으로 '둘러싼' -> 둘러싸려면 *3
    for s in Stars:
        L.append(s+' '*(l//3)+s) # N/3의 공백
    for s in Stars:
        L.append(s*3) # N/3 패턴으로 '둘러싼' -> 둘러싸려면 *3
    return L

n = int(input().strip())
print('\n'.join(star(n)))