#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("API_ID", "10000844", cast=int)
API_HASH = config("API_HASH", "776f257fc1d1f8aa4aea9dd35d10a45b")
BOT_TOKEN = config("BOT_TOKEN", "7395932935:AAFxSqwIZkTTdosHWGEfipS9u1nuG54ZfZY")
SESSION = config("SESSION", "BQCYmcwAqrKNkxcHi8R9hR05aSXpHrKs87NUOudJzZhGZag1eE-pUCMuQxh1gZBzakmeiYsEr9wiPhsc8_AVEEXaGQFjmgTB6vlijXCA5ucSc3hCI8gob3o8By9yJuFqRzkrJjE_orNO074SI6s04UC797FOzb_8KYDv0Ty01-aBioE0tbye1SiVmCAZQoz94CQqk6oSDGWGO2rO773xNWGMki67OBPkAgV9YC80zI7OPLImIclkLfwRZnGeTCjjoxMce9ZeRhzwjGuzOHrMxxZindherrbyQka_k8qODaLveSiEeKmIHRkmhhHBCSivsREQ1u1veBSmidRA61o_lE2jlBZ0QQAAAAE7-5OBAA")
FORCESUB = config("FORCESUB", "funnyzilla")
AUTH = config("AUTH", "6750546542")
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
