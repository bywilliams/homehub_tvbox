import configparser
import os


class ConfigManager:

    def __init__(self):

        self.base_path = os.path.expanduser(
            "~/Homehub/configs"
        )


    def load(self, filename):

        config = configparser.ConfigParser()

        path = os.path.join(
            self.base_path,
            filename
        )

        config.read(path)

        return config
