import sys
input= sys.stdin.readline

words = input().strip()

# 입력 문자열이 비어 있지 않은 경우에만 단어의 개수 계산
if words:
    cnt = words.split(' ')
    print(len(cnt))
    
else:
    print(0)
    

