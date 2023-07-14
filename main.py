from io import BytesIO
import discord
from ImageLogger import *
from PIL import Image
from DatabaseHandler import *

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


        if channel.name == 'spam' or channel.name == 'general':
            if message.attachments:
                for attachment in message.attachments:
                    if any(attachment.filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
                        dest_extension = attachment.filename.split('.')[-1]
                        dest_filename = il.savePicture()

                        # shady file conversion
                        image_data = await attachment.read()
                        image = Image.open(BytesIO(image_data))
                        target_file_name = str("{0}.{1}".format(dest_filename, "png"))
                        image.save("images/" + target_file_name)
                        dh.addEntry(target_file_name, ".{0}".format(dest_extension))

                        # await client.get_channel(channel_id).send("I got that picture saved!!!")
                    if any(attachment.filename.lower().endswith(ext) for ext in ['.mp4', '.webm']):
                        dest_extension = attachment.filename.split('.')[-1]
                        dest_filename = il.savePicture()
                        target_file_name = str("{0}.{1}".format(dest_filename, dest_extension))
                        await attachment.save("images/" + target_file_name)
                        dh.addEntry(target_file_name, ".{0}".format(dest_extension))

        if message.content.startswith('!hello'):
            print("We received a message: {0}".format(message.content))
            await message.reply('Hello!', mention_author=True)


intents = discord.Intents.default()
intents.message_content = True

with open("token.txt") as f:
    token = f.read()
il = ImageLogger()
dh = DatabaseHandler()
dh.setServerURL("{YOURSERVERURL}")
dh.setDBFile("images.db")
client = MyClient(intents=intents)
client.run(token=token)
