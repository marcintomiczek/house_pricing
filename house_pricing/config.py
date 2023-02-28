from pydantic import BaseSettings


class Settings(BaseSettings):
    db_provider: str
    db_url: str
    user: str
    password: str

    class Config:
        env_file = ".env"  # supports loading env variables using python-dotenv


def get_settings() -> Settings:
    settings = Settings()
    return settings
