from diskspace import subprocess_check_output
from diskspace import bytes_to_readable
from diskspace import print_tree
from diskspace import show_space_list

import unittest
import os
import StringIO
import subprocess
import sys


class DiskspaceTest(unittest.TestCase):

    def setUp(self):
        self.path = 'teste'
        self.largest_size = 6
        self.total_size = 4
        self.file_tree_node = {'print_size': '6.00Kb',
                               'children': [], 'size': self.total_size}
        self.file_tree = {self.path: self.file_tree_node}

    def test_bytes_to_readable(self):
        blocks = 64
        result = "32.00Kb"
        self.assertEqual(bytes_to_readable(blocks), result)


if __name__ == '__main__':
    unittest.main()
