from pathlib import Path
import logging


class HomeHubLogger:

    def __init__(self, base_path=None):

        self.log_path = (
            Path(base_path)
            if base_path
            else Path.home() / "Homehub" / "logs" / "homehub.log"
        )


        self.log_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        logging.basicConfig(

            filename=self.log_path,

            level=logging.INFO,

            format=
            "%(asctime)s | %(levelname)s | %(message)s"

        )


    def info(self, message):

        logging.info(message)


    def error(self, message):

        logging.error(message)


    def warning(self, message):

        logging.warning(message)
