import os
import subprocess
import glob


class StorageManager:

    def __init__(self, config):

        self.config = config

        self.storage = config.load(
            "storage.conf"
        )

        self.base_path = None


    def configured_path(self):

        return self.storage["storage"]["path"]


    def discover_storage(self):

        """
        Procura automaticamente cartões disponíveis
        no Termux.
        """

        candidates = glob.glob(
            os.path.expanduser(
                "~/storage/external-*"
            )
        )


        for candidate in candidates:

            test_path = os.path.join(
                candidate,
                "HomeHub"
            )

            if os.path.exists(test_path):

                return test_path


        return None



    def resolve_path(self):

        configured = self.configured_path()


        # caminho configurado existe
        if os.path.exists(configured):

            self.base_path = configured
            return configured


        # tenta descobrir automaticamente

        discovered = self.discover_storage()


        if discovered:

            self.base_path = discovered
            return discovered


        return None



    def disk_info(self, path):

        try:

            result = subprocess.check_output(
                [
                    "df",
                    "-h",
                    path
                ]
            ).decode()


            lines = result.splitlines()


            if len(lines) >= 2:

                values = lines[1].split()

                return {

                    "total": values[1],
                    "used": values[2],
                    "free": values[3],
                    "usage": values[4]

                }


        except Exception:

            pass


        return {}



    def info(self):

        path = self.resolve_path()


        data = {

            "name":
            self.storage["storage"]["name"],

            "type":
            self.storage["storage"]["type"],

            "capacity":
            self.storage["storage"]["capacity"],

            "path":
            path,

            "status":
            "ONLINE"
            if path
            else "NOT_MOUNTED",

        }


        if path:

            data.update(
                self.disk_info(path)
            )


        return data



    def status(self):

        return self.info()["status"]
