class SystemService:
    def __init(self, system_manager):
        self.system = system_manager

    def summary(self):
        return self.system.info()

        
