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

