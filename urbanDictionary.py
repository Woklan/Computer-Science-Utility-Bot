import urllib.request
from bs4 import BeautifulSoup
import json

'''
TODO --------------------------------------
- Extend Pages to complete story
- Make hyperlinks in stories clickable on discord
- Fix Formatting
- Add Random Pages
'''

def urbanSearch(searchInput):
    apiUrl = "http://api.urbandictionary.com/v0/define?term="
    userUrl = "https://www.urbandictionary.com/define.php?term="

    titleSearch = ""

    returnDataArray = []

    userSearchSplit = searchInput.split(" ")

    for x in range(len(userSearchSplit)):
        word = userSearchSplit[x]
        capWord = str(word).capitalize()

        titleSearch = titleSearch + capWord
        apiUrl = apiUrl + capWord
        userUrl = userUrl + capWord

        if len(userSearchSplit) > x + 1:
            apiUrl = apiUrl + "%20"
            userUrl = userUrl + "%20"

            titleSearch = titleSearch + " "

    returnDataArray.append(titleSearch)
    returnDataArray.append(userUrl)

    pageObject = urllib.request.urlopen(apiUrl)
    page = BeautifulSoup(pageObject, "lxml")
    stringPage = str(page)[15:-18]

    if "</had></a>" in stringPage:
        stringPage = stringPage[:-10]

        # Urban Dictionary's Api holds some broken JSON Files
    try:
        datastore = json.loads(stringPage)
    except:
        return 0

    if len(datastore["list"]) == 0:
        return 0
    else:
        # Grabs necessary data and makes them go under the 1024 limit
        data = datastore["list"][0]["definition"]
        quote = datastore["list"][0]["example"]

        reformat = data.split(".")
        charCount = 0
        formattedParagraph = ""

        for x in range(len(reformat)):
            charCount = charCount + len(reformat[x]) + 2

            if charCount < 1024:
                formattedParagraph = formattedParagraph + reformat[x] + '. '

        reformat = quote.split(".")
        charCount = 0
        formattedQuote = ""

        for x in range(len(reformat)):
            charCount = charCount + len(reformat[x]) + 2

            if charCount < 1024:
                formattedQuote = formattedQuote + reformat[x] + ". "


    returnDataArray.append(formattedQuote)
    returnDataArray.append(formattedParagraph)

    # Returns --> [Title, URL, Quote, Content]
    return returnDataArray
