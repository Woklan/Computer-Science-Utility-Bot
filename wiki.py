import urllib.request
from bs4 import BeautifulSoup

# Function Finds which index we want to use
def wikiArray(content):
    for x in range(len(content)):
        if '.' in content[x]:
            return content[x]

def wikiSearch(searchInput):
    apiUrl = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles="
    userUrl = "https://en.wikipedia.org/wiki/"

    titleSearch = ""

    returnDataArray = []

    userSearchSplit = searchInput.split(" ")

    # Prepares the User Search to be placed into URL's
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

    # Grabs the page from the wikipedia API, and prepares for operation
    pageObject = urllib.request.urlopen(apiUrl)
    page = BeautifulSoup(pageObject, "lxml")
    stringPage = str(page)

    if "\",\"missing\"" in stringPage:
        returnDataArray.append("This page cannot be found...")
        return returnDataArray
    elif "may refer to" in stringPage:
        returnDataArray.append("This has returned a page for you to select which one you want, please be more specific in your search...")
        return returnDataArray
    elif "may also refer to" in stringPage:
        returnDataArray.append("This has returned a page for you to select which one you want, please be more specific in your search...")
        return returnDataArray
    else:
        # Grabs main paragraph, cutting away extra html
        stringPageSplit = stringPage.split("{")

        stringPage = wikiArray(stringPageSplit)

        stringPageSplit = stringPage.split("}")

        stringPage = wikiArray(stringPageSplit)

        stringPageSplit = stringPage.split('":"')

        stringPage = wikiArray(stringPageSplit)

        stringPage = stringPage[:-1]

        charCount = 0
        reformat = stringPage.split(".")

        formattedParagraph = ""


        # Keeps on placing sentances until one goes over the limit
        for x in range(len(reformat)):
            charCount = charCount + len(reformat[x]) + 2

            if charCount < 1024:
                formattedParagraph = formattedParagraph + reformat[x] + '. '

        returnDataArray.append(formattedParagraph)
        return returnDataArray
