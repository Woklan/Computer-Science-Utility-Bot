import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

        if message.content.startswith('$cipher'):
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

            await message.channel.send(''.join(fin))

        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('Your Discord Key')
