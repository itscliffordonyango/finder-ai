from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Job Finder AI"
    APP_VERSION: str = "0.1.0"

    DEBUG: bool = True

    API_V1_PREFIX: str = "/api/v1"

    DATABASE_URL: str

    SECRET_KEY: str

    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4.1-mini"

    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-3.6-flash"

    OLLAMA_API_KEY: str = ""
    

    AI_PROVIDER: str = "ollama"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    ALGORITHM: str = "HS256"
    

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()
