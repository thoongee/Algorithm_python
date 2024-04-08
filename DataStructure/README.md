## 스택

### 정의

- 한쪽 끝에서만 원소를 넣거나 뺄 수 있는 자료구조 : **Last in First Out (LIFO)**

### 성질

- 특정 위치(한쪽 끝)에서만 원소를 넣거나 뺄 수 있음
- 원소 추가&제거 : **O(1)**

### 구현

- 기본 리스트에서 append()와 pop() method를 이용하면 스택 자료구조와 동일하게 동작함
    - `append()` : 리스트의 가장 뒤쪽에 데이터를 삽입
    - `pop()`: 리스트의 가장 뒤쪽에서 데이터를 꺼냄
- 스택 자료구조를 활용해야 하는 알고리즘은 재귀 함수를 이용하여 간단하게 구현 가능
    - 재귀함수는 내부적으로 스택 자료구조와 동일하다

```python
## 예시 코드

stack = []
# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()
print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력
```

## 큐

### 정의

- 한쪽 끝으로 원소를 넣고, 반대쪽 끝에서 원소를 뺄 수 있는 자료구조 **(FIFO)**
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
- **파이썬으로 큐를 구현할 경우, collections 모듈에서 제공하는 deque 자료구조 활용**
    
    ```python
    from collections import deque 
    
    queue = deque()
    
    queue.append(1) # push
    queue.append(2) # push
    queue.append(3) # push
    queue.popleft() # pop
    queue.reverse() # 역순으로 바꾸기
    
    print(queue) # dequeue([3,2]) 
    ```
    

## 연결리스트

### **정의**

<p align="center"><img src="https://github.com/thoongee/Algorithm_python/assets/94193480/cd34b6fd-ccc5-4acf-8165-d5396dcb1a517" width="40%">

- Single linked list : 데이터 요소의 선형 집합으로, 각 요소는 데이터와 다음 요소를 가리키는 포인터를 포함.
    - 데이터 요소(노드): 메모리 내에 연속적으로 위치할 필요가 없으며, 포인터를 통해 순서대로 연결.
    - 단일 연결 리스트에서는 각 노드가 **다음 노드만**을 가리킴
- Double linked list : 각 노드가 **이전 및 다음 노드** 양쪽을 가리킴

### 특징

- **동적 배열**: 크기를 동적으로 조절할 수 있다.
- **삽입과 삭제의 용이성**: 시작점이나 중간에 새로운 노드를 추가하거나 기존 노드를 제거하는 것이 배열에 비해 간단하고 효율적이다.

### 복잡도

- 원소 추가: 리스트의 시작에 추가할 경우 **O(1)**, 중간 또는 끝에 추가할 경우 **O(n)**
- 원소 제거: 리스트의 시작에서 제거할 경우 **O(1)**, 중간 또는 끝에서 제거할 경우 **O(n)**
- 원소 검색: **O(n)**

### **구현**

- 단일 연결 리스트에서는 각 노드가 데이터와 '다음 노드'를 가리키는 포인터로 구성됩니다.
- 이중 연결 리스트에서는 각 노드가 데이터, '다음 노드'를 가리키는 포인터, 그리고 '이전 노드'를 가리키는 포인터로 구성됩니다.
- 노드 추가나 제거 시, 해당 노드의 포인터를 조정하여 리스트의 연결 상태를 유지합니다.

```python
class Node:
    def __init__(self, data):
        self.data = data # 값을 가리키는 변수
        self.next = None # 다음 node를 가리키는 변수

class LinkedList: # single linked list
    def __init__(self):
        self.head = None

    # 리스트 시작 부분에 노드 추가
    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 리스트 끝 부분에 노드 추가
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # 리스트 출력
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
# 예시
llist = LinkedList()
llist.push_front(1)
llist.append(2)
llist.append(3)
llist.push_front(0)

print("Original List:")
llist.print_list() # 0 -> 1 -> 2 -> 3 -> None

# 노드 삭제
llist.delete_node(2)

print("After deleting a node with value 2:")
llist.print_list() # 0 -> 1 -> 3 -> None
```

- 참고 자료 : https://wikidocs.net/192069
