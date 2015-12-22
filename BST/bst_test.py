import unittest
from bst import BST


class MyTestCase(unittest.TestCase):
    def test_bst(self):
        self.assertEqual(True, False)

    def test_insert(self):
        filename = 'tiny.txt'
        tree = BST()
        with open(filename, 'r') as tfile:
            for line in tfile:
                key, value = line.split(' ')
                tree.insert(int(key), int(value))
        tree.inorder(tree.root)

    def test_search(self):
        filename = 'tiny.txt'
        tree = BST()
        with open(filename, 'r') as tfile:
            for line in tfile:
                key, value = line.split(' ')
                tree.insert(int(key), int(value))
        key = 7
        exp_res = 2
        res = tree.search(tree.root, key).value
        print 'res:', res, 'exp_res:', exp_res
        self.assertEqual(res, exp_res)
        key = 5
        exp_res = 1
        res = tree.search(tree.root, key).value
        print 'res:', res, 'exp_res:', exp_res
        self.assertEqual(res, exp_res)
        key = 2
        exp_res = 6
        res = tree.search(tree.root, key).value
        print 'res:', res, 'exp_res:', exp_res
        self.assertEqual(res, exp_res)

    def test_min_max(self):
        filename = 'tiny.txt'
        tree = BST()
        with open(filename, 'r') as tfile:
            for line in tfile:
                key, value = line.split(' ')
                tree.insert(int(key), int(value))
        exp_res = 1
        res = tree.min(tree.root)
        print 'res:', res.key, 'exp_res:', exp_res
        self.assertEqual(res.key, exp_res)
        exp_res = 7
        res = tree.max(tree.root)
        print 'res:', res.key, 'exp_res:', exp_res
        self.assertEqual(res.key, exp_res)

    def test_floor(self):
        filename = 'tiny.txt'
        tree = BST()
        with open(filename, 'r') as tfile:
            for line in tfile:
                key, value = line.split(' ')
                tree.insert(int(key), int(value))
        exp_res = 7
        key = 10
        res = tree.floor(tree.root, key)
        print 'res:', res, 'exp_res:', exp_res
        self.assertEqual(res, exp_res)
        exp_res = 3
        key = 3
        res = tree.floor(tree.root, key)
        print 'res:', res, 'exp_res:', exp_res
        self.assertEqual(res, exp_res)
        exp_res = 2
        key = 2
        res = tree.floor(tree.root, key)
        print 'res:', res, 'exp_res:', exp_res
        self.assertEqual(res, exp_res)
        exp_res = 5
        key = 6
        res = tree.floor(tree.root, key)
        print 'res:', res, 'exp_res:', exp_res
        self.assertEqual(res, exp_res)
        exp_res = None
        key = 0
        res = tree.floor(tree.root, key)
        print 'res:', res, 'exp_res:', exp_res
        self.assertEqual(res, exp_res)

    def test_ceiling(self):
        filename = 'tiny2.txt'
        tree = BST()
        with open(filename, 'r') as tfile:
            for line in tfile:
                key, value = line.split(' ')
                tree.insert(int(key), int(value))
        exp_res = None
        key = 77
        res = tree.ceiling(tree.root, key)
        print 'res:', res, 'exp_res:', exp_res
        self.assertEqual(res, exp_res)
        exp_res = 68
        key = 66
        res = tree.ceiling(tree.root, key)
        print 'res:', res, 'exp_res:', exp_res
        self.assertEqual(res, exp_res)
        exp_res = 21
        key = 21
        res = tree.ceiling(tree.root, key)
        print 'res:', res, 'exp_res:', exp_res
        self.assertEqual(res, exp_res)
        exp_res = 32
        key = 31
        res = tree.ceiling(tree.root, key)
        print 'res:', res, 'exp_res:', exp_res
        self.assertEqual(res, exp_res)

    def test_delete_min(self):
        filename = 'tiny2.txt'
        tree = BST()
        with open(filename, 'r') as tfile:
            for line in tfile:
                key, value = line.split(' ')
                tree.insert(int(key), int(value))
        tree.delete_min(tree.root)
        tree.inorder(tree.root)
        print ''
        tree.delete_min(tree.root)
        tree.inorder(tree.root)

    def test_delete_max(self):
        filename = 'tiny2.txt'
        tree = BST()
        with open(filename, 'r') as tfile:
            for line in tfile:
                key, value = line.split(' ')
                tree.insert(int(key), int(value))
        tree.delete_max(tree.root)
        tree.inorder(tree.root)
        print ''
        tree.delete_max(tree.root)
        tree.inorder(tree.root)

    def test_delete(self):
        filename = 'tiny2.txt'
        tree = BST()
        with open(filename, 'r') as tfile:
            for line in tfile:
                key, value = line.split(' ')
                tree.insert(int(key), int(value))
        tree.inorder(tree.root)
        print ''
        key = 62
        tree.delete(tree.root, key)
        tree.inorder(tree.root)
        print ''
        key = 41
        tree.delete(tree.root, key)
        tree.inorder(tree.root)
        print ''
        key = 50
        tree.delete(tree.root, key)
        tree.inorder(tree.root)

if __name__ == '__main__':
    unittest.main()
