import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2] / "src"))

import tempfile

import pytest

from data.handlers.file_handler import FileHandler
from data.processor import DataProcessor
from services.data_processing_service import DataProcessingService


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

        (test_folder_1 / "TEST_file1.txt").write_text("1-3, 5")
        (test_folder_2 / "TEST_file2.txt").write_text("2, 4-6")

        yield tempdir_path, [test_folder_1, test_folder_2], result_dir


def test_data_processing_service(setup_test_environment):
    tempdir_path, test_dirs, result_dir = setup_test_environment
    file_handler = FileHandler(tempdir_path)
    data_processor = DataProcessor()
    data_processing_service = DataProcessingService(
        file_handler, data_processor, test_dirs, "TEST_*", result_dir
    )

    data_processing_service.execute()

    assert (result_dir / "TEST_AUCHAN_success_1.txt").exists()
    assert (result_dir / "TEST_AUCHAN_success_2.txt").exists()
