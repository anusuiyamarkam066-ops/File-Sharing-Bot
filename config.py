import os

API_HASH = os.environ.get("API_HASH", "")
APP_ID = int(os.environ.get("APP_ID", "0") or 0)
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "0") or 0)
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0") or 0)
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4") or 4)
PORT = int(os.environ.get("PORT", "8080") or 8080)

# Logger
import logging
LOGGER = logging.getLogger(__name__)
