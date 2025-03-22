import unittest

from dlake.base.util.str import StrUtil


class StrUtilTestCase(unittest.TestCase):
    def test_isblank(self):
        test_str = None
        target_str = True
        result = StrUtil.isblank(test_str)
        self.assertEqual(result, target_str)

    def test_upper(self):
        test_str = "Private_Key"
        target_str = "PRIVATE_KEY"
        result = StrUtil.upper(test_str)
        self.assertEqual(result, target_str)  # add assertion here

if __name__ == '__main__':
    unittest.main()
