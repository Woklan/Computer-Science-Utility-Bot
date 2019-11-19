import json
import urllib.request
from bs4 import BeautifulSoup

'''
TODO -----------------------------------
- Update Module to handle American Time, so it doesn't run into error
'''

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

def pageGet(URL):
    returnData = []
    pageObject = urllib.request.urlopen(URL)

    page = BeautifulSoup(pageObject, "lxml")
    stringPage = str(page)[15:-18]

    returnData.append(stringPage)

    try:
        datastore = json.loads(stringPage)
    except:
        return 0

    returnData.append(datastore)
    return returnData


def URLFormat(userInput, apiUrl, userUrl):
    returnArray = []

    titleSearch = ""

    userSearchSplit = userInput.split(" ")

    for x in range(len(userSearchSplit)):
        word = userSearchSplit[x]
        capWord = str(word).capitalize()

        titleSearch = titleSearch + capWord
        apiUrl = apiUrl + capWord
        userUrl = userUrl  + capWord

        if len(userSearchSplit) > x + 1:
            apiUrl = apiUrl + "%20"
            userUrl = userUrl + "%20"

            titleSearch = titleSearch + " "

    returnArray.append(titleSearch)
    returnArray.append(apiUrl)
    returnArray.append(userUrl)

    # Returns --> [Title, apiURL, userURL]
    return returnArray

def displayFormatting(data):
    reformat = data.split(".")
    charCount = 0
    formattedParagraph = ""

    for x in range(len(reformat)):
        charCount = charCount + len(reformat[x]) + 2

        if charCount < 1024:
            formattedParagraph = formattedParagraph + reformat[x] + '. '

    return formattedParagraph
