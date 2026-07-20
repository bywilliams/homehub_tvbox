from fastapi import APIRouter


router = APIRouter()


def setup_storage(homehub):

    @router.get("/api/storage")
    def storage():

        return homehub.storage.info()


    return router
