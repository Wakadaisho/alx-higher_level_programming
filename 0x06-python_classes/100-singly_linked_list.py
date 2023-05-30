#!/usr/bin/python3


class Node:
    def __init__(self, data, next_node=None):
        if (not isinstance(data, int)):
            raise TypeError("data must be an integer")
        self.__data = data
        if (type(next_node) not in [type(None), type(Node)]):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if (not isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        self.__next_node = value


class SinglyLinkedList(Node):
    def __init__(self):
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
