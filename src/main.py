import logging
import sys
from pathlib import Path

from src.data.file_handler import FileHandler
from src.data.processor import DataProcessor
from src.services.data_processing_service import DataProcessingService

# Настраиваем логирование
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Добавляем корневую директорию проекта в sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))


def main():
    logger.info("Начало работы программы")
    input_path = Path("./input_files")
    result_directory = input_path / "Result"
    directories = [input_path / "TEST_Folder_1", input_path / "TEST_Folder_2"]
    pattern = "TEST_*"

    # Создаем экземпляры классов
    file_handler = FileHandler(input_path)
    data_processor = DataProcessor()
    data_processing_service = DataProcessingService(
        file_handler, data_processor, directories, pattern, result_directory
    )

    # Выполняем обработку файлов
    data_processing_service.execute()

    logger.info("Работа программы завершена")


if __name__ == "__main__":
    main()
