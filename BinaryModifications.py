    # Prepares String for And/Or/XOR etc.
def binaryPrep(message, userMessage):
    updatedBinary = ['', '']

    if len(userMessage) < 2:
        print(userMessage)
        print("YEEEE")
        return 0

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
