# 10845랑 문제는 같다.
# 같은 답을 냈더니 10845는 84ms인 반면, 18258은 2036ms가 걸린다. 왜지??
# 이건 980ms 나온 사람의 답 (덱 사용)
import sys
from collections import deque
class Queue:
  def __init__(self,N):
    self.queue_list = deque([])
    self.size = 0
    self.capacity = N
    self.result = []

  def isempty(self):
    if self.size == 0:
      return 1
    else:
      return 0

  def Size(self):
    self.result.append(self.size)

  def peek(self):
    if self.isempty() == 1:
      self.result.append(-1)
    else:
      self.result.append(self.queue_list[0])

  def back(self):
    if self.isempty() == 1:
      self.result.append(-1)
    else:
      self.result.append(self.queue_list[self.size - 1])

  def push(self,x):
    self.queue_list.append(x)
    self.size = self.size + 1

  def pop(self):
    if self.isempty() == 1:
      return -1
    else:
      self.size = self.size - 1
      return self.queue_list.popleft()




N = int(sys.stdin.readline())

queuec = Queue(N)


for _ in range(N):
  order = sys.stdin.readline().strip()
  if order == "front":
    queuec.peek()
  elif order == "back":
    queuec.back()
  elif order == "size":
    queuec.Size()
  elif order == "empty":
    queuec.result.append(queuec.isempty())
  elif order == "pop":
    queuec.result.append(queuec.pop())
  else:
    idx = order.find(" ")
    queuec.push(int(order[idx+1:]))

for i in queuec.result:
  print(i)
