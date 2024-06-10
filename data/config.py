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

    @staticmethod
    def generate_env_file():
        print("Файл .env не найден. Пожалуйста, введите необходимые значения:")
        bot_api_token = input("Токен телеграм бота от @botfather: ")
        if_always_private = input("Всегда обрабатывать только в личных сообщениях (1 для включения, 0 для отключения): ")
        anti_flood_interval = input("Анти-флуд система (рекомендуемое значение 0.7): ")

        with open('.env', 'w', encoding='utf-8') as file:
            file.write(f'''# ! Токен телеграм бота от @botfather
BOT_API_TOKEN={bot_api_token}

# ? Всегда обрабатывать только в личных сообщениях. Если везде только в личных - 1, если хотите отключить то 0. По умол. 0:
If_ALWAYS_PRIVATE={if_always_private}

# ? Анти флуд система: Возможные типы float, integer (1 | 1.11). При значения 0 отключается. НЕ РЕКАМЕНДУЕТСЯ. Рекамендуемое значения 0.7
ANTI_FLOOD_INTERVAL={anti_flood_interval}''')