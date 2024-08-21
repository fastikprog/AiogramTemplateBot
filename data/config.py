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
        if not self.env_file or not os.path.exists(self.env_file):
            self.generate_env_file()
            self.load_env()
        else:
            load_dotenv(self.env_file)

    def get_secret(
        self,
        key: str,
        default: Optional[Union[str, int]] = None
    ) -> Optional[Union[str, int]]:
        """
        Получить значение секрета по ключу.

        Если ключ не найден, добавляет его в .env файл с дефолтным значением.

        Args:
            key (str): Ключ для доступа к секрету.
            default (str, optional): Значение по умолчанию. По умолчанию None.

        Returns:
            str: Значение секрета, если найдено, иначе значение по умолчанию.
        """
        value = os.getenv(
            key=key
        )

        if value is None:
            value = default
            self.set_secret(key, value)

        return value

    def set_secret(
        self,
        key: str,
        value: Union[str, int]
    ) -> None:
        """
        Добавить ключ и значение в .env файл, если они отсутствуют.

        Args:
            key (str): Ключ для секрета.
            value (str): Значение секрета.
        """
        with open(self.env_file, 'a', encoding='utf-8') as file:
            file.write(f'\n{key}={value}')
        load_dotenv(self.env_file, override=True)

    @staticmethod
    def generate_env_file():
        print("Файл .env не найден. Пожалуйста, введите необходимые значения:")

        # Словарь с категориями и их соответствующими настройками
        config_structure = {
            "Токены и ключи": {
                "BOT_API_TOKEN": "Токен телеграм бота от @botfather: "
            },
            "Основные настройки": {
                "If_ALWAYS_PRIVATE": "Всегда обрабатывать только в личных сообщениях (1 для включения, 0 для отключения): ",
                "ANTI_FLOOD_INTERVAL": "Анти-флуд система (рекомендуемое значение 0.7): "
            },
            "Настройки базы данных": {
                "DATABASE_LOGIN": "Логин для базы данных (по умолчанию root): ",
                "DATABASE_PASSWORD": "Пароль для базы данных: ",
                "DATABASE_NAME": "Название базы данных (en): ",
                "DATABASE_IP": "IP адрес базы данных (по умолчанию localhost): ",
                "DATABASE_PORT": "Порт базы данных (по умолчанию 3306): "
            }
        }

        config_defaults = {
            "DATABASE_LOGIN": 'root',
            "If_ALWAYS_PRIVATE": 0,
            "ANTI_FLOOD_INTERVAL": 0.7,
            "DATABASE_IP": "localhost",
            "DATABASE_PORT": 3306
        }

        config_values = {}

        # Запрос значений у пользователя
        for category, prompts in config_structure.items():
            print(f"\n{category}:")
            for key, prompt in prompts.items():
                value = input(prompt) or str(config_defaults.get(key, ""))
                config_values[key] = value

        # Запись в .env файл с разделением по категориям
        with open('.env', 'w', encoding='utf-8') as file:
            for category, prompts in config_structure.items():
                file.write(f"\n# {category}\n")
                for key in prompts.keys():
                    value = config_values[key]
                    file.write(f"{key}={value}\n")

        print("Конфигурационный файл успешно создан.")
