__author__ = 'aahamed'


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None

    def num_children(self):
        num = 0
        if self.left_child is not None:
            num += 1
        if self.right_child is not None:
            num += 1
        return num

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.key == other.key
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


class BST(object):
    def __init__(self, root=None):
        self.root = root

    def insert(self, key, value):
        self.root = self.insert_2(Node(key, value), self.root)

    def insert_2(self, node, root):
        if root is None:
            return node
        elif root.key == node.key:
            root.value = node.value
        if node.key < root.key:
            root.left_child = self.insert_2(node, root.left_child)
        elif node.key > root.key:
            root.right_child = self.insert_2(node, root.right_child)
        return root

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left_child)
        print ('({}, {}) '.format(root.key, root.value)),
        self.inorder(root.right_child)

    def search(self, root, key):
        if root is None:
            return None
        if root.key == key:
            return root
        if key < root.key:
            search_node = self.search(root.left_child, key)
        elif key > root.key:
            search_node = self.search(root.right_child, key)
        return search_node

    def min(self, root):
        if root.left_child is None:
            return root
        min_node = self.min(root.left_child)
        return min_node

    def max(self, root):
        while root.right_child is not None:
            root = root.right_child
        return root

    def delete_min(self, root):
        if root.left_child is None:
            # delete right link for garbage collection - no
            if root is self.root:
                self.root = root.right_child
            return root.right_child
        root.left_child = self.delete_min(root.left_child)
        return root

    def delete_max(self, root):
        if root.right_child is None:
            if root is self.root:
                self.root = root.left_child
            return root.left_child
        root.right_child = self.delete_max(root.right_child)
        return root

    def floor(self, root, key):
        if root is None:
            return None
        if key == root.key:
            return key
        if key < root.key:
            res = self.floor(root.left_child, key)
            return res
        if key > root.key:
            t1 = root.key
            t2 = self.floor(root.right_child, key)
            if t2 is not None:
                return t2
            else:
                return t1

    def ceiling(self, root, key):
        if root is None:
            return None
        if key == root.key:
            return key
        if key > root.key:
            return self.ceiling(root.right_child, key)
        else:
            # key < root.key -> ceiling may be in left subtree
            temp = self.ceiling(root.left_child, key)
            if temp is not None:
                return temp
            else:
                return root.key

    def delete(self, root, key):
        if root is None:
            return None
        if root.key == key:
            # root is node to be deleted
            if root.num_children() == 0:
                replacement_node = None
            elif root.num_children() == 1:
                if root.left_child is not None:
                    replacement_node = root.left_child
                else:
                    replacement_node = root.right_child
            else:
                # find successor
                successor = self.min(root.right_child)
                # set successor.right <= delete_min(root.right)
                successor.right_child = self.delete_min(root.right_child)
                # successor.left is root.left
                successor.left_child = root.left_child
                replacement_node = successor
            if root is self.root:
                self.root = replacement_node
            return replacement_node
        if key < root.key:
            root.left_child = self.delete(root.left_child, key)
        if key > root.key:
            root.right_child = self.delete(root.right_child, key)
        return root


