import sys
input = sys.stdin.readline

case = int(input().strip())

for i in range(case):
    n,m = map(int, input().strip().split())
    level = list(map(int, input().strip().split()))
    position = [0]*n
    position[m] = 1 # 몇번째로 인쇄되었는지 궁금한 문서(=1)는 현재 m번째 인덱스에 있음
    cnt = 0

    while True:
        if level[0] == max(level): # 주어진 문서 중 가장 큰 값이 맨 앞에 있을때
            cnt += 1 # 해당 문서 인쇄! 한다는 의미

            if position[0] == 1: # 몇번째로 인쇄되었는지 궁금한 문서가 맨 앞에 있을때
                print(cnt) 
                break # 코드 종료

            level.pop(0)
            position.pop(0)

        else: # 주어진 문서 중 가장 큰 값이 어디 중간쯤 있을 때 
            level.append(level.pop(0))
            position.append(position.pop(0))