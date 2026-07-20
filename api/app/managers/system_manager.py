import socket


class SystemManager:

    def __init__(self, config):

        self.config = config

        self.device = config.load(
            "device.conf"
        )

        self.version = config.load(
            "version.conf"
        )


    def info(self):

        return {

            "device":
            self.device["device"]["name"],

            "id":
            self.device["device"]["id"],

            "hardware":
            self.device["device"]["hardware"],

            "version":
            self.version["version"]["version"],

            "hostname":
            socket.gethostname()
        }
