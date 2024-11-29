from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_MODE: str
    # MODE: str = os.getenv('MODE')

    class Config:
        env_file = ".env"

config = Settings()