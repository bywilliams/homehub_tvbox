from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse

from app.schemas.files import (
    FilesInfo,
    FilesList
)


def setup_files(homehub):

    router = APIRouter()

    @router.get(
        "/api/files",
        response_model=FilesInfo
    )
    def info():

        return homehub.files.info()


    @router.get(
        "/api/files/list",
        response_model=FilesList
    )
    def list_files():
        result = homehub.files.list_files()
        
        result["count"] = len(
            result["files"]
        )

        return result


    @router.post("/api/files/upload")
    async def upload(
        file: UploadFile = File(...)
    ):

        content = await file.read()

        return homehub.files.save_file(
            file.filename,
            content
        )


    @router.get(
        "/api/files/download/{filename:path}"
    )
    def download(filename: str):

        path = homehub.files.get_file_path(
            filename
        )

        if not path:

            return {
                "status": "ERROR",
                "message": "File not found"
            }


        return FileResponse(
            path,
            filename=filename
        )



    @router.delete(
        "/api/files/{filename}"
    )
    def delete(filename: str):

        result = homehub.files.delete_file(
            filename
        )


        if result:

            return {
                "status": "DELETED",
                "file": filename
            }


        return {
            "status": "ERROR",
            "message": "File not found"
        }
    
    return router
