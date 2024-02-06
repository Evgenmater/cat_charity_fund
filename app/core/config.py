from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Благотворительный фонд поддержки котиков'
    database_url: str
    secret: str = 'SECRET'
    # Атрибуты по умолчанию, для создания суперюзера при запуске приложения
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
