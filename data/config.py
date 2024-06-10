import os
from dotenv import load_dotenv
from typing import Optional, Union

class SecretConfig:
    """
    Класс для работы с секретами из переменных окружения и .env файла.
    """
    def __init__(
        self,
        env_file: Optional[str] = '.env'
    ) -> None:
        """
        Инициализация объекта SecretConfig.

        Args:
            env_file (str, optional): Путь к файлу .env. По умолчанию '.env'.
        """
        self.env_file = env_file
        self.load_env()

    def load_env(
        self
    ) -> None:
        """
        Загрузка переменных окружения из .env файла.
        """
        if self.env_file and os.path.exists(self.env_file):
            load_dotenv(self.env_file)

    def get_secret(
        self,
        key: str,
        default: Optional[Union[str, int]] = None
    ) -> Optional[str]:
        """
        Получить значение секрета по ключу.

        Сначала пытается получить из переменных окружения,
        затем из .env файла.

        Args:
            key (str): Ключ для доступа к секрету.
            default (str, optional): Значение по умолчанию. По умолчанию None.

        Returns:
            str: Значение секрета, если найдено, иначе значение по умолчанию.
        """
        return os.getenv(key, default)
