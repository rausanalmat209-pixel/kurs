from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


ROOT_ENV_PATH = Path(__file__).resolve().parents[3] / ".env"


class Settings(BaseSettings):
    ENVIRONMENT: str = "local"
    CORS_ORIGINS: list[str] = ["http://localhost:3000"]

    POSTGRES_USER: str = "qadam"
    POSTGRES_PASSWORD: str = "your-password"
    POSTGRES_DB: str = "qadam"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3.2"

    model_config = SettingsConfigDict(
        env_file=str(ROOT_ENV_PATH),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


settings = Settings()

