from diskspace import subprocess_check_output
from diskspace import bytes_to_readable
from diskspace import print_tree
from diskspace import show_space_list

import unittest
import StringIO
import subprocess
import sys


class DiskspaceTest(unittest.TestCase):

    def setUp(self):
        self.path = 'teste'
        self.largest_size = 6
        self.total_size = 4
        self.file_tree_node = {'print_size': '10.00Kb',
                               'children': [], 'size': self.total_size}
        self.file_tree = {self.path: self.file_tree_node}

    def test_subprocess_check_output(self):
        cmd = 'du'
        raw_output = subprocess.check_output(cmd)
        result = subprocess_check_output(cmd)
        self.assertEqual(raw_output, result)

    def test_bytes_to_readable(self):
        blocks = 64
        result = "32.00Kb"
        self.assertEqual(bytes_to_readable(blocks), result)

    def test_print_tree(self):
        cap = StringIO.StringIO()
        sys.stdout = cap

        print_tree(self.file_tree, self.file_tree_node, self.path,
                   self.largest_size, self.total_size)
        result = "10.00Kb  100%  teste\n"
        sys.stdout = sys.__stdout__
        self.assertEqual(result, cap.getvalue())

    def test_show_space_list(self):
        cap = StringIO.StringIO()
        sys.stdout = cap

        show_space_list(self.path)
        top = "   Size   (%)  File\n"
        path = "/home/mateus/Tec_Prog/05--Mateusas3s/teste"
        file = "10.00Kb  100%  " + path + "\n"
        in_file_1 = " 4.00Kb   40%  " + path + "/teste_2\n"
        in_file_2 = " 4.00Kb   40%  " + path + "/teste_1\n"
        result = top + file + in_file_1 + in_file_2
        sys.stdout = sys.__stdout__
        self.assertEqual(result, cap.getvalue())


if __name__ == '__main__':
    unittest.main()
