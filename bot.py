from credentials import token, fromChannel, toChannels
import discord


class Client(discord.Client):
    async def send_messages(self, key, message):
        channels = toChannels[key]
        for channelID in channels:
            channel = self.get_channel(channelID)
            print("Sending to " + channel.name +" in " + channel.guild.name)
            await channel.send(message)

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.channel.id == fromChannel:
            parts = message.content.split(":")
            keys = toChannels.keys()
            for key in keys:
                if parts[0] == key:
                    await self.send_messages(key, ":".join(parts[1:]))
                    return
            await self.send_messages("general", message.content)

client = Client()
client.run(token, bot=False)