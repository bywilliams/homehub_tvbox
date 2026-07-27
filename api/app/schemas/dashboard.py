from pydantic import BaseModel


class DashboardSystem(BaseModel):

    device: str
    hardware: str
    software: str
    version: str
    hostname: str
    mode: str



class DashboardMQTT(BaseModel):

    status: str
    broker: str
    config: bool
    process: bool
    port: bool



class DashboardStorage(BaseModel):

    status: str
    type: str
    capacity: str
    path: str



class DashboardFiles(BaseModel):

    status: str
    count: int



class DashboardDoctor(BaseModel):

    status: str



class DashboardServices(BaseModel):

    mqtt: DashboardMQTT
    storage: DashboardStorage
    files: DashboardFiles
    doctor: DashboardDoctor



class DashboardHealth(BaseModel):

    overall: str



class DashboardResponse(BaseModel):

    system: DashboardSystem
    services: DashboardServices
    health: DashboardHealth
