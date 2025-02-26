class Queue:

    def __init__(self):
        self.head = self.tail = None
        self.count = 0

    def put(self, item):
        new_node = Node(item)
        self.count += 1

        if self.head == None:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node


    def get(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")

        return_value = self.tail.item

        if self.count == 1:
            self.head = self.tail = None
        else:
            new_tail = self.tail.prev
            self.tail.prev = None
            new_tail.next = None
            self.tail = new_tail

        self.count -= 1
        return return_value

    def is_empty(self):
        return self.count == 0


class Node:

    def __init__(self, item):
        self.item = item
        self.next = self.prev = None


if __name__ == "__main__":
    #Queue Test
    q = Queue()

    for i in range(10):
        q.put(i)

    while not q.is_empty():
        print(q.get())