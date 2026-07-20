from pydantic import BaseModel


class StorageInfo(BaseModel):
    name: str
    type: str
    capacity: str
    status: str
