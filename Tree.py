class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree: # 이진탐색트리
    def __init__(self, root_value):
        self.root = TreeNode(root_value)
    def insert(self, value): # 삽입 (이진탐색트리 규칙에 따라 삽입)
        def insert_recursive(node, value):
            if not node: # node == None (새로운 노드 생성 후 삽입)
                return TreeNode(value)
            if value < node.value: # 삽입할 값이 작으면
                t = insert_recursive(node.left, value)
            elif value > node.value: # 삽입할 값이 크면
                node.right = insert_recursive(node.right, value)
                return node # 중복된 값
                self.root = insert_recursive(self.root, value) # 루트 위치부터 삽입

    def search(self, value): # 탐색 (찾으면 True, 못찾으면 False 반환)
        def search_recursive(node, value):
            if not node: # node == None, 못찾음
                return False
            if node.value == value: # 탐색할 값을 찾으면
                return True
            elif value < node.value: # 탐색할 값이 작으면
                    return search_recursive(node.left, value)
            else : # 탐색할 값이 크면
                return search_recursive(node.right, value)
                return search_recursive(self.root, value)

    def delete(self, value): # 삭제
        def delete_recursive(node, value):
            if not node: # node == None, 못찾음
                return node
            if value < node.value: # 삭제할 값이 작으면
                node.left = delete_recursive(node.left, value)
            elif value > node.value: # 삭제할 값이 크면
                node.right = delete_recursive(node.right, value)
            else: # 삭제할 노드를 찾은 경우
                # 1. 자식이 없는 경우
                if not node.left and not node.right:
                    return None
                # 2. 하나의 자식이 있는 경우
                elif not node.left: # 오른쪽 자식만 있음
                    return node.right
                elif not node.right: # 왼쪽 자식만 있음
                    return node.left
    # 3. 두 개의 자식이 있는 경우
                temp = self.find_min(node.right) # 오른쪽 서브트리 중 가장 작은 값 찾기
                node.value = temp.value # 현재 노드 값을 최소값으로 교체
                node.right = delete_recursive(node.right, temp.value) # 최소값 노드 삭제
                return node # 수정된 노드를 반환함
                self.root = delete_recursive(self.root, value)
    def find_min(self, node): # 최소값 찾기 (삭제 시 사용)
        while node.left:
            node = node.left # 왼쪽 자식으로 계속 이동함
            return node # 가장 왼쪽에 있는 노드를 반환함
    def preorder(self): # 전위 순회 (Pre-order): Root -> Left -> Right (VLR)
        stack = [self.root]
        result = []
        while stack:
            node = stack.pop() # 스택에서 노드 하나 빼기
            if node:
                result.append(node.value) # 뺀 노드의 값을 출력하기
                stack.append(node.right) # 오른쪽 자식을 스택에 추가하기
                stack.append(node.left) # 왼쪽 자식을 스택에 추가하기
            return result
    def inorder(self): # 중위 순회 (In-order): Left -> Root -> Right (LVR)
        stack = []
        result = []
        node = self.root
        while node or stack:
            while node: # 왼쪽 자식으로 이동하면서 스택에 넣기
                stack.append(node)
                node = node.left
                node = stack.pop() # 스택에서 1개 빼기
                result.append(node.value) # 뺀 노드를 결과로 출력
                node = node.right # 오른쪽 자식으로 이동
                return result

    def postorder(self): # 후위 순회 (Post-order): Left -> Right -> Root (LRV)
        stack = [self.root]
        result = []
        while stack:
            node = stack.pop() #스택에서 노드 하나 빼기
            if node:
                result.append(node.value) # 뺀 노드의 값을 출력하기
                stack.append(node.left) # 왼쪽 자식을 스택에 추가하기
                stack.append(node.right) # 오른쪽 자식을 스택에 추가하기
            return result[::-1] # 결과 역순으로 만들기

# 이진 트리 사용 예제
tree = BinaryTree(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)
tree.insert(12)
tree.insert(20)
# 탐색 결과 확인
print("탐색 (7):", tree.search(7)) # 출력: 탐색 (7): True
print("탐색 (17):", tree.search(17)) # 출력: 탐색 (17): False
# 삭제 수행
tree.delete(15)
# 순회 결과 출력
print("전위 순회:", tree.preorder()) # 출력 예: 전위 순회: [10, 5, 2, 7, 20, 12]
print("중위 순회:", tree.inorder()) # 출력 예: 중위 순회: [2, 5, 7, 10, 12, 20]
print("후위 순회:", tree.postorder()) # 출력 예: 후위 순회: [2, 7, 5, 12, 20, 10]