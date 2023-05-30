#!/usr/bin/python3
"""
Module 100-singly_linked_list
Has a Node class that defines a unit of data,
        with appropriate type checks and getters and setters
SinglyLinkedList class that links up mulitple Node instances
"""


class Node:
    """Linked list node class
    """
    def __init__(self, data, next_node=None):
        """Init Node

        Args:
            data (int): value to store in Node
            next_node (Node/None): next node pointed to
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter

        Returns:
            data (int): value stored in Node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Setter

        Raises:
            TypeError: if data is not an integer
        """
        if (not isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter

        Returns:
            next_node (Node/None): next node poined to
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter

        Raises:
            TypeError: if value is not a Node object or None
        """
        if (not (value is None or isinstance(value, Node))):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList(Node):
    """Singly linded list class

    List of Nodes pointing to the next in one direction
    """
    def __init__(self):
        """Init SinglyLinkedList

        Args:
            head (Node/None): first node in list
        """
        self.__head = None

    def __str__(self):
        node = self.__head
        __str = ""
        if (node is None):
            return __str
        while (node.next_node is not None):
            __str += f"{node.data}\n"
            node = node.next_node
        __str += f"{node.data}"
        return __str

    def sorted_insert(self, value):
        """Insert a node into list in the correct ascending position

        Args:
            value (int): value to be used in new node to insert
        """
        node = self.__head
        new_node = Node(value)
        if (node is None):
            self.__head = new_node
            return
        if (node.data > value):
            new_node.next_node = node
            self.__head = new_node
            return
        while (node.next_node is not None):
            if (node.next_node.data > value):
                new_node.next_node = node.next_node
                node.next_node = new_node
                return
            node = node.next_node
        node.next_node = new_node
