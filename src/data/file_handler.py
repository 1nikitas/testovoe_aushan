import logging
from pathlib import Path
from typing import List, Tuple

logger = logging.getLogger(__name__)


class FileHandler:
    def __init__(self, base_path: Path):
        self.base_path = base_path

    def read_files(
        self, directories: List[Path], pattern: str
    ) -> List[Tuple[str, str]]:
        """Читает файлы по заданной маске из указанных директорий"""
        logger.info("Начало чтения файлов")
        files_content = []
        for directory in directories:
            for filepath in directory.glob(pattern):
                with open(filepath, "r") as file:
                    files_content.append((filepath.name, file.read()))
                    logger.debug(f"Прочитан файл: {filepath.name}")
        logger.info("Чтение файлов завершено")
        return files_content

    def save_results(
        self, processed_data: List[Tuple[str, List[int]]], output_directory: Path  # noqa: E501
    ):
        """Сохраняет обработанные данные в результирующую директорию"""
        logger.info("Начало сохранения результатов")
        output_directory.mkdir(parents=True, exist_ok=True)
        for idx, (filename, numbers) in enumerate(processed_data):
            result_filename = output_directory / f"TEST_AUCHAN_success_{idx+1}.txt"  # noqa: E501
            with open(result_filename, "w") as file:
                for number in numbers:
                    file.write(f"{number}\n")
            logger.debug(f"Сохранен файл: {result_filename}")
        logger.info("Сохранение результатов завершено")
