import pytest
from pathlib import Path
from src.data.file_handler import FileHandler
import tempfile


@pytest.fixture
def setup_test_environment():
    with tempfile.TemporaryDirectory() as tempdir:
        tempdir_path = Path(tempdir)
        test_folder_1 = tempdir_path / "TEST_Folder_1"
        test_folder_2 = tempdir_path / "TEST_Folder_2"
        result_dir = tempdir_path / "Result"
        test_folder_1.mkdir()
        test_folder_2.mkdir()
        result_dir.mkdir()

        (test_folder_1 / "TEST_file1.txt").write_text("1-3 5")
        (test_folder_2 / "TEST_file2.txt").write_text("2 4-6")

        yield tempdir_path, [test_folder_1, test_folder_2], result_dir


def test_read_files(setup_test_environment):
    tempdir_path, test_dirs, _ = setup_test_environment
    file_handler = FileHandler(tempdir_path)
    files_content = file_handler.read_files(test_dirs, "TEST_*")

    assert len(files_content) == 2
    assert files_content[0][0] == "TEST_file1.txt"
    assert files_content[1][0] == "TEST_file2.txt"


def test_save_results(setup_test_environment):
    tempdir_path, _, result_dir = setup_test_environment
    file_handler = FileHandler(tempdir_path)
    processed_data = [
        ("TEST_file1.txt", [1, 2, 3, 5]),
        ("TEST_file2.txt", [2, 4, 5, 6]),
    ]

    file_handler.save_results(processed_data, result_dir)

    assert (result_dir / "TEST_AUCHAN_success_1.txt").exists()
    assert (result_dir / "TEST_AUCHAN_success_2.txt").exists()
