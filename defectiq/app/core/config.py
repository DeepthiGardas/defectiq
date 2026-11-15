from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    llm_provider: str = "gemini"
    google_api_key: str = ""
    groq_api_key: str = ""
    openai_api_key: str = ""
    postgres_url: str = "postgresql+psycopg2://defectiq:defectiq@localhost:5432/defectiq"
    qdrant_url: str = "http://localhost:6333"
    compass_mock_url: str = "http://localhost:8001"
    cvms_mock_url: str = "http://localhost:8002"
    log_level: str = "INFO"


settings = Settings()
