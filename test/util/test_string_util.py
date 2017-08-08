import unittest

from util.string_util import capitalize_all


class TestStringUtil(unittest.TestCase):
    def test_capatialize_all(self):
        self.assertEqual('Foo', capitalize_all('FOO'))
        self.assertEqual('This Is A Test', capitalize_all('THIS IS A TEST'))


if __name__ == '__main__':
    unittest.main()
