class ChannelController:
    def __init__(self, event):
        self.event = event

    async def post(self, channel):
        await channel.comment('test')
