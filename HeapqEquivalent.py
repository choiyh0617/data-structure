class HeapqEquivalent:
    def __init__(self):
        self.heap = []
    def heappush(self, item): # item 삽입
        self.heap.append(item) # item을 heap 리스트 끝에 추가
        self.siftup(len(self.heap) - 1) # 삽입한 값이 적절한위치에 오도록 힙 조정
    def heappop(self): # 힙의 최솟값을 삭제 후 반환함
        if not self.heap: #힙이 비어있으면
            raise IndexError("pop from an empty heap")
        lastelt = self.heap.pop() # 가장 마지막 위치에 있는 요소를 삭제 후, lastelt에 저장
        if not self.heap: # heap이 비었으면
            return lastelt
        min_item = self.heap[0] # 최소값(루트값) 저장
        self.heap[0] = lastelt # lastelt를 루트 자리에 넣음
        self.siftdown(0) # 힙 속성 유지시키기
        return min_item # 최소값 반환
    def heapify(self, data): # 주어진 data을 힙 구조로 변환함
        self.heap = list(data)
        for i in reversed(range(len(self.heap) // 2)):
            self.siftdown(i)
    def heappushpop(self, item): # item을 추가 -> 최솟값을 삭제&반환
        if self.heap and item > self.heap[0]: # 삽입할 값(item) > 루트값
            item, self.heap[0] = self.heap[0], item # 삽입할 값(item) <-> 루트값
        self.siftdown(0) # 힙 조정
        return item # 최소값 반환
    def heapreplace(self, item): # 최솟값 삭제 -> item 추가 -> 최솟값 반환
        if not self.heap: # self.heap == None (빈 힙이면)
            raise IndexError("replace on empty heap")
        min_item = self.heap[0] # 최소값 저장
        self.heap[0] = item # 루트 위치에 item 삽입
        self.siftdown(0) # 힙 재조정
        return min_item # 최소값 반환
    def nlargest(self, n): # 힙에서 가장 큰 n개의 요소를 반환함
        return sorted(self.heap, reverse=True)[:n]
    def nsmallest(self, n): # 힙에서 가장 작은 n개의 요소를 반환함
        return sorted(self.heap)[:n]

    def siftup(self, pos): # 삽입 시 힙 속성을 유지하도록 조정함 (값을 위로 이동)
        child = pos
        while child > 0: # child가 루트에 도달할 때 까지 반복
            parent = (child - 1) // 2
            if self.heap[child] < self.heap[parent]: # 부모>자식 (최소힙 조건 만족 안할 때)
                self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child] #부모<->자식
                child = parent # 새로운 child 인덱스 위치 조정
            else: # 부모 < 자식 (최소힙 조건 만족할 때)
                break
    def siftdown(self, pos): # 루트 요소를 아래로 이동시켜 힙 속성을 유지함 (값을 아래로 이동)
        end = len(self.heap) #힙크기
        parent = pos # 부모 인덱스
        child = 2 * parent + 1 # 왼쪽 자식의 인덱스
        while child < end : # 자식인덱스가 힙 범위 안에 있을때까지만 반복
            if child+1 < end and self.heap[child+1] < self.heap[child]: # 왼쪽자식>오른쪽자식
                child = child+1
            if self.heap[child] < self.heap[parent]: # 부모>자식 이면 (최소힙 조건 만족 안할 때)
                self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child] #부모<->자식
                parent = child #부모인덱스 위치 이동
                child = 2 * parent + 1 #자식인덱스 위치 이동
            else: # 부모<자식 이면 (최소힙 조건 만족할 때)
                break

# 예제 사용
heap = HeapqEquivalent()
heap.heappush(10)
heap.heappush(5)
heap.heappush(3)
heap.heappush(8)
print("힙의 최솟값:", heap.heappop()) # 최솟값을 제거하고 반환
heap.heapify([7, 1, 5, 9, 3]) # 리스트를 힙으로 변환
print("힙에서 가장 큰 2개의 요소:", heap.nlargest(2)) # 가장 큰 2개의 요소
print("힙에서 가장 작은 3개의 요소:", heap.nsmallest(3)) # 가장 작은 3개의 요소
print("힙에 6 추가 후 최소 제거:", heap.heappushpop(6)) # 6을 추가하고 최솟값 제거
print("최소를 2로 교체 후 반환:", heap.heapreplace(2)) # 최솟값을 2로 교체하고 반환
# 현재 힙 상태
print("힙 내용:", heap.heap)