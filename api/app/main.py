from app.homehub import HomeHub


hub = HomeHub()


print("=" * 40)
print("HomeHub Core")
print("=" * 40)


info = hub.system.info()

for key, value in info.items():

    print(f"{key:10}: {value}")


print("=" * 40)

mqtt = hub.mqtt.info()

print()
print("MQTT:")

for key, value in mqtt.items():
    print(f"{key:10}: {value}")


storage = hub.storage.info()


print()

print("Version:")

for key, value in hub.version.info().items():

    print(f"{key:10}: {value}")

print()

print("Storage:")

for key, value in storage.items():

    print(f"{key:10}: {value}")


print("=" * 40)

print()

print("Registered Services:")

for name in hub.registry.all():

    print(" -", name)
