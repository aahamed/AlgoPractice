"""
Author: Aadil Ahamed
even_tree.py: Module to break down a tree into largest number of connected components with even number of vertices
making change
"""

import logging


logging.basicConfig(level=logging.DEBUG)


class Node:
    """Node class to represent nodes in a tree"""
    def __init__(self, number):
        self.children = None
        self.parent = None
        self.number = number

    def add_child(self, child):
        if self.children is None:
            self.children = {child}
        else:
            self.children.add(child)

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)

    def modify_parent(self, parent):
        self.parent = parent

    def is_leaf(self):
        if self.children is None:
            return True
        else:
            return False

    def has_parent(self):
        if self.parent is None:
            return False
        else:
            return True

    def break_from_parent(self):
        """
        Breaks the edge from this node to its parent
        """
        parent = self.parent
        if parent is None:
            return
        self.modify_parent(None)
        parent.remove_child(self)

    def node_number(self):
        return self.number


class EvenTree(object):
    """docstring"""
    def __init__(self):
        pass


def load_tree(filename):
    """load tree as an adjacency list"""
    with open(filename, 'r') as gfile:
        tree = {}
        for i, line in enumerate(gfile):
            edge = [int(j) for j in line.split(' ')]
            if edge[1] in tree:
                tree[edge[1]].add(edge[0])
            else:
                tree[edge[1]] = {edge[0]}
            if edge[0] not in tree:
                tree[edge[0]] = set()
    return tree


def load_tree2(filename):
    """
    Parses input file into a Tree object
    :param filename: path to input file
    :return: root of tree
    """
    dict_nodes = {}
    with open(filename, 'r') as gfile:
        for line in gfile:
            edge = [int(j) for j in line.split(' ')]
            if edge[0] in dict_nodes:
                node0 = dict_nodes[edge[0]]
            else:
                node0 = Node(edge[0])
                dict_nodes[edge[0]] = node0
            if edge[1] in dict_nodes:
                node1 = dict_nodes[edge[1]]
            else:
                node1 = Node(edge[1])
                dict_nodes[edge[1]] = node1
            node0.modify_parent(node1)
            node1.add_child(node0)
    return dict_nodes[1]


def in_order(root):
    """In order traversal of tree starting from root"""
    if root is None:
        return
    print root.node_number()
    if root.children is not None:
        for child in root.children:
            in_order(child)


def subtree_size(tree, root):
    """Determine size of subtree starting from root. Assumes adjacency list rep of tree"""
    if root is None:
        return 0
    size = 1
    for child in tree[root]:
        size += subtree_size(tree, child)
    return size


def subtree_size2(root):
    """Determine size of subtree starting from root. Assumes object + pointers representation of tree"""
    if root is None:
        return 0
    size = 1
    if root.children is not None:
        for child in root.children:
            size += subtree_size2(child)
    return size


# def break_from_parent(node):
#     """
#     Breaks a child from its parent
#     """
#     parent = node.parent
#     node.modify_parent(None)
#     parent.remove_child(node)
#     return node


def even_tree(root, cc_list):
    """Determine the edges that can be removed from the tree while keeping all cc even"""
    ss_size = subtree_size2(root)
    if ss_size == 2:
        # root.break_from_parent()
        cc_list.append(root.node_number())
        return cc_list
    if ss_size < 2:
        return cc_list
    for child in root.children:
        cc_list = even_tree(child, cc_list)
    if ss_size % 2 == 0:
        # root.break_from_parent()
        cc_list.append(root.node_number())
    return cc_list
