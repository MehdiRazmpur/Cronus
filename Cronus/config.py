from telethon.sync import TelegramClient


SESSION = 'name'
api_id = 0
api_hash = ''
device_model = 'Samsung SM-A516V'
system_version = 'SDK 34'
app_version = '10.9.2'


client = TelegramClient(
    session=f'Cronus/App/Storage/Sessions/{SESSION}',
    api_id=api_id,
    api_hash=api_hash,
    device_model=device_model,
    system_version=system_version,
    app_version=app_version,
)
