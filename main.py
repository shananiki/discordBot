from io import BytesIO
import discord
from ImageLogger import *
from PIL import Image

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


        if channel.name == 'spam':
            if message.attachments:
                for attachment in message.attachments:
                    if any(attachment.filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
                        dest_extension = attachment.filename.split('.')[-1]
                        dest_filename = il.savePicture()

                        # shady file conversion
                        image_data = await attachment.read()
                        image = Image.open(BytesIO(image_data))

                        image.save("images/" + str("{0}.{1}".format(dest_filename, "png")))

                        # await client.get_channel(channel_id).send("I got that picture saved!!!")


        if message.content.startswith('!hello'):
            print("We received a message: {0}".format(message.content))
            await message.reply('Hello!', mention_author=True)


intents = discord.Intents.default()
intents.message_content = True

with open("token.txt") as f:
    token = f.read()
il = ImageLogger()
client = MyClient(intents=intents)
client.run(token=token)
