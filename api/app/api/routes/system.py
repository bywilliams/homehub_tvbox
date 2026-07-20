from fastapi import APIRouter


router = APIRouter()


def setup_system(homehub):

    @router.get("/api/system")
    def system():

        return homehub.system.info()


    return router
