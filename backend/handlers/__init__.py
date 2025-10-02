from .start_handler import router as start_router
from .notification_handler import router as not_router

handlers = [
    start_router,
    not_router
]