import unittest

import pathlib

import HelperClasses


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)


class ValidTestCases(unittest.TestCase):
    def test_valid_file_name(self):

        file_path = pathlib.Path('SIC_04_ABLeonSteinmeier')
        res = HelperClasses.SICFileName(file_path).extract_header()

        self.assertEqual('A. B. Leon Steinmeier', res)


if __name__ == '__main__':
    unittest.main()
