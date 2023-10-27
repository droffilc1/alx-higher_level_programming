#!/usr/bin/python3
""" A singly linked list module"""
class Node:
    "A singly liniked list class Node"
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        "Private instance attribute data getter and setter"
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        "Private instance attribute next_node getter and setter"
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self, head=None):
        """Initializing data"""
        self.__head = head

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted
        position in the list
        """
        new_node = Node(value)
        new_node.next_node = self.__head
        self.__head = new_node
