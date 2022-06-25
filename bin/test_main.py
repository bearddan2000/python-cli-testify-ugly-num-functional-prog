from testify import *

import main

class TestMain(TestCase):
    """docstring for TestMain."""
    def test_max_divide(self):
        assert_equal(main.max_divide(10, 5), 2)

    def test_is_ugly(self):
        assert_equal(main.is_ugly(0, [2,3,5], 12), True)

    def test_find_ugly(self):
        assert_equal(main.find_ugly(10, 1, 1, [2,3,5]), 12)

if __name__ == '__main__':
    run()
