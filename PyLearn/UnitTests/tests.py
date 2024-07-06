import unittest


def fun(num1, *args):
    total = num1
    for num in args:
        total += num
    return total


class TestMyModule(unittest.TestCase):

    def test_fun_with_multiple_arguments(self):
        result = fun(1, 2, 3, 4)
        self.assertEqual(result, 10)

    def test_fun_with_single_argument(self):
        result = fun(5)
        self.assertEqual(result, 5)

    def test_fun_with_no_arguments(self):
        with self.assertRaises(TypeError):
            fun()

    def test_fun_with_negative_numbers(self):
        result = fun(-1, -2, -3, -4)
        self.assertEqual(result, -10)

    def test_fun_with_mixed_numbers(self):
        result = fun(1, -2, 3, -4)
        self.assertEqual(result, -2)

    def test_fun_with_large_numbers(self):
        result = fun(1000000, 2000000, 3000000)
        self.assertEqual(result, 6000000)


if __name__ == '__main__':
    unittest.main()
