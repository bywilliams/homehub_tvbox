from pydantic import BaseModel


class HealthInfo(BaseModel):
    config: str
    mqtt: str
    storage: str
    system: str
