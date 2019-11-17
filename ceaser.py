def ceaserCipher(message):
    
    preUserInput = message.content[8:] # Snips the call-tag off the string

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
