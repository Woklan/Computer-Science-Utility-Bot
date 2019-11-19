from ExtraFunctions import pageGet
import json
import requests
import datetime
import time

'''
TODO ------------------------------
- Handle if the user selects HD, but there is no hdUrl
- Handle if the user selects date below the date limit
'''

def nasaApod(command_handle, userMessage):
    url = "https://api.nasa.gov/planetary/apod?"

        # If the user wants a specific date
    if command_handle == 1 or command_handle == 2:
        charCommand = userMessage.split(" ")
        day, month, year = str(charCommand[0]).split("/")

        # Handles if a user imputted a 2 digit year (1/1/19 rather than 1/1/2019)
        if len(year) == 2:
            year = "20" + year


        # Checks if the date is in the correct format
        isValidDate = True

        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        if (isValidDate == False):
            return 0

        # Checks if the date is in the future

        userDate = str(day) + '/' + str(month) + '/' + str(year)
        currentDay = str(datetime.date.today().day)
        currentMonth = str(datetime.date.today().month)
        currentYear = str(datetime.date.today().year)
        currentDate = currentDay + '/' + currentMonth + '/' + currentYear

        formattedUserDate = time.strptime(userDate, "%d/%m/%Y")
        formattedCurrentDate = time.strptime(currentDate, "%d/%m/%Y")

        if(formattedUserDate > formattedCurrentDate):
            return 0

        # Handles updating the API URL with the date
        url = url + "date=" + str(year) + "-" + str(month) + "-" + str(day)
        if command_handle == 1:
            # Handles updating the API URL with the HD Tag
            url = url + '&hd=True&'
        else:
            url = url + '&'

    # If user just wanted HD, but didn't select a date (auto chooses today)
    elif command_handle == 0 or command_handle == 3:
        today = datetime.date.today()
        url = url + 'date=' + str(today) + "&"

        if command_handle == 3:
            url = url + '&hd=True&'

    # Adds on our API Key
    with open("config.json") as config_json:
        configDictionary = json.load(config_json)

    nasaToken = configDictionary["nasa_token"]

    url = url + 'api_key=' + nasaToken
    print(url)

    # [stringPage, datastore]
    dataArray = pageGet(url)
    if dataArray == 0:
        return 0
    else:
        datastore = dataArray[1]

    # Chooses which URL to select
    if command_handle == 1 or command_handle == 3:
        url = datastore["hdurl"]
    else:
        url = datastore["url"]


    # Grabs necessary Data
    dataType = datastore["media_type"]
    content = datastore["explanation"]

    returnDataArray = []

    print("System (2/3) - System has recieved Nasa API page successfully!")

    returnDataArray.append(dataType)

    # Handles if data we are reciveing is a JPG or Youtube video
    if dataType == "image":
        img_data = requests.get(url).content
        with open('nasa_image.jpg', 'wb') as handler:
            handler.write(img_data)
        returnDataArray.append(url)

    elif dataType == "video":
        returnDataArray.append(datastore["url"])


    # Breaks the content up into sentances and keeps inserting until a sentance would go over the limit (discord limitations on messages)
    reformat = content.split(".")
    charCount = 0
    formattedParagraph = ""

    for x in range(len(reformat)):
        charCount = charCount + len(reformat[x]) + 2

        if charCount < 1024:
            formattedParagraph = formattedParagraph + reformat[x] + '. '

    # Returns relevant data
    returnDataArray.append(formattedParagraph)
    returnDataArray.append(datastore["title"])

    # Returns --> [DataType, URL, Content, Title]
    return returnDataArray
