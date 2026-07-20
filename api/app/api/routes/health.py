from fastapi import APIRouter


router = APIRouter()


def setup_health(homehub):

    @router.get("/api/health")
    def health():

        doctor = homehub.registry.get(
            "doctor"
        )

        result = doctor.check()

        healthy = all(
            value not in ["ERROR", "OFFLINE"]
            for value in result.values()
        )

        result["status"] = (
            "HEALTHY"
            if healthy
            else "DEGRADED"
        )

        return result


    return router
