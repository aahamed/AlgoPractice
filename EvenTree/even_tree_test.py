import unittest
import even_tree


class EvenTreeTest(unittest.TestCase):
    def test_load_tree(self):
        filename = 'tree1.txt'
        exp_result = {1: {2, 3, 4}, 2: {5, 6}, 3: set(), 4: {7, 8, 9}, 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}
        result = even_tree.load_tree(filename)
        print 'res:', result
        print 'exp res:', exp_result
        self.assertEqual(result, exp_result)

    def test_subtree_size(self):
        filename = 'tree1.txt'
        tree = even_tree.load_tree(filename)
        root = 1
        exp_result = 9
        result = even_tree.subtree_size(tree, root)
        print 'res:', result
        print 'exp res:', exp_result
        self.assertEqual(result, exp_result)

    def test_load_tree2(self):
        filename = 'tree1.txt'
        root = even_tree.load_tree2(filename)
        even_tree.in_order(root)

    def test_subtree_size2(self):
        filename = 'tree1.txt'
        root = even_tree.load_tree2(filename)
        exp_res = 10
        res = even_tree.subtree_size2(root)
        print 'res:', res
        print 'exp_res:', exp_res
        self.assertEqual(res, exp_res)

    def test_node_class(self):
        node1 = even_tree.Node(1)
        node2 = even_tree.Node(2)
        node1.add_child(node2)
        exp_res = {node2}
        res = node1.children
        print 'res:', res
        print 'exp_res:', exp_res
        self.assertEqual(res, exp_res)
        node1.remove_child(node2)
        exp_res = set()
        res = node1.children
        print 'res', res
        print 'exp res', exp_res
        self.assertEqual(res, exp_res)

    def test_even_tree(self):
        filename = 'tree1.txt'
        root = even_tree.load_tree2(filename)
        cc_list = []
        res = even_tree.even_tree(root, cc_list)
        print 'res:', res
        filename = 'tree2.txt'
        root = even_tree.load_tree2(filename)
        cc_list = []
        exp_res = 2
        res = even_tree.even_tree(root, cc_list)
        print 'res:', res
        print 'len res:', len(res)-1
        print 'exp_res:', exp_res
        self.assertEqual(len(res)-1, exp_res)



if __name__ == '__main__':
    unittest.main()
