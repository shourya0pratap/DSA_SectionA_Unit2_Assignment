class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = self.tail = newNode
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
    
    def insert_after_node(self, target, x):
        curr = self.head
        while curr and curr.val != target:
            curr = curr.next
        if not curr:
            print("Error: Value not found in list")
            return
        newNode = Node(x)
        newNode.next = curr.next
        newNode.prev = curr
        
        if curr.next:
            curr.next.prev = curr.next
        else:
            self.tail = newNode
    
    def delete_at_position(self, pos):
        pass
    
def main():
    DLL = DoublyLinkedList()
    
if __name__ == "__main__":
    main()