class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def add(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
            
    def remove(self, ind):
        if ind == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for i in range(1,ind):
                curr = curr.next
            curr.next = curr.next.next

def main():
    LL = SinglyLinkedList()
    LL.add(1)

if __name__ == "__main__":
    main()