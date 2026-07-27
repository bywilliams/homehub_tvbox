class VersionManager:

    def __init__(self, config):

        self.config = config

        self.version_config = config.load(
            "version.conf"
        )


    def info(self):

        data = self.version_config["version"]

        api_version = (
            self.version_config["api"]["version"]
            if "api" in self.version_config
            else "unknown"
        )

        return {

            "software": data["software"],

            "version": data["version"],

            "mode": data["mode"],

            "api_version": api_version

        }
