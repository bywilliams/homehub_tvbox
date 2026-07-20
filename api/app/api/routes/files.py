from fastapi import APIRouter


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

    
    return router
