import sys
input = sys.stdin.readline

c = int(input())
for _ in range(c):
    n = list(map(int,input().split()))
    total = 0

    for i in range(1,n[0]+1):
        total += n[i]

    avg = total/n[0]
    over = 0

    for i in range(1,n[0]+1):
        if n[i]>avg:
            over += 1

    ratio = over/n[0]*100
    print('%.3f%%'%ratio)
    
    ## 여기서는 strip을 안써도 되네? 왜그럴까?
