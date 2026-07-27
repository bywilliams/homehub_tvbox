class DoctorManager:

    def __init__(self, registry):

        self.registry = registry


    def check(self):

        result = {}


        # Config

        config = self.registry.get(
            "config"
        )

        result["config"] = (
            "OK"
            if config
            else "ERROR"
        )


        # MQTT

        mqtt = self.registry.get(
            "mqtt"
        )

        result["mqtt"] = (
            mqtt.status()
            if mqtt
            else "ERROR"
        )


        # Storage

        storage = self.registry.get(
            "storage"
        )

        result["storage"] = (
            storage.status()
            if storage
            else "ERROR"
        )


        # System

        system = self.registry.get(
            "system"
        )

        result["system"] = (
            "OK"
            if system
            else "ERROR"
        )

        # Files 
        files = self.registry.get("files")
        
        result["files"] = (
            files.info()["status"]
            if files
            else "ERROR"
        )

        logger = self.registry.get("logger")
        
        result["logger"] = (
            "OK"
            if logger
            else "ERROR"
        )


        version = self.registry.get("version")
        
        result["version"] = (
            "OK"
            if version
            else "ERROR"
        )


        return result
