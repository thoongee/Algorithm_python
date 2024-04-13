import sys

# 입력 함수 재정의
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):

    sentence = input().strip().split() # ['i', 'am', 'happy']
    
    # 각 단어를 뒤집어서 새로운 리스트에 저장
    reversed_words = [word[::-1] for word in sentence] # ['i', 'ma', 'yppah']

    # 단어를 공백을 기준으로 이어붙여 새로운 문장 생성
    reversed_sentence = ' '.join(reversed_words)

    print(reversed_sentence)