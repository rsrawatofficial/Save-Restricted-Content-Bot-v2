# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "28771159"))
API_HASH = getenv("API_HASH", "a6ff05d5e26feb62d29eea1c411a15b9")
BOT_TOKEN = getenv("BOT_TOKEN", "7703810356:AAGSlmJeIXBbTiWCt0okoyPH4C3EdRenUXU")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7967446224").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://rsrasasingh:FS2G9YbI28KbPHLC@cluster0.yljr3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002502765617")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002502765617"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
