import sys
input = sys.stdin.readline

n, m, k = map(int, input().strip().split())
team = 0 

while n >= 2 and m >= 1 and n + m >= k + 3:  # 2명의 여학생과 1명의 남학생이 필요하고, 인턴쉽에 참여하지 않을 충분한 인원이 남아있어야 함
  team += 1
  n -= 2
  m -= 1

print(team)
