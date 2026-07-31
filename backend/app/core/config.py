from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Job Finder AI"

    APP_VERSION: str = "0.1.0"

    DEBUG: bool = True

    API_V1_PREFIX: str = "/api/v1"

    DATABASE_URL: str = (
        "postgresql+asyncpg://postgres:password@localhost:5432/jobfinder"
    )

    SECRET_KEY: str = "4206866afd215ab56959eb5989d3a3112016778d5a1e0e4cbbda19e9a76c3ef5"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    ALGORITHM: str = "HS256"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()