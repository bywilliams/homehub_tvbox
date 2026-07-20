import socket


class SystemManager:

    def __init__(self, config, version):

        self.config = config

        self.device = config.load(
            "device.conf"
        )

        self.version = version


    def info(self):
        
            version = self.version.info()
        
            return {
        
                "device":
                    self.device["device"]["name"],
        
                "id":
                    self.device["device"]["id"],
        
                "hardware":
                    self.device["device"]["hardware"],
        
                "software":
                    version["software"],
        
                "version":
                    version["version"],
        
                "mode":
                    version["mode"],
        
                "api_version":
                    version["api_version"],
        
                "hostname":
                    socket.gethostname()
            }
