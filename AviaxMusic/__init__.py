import config
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from AviaxMusic.core.bot import Aviax, Bad
from AviaxMusic.core.dir import dirr
from AviaxMusic.core.git import git
from AviaxMusic.core.userbot import Userbot
from AviaxMusic.misc import dbb, heroku

from .logging import LOGGER

#time zone
TIME_ZONE = pytz.timezone(config.TIME_ZONE)
scheduler = AsyncIOScheduler(timezone=TIME_ZONE)


dirr()
git()
dbb()
heroku()

app = Aviax()
Bad = Bad()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
HELPABLE = {}
