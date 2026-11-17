from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Настройки проекта. Читаются из переменных окружения и файла .env"""
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    base_url: str = 'http://localhost:8080/api/v3' # По умолчанию локальный сервер
    api_key: str = 'special-key'
    timeout: float = 15.0

    @property
    def headers(self) -> dict:
        return {
            "accept": "application/json",
            "Content-Type": "application/json",
            "api_key": self.api_key
        }


settings = Settings()