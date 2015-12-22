import unittest
from bfs import BFS


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_bfs(self):
        graph = {0: {1}, 1: {0, 2, 3, 4}, 2: {1, 3}, 3: {1, 2, 5, 6, 7}, 4: {1},
                 5: {3}, 6: {3, 7, 8}, 7: {6, 3, 8}, 8: {6, 7}, 9: {10}, 10: {9}}
        source = 1
        bfs = BFS(graph, source)
        # test_has_path_to
        for key in graph:
            if key < 9:
                self.test_has_path_to(bfs, key, True)
            else:
                self.test_has_path_to(bfs, key, False)
        # test_path_to
        v = 7
        exp_res = [7, 3, 1]
        self.test_path_to(bfs, v, exp_res)
        v = 8
        exp_res = [8, 6, 3, 1]
        self.test_path_to(bfs, v, exp_res)
        v = 10
        exp_res = None
        self.test_path_to(bfs, v, exp_res)
        # test_dist_to
        v = 7
        exp_res = 2
        self.test_dist_to(bfs, v, exp_res)
        v = 8
        exp_res = 3
        self.test_dist_to(bfs, v, exp_res)
        v = 0
        exp_res = 1
        self.test_dist_to(bfs, v, exp_res)
        v = 9
        exp_res = None
        self.test_dist_to(bfs, v, exp_res)

    def test_has_path_to(self, bfs, v, exp_res):
        res = bfs.has_path_to(v)
        print 'res: {} exp: {}'.format(res, exp_res)
        self.assertEqual(res, exp_res)

    def test_path_to(self, bfs, v, exp_res):
        res = bfs.path_to(v)
        print 'res: {} exp: {}'.format(res, exp_res)
        self.assertEqual(res, exp_res)

    def test_dist_to(self, bfs, v, exp_res):
        res = bfs.distance_to(v)
        print 'res: {} exp: {}'.format(res, exp_res)
        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    unittest.main()
