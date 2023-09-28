import unittest
from unittest.mock import patch
from app import rm

class TestRm(unittest.TestCase):

    def test_rm_deletes_file(self):
        # Create a test file
        with open('somefile1.txt', 'w') as f:
            f.write('Test data')

        # Call the rm function to delete the file
        rm('somefile1.txt')

        # Check if the file has been deleted
        with self.assertRaises(FileNotFoundError):
            with open('somefile1.txt', 'r'):
                pass
    
    @patch('app.os.remove')
    def test_rm_calls_os_remove_if_file_exists(self, mock_remove):
        # Call the rm function
        rm('somefile1.txt')

        # Check if os.remove was called
        mock_remove.assert_called_once_with('somefile1.txt')
    
    @patch('app.os.remove')
    def test_rm_does_not_call_os_remove_if_file_does_not_exist(self, mock_remove):
        # Mock os.remove to raise FileNotFoundError
        mock_remove.side_effect = FileNotFoundError

        # Call the rm function for a non-existing file
        with self.assertRaises(FileNotFoundError):
            rm('non_existent_file.txt')
    
    @patch('app.os.remove')
    def test_rm_raises_file_not_found_error_if_file_does_not_exist(self, mock_remove):
        # Mock os.remove to raise FileNotFoundError
        mock_remove.side_effect = FileNotFoundError

        # Call the rm function for a non-existing file and check for FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            rm('non_existent_file.txt')

if __name__ == '__main__':
    unittest.main()

# OUTPUT:

# dci-student  28-09-2023-python-testing-mocking-Lightmaker777  ➜ ( main)  ♥ 14:45  cd src
# dci-student  src  ➜ ( main)  ♥ 14:46  python3 -m unittest -v mock_test.py
# test_rm_calls_os_remove_if_file_exists (mock_test.TestRm.test_rm_calls_os_remove_if_file_exists) ... ok
# test_rm_deletes_file (mock_test.TestRm.test_rm_deletes_file) ... ok
# test_rm_does_not_call_os_remove_if_file_does_not_exist (mock_test.TestRm.test_rm_does_not_call_os_remove_if_file_does_not_exist) ... ok
# test_rm_raises_file_not_found_error_if_file_does_not_exist (mock_test.TestRm.test_rm_raises_file_not_found_error_if_file_does_not_exist) ... ok

# ----------------------------------------------------------------------
# Ran 4 tests in 0.002s

# OK
