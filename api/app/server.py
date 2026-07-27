# Bilioteca padrão
from pathlib import Path

#terceiros
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# Projeto
from app.homehub import HomeHub
from app.api.routes.dashboard import setup_dashboard
from app.api.routes import register_routes

def create_server():

    hub = HomeHub()

    app = FastAPI(
        title="HomeHub Gateway API",
        version=hub.version.info()["version"]
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://192.168.0.159:8080"
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    BASE_DIR = Path(__file__).resolve().parents[2]
    
    DASHBOARD_DIR = BASE_DIR / "dashboard"

    app.mount(
        "/static",
        StaticFiles(directory=DASHBOARD_DIR),
        name="dashboard"
    )


    @app.get("/")
    def root():

        return {
            "name": "HomeHub Gateway",
            "version": hub.version.info(),
            "status": "online"
        }

    @app.get("/dashboard")
    def dashboard():
    
        return FileResponse(
            DASHBOARD_DIR / "index.html"
        )


    register_routes(app, hub)


    return app
