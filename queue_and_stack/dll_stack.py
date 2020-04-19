from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

# LAST IN, FIRST OUT


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.stack = DoublyLinkedList()

    def push(self, value):
        self.stack.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.stack.remove_from_tail()
            self.size -= 1

        else:
            return None

    def len(self):
        self.size = len(self.stack)
        return self.size
