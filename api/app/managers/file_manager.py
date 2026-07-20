import os


class FileManager:

    def __init__(self, storage):

        self.storage = storage


    def base_path(self):

        path = self.storage.resolve_path()

        if not path:
            return None

        return os.path.join(
            path,
            "files"
        )


    def info(self):

        path = self.base_path()

        return {

            "path": path,

            "status":
                "ONLINE"
                if path and os.path.exists(path)
                else "OFFLINE"

        }

    def list_files(self):

        path = self.base_path()


        if not path:

            return {
                "status": "OFFLINE",
                "files": []
            }


        result = {

            "status": "ONLINE",

            "files": []

        }


        for root, dirs, files in os.walk(path):

            for file in files:

                full_path = os.path.join(
                    root,
                    file
                )

                result["files"].append(
                    os.path.relpath(
                        full_path,
                        path
                    )
                )


        return result

        
