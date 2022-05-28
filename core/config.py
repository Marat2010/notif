from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    DATABASE_URL: str = 'postgresql://marat:1222@localhost:50432/db_notif'


settings = Settings(
    _env_file='.env_dev',
    _env_file_encoding='utf-8'
)

print(settings)

# --------------------------------------
# database_url: str = "postgresql://root:root@localhost:32700/employment_exchange"
# DATABASE_URL: str = 'postgresql://root:root@localhost:50432/db_notifications'
# DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="")
# DATABASE_URL = settings("EE_DATABASE_URL", cast=str, default="")

# --------------------------------------
# class Config:
#     _env_file = 'settings'
#     _env_file_encoding = 'utf-8'
# ---------------------------------------

# def settings():
#     return settings.value
