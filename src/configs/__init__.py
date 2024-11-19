from .env import *
from .log import *

config = ApplicationConfig()
project_config = ProjectConfig()


__all__ = ["project_config", "config", "console_handler", "file_handler", "LOGGER"]
