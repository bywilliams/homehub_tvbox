class VersionManager:

    def __init__(self, config):

        self.config = config

        self.version = config.load(
            "version.conf"
        )


    def info(self):

        data = self.version["version"]

        api_version = "unknown"

        if "api" in self.version:
            api_version = self.version["api"]["version"]

        return {

            "software":
            data["software"],

            "version":
            data["version"],

            "mode":
            data["mode"],

            "api_version":
            api_version

        }
