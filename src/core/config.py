import os
from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings

load_dotenv(dotenv_path=find_dotenv(".env"))


class DBSettings(BaseSettings):
    port: int = os.environ.get("PG_PORT")
    name: str = os.environ.get("PG_NAME")
    user: str = os.environ.get("PG_USER")
    password: str = os.environ.get("PG_PASS")
    host: str = os.environ.get("PG_HOST")

    @property
    def db_sync_url(self):
        return f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}/{self.name}'


class Settings(BaseSettings):
    db: DBSettings = DBSettings()



settings: Settings = Settings()



