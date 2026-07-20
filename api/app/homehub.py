from app.managers.doctor_manager import DoctorManager
from app.registry.service_registry import ServiceRegistry
from app.core.config import ConfigManager
from app.core.logger import HomeHubLogger
from app.core.version import VersionManager

from app.managers.system_manager import SystemManager
from app.managers.storage_manager import StorageManager
from app.managers.mqtt_manager import MQTTManager


class HomeHub:

    def __init__(self):
               
        self.config = ConfigManager()

        self.logger = HomeHubLogger()
        self.logger.info("HomeHub Core initialized")

        self.version = VersionManager(
            self.config
        )

        self.system = SystemManager(
            config = self.config,
            version = self.version
        )

        self.storage = StorageManager(
            self.config
        )

        self.mqtt = MQTTManager(
            self.config
        )

        #8  Registrar serviços
        self.registry = ServiceRegistry()
        self.registry.register("config", self.config)
        self.registry.register("version", self.version)
        self.registry.register("logger", self.logger)
        self.registry.register("system", self.system)
        self.registry.register("mqtt", self.mqtt)
        self.registry.register("storage", self.storage)

        self.doctor = DoctorManager(
            self.registry
        )
        
        self.registry.register(
            "doctor",
            self.doctor
        )
