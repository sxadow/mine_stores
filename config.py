import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5498017223:AAGi_caKGS_JO5gH40a0bG_Lo3iy58KjCA8")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "5166878"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fdafb41f9a67f40e34a6c67f47730a92")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001646782459"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "762308466"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgresql://postgres:2zrUrlUsgFNC4ui4@db.gtpvgilwuybmlxkhmapi.supabase.co:5432/postgres")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001733156427"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first} I store private files in @TVHD10 Channel and users can access it from special link.")
try:
    ADMINS=[762308466 1825540060]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}<b> You need to join @TVHD10 to use me Kindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
