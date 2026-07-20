import os
import subprocess


class MQTTManager:

    def __init__(self, config):

        self.config = config

        self.config_file = os.path.expanduser(
            "~/Homehub/configs/mosquitto/mosquitto.conf"
        )

    def _process_running(self):

        try:
            output = subprocess.check_output(
                ["pgrep", "-f", "mosquitto"]
            ).decode().strip()

            return bool(output)

        except subprocess.CalledProcessError:
            return False

    def _port_listening(self):

        try:
            output = subprocess.check_output(
                ["ss", "-tln"]
            ).decode()

            return ":1883" in output

        except Exception:
            return False

    def info(self):

        process = self._process_running()
        port = self._port_listening()

        return {
            "broker": "Mosquitto",
            "config": os.path.exists(self.config_file),
            "process": process,
            "port": port,
            "status": "ONLINE" if process and port else "OFFLINE",
        }

    def status(self):

        return self.info()["status"]
