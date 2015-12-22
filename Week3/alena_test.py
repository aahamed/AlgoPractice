import unittest
import alena


class MyTestCase(unittest.TestCase):
    def test_alena(self):
        a = [0, 1, 0, 1, 1]
        exp_res = 4
        res = alena.alena(a)
        print 'res:', res, 'exp_res:', exp_res
        self.assertEqual(res, exp_res)
        a = [1, 0, 1, 0, 0, 1, 0]
        exp_res = 4
        res = alena.alena(a)
        print 'res:', res, 'exp_res:', exp_res
        self.assertEqual(res, exp_res)
        a = [0, 0, 0, 1, 0, 1, 0, 0, 0]
        exp_res = 3
        res = alena.alena(a)
        print 'res:', res, 'exp_res:', exp_res
        self.assertEqual(res, exp_res)


if __name__ == '__main__':
    unittest.main()
