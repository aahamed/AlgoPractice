import unittest
import dijkstras


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_djikstras(self):
        graph = {0: {(1, 1), (2, 2), (4, 5)}, 1: {(0, 1), (2, 2), (3, 1), (4, 3)}, 2: {(0, 2), (1, 2), (4, 3)},
                 3: {(1, 1), (4, 1), (5, 2)}, 4: {(1, 3), (2, 3), (3, 1), (5, 5)}, 5: {(4, 5), (3, 2)}}
        src = 0
        res = dijkstras.dijkstras(graph, src)
        print res

if __name__ == '__main__':
    unittest.main()
