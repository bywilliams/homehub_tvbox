class VersionManager:

    def __init__(self, config):

        self.config = config

        self.version = config.load(
            "version.conf"
        )


    def info(self):

        data = self.version["version"]

        return {

            "software":
            data["software"],

            "version":
            data["version"],

            "mode":
            data["mode"]

        }
