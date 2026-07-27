from app.api.routes.health import setup_health
from app.api.routes.system import setup_system
from app.api.routes.storage import setup_storage
from app.api.routes.mqtt import setup_mqtt
from app.api.routes.info import setup_info
from app.api.routes.files import setup_files
from app.api.routes.dashboard import setup_dashboard


def register_routes(app, hub):
    app.include_router(setup_health(hub))
    app.include_router(setup_system(hub))
    app.include_router(setup_storage(hub))
    app.include_router(setup_mqtt(hub))
    app.include_router(setup_info(hub))
    app.include_router(setup_files(hub))
    app.include_router(setup_dashboard(hub))
