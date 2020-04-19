from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.queue = DoublyLinkedList()

    def enqueue(self, value):
        # increment the size of the queue

        self.queue.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.queue.remove_from_head()
            self.size -= 1

        else:
            return None

    def len(self):
        self.size = len(self.queue)
        return self.size
