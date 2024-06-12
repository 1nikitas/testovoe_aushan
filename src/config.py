from pathlib import Path

ARCHIVE_PATH = Path("/mnt/data/AUCHAN_TEST.zip")
EXTRACT_PATH = Path("/mnt/data/AUCHAN_TEST")
RESULT_DIRECTORY = EXTRACT_PATH / "Result"
DIRECTORIES = [EXTRACT_PATH / "TEST_Folder_1", EXTRACT_PATH / "TEST_Folder_2"]
PATTERN = "TEST_*"
