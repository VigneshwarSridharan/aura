from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Aura AI Backend"
    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    openai_api_key: str | None = None
    openai_model_id: str = Field(default="gpt-4o-mini", validation_alias="AGNO_MODEL_ID")
    agno_enable_web_search: bool = Field(default=True, validation_alias="AGNO_ENABLE_WEB_SEARCH")
    cors_origins_raw: str = Field(
        default="http://localhost:3000",
        validation_alias="BACKEND_CORS_ORIGINS",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins_raw.split(",") if origin.strip()]


settings = Settings()
