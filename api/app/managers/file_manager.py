import os
MAX_FILE_SIZE = 100 * 1024 * 1024

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


    def save_file(self, filename, content):

        path = self.base_path()

        if not path:

            return {
                "status": "OFFLINE"
            }


        destination = os.path.join(
            path,
            filename
        )

        if os.path.exists(destination):
        
            return {
                "status":"ERROR",
                "message":"File already exists"
            }


        if len(content) > MAX_FILE_SIZE:
        
            return {
        
                "status":"ERROR",
        
                "message":
                "File too large"
        
            }


        with open(
            destination,
            "wb"
        ) as file:

            file.write(content)


        return {

            "status": "ONLINE",

            "file": filename

        }


    def delete_file(self, filename):

         path = self.get_file_path(
             filename
         )


         if not path:

             return False


         os.remove(path)

         return True 
        

    def get_file_path(self, filename):

        base = self.base_path()

        if not base:
            return None

        base = os.path.abspath(base)

        file_path = os.path.abspath(
           os.path.join(base,filename)
        )

        if not file_path.startswith(base + os.sep):
            return none
        
        if os.path.isfile(file_path):
            return file_path


        return None
