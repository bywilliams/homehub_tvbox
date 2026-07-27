from pathlib import Path
import configparser



class ConfigManager:

    def __init__(self, base_path=None):
        
         self.base_path = (
            Path(base_path)
            if base_path
            else Path.home() / "Homehub" / "configs"
         )


    def load(self, filename):
        
        path = self.base_path / filename
    
        if not path.exists():
            raise FileNotFoundError(
                f"Configuration  file not found: {path}"
            )
    
        config = configparser.ConfigParser()
    
        config.read(path)
    
        return config
