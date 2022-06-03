class Node:
    # next는 포인터가 가리키는 다음노드
    # 다음 노드지만 이전에 push한 것을 가리킴
    # ex) none <- 1 <- 2 <- 3 <- 4 <- 5(last)
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        # self.last는 현재 last, Node 생성하면 다음 노드(이전에 푸쉬한 노드)가 되므로 next 자리에 넣어줌
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item

stack = Stack()
stack.push(1)
stack.push(2)

for _ in range(2):
    print(stack.pop())
