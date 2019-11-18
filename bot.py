import discord
import json
import datetime

# All commands used
import BinaryModifications
import binXor
import binAnd
import binOr
import ceaser
import wiki
import nasa
import urbanDictionary

# Grabs Discord Token from config.json
with open("config.json") as config_json:
    configDictionary = json.load(config_json)

discordToken = configDictionary["discord_token"]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):

        # Doesn't reply to itself
        if message.author == self.user:
            return

        # Prints the line out when a user uses command
        if message.content.startswith('$'):
            print('User {0.author} used the following command: {0.content}'.format(message))

        # Simple Hello Reply
        if message.content.startswith('$hello '):
            await message.channel.send('Hello World!')

        if message.content.startswith('$urban '):
            userMessage = message.content[7:]
            test = urbanDictionary.urbanSearch(userMessage)

            if test == 0:
                await message.channel.send("This page doesn't exist or work lmao")
            else:
                embed = discord.Embed(title = test[0], description = test[1], color = 0x00ff00)
                embed.add_field(name = "Info", value = test[3], inline = False)
                embed.add_field(name = "Quote", value = test[2], inline = False)
                await message.channel.send(embed = embed)

        if message.content.startswith('$nasa '):

            # Used to handle command changes based on user input
            command_handle = 0

            userMessage = message.content[6:]

            if '/' in userMessage and 'hd' in userMessage:
                command_handle = 1
            elif '/' in userMessage:
                command_handle = 2
            elif 'hd' in userMessage:
                command_handle = 3

            print('System (1/3) - User Command has been recieved')
            test = nasa.nasaApod(command_handle, userMessage)

            # Determines which message to send based on data recived
            if test == 0:
                await message.channel.send('There has been an error! Please check your inputs...')
            elif test[0] == 'image':
                embed = discord.Embed(title = test[3], description = test[1], color = 0x00ff00)
                embed.add_field(name = "Info", value = test[2], inline = False)
                embed.set_image(url = test[1])
                await message.channel.send(embed = embed)

            elif test[0] == 'video':
                embed = discord.Embed(title = test[3], description = test[1], color = 0x00ff00)
                embed.add_field(name="Info", value = test[2], inline = False)
                await message.channel.send(embed = embed)

            print("System (3/3) - User Command has successfully been handled!")

        # A Ceaser Cipher
        if message.content.startswith('$cipher '):
            fin = ceaser.ceaserCipher(message)
            await message.channel.send(''.join(fin))

        # Binary AND/OR/XOR
        if message.content.startswith('$binary '):
            userMessage = message.content[7:].split() # Grabs data from user
            test = BinaryModifications.binaryPrep(message, userMessage)
            if test != 0:
                # BUG:: Would place the join's in the message.channel command, but Discord recieves the message twice
                andBinary = ''.join(binAnd.binaryAnd(test))
                orBinary = ''.join(binOr.binaryOr(test))
                xorBinary = ''.join(binXor.binaryXor(test))
                await message.channel.send('The Results Are: ```NUM1: ' + test[0] + '\nNUM2: ' + test[1] + '\n -------------------' + '\nAND: ' + andBinary + '\nOR: ' + orBinary + '\nXOR: ' + xorBinary + '```')
            else:
                await message.channel.send('There has been an error! Please check your inputs...')

        # Searches Wikipedia for article
        if message.content.startswith('$wiki '):
            userMessage = message.content[6:]
            test = wiki.wikiSearch(userMessage)

            embed = discord.Embed(title=test[0], description=test[1], color=0x00ff00)
            embed.add_field(name="Info", value=test[2], inline=False)
            await message.channel.send(embed=embed)

client = MyClient()
client.run(discordToken)
