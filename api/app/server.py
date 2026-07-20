from fastapi import FastAPI
from app.api.routes.system import setup_system
from app.api.routes.storage import setup_storage
from app.api.routes.mqtt import setup_mqtt
from app.api.routes.info import setup_info
from app.api.routes.health import setup_health
from app.homehub import HomeHub

def create_server():

    app = FastAPI(
        title="HomeHub Gateway API",
        version="0.3.0-dev"
    )

    hub = HomeHub()


    @app.get("/")
    def root():

        return {
            "name": "HomeHub Gateway",
            "version": "0.3.0-dev",
            "status": "online"
        }

    app.include_router(
        setup_health(hub)
    )

    app.include_router(
        setup_system(hub)
    )

    app.include_router(
        setup_storage(hub)
    )   

    app.include_router(
        setup_mqtt(hub)
    )

    app.include_router(
        setup_info(hub)
    )


    return app
