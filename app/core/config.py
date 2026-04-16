from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./qr_scanner.db"

    class Config:
        env_file = ".env"

settings = Settings()