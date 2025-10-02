import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional

try:
    from core.config import settings
except Exception:
    settings = None

_LEVELS = {
    "CRITICAL": logging.CRITICAL,
    "ERROR": logging.ERROR,
    "WARNING": logging.WARNING,
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "NOTSET": logging.NOTSET,
}

def setup_logging(
    log_dir: Optional[str | Path] = None,
    level: Optional[str] = None,
):
    if settings:
        log_dir = log_dir or settings.LOG_DIR
        level = level or settings.LOG_LEVEL
    else:
        log_dir = log_dir or "logs"
        level = level or "INFO"

    path = Path(log_dir).resolve()
    path.mkdir(parents=True, exist_ok=True)

    level_num = _LEVELS.get(str(level).upper(), logging.INFO)

    fmt = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    root = logging.getLogger()
    root.setLevel(level_num)

    for h in list(root.handlers):
        root.removeHandler(h)

    console = logging.StreamHandler()
    console.setLevel(level_num)
    console.setFormatter(logging.Formatter(fmt, datefmt))

    file_main = RotatingFileHandler(
        path / "app.log", maxBytes=2_000_000, backupCount=5, encoding="utf-8"
    )
    file_main.setLevel(level_num)
    file_main.setFormatter(logging.Formatter(fmt, datefmt))

    file_err = RotatingFileHandler(
        path / "errors.log", maxBytes=1_000_000, backupCount=3, encoding="utf-8"
    )
    file_err.setLevel(logging.ERROR)
    file_err.setFormatter(logging.Formatter(fmt, datefmt))

    root.addHandler(console)
    root.addHandler(file_main)
    root.addHandler(file_err)

    logging.getLogger("aiogram.event").setLevel(logging.WARNING)
    logging.getLogger("aiohttp.access").setLevel(logging.WARNING)

def get_logger(name: str | None = None):
    return logging.getLogger(name)