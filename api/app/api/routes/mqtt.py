from fastapi import APIRouter


router = APIRouter()


def setup_mqtt(homehub):

    @router.get("/api/mqtt")
    def mqtt():

        return homehub.mqtt.info()


    return router
