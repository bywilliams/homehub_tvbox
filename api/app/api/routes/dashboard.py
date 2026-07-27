from fastapi import APIRouter

from app.schemas.dashboard import DashboardResponse


def setup_dashboard(hub):

    router = APIRouter()


    @router.get(
        "/api/dashboard",
        response_model=DashboardResponse
    )
    def dashboard():


        system = hub.system.info()

        mqtt = hub.mqtt.info()

        storage = hub.storage.info()

        files = hub.files.info()

        file_list = hub.files.list_files()


        return {

            "system": {

                "device":
                    system.get(
                        "device"
                    ),

                "hardware":
                    system.get(
                        "hardware",
                        "RK3066"
                    ),

                "software":
                    system.get(
                        "software",
                        "HomeHub Gateway"
                    ),

                "version":
                    system.get(
                        "version"
                    ),

                "hostname":
                    system.get(
                        "hostname"
                    ),

                "mode":
                    system.get(
                        "mode"
                    )
            },


            "services": {

                "mqtt": mqtt,


                "storage": {

                    "status":
                        storage.get(
                            "status"
                        ),

                    "type":
                        storage.get(
                            "type",
                            "SDCARD"
                        ),

                    "capacity":
                        storage.get(
                            "capacity",
                            "UNKNOWN"
                        ),

                    "path":
                        storage.get(
                            "path"
                        )
                },


                "files": {

                    "status":
                        files.get(
                            "status"
                        ),

                    "count":
                        len(
                            file_list.get(
                                "files",
                                []
                            )
                        )
                },


                "doctor": {

                    "status":
                        "OK"

                }

            },


            "health": {

                "overall":
                    "ONLINE"

            }

        }


    return router
