import logging
from typing import List

# Настраиваем логирование
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class DataProcessor:
    def __init__(self):
        pass

    def process_content(self, content: str) -> List[int]:
        """Обрабатывает содержимое файла и возвращает отсортированный список чисел"""  # noqa: E501
        logger.info("Начало обработки содержимого файла")
        numbers = []
        for line in content.splitlines():
            logger.debug(f"Обработка строки: {line}")
            # Удаляем кавычки и заменяем запятые на пробелы для корректного разделения  # noqa: E501
            for part in line.replace('"', "").replace(",", " ").split():
                if "-" in part:
                    try:
                        start, end = map(int, part.split("-"))
                        numbers.extend(range(start, end + 1))
                        logger.debug(f"Добавлен диапазон чисел: {start}-{end}")
                    except ValueError as e:
                        logger.warning(
                            f"Невозможно обработать диапазон: {part}, ошибка: {e}"  # noqa: E501
                        )
                else:
                    try:
                        numbers.append(int(part))
                        logger.debug(f"Добавлено число: {part}")
                    except ValueError as e:
                        logger.warning(
                            f"Невозможно обработать число: {part}, ошибка: {e}"
                        )
        sorted_numbers = self.__merge_sort(numbers)
        logger.info("Обработка содержимого файла завершена")
        return sorted_numbers

    def __merge_sort(self, numbers: List[int]) -> List[int]:
        """Сортирует список чисел с помощью алгоритма слияния"""
        if len(numbers) <= 1:
            return numbers

        mid = len(numbers) // 2
        left_half = self.__merge_sort(numbers[:mid])
        right_half = self.__merge_sort(numbers[mid:])

        return self.__merge(left_half, right_half)

    def __merge(self, left: List[int], right: List[int]) -> List[int]:
        """Объединяет два отсортированных списка в один"""
        sorted_list = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                sorted_list.append(left[left_idx])
                left_idx += 1
            else:
                sorted_list.append(right[right_idx])
                right_idx += 1

        sorted_list.extend(left[left_idx:])
        sorted_list.extend(right[right_idx:])
        return sorted_list
