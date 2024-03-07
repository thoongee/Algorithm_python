#주어진 조건이 1,2번이라면
#코딩은 2->1 순으로
import sys
input = sys.stdin.readline #문자열에 개행문자\n 자동추가

n = int(input())
word_list = set() #set으로 선언하면 값이 추가될 때 알아서 중복값은 걸러줌

for i in range(n):
  word = input().strip()
  word_list.add(word) #append : list

word_list = list(word_list) # set->list
word_list.sort() #알파벳 순
word_list.sort(key = lambda x: len(x)) #짧은 것부터

print('\n'.join(word_list)) # join으로 \n포함하여 출력 --> for문 안써도 됌


