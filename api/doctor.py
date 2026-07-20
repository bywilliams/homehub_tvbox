from app.homehub import HomeHub


hub = HomeHub()


result = hub.doctor.check()


print("================================")
print("       HomeHub Doctor")
print("================================")
print()


for service, status in result.items():

    print(
        f"{service.capitalize():10}: {status}"
    )


print()

failed = [
    s for s,v in result.items()
    if v in ["ERROR", "OFFLINE"]
]


if failed:

    print("Result:")
    print("✗ SYSTEM ISSUES")

else:

    print("Result:")
    print("✓ SYSTEM HEALTHY")


print("================================")
