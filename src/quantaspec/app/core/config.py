from functools import lru_cache
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL

class Settings(BaseSettings):

    APP_NAME: str = 'AI QuantaSpec'
    DEBUG: bool = False

    DB_HOST: str = 'db'
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASSWORD: SecretStr = "postgres"
    DB_NAME: str = "quantaspec"
    DB_SCHEMA: str = "public"


    model_config = SettingsConfigDict(
        env_file='.env',env_file_encoding='utf-8', extra='ignore'
    )

    @property
    def DATABASE_URL(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.DB_USER,
            password=self.DB_PASSWORD.get_secret_value(),
            host=self.DB_HOST,
            port=self.DB_PORT,
            database=self.DB_NAME,
        )


@lru_cache
def get_settings():
    return Settings()