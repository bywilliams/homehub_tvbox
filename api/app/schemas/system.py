from pydantic import BaseModel


class SystemInfo(BaseModel):
    device: str
    id: str
    hardware: str
    software: str
    version: str
    mode: str
    api_version: str
    hostname: str
