from tortoise import Tortoise
import pymysql
import aiomysql

class DatabaseManager:
    def __init__(self, username: str, password: str, db_name: str, ip: str = 'localhost', port: int = 3306):
        self.username = username
        self.password = password
        self.db_name = db_name
        self.ip = ip
        self.port: int = int(port)

    async def create_database_if_not_exists(self):
        try:
            conn = pymysql.connect(host=self.ip, user=self.username, password=self.password, port=self.port)
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{self.db_name}`")
            cursor.close()
            conn.close()
        except pymysql.MySQLError as e:
            print(f"Failed to create database: {e}")
            exit(1)

    async def init_db(self):
        if not self.username:
            print(f'No existing username!')
            exit(403)

        if not self.password:
            print(f'No existing password!')
            exit(403)

        if not self.db_name:
            print(f'No existing db_name!')
            exit(403)

        await self.create_database_if_not_exists()

        try:
            await Tortoise.init(
                db_url=f"mysql://{self.username}:{self.password}@{self.ip}:{self.port}/{self.db_name}",
                modules={'models': ['utils.database.models']}
            )
            await Tortoise.generate_schemas()
        except aiomysql.Error as e:
            print(f"Failed to connect to the database: {e}")
            exit(1)

    async def close_db(self):
        await Tortoise.close_connections()
