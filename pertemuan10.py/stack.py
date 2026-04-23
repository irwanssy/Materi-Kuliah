class Stack:
    def __init__(self, data):
        self.data = data
    
    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def display(self):
        temp = self.head
        while temp:
            print(temp.dat,end=" <- ")
            temp = temp.next
        print("None")

    def pop(self):
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        return temp.data 

myStack = Stack()



