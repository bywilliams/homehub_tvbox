import logging
import os


class HomeHubLogger:

    def __init__(self):

        self.log_path = os.path.expanduser(
            "~/Homehub/logs/homehub.log"
        )


        os.makedirs(
            os.path.dirname(self.log_path),
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
