from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///encurtaurl.db"

    class Config:
        env_prefix = ".env"

@lru_cache()
def get_settings():
    settings = Settings()
    print(f"iniciando as configurações de {settings.env_name}")
    return settings