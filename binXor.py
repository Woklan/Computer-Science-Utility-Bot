def binaryXor(updatedBinary):
    finalBinary = []

    for x in range(len(updatedBinary[0])):
        if updatedBinary[0][x] == '1' and updatedBinary[1][x] == '0' or updatedBinary[0][x] == '0' and updatedBinary[1][x] == '1':
            finalBinary.append('1')
        else:
            finalBinary.append('0')

    return finalBinary
