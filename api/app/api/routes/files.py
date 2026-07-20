from fastapi import APIRouter, UploadFile, File


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
    
    return router
