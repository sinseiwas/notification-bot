from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str = ""

    LOG_DIR: str = "logs"
    LOG_LEVEL: str = "INFO"

    IS_TEST: bool = False

    CHAT_ID: int = 0
    

    class Config:
        env_file=".env"
        env_file_encoding = "utf-8"


settings = Settings()