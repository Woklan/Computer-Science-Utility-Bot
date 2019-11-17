import discord
import json

# All commands used
import BinaryModifications
import binXor
import binAnd
import binOr
import ceaser
import wiki

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
