import socket


class SystemManager:

    def __init__(self, config, version):

        self.config = config

        self.device_config = config.load("device.conf")

        self.version = version


    def info(self):

        device = self.device_config["device"]
        version = self.version.info()
    
        return {
    
            "device": device["name"],
    
            "id": device["id"],
    
            "hardware": device["hardware"],
    
            "software": version["software"],
    
            "version": version["version"],
            
            "mode": version["mode"],
    
            "api_version": version["api_version"],
    
            "hostname": socket.gethostname()
        }
