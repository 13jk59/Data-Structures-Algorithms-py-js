""" This module contains code for a class that represents the
queue data structure """
from py.utils.linked_list import SinglyLinkedListNode


class Queue:
    """ This class represents the Queue data structure implemented using
    singly linked nodes.

    A queue consists of a sequence of entities managed using the First In
    First Out (FIFO) principle, where the first elements added are
    the first ones removed.

    The queue has a variety of applications, including being used to traverse
    trees and graphs in a breadth first manner, in operating systems to maintain
    a queue of processes ready to execute, within computer systems, and so on.

    Attributes:
        head:
            Variable of type SinglyLinkedListNode that points to the start of
            the queue

        tail:
            Variable of type SinglyLinkedListNode that points to the end of
            the queue
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        new_node = SinglyLinkedListNode(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def poll(self):
        if self.head:
            return_val = self.head.val
            self.head = self.head.next
            return return_val
        else:
            raise IndexError("poll from empty queue")

    def top(self):
        if self.head:
            return self.head.val
        else:
            raise IndexError("queue is empty")

    def __len__(self):
        node = self.head
        length = 0
        while node:
            length += 1
            node = node.next
        return length
