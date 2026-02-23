from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    DB_PATH: str = "sqlite+aiosqlite:///database.sqlite3"
    
    XUI_URL: str = ""
    XUI_USERNAME: str = ""
    XUI_PASSWORD: str = ""
    
    # ID для платежей
    PAYMENT_PROVIDER_TOKEN: str = ""
    
    # Цены
    PRICE_1_MONTH_RUB: int = 299 # Цена за месяц (поправил под скрин)
    PRICE_3_MONTHS_RUB: int = 790
    PRICE_6_MONTHS_RUB: int = 1390
    PRICE_12_MONTHS_RUB: int = 2690
    PRICE_ADDITIONAL_DEVICE_RUB: int = 50 # За доп. устройство (по ТЗ)
    
    REFERRAL_BONUS_RUB: int = 50 # Бонус за рефералку
    
    class Config:
        env_file = ".env"

config = Settings()
