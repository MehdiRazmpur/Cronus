from telethon import functions


class Account:
    def __init__(self, client):
        self.client = client

    def message(self, text, to='me'):
        self.client.send_message(to, text)

    def join(self, channel):
        result = self.client(functions.channels.JoinChannelRequest(
            channel=channel
        ))
        return result

    def left(self, channel):
        result = self.client(functions.channels.LeaveChannelRequest(
            channel=channel
        ))
        return result
