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
            
    def display(self):
        if not self.head:
            print("[ ]")
        out = ""
        curr = self.head
        while curr:
            out += str(curr.val) + " , "
            curr = curr.next
        print(f"[{out[:-3]}]")

def main():
    LL = SinglyLinkedList()
    for i in range(1,6):
        LL.add(i)
    LL.remove(1)
    LL.display()

if __name__ == "__main__":
    main()