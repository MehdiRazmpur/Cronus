from telethon import functions
from Cronus.Controllers.Events.channel import ChannelController
from Cronus.App.Models.CHANNEL import ChannelModel


class EventHandler:
    def __init__(self):
        self.last_album_comment = 0

    async def new_message(self, event):
        channel = ChannelController(event)

        if event.is_channel and event.message.post:
            if event.grouped_id is None:

                message = event.message
                channel_model = ChannelModel(event.client, message)
                await channel.post(channel_model)

        elif event.is_group:
            pass

        elif event.is_private:
            pass

    async def new_album(self, event):
        channel = ChannelController(event)
        message = event.messages[0]
        if message.post:
            if self.last_album_comment != message.grouped_id:
                self.last_album_comment = message.grouped_id

                channel_model = ChannelModel(event.client, message)
                await channel.post(channel_model)
