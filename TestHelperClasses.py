import unittest

import pathlib

import HelperClasses


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)


class ValidTestCases(unittest.TestCase):
    def test_valid_file_name(self):
        file_path = pathlib.Path('SIC_04_ABLSteinmeier')
        res = HelperClasses.SICFileName(file_path).extract_header()
        self.assertEqual(res, 'A. B. L. Steinmeier')


if __name__ == '__main__':
    unittest.main()
