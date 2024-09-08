class DoublyLinkedNode:
    def __init__(self, value, p=None, n=None):
        self.value = value
        self.prev = p
        self.next = n

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_prev(self, prev):
        self.prev = prev

    def set_next(self, next):
        self.next = next

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def prepend(self, value):
        node = DoublyLinkedNode(value)
        if self._size == 0 and not self._head and not self._tail:
            self._head = node
            self._tail = node
        else:
            self._head.prev = node
            self._head = node
        self._size += 1

    def append(self, value):
        node = DoublyLinkedNode(value)
        if self._size == 0 and not self._head and not self._tail:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def add_before(self, key, value):
        # check for empty structure
        if self._size == 0 and not self._head and not self._tail:
            print("Please add some data to your List.")
        else:
            new_node = DoublyLinkedNode(value)
            current_node = self._head
            previous_node = None
            while current_node:
                # add before the head node
                if current_node.value == key:
                    if not previous_node:
                        new_node.next = current_node
                        current_node.prev = previous_node
                        self._head = current_node
                    else:
                        # adding before any node BUT the head node
                        previous_node.next = new_node
                        new_node.prev = previous_node
                        new_node.next = current_node
                        current_node.prev = new_node
                    self._size += 1
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next

    def add_after(self, key, value):
        # check for empty structure
        if self._size == 0 and not self._head and not self._tail:
            print("Please add some data to your List.")
        else:
            new_node = DoublyLinkedNode(value)
            current_node = self._head
            while current_node:
                # add before the head node
                if current_node.value == key:
                    if not current_node.next:
                        current_node.next = new_node
                        new_node.prev = current_node
                        self._tail = current_node
                    else:
                        # adding before any node BUT the head node
                        next_node = current_node.next

                        new_node.next = current_node.next
                        current_node.next = new_node
                        new_node.prev = current_node

                        next_node.prev = current_node
                    self._size += 1
                    return
                else:
                    current_node = current_node.next

    def remove(self, data):
        if self._size == 0 and not self._head and not self._tail:
            print("Please add some data to your List.")
        elif self._size == 1:
            self._head = None
            self._tail = None
            self._size = 0
        else:
            current_node = self._head
            previous_node = None
            while current_node:
                if current_node.value == data:
                    if not previous_node:
                        next_current_node = current_node.next
                        current_node.next = None
                        next_current_node.prev = None
                        del current_node
                        self._head = next_current_node
                    elif current_node.next:
                        previous_node.next = None
                        current_node.prev = None
                        del current_node
                        self._tail = previous_node
                    else:
                        next_current_node = current_node.next
                        current_node.next = None
                        current_node.prev = None
                        del current_node
                        previous_node.next = next_current_node
                        next_current_node.prev = previous_node

                    self._size -= 1
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next

    def find(self, data):
        current_node = self._head
        while current_node:
            if current_node.value == data:
                return current_node
            else:
                current_node = current_node.next
        else:
            print(f"{data} not found.")

    def traverse_fw(self):
        current_node = self._head
        while current_node:  # while the current node is not None
            print(current_node.value)
            current_node = current_node.next

    def traverse_bw(self):
        current_node = self._tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev

    def list_size(self):
        return self._size


if __name__ == "__main__":
    myList = DoublyLinkedList()
    myList.append(1)
    myList.append(2)
    myList.append(3)

    myList.prepend(0)
    myList.prepend(-1)
    myList.prepend(-2)

    myList.add_before(-2, -3)
    myList.add_before(0, -0.5)

    myList.add_after(3, 4)
    myList.add_after(0, 0.5)

    myList.remove(-3)
    myList.remove(0)
    myList.remove(4)

    myList.traverse_fw()
    print()
    myList.traverse_bw()
    print()

    print("Size:", myList.list_size())

    myList.find(0.5)
