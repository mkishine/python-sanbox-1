import unittest

import inspect
import os
from io import StringIO
from unittest.mock import patch

import sys

# inspired by https://stackoverflow.com/a/11158224
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import generate_brk2_data


class GenerateBrk2DataTestCase(unittest.TestCase):
    def test_main_no_args(self):
        with self.assertRaisesRegex(SystemExit, "2"):
            generate_brk2_data.main([])

    def test_main_help(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with self.assertRaisesRegex(SystemExit, "0"):
                generate_brk2_data.main(["-h"])
            self.assertRegex(fake_out.getvalue(), "-h.*--cusip_file.*-breakdown_file")

    def test_main_base_case(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rv = generate_brk2_data.main(
                ["--cusip_file", "../data/input/cusips.csv", "--breakdown_file",
                 "../data/input/4p-industry-sectors.txt"])
        self.assertEqual(rv, 0)
        expected = "insert into dbo.brk2 values('4P', '00037BAB8', 'Cash Securities', 1)\ngo\n" \
                   "insert into dbo.brk2 values('4P', '00037BAB8', 'Cash Securities.Other', 2)\ngo\n" \
                   "insert into dbo.brk2 values('4P', '00037BAC6', 'Corporates', 1)\ngo\n" \
                   "insert into dbo.brk2 values('4P', '00037BAC6', 'Corporates.Financial Institutions', 2)\ngo\n" \
                   "insert into dbo.brk2 values('4P', '00037BAC6', " \
                   "'Corporates.Financial Institutions.Banking', 3)\ngo\n"
        self.assertEqual(fake_out.getvalue()[0:len(expected)], expected)


if __name__ == '__main__':
    unittest.main()
