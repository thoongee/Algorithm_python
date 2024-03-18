import sys
input = sys.stdin.readline

n = int(input())

# 3kg, 5kg 봉지 있음 -> 5는 3의 배수가 아닌데, 그럼 DP로 해야하는건가?

cnt = 0

while n>=0:
    if n%5 == 0: # n이 5의 배수라면
        cnt += n//5
        n = 0
        break
        
    n -= 3 # n이 5의 배수가 아닌 경우
    cnt += 1
    
if n==0:
    print(cnt)
else:
    print(-1) # 정확하게 N킬로그램을 만들 수 없다면 -1을 출력


'''
bag = 0
check = True
while(check):
    # 
    if n//5 >=1 :
        n = n//5
        bag += 1
    elif n//3 >=1 :
        n = n//3
        bag += 1
    else:
        bag = -1
        check= False

print(bag)
'''
