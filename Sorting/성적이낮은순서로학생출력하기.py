import sys
input = sys.stdin.readline

n = int(input().strip())

std_li = []
for _ in range(n):
    name, grade = input().strip().split(' ')
    std_li.append((name, int(grade)))  # grade를 정수로 변환하여 저장

# 람다 표현식을 사용하여 정렬
std_li.sort(key=lambda x: x[1])

for name, _ in std_li:
    print(name, end=' ')

# 딕셔너리 사용 x : 중복 처리하기 어려움. 같은 성적을 가진 학생이 여러 명 있을 경우, 딕셔너리의 키(성적)가 중복될 수 있으므로, 마지막에 입력된 학생의 이름만 저장되고 나머지는 덮어쓰여집니다.