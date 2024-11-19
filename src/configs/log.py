# import yaml
import logging
import logging.config
from logging.handlers import RotatingFileHandler


class StandardFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format_str = "%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s"

    FORMATS = {
        logging.DEBUG: format_str.format(grey, reset),
        logging.INFO: format_str.format(grey, reset),
        logging.WARNING: format_str.format(yellow, reset),
        logging.ERROR: format_str.format(red, reset),
        logging.CRITICAL: format_str.format(bold_red, reset),
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)


LOGGER = logging.getLogger(__name__)

# ? Console Handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(StandardFormatter())
console_handler.setLevel(logging.INFO)

# ? File Handler
file_handler = RotatingFileHandler("./logs/app.log", maxBytes=1048576, backupCount=4)
file_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s [%(levelname)s] %(module)s - %(funcName)s - %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )
)
file_handler.setLevel(logging.DEBUG)

# ? Handling
LOGGER.addHandler(file_handler)
LOGGER.addHandler(console_handler)
