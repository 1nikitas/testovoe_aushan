import logging
from pathlib import Path
from typing import List

from data.handlers.file_handler import FileHandler
from data.processor import DataProcessor

logger = logging.getLogger(__name__)


class DataProcessingService:
    def __init__(
        self,
        file_handler: FileHandler,
        data_processor: DataProcessor,
        directories: List[Path],
        pattern: str,
        result_dir: Path,
    ):
        self.file_handler = file_handler
        self.data_processor = data_processor
        self.directories = directories
        self.pattern = pattern
        self.result_dir = result_dir

    def execute(self):
        """Выполняет весь процесс обработки файлов"""
        logger.info("Начало выполнения процесса обработки файлов")
        
        files_content = self.file_handler.read_files(self.directories, self.pattern)
        logger.debug(f"Прочитано файлов: {len(files_content)}")
        
        processed_data = [
            (filename, self.data_processor.process_content(content))
            for filename, content in files_content
        ]
        
        logger.debug("Данные обработаны")
        self.file_handler.save_results(processed_data, self.result_dir)
        
        logger.info("Процесс обработки файлов завершен")
