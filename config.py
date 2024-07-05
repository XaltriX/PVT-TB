#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/YukkiChatBot >.
#
# This file is part of < https://github.com/TeamYukki/YukkiChatBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiChatBot/blob/master/LICENSE >
#
# All rights reserved.
#

from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", "24955235"))
API_HASH = getenv("API_HASH", "f317b3f7bbe390346d8b46868cff0de8")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "5720319337:AAH2DWngyxymYf4MvfC8-hEuq6jsCIL0X_U")

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("SUDO_USER", "1837294444").split())
)  # Input type must be interger

# ADMIN USERS
ADMIN_USER = list(
    map(int, getenv("ADMIN_USER", "1837294444").split())
)  # Input type must be interger

# Message to display when someone starts your bot
PRIVATE_START_MESSAGE = getenv(
    "PRIVATE_START_MESSAGE",
    "Hello! Welcome to NeonGhost Feedback Bot, Send feedback about our bots here",
)
