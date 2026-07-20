from fastapi import APIRouter

from app.schemas.info import InfoResponse

def setup_info(hub):

    router = APIRouter()


    @router.get("/api/info", response_model=InfoResponse)
    def info():

        return {

            "system":
                hub.system.info(),

            "mqtt":
                hub.mqtt.info(),

            "storage":
                hub.storage.info(),

            "health":
                hub.doctor.check()

        }


    return router
