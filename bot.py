import discord
import json

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

        # Simple Hello Reply
        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

        # A Ceaser Cipher
        if message.content.startswith('$cipher'):
            fin = MyClient.ceaserCipher(message)
            await message.channel.send(''.join(fin))

        # ANDs two binary inputs from the user
        if message.content.startswith('$and'):
            userMessage = message.content[5:].split()
            test = MyClient.binaryPrep(message, userMessage)
            if test != 0:
                finalBinary = MyClient.binaryAnd(test)
                await message.channel.send('The binary AND equals ```' + ''.join(finalBinary) + '```')
            else:
                await message.channel.send('There has been an error! Please check your inputs...')

        # ORs two binary inputs from the user
        if message.content.startswith('$or'):
            userMessage = message.content[4:].split()
            test = MyClient.binaryPrep(message, userMessage)
            if test != 0:
                finalBinary = MyClient.binaryOr(test)
                await message.channel.send('The binary OR equals ```' + ''.join(finalBinary) + '```')
            else:
                await message.channel.send('There has been an error! Please check your inputs...')

        if message.content.startswith('$'):
            print('User {0.author} used the following command: {0.content}'.format(message))


    def binaryOr(updatedBinary):
        finalBinary = []

        for x in range(len(updatedBinary[0])):
            if updatedBinary[0][x] == '1' or updatedBinary[1][x] == '1':
                finalBinary.append('1')
            else:
                finalBinary.append('0')

        return finalBinary


    def binaryAnd(updatedBinary):
        finalBinary = []

        for x in range(len(updatedBinary[0])):
            if updatedBinary[0][x] == '1' and updatedBinary[1][x] == '1':
                finalBinary.append('1')
            else:
                finalBinary.append('0')

        return finalBinary


        # Prepares String for And/Or/XOR etc.
    def binaryPrep(message, userMessage):
        updatedBinary = ['', '']
        binary1 = userMessage[0]
        binary2 = userMessage[1]

        #Verifys the string's are binary
        for x in range(len(binary1)):
            if binary1[x] != '0' and binary1[x] != '1':
                return 0

        for x in range(len(binary2)):
            if binary2[x] != '0' and binary2[x] != '1':
                return 0

        # Longifies the Strings
        if len(binary1) > len(binary2):
            temp = len(binary1) - len(binary2)

            for x in range(temp):
                updatedBinary[0] += '0'

            for x in range(len(binary2)):
                updatedBinary[0] += binary2[x]

            updatedBinary.insert(0, binary1)

        elif len(binary1) < len(binary2):
            temp = len(binary2) - len(binary1)

            for x in range(temp):
                updatedBinary[0] += '0'

            for x in range(len(binary1)):
                updatedBinary[0] += binary1[x]

            updatedBinary.insert(1, binary2)


        else:
            updatedBinary.insert(0, binary1)
            updatedBinary.insert(1, binary2)

        return updatedBinary

    def ceaserCipher(message):
        # Snips the call-tag off the string
        preUserInput = message.content[8:]

        fin = []

        userInput = preUserInput.upper()

        for x in range(len(userInput)):
            if userInput[x] != ' ':
                tempInt = ord(userInput[x]) + 5

                if tempInt > 90:
                    tempInt = tempInt - 26

                fin.append(chr(tempInt))
            else:
                fin.append(' ')

        return fin

client = MyClient()
client.run(discordToken)
