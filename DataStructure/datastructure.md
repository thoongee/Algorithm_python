## Stack

### 정의

- 한쪽 끝에서만 원소를 넣거나 뺄 수 있는 자료구조 : Last in First Out (LIFO)

### 성질

- 특정 위치(한쪽 끝)에서만 원소를 넣거나 뺄 수 있음
- 원소 추가&제거 : **O(1)**

### 구현

- 기본 리스트에서 append()와 pop() 메서드를 이용하면 스택 자료구조와 동일하게 동작함
- 스택 자료구조를 활용해야 하는 알고리즘은 재귀 함수를 이용하여 간단하게 구현 가능
    - 재귀함수는 내부적으로 스택 자료구조와 동일하다

### 기능

- push : 원소 추가
- pop : 원소 제거
- top: 원소 확인

참고 자료 : https://blog.encrypted.gg/933

## Queue

### 정의

- 한쪽 끝으로 원소를 넣고, 반대쪽 끝에서 원소를 뺄 수 있는 자료구조 (FIFO)
- 원소가 추가되는 곳 : rear
- 원소가 제거되는 곳 : front

### 성질

- 원소의 추가&제거&제일 앞/뒤 확인 : **O(1)**

### 구현

- 원소를 담을 배열 + 가장 앞에 있는 원소의 인덱스(head) + 가장 뒤에 있는 원소의 인덱스(+1)(tail)
- push → tail 증가, pop → head 증가
- push, pop을 반복하면 배열 앞쪽에 사용하지 않는 공간이 많아짐
- 배열의 길이가 고정되어 있다면, tail이 배열 끝까지 갔다가, 다시 0으로 돌아옴 (마치 원형 배열)
- 혹은, push의 최대 횟수가 정해져 있다면 배열의 크기를 push의 최대 횟수보다 크게 두면 됌.

참고자료 : https://blog.encrypted.gg/934?category=773649

## Deque

### 정의

- 양쪽 끝에서 삽입, 삭제가 모두 가능한 자료구조 : Double Ended Queue

### 성질

- 원소의 추가, 제거, 제일 앞/뒤 확인 : **O(1)**
- 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적임
- queue 라이브러리를 이용하는 것 보다 간단함

### 구현

- 배열
- 가장 앞에 있는 원소의 index : head
- 가장 뒤에 있는 원소의 index+1 : tail
- head와 tail의 초기값 != 0 (초기값 = 중간)
- 파이썬으로 큐를 구현할 경우, collections 모듈에서 제공하는 deque 자료구조 활용
    
    ```python
    from collections import deque 
    
    queue = deque()
    
    queue.append(1) # push
    queue.popleft() # pop
    queue.reverse() # 역순으로 바꾸기
    ```
    

참고자료 : https://blog.encrypted.gg/935
