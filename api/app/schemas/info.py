from pydantic import BaseModel

from .system import SystemInfo
from .mqtt import MQTTInfo
from .storage import StorageInfo
from .health import HealthInfo


class InfoResponse(BaseModel):
    system: SystemInfo
    mqtt: MQTTInfo
    storage: StorageInfo
    health: HealthInfo
