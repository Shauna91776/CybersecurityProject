import unittest
from pathlib import Path
from monitor import calculate_hash, create_baseline,save_baseline, load_baseline,check_integrity
from tempfile import TemporaryDirectory
from unittest.mock import patch


# reate a test file
# calculate its hash twice
# assert that both hashes are equal

class TestFileIntegrityMonitor(unittest.TestCase):
    def test_same_file_has_same_hash(self):
        with TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "test.txt"

            file_path.write_text("Some test content")

            hash1 = calculate_hash(file_path)
            hash2 = calculate_hash(file_path)

            self.assertEqual(hash1, hash2)
        
    def test_changed_file_has_different_hash(self):
        with TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "test.txt"

            file_path.write_text("Original content")
            hash1 = calculate_hash(file_path)

            file_path.write_text("This is different content")
            hash2 = calculate_hash(file_path)

            self.assertNotEqual(hash1, hash2)
            
    def test_create_baseline_contains_file(self):
        with TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "test.txt"

            file_path.write_text("Original content")

            directory = Path(temp_dir)
            baseline = create_baseline(directory)

            self.assertIn("test.txt", baseline)
            
    def test_create_baseline_stores_correct_hash(self):
        with TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "test.txt"

            file_path.write_text("Original content")

            directory = Path(temp_dir)
            baseline = create_baseline(directory)
            
    def test_save_and_load_baseline(self):
        with TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "test_baseline.json"

            baseline = {
                "test.txt": "abc123"
            }
            save_baseline(baseline, file_path)
            loaded_baseline = load_baseline(file_path)
            
            self.assertEqual(baseline, loaded_baseline)
            
    def test_modified_file_is_detected(self):
        with TemporaryDirectory() as temp_dir:
            directory = Path(temp_dir)
            file_path = directory / "test.txt"

            file_path.write_text("Original content")

            baseline = create_baseline(directory)

            file_path.write_text("Changed content")

            with patch("builtins.print") as mock_print:
                check_integrity(directory, baseline)

            mock_print.assert_any_call("[WARNING] File modified: test.txt")
            
            
    def test_new_file_is_detected(self):
        with TemporaryDirectory() as temp_dir:
            directory = Path(temp_dir)

            file_path = directory / "test.txt"
            file_path.write_text("Original content")

            baseline = create_baseline(directory)

            new_file = directory / "new.txt"
            new_file.write_text("New file")

            with patch("builtins.print") as mock_print:
                check_integrity(directory, baseline)

            mock_print.assert_any_call("[WARNING] New file detected: new.txt")


def test_deleted_file_is_detected(self):
    with TemporaryDirectory() as temp_dir:
        directory = Path(temp_dir)

        file_path = directory / "test.txt"
        file_path.write_text("Original content")

        baseline = create_baseline(directory)

        file_path.unlink()

        with patch("builtins.print") as mock_print:
            check_integrity(directory, baseline)

        mock_print.assert_any_call("[WARNING] File deleted: test.txt")
                
                
                
    
        
    