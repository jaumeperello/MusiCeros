from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")


load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

USE_DB = bool(getenv("USE_DB", "False"))
DB_HOST = getenv("DB_HOST")
DB_NAME = getenv("DB_NAME")
DB_USER = getenv("DB_USER")
DB_PASS = getenv("DB_PASS")


#extra things

BOT_USERNAME = "[bot username without @]"
BOT_NAME = "[ bot name ]"
