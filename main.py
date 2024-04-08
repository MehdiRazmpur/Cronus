# Welcome to Cronus V1
# Cronus published with MIT license
# You can find documentation hear: https://github.com/MehdiRazmpur/Cronus

from telethon.sync import events
from Cronus.config import client
from Cronus.App.event_handler import EventHandler
from Cronus.Controllers.bootstrap import Bootstrap

Handle = EventHandler()
bootstrap = Bootstrap(client)

with client:

    bootstrap.bootstrap()

    # Forwarding Events for Process
    @client.on(events.NewMessage)
    async def new_message(event):
        await Handle.new_message(event)

    @client.on(events.Album)
    async def new_album(event):
        await Handle.new_album(event)
    # End

client.start()
client.run_until_disconnected()

