from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # `.env.prod` takes priority over `.env`
        env_file=(".env", ".env.prod")
    )
    PROJECT_NAME: str
    API_V1_STR: str = "/api/v1"


settings = Settings()
