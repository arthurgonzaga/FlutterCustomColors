import sys
import os.path
import requests
from bs4 import BeautifulSoup
import re

CLASS_NAME = "Colors" # Insert your class name here...
FILE_NAME = "Theme.dart" # Insert your file name here...

# Contain names at [0] and colors at [1]
arrayColorsAndNames = []

# Flutter templates
startTemplate = "import 'package:flutter/material.dart';\n\n"
MaterialColorTemplate = "final MaterialColor {0} = MaterialColor({1}.{0}[500].value, {1}.{0});\n"
classTemplate = "\nclass {0}{{\n  {0}();\n"
colorMapTemplate = "\n  static const Map<int, Color> {0} = <int, Color>{{\n    50: Color(0xFF{1}),\n    100: Color(0xFF{2}),\n    200: Color(0xFF{3}),\n    300: Color(0xFF{4}),\n    400: Color(0xFF{5}),\n    500: Color(0xFF{6}),\n    600: Color(0xFF{7}),\n    700: Color(0xFF{8}),\n    800: Color(0xFF{9}),\n    900: Color(0xFF{10}),\n  }};\n"

# All the colorsMap templates together from the array
colorMapString = ""

# All the colors templates together from the array
colorString = ""

# The final flutter code
flutterCode = ""

# Current path
path = str(sys.argv[2])

# Call all the functions
def init():
    askColors()
    getAllColorsMapTogether(colorString, colorMapString, flutterCode)

def isHex(string):
    return re.search(r'(?:[0-9a-fA-F]{3}){1,2}$', string)

# Ask colors to the user
def askColors():
    try:
        numberOfColors = int(sys.argv[1])
    except ValueError:
        print('This is not a number')
        sys.exit()
    colors = ''
    index = 0
    while(index < numberOfColors):
        if(index+1 == numberOfColors):
            userInput = str(raw_input())
            if(userInput.find(":") != -1 and isHex(userInput)):
                colors += userInput
            else:
                print("Try using: <color name>:<hex color code>")
                sys.exit()
        else:
            userInput = str(raw_input())
            if(userInput.find(":") != -1  and isHex(userInput)):
                colors += userInput + ","
            else:
                print("Try using: <color name>:<hex color code>")
                sys.exit()
        index += 1
    splitArrayByString(colors)

    
# This function split what the user typed in the shell command to a two-dimensional array
def splitArrayByString(string):
    splittedArray = string.split(",")
    for splittedIndex in splittedArray:
        arrayColorsAndNames.append(splittedIndex.split(":"))

# This functions get color hex from the website: https://www.htmlcsscolor.com/
def getColorShadeFromWeb(color):
    r = requests.get("https://www.htmlcsscolor.com/hex/{0}".format(color))
    soup = BeautifulSoup(r.text, "html.parser")
    statusCode = r.status_code
    if(statusCode == 200):
        colorShades = []
        for colorbox in soup.find_all(class_="colorbox"):
            colorHex = str(colorbox.find("a").string)
            colorShades.append(colorHex.lstrip("#"))
        # Reversing the array to get life easier
        colorShades.reverse()
        var1 = colorShades[5:11]
        colorShades.reverse()
        var2 = colorShades[1:6]
        return var1 + var2
    else:
        print("Error {0}".format(statusCode))

# Get all the colors Together
def getAllColorsMapTogether(colorString,colorMapString, flutterCode):
    index = 0
    while index < len(arrayColorsAndNames):
        nameFromIndex = arrayColorsAndNames[index][0]
        colorFromIndex = arrayColorsAndNames[index][1].lstrip("#")
        colorShades = getColorShadeFromWeb(colorFromIndex)
        try:
            colorMapString += colorMapTemplate.format(nameFromIndex, colorShades[0], colorShades[1],
                colorShades[2], colorShades[3], colorShades[4], colorShades[5],
                colorShades[6], colorShades[7], colorShades[8], colorShades[9])
            colorString += MaterialColorTemplate.format(nameFromIndex, CLASS_NAME)
            index += 1
            print(nameFromIndex+ u"\u2714".encode('utf8'))
            pass
        except IndexError:
            print(nameFromIndex+ u"\u2716".encode('utf8'))
            os.exit()
            pass
    createFlutterCode(colorString, colorMapString, flutterCode)

# Get all the templates together 
def createFlutterCode(colorString, colorMapString, flutterCode):
    flutterCode = startTemplate + colorString + classTemplate.format(CLASS_NAME) + colorMapString + "}"
    createFile(flutterCode)

# Create the Dart file
def createFile(string):
    if(os.path.isfile(FILE_NAME) != True):
        flutterFile = open(FILE_NAME, "a+")
        flutterFile.write(string)
        flutterFile.close()
        print("{0} created successfully".format(FILE_NAME))
    else:
        print("Couldn't create a {0} because it already has one in the current path.".format(FILE_NAME))

if __name__ == "__main__":
    init()