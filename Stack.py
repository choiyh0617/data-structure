class Stack:
    def __init__(self):
        self.items = [] # 스택을 리스트로 초기화
    def is_empty(self): # 스택이 비어 있는지 확인
        return len(self.items) == 0
    def push(self, item): # 스택에 요소를 추가 (삽입)
        self.items.append(item)
    def pop(self): # 스택에서 요소를 제거하고 반환 (삭제)
        if not self.is_empty():
            return self.items.pop()
        else: # 스택이 비어 있을 때 None 반환
            return None
    def peek(self): # 스택의 가장 위에 있는 요소를 반환 (삭제하지 않음)
        if not self.is_empty():
            return self.items[-1]
        else: # 스택이 비어 있을 때 None 반환
            return None
    def size(self): # 스택의 크기를 반환
        return len(self.items)

# 스택 사용 예제
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("스택 크기:", stack.size()) # 출력: 스택 크기: 3
print("스택 최상단 요소:", stack.peek()) # 출력: 스택 최상단 요소: 3
print("스택에서 꺼낸 요소:", stack.pop()) # 출력: 스택에서 꺼낸 요소: 3
print("스택 크기:", stack.size()) # 출력: 스택 크기: 2
print("스택이 비어 있는가:", stack.is_empty()) # 출력: 스택이 비어 있는가? False