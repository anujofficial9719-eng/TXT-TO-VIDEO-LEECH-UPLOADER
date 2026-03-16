

from os import environ

API_ID = int(environ.get("API_ID", "34724970"))
API_HASH = environ.get("API_HASH", "f240eae7c60e8e30c17203ab0e052f7e")
BOT_TOKEN = environ.get("BOT_TOKEN", "8656231605:AAGVZvUNt7VJiqq1r7MT_wbhCLO229ztU2I")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "bot_subscription")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/log_channel_anuj")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "7521421400").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "7521421400"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")





