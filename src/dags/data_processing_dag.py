import logging
import sys
from datetime import datetime
from pathlib import Path

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from constants import DagConfig
from data.handlers.file_handler import FileHandler
from data.processor import DataProcessor
from services.data_processing_service import DataProcessingService

sys.path.append(str(Path(__file__).resolve().parents[2] / "src"))

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}


def process_data_files():
    logger.info("Начало обработки данных")
    input_path = DagConfig.EXTRACT_PATH.value
    result_directory = DagConfig.RESULT_DIRECTORY.value
    directories = DagConfig.DIRECTORIES.value
    pattern = DagConfig.PATTERN.value

    # Создаем экземпляры классов
    file_handler = FileHandler(input_path)
    data_processor = DataProcessor()
    data_processing_service = DataProcessingService(
        file_handler=file_handler,
        data_processor=data_processor,
        directories=directories,
        pattern=pattern,
        result_dir=result_directory
    )

    # Выполняем обработку файлов
    data_processing_service.execute()

    logger.info("Обработка данных завершена")


with DAG(
    "data_files_processing_dag", default_args=default_args, schedule_interval="@daily"
) as dag:
    start_pipeline = DummyOperator(task_id="start_pipeline")

    process_data_files_task = PythonOperator(
        task_id="process_data_files",
        python_callable=process_data_files,
    )

    finish_pipeline = DummyOperator(task_id="finish_pipeline")

    start_pipeline >> process_data_files_task >> finish_pipeline
