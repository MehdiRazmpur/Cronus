from telethon import functions


class ChannelModel:
    def __init__(self, client, message):
        self.client = client
        self.message = message

    async def comment(self, text):
        discussion = await self.client(functions.messages.GetDiscussionMessageRequest(
            peer=self.message.peer_id.channel_id,
            msg_id=self.message.id
        ))
        discussion = discussion.messages[0]

        await self.client.send_message(discussion.peer_id, text, reply_to=discussion.id)
