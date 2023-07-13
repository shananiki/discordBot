import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        channel = message.channel
        channel_id = message.channel.id

        print(message)

        if message.author.id == self.user.id:
            return


        if channel.name == 'Allgemein':
            if message.attachments:
                for attachment in message.attachments:
                    if any(attachment.filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif']):
                        await attachment.save(attachment.filename)
                        print(f'Saved image: {attachment.filename}')
                        await client.get_channel(channel_id).send("I got that picture saved!!!")


        if message.content.startswith('!hello'):
            print("We received a message: {0}".format(message.content))
            await message.reply('Hello!', mention_author=True)


intents = discord.Intents.default()
intents.message_content = True

with open("token.txt") as f:
    token = f.read()

client = MyClient(intents=intents)
client.run(token=token)