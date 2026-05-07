class Queue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        else:
            print("Baris Kosong")

    def peek(self):
        if not self.is_empty():
            print(f"Antrian pertama: {self.data[0]}")
        else:
            print("Baris Kosong")

    def size(self):
        return len(self.data)
    
    def display(self):
        print("Queue:", self.data)

b1 = Queue()
print("=" * 10,"Selamat datang di Antrian Integerist", "=" * 10)
b1.enqueue("Nazwa")
b1.enqueue("Daffa")
b1.enqueue("Rizky")
print("Antrian awal:")
b1.display()
#=============
print("\nAntrian setelah dequeue:")
b1.dequeue()
b1.dequeue()
b1.dequeue()
b1.display()
#============
b1.enqueue("Irwan Keren")
b1.display()
b1.peek() 
b1.enqueue("Daffa")
b1.display()
