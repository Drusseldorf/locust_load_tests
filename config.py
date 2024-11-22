from typing import List
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

ENV_FILE = Path(__file__).parent.joinpath(".env")


class Company(BaseSettings):
    id: str
    token: str


class PayInH(BaseSettings):
    currency: str
    direct_method: str


class PayOut(BaseSettings):
    currency: str
    direct_method: List[str] = Field(default_factory=list)
    bank_name: List[str] = Field(default_factory=list)
    customer_requisite: str


class SMSReader(BaseSettings):
    id: str
    sender: str
    device_id: str
    text: str
    operator_token: str


class Settings(BaseSettings):
    company: Company
    payin: PayInH
    payout: PayOut
    smsreader: SMSReader

    model_config = SettingsConfigDict(
        env_file=ENV_FILE, env_file_encoding="utf-8", env_nested_delimiter="__"
    )


settings = Settings()
