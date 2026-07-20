class ServiceRegistry:

        def __init__(self):
            self._services = {}

        def register(self, name, service):
            self._services[name] = service

        def get(self, name):
            return self._services.get(name)

        def all(self):
            return self._services
