from ExtraFunctions import URLFormat, pageGet, displayFormatting

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

    returnDataArray = []

    # [Title, apiUrl, userUrl]
    returnArray = URLFormat(searchInput, apiUrl, userUrl)

    returnDataArray.append(returnArray[0])
    returnDataArray.append(returnArray[2])

    # [stringPage, datastore]
    returnArray = pageGet(returnArray[1])
    datastore = returnArray[1]

    if len(datastore["list"]) == 0:
        return 0

    # Grabs necessary data and makes them go under the 1024 limit
    data = datastore["list"][0]["definition"]
    quote = datastore["list"][0]["example"]

    returnDataArray.append(displayFormatting(quote))
    returnDataArray.append(displayFormatting(data))

    # Returns --> [Title, URL, Quote, Content]
    return returnDataArray
