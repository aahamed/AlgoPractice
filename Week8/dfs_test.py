import unittest
from dfs import DFS


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_dfs(self):
        graph = {0: {2, 1, 5}, 1: {0, 2}, 2: {0, 1, 3, 4}, 3: {5, 4, 2}, 4: {3, 2}, 5: {0, 3}}
        source = 0
        # test has_path_to
        dfs = DFS(graph, source)
        for key in graph:
            self.test_has_path_to(dfs, key, True)
        # test path_to
        v = 4
        exp_res = [4, 3, 2, 1, 0]
        self.test_path_to(dfs, v, exp_res)
        v = 5
        exp_res = [5, 3, 2, 1, 0]
        self.test_path_to(dfs, v, exp_res)
        v = 2
        exp_res = [2, 1, 0]
        self.test_path_to(dfs, v, exp_res)

    def test_has_path_to(self, dfs, v, exp_res):
        res = dfs.has_path_to(v)
        print 'res: {} exp: {}'.format(res, exp_res)
        self.assertEqual(res, exp_res)

    def test_path_to(self, dfs, v, exp_res):
        res = dfs.path_to(v)
        print 'res: {} exp: {}'.format(res, exp_res)
        # self.assertEqual(res, exp_res)

if __name__ == '__main__':
    unittest.main()
