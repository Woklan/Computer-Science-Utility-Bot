def subnetting(userInput):
'''
PLEASE NOTE: THIS CODE IS EARLY DEVELOPMENT, AND WILL BE REFACTORED TO BE MORE STREAMLINED. MORE OR LESS ME THROWING AROUND A COUPLE IDEAS

# TODO:
- Handle VLSM
- Fix Class Bug
- Refactor Code to Streamline
'''


    returnDataArray = []

    intUserInput = int(userInput)

    returnDataArray.append(intUserInput)

    MagicNum = [128, 64, 32, 16, 8, 4, 2, 1]
    Networking = [0, 2, 6, 14, 30, 62, 126, 256]
    Hosts = [128, 64, 32, 16, 8, 4, 2, 0]
    Class = ["/25", "/26", "/27", "/28", "/29", "/30", "/31", "/32"]

    ip = "192.168."
    SubnetMask = "255.255.255."
    thirdOctet = 1

    finIp = ip + str(thirdOctet) + '.'

    count = -1
    found = False
    while found == False:

        count = count + 1


        if Networking[count] >= intUserInput:
            index = count
            found = True

    returnDataArray.append(Networking[index])
    returnDataArray.append(Hosts[index])
    returnDataArray.append(Class[index])

    count = 0
    subMaskCalc = 0
    while count <= index:
        subMaskCalc = subMaskCalc + MagicNum[count]
        count = count + 1


    SubnetMask = SubnetMask + str(subMaskCalc)

    Network = 0 - MagicNum[index]
    count = 1

    for x in range(intUserInput):
        Network = Network + MagicNum[index]

        if Network + 31 > 255:
            Network = 0
            thirdOctet = thirdOctect + 1
            finIp = ip + str(thirdOctet) + '.'

        fullNetwork = finIp + str(Network)

        Range = finIp + str(Network + 1) + ' - ' + finIp + str(Network + MagicNum[index] - 2)

        Broadcast = finIp + str(Network + MagicNum[index] - 1)

        returnDataArray.append(count)
        returnDataArray.append(fullNetwork)
        returnDataArray.append(Range)
        returnDataArray.append(Broadcast)

        count = count + 1

    stringHelper = []

    stringHelper.append(intUserInput)
    stringHelper.append(Networking[index])
    stringHelper.append(Hosts[index])
    stringHelper.append(SubnetMask)
    stringHelper.append(Class[index])

    bigBoi = ""

    print(len(returnDataArray))
    print("\n\n\n\n\n\n\n\n")

    testing = 4
    for x in range(returnDataArray[0]):
        bigBoi = bigBoi + str(returnDataArray[testing]) + '.\n ------------------------------------------------------- \nNetwork: ' + str(returnDataArray[testing + 1]) + '\nRange: ' + str(returnDataArray[testing + 2]) + '\nBroadcast: ' + str(returnDataArray[testing + 3]) + '\n' + '------------------------------------------------------- \n'
        testing = testing + 4
        if len(bigBoi) + 220 > 2000:
            print("E: " + bigBoi)
            stringHelper.append(bigBoi)
            bigBoi = ""

    stringHelper.append(bigBoi)

    count = 5
    while count < len(returnDataArray):
        print("E: " + str(returnDataArray[count]))
        count = count + 1
    #for x in range(len(returnDataArray)):
    #    print(len(returnDataArray[x]))

    print(stringHelper)
    return stringHelper
