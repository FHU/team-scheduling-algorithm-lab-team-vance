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

    def _partition(self, head, end):
        if head == end or head.next == end:
            return head

        pivot = head
        i = head
        j = head.next

        while j != end:
            if j.item > pivot.item:
                i = i.next
                i.item, j.item = j.item, i.item
            j = j.next

        head.item, i.item = i.item, head.item
        return i


    def _quick_sort(self, head, end):
        if head == end or head == None or head.next == end:
            return head

        pivot = self._partition(head, end)
        self._quick_sort(head, pivot)
        self._quick_sort(pivot.next, end)
        return head


    def sort(self):
        self._quick_sort(self.head, None)


    def sorted_insert(self, item):
        new_node = Node(item)
        self.count += 1

        if self.head == None:
            self.head = self.tail = new_node
            return

        curr = self.tail

        while curr != None:
            if curr.item < new_node.item:
                curr = curr.prev
            else:
                new_node.prev = curr
                new_node.next = curr.next
                curr.next = new_node

                if new_node.next != None:
                    new_node.next.prev = new_node

                if curr == self.tail:
                    self.tail = new_node
                break


class Node:

    def __init__(self, item):
        self.item = item
        self.next = self.prev = None


if __name__ == "__main__":
    #Queue Test
    import random
    q = Queue()

    for i in range(20):
        j = random.randint(0,30)
        q.sorted_insert(j)

    while not q.is_empty():
        print(q.get())