from pydantic import BaseModel


class MQTTInfo(BaseModel):
    broker: str
    config: bool
    process: bool
    port: bool
    status: str
