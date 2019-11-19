from ExtraFunctions import URLFormat, pageGet, displayFormatting

'''
TODO --------------------------------
- Handle Disambiguation Pages
'''

def wikiSearch(searchInput):
    apiUrl = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles="
    userUrl = "https://en.wikipedia.org/wiki/"

    returnDataArray = []

    # [Title, apiUrl, userUrl]
    returnArray = URLFormat(searchInput, apiUrl, userUrl)

    returnDataArray.append(returnArray[0])
    returnDataArray.append(returnArray[2])

    # [stringPage, datastore]
    returnArray = pageGet(returnArray[1])
    stringPage = returnArray[0]
    datastore = returnArray[1]

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
        data = list(datastore["query"]["pages"].values())[0]["extract"]

        returnDataArray.append(displayFormatting(data))
        return returnDataArray
