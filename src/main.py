import logging
import sys
from pathlib import Path

from constants import Config
from data.handlers.file_handler import FileHandler
from data.processor import DataProcessor
from services.data_processing_service import DataProcessingService

# Добавляем путь к src в sys.path
sys.path.append(str(Path(__file__).resolve().parent))


# Настраиваем логирование
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def process_data_files():
    logger.info("Начало обработки данных")
    input_path = Config.EXTRACT_PATH.value
    result_directory = Config.RESULT_DIRECTORY.value
    directories = Config.DIRECTORIES.value
    pattern = Config.PATTERN.value

    # Создаем экземпляры классов
    file_handler = FileHandler(input_path)
    data_processor = DataProcessor()
    data_processing_service = DataProcessingService(
        file_handler, data_processor, directories, pattern, result_directory
    )

    # Выполняем обработку файлов
    data_processing_service.execute()

    logger.info("Обработка данных завершена")


def main():
    process_data_files()


if __name__ == "__main__":
    main()
