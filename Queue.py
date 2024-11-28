class Queue:
    def __init__(self):
        self.items = [] # 큐를 리스트로 초기화
    def is_empty(self): # 큐가 비어 있는지 확인
        return len(self.items) == 0
    def enqueue(self, item): # 큐의 끝에 요소를 추가 (삽입)
        self.items.append(item)
    def dequeue(self): # 큐의 앞에서 요소를 제거하고 반환 (삭제)
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None # 큐가 비어 있을 때 None 반환
    def size(self): # 큐의 크기를 반환
        return len(self.items)

# 큐 사용 예제
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("큐 크기:", queue.size()) # 출력: 큐 크기: 3
print("큐에서 꺼낸 요소:", queue.dequeue()) # 출력: 큐에서 꺼낸 요소: 1
print("큐 크기:", queue.size()) # 출력: 큐 크기: 2
print("큐가 비어 있는가:", queue.is_empty()) # 출력: 큐가 비어 있는가: False