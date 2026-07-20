from fastapi import FastAPI
from app.api.routes.system import setup_system
from app.api.routes.storage import setup_storage
from app.api.routes.mqtt import setup_mqtt
from app.homehub import HomeHub
from app.api.routes.health import setup_health

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


    return app
