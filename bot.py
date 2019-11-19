import discord
import json

# All commands used
from ExtraFunctions import binaryPrep
import binXor
import binAnd
import binOr
import ceaser
import wiki
import nasa
import urbanDictionary
import subnet

# Grabs Discord Token from config.json
with open("config.json") as config_json:
    configDictionary = json.load(config_json)

discordToken = configDictionary["discord_token"]

class MyClient(discord.Client):
    subnetFlag = False
    subnetHold = []
    subnetCount = 4

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print(message.content)

        # Prints the line out when a user uses command
        if message.content.startswith('$'):
            print('User {0.author} used the following command: {0.content}'.format(message))

        # Simple Hello Reply
        if message.content.startswith('$hello '):
            await message.channel.send('Hello World!')


            # Handles the Extra Printing of the Subnetting Command
        if message.author == self.user and MyClient.subnetFlag == True:
            if len(MyClient.subnetHold) > MyClient.subnetCount:
                MyClient.subnetCount = MyClient.subnetCount + 1
                await message.channel.send("```" + MyClient.subnetHold[MyClient.subnetCount - 1] + "```")
            else:
                MyClient.subnetFlag = False
                MyClient.subnetHold = []
                MyClient.subnetCount = 3

        # Doesn't reply to itself
        if message.author == self.user:
            return

        # Subnets to as many subnetworks as you may like
        if message.content.startswith('$subnet '):
            userMessage = message.content[8:]
            test = subnet.subnetting(userMessage)
            if len(test) > 5:
                MyClient.subnetFlag = True
                MyClient.subnetHold = test
                MyClient.subnetCount = MyClient.subnetCount + 1
                await message.channel.send("```# of subnets: " + str(test[1]) + "\n# of Hosts per Subnet: " + str(test[2]) + '\nSubnetMask: ' + str(test[3]) + "\nClass: " + str(test[4]) + '\n ------------------------------------------------------- \n' + "```")
            else:
                await message.channel.send("```# of subnets: " + str(test[1]) + "\n# of Hosts per Subnet: " + str(test[2]) + "\nSubnetMask: " + str(test[3]) + "\nClass: " + str(test[4]) + '\n ------------------------------------------------------- \n' + test[5] + "```")

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
            test = binaryPrep(message, userMessage)
            if test != 0:
                await message.channel.send('The Results Are: ```NUM1: ' + test[0] + '\nNUM2: ' + test[1] + '\n -------------------' + '\nAND: ' + ''.join(binAnd.binaryAnd(test)) + '\nOR: ' + ''.join(binOr.binaryOr(test)) + '\nXOR: ' + ''.join(binXor.binaryXor(test)) + '```')
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
