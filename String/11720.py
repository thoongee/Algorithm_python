import sys
input = sys.stdin.readline

N = int(input())

string = input().strip()

res = 0
for i in range(N):
    res += int(string[i])

print(res)

## 내 풀이 : 문자열도 마치 배열처럼 인덱싱이 된다는 성질을 이용함

## 다른 풀이 : 애초에 입력을 받을 때, list함수를 이용하여 숫자를 한 자리씩 나누어 입력받음 ['5', '4', '3', '2', '1']

'''
n = input()
numbers = list(input())
print(numbers)

sum = 0

for i in numbers : 
    sum = sum + int(i)

print(sum)
'''