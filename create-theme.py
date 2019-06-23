import sys
import os.path

CLASS_NAME = "Colors" # Insert your class name here...
FILE_NAME = "Theme.dart" # Insert your file name here...

# Contain names at [0] and colors at [1]
arrayColorsAndNames = []

# Flutter templates
startTemplate = "import 'package:flutter/material.dart';\n\n"
MaterialColorTemplate = "final MaterialColor {0} = MaterialColor({1}.{0}[500].value, {1}.{0});\n"
classTemplate = "\nclass {0}{{\n  {0}();\n"
colorMapTemplate = "\n  static const Map<int, Color> {0} = <int, Color>{{\n    500: Color(0xFF{1}),\n  }};\n"

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
            if(userInput.find(":") != -1):
                colors += userInput
            else:
                print("Try using: <color name>:<hex color code>")
                sys.exit()
        else:
            userInput = str(raw_input())
            if(userInput.find(":") != -1):
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


# Get all the colors Together
def getAllColorsMapTogether(colorString,colorMapString, flutterCode):
    index = 0
    while index < len(arrayColorsAndNames):
        nameFromIndex = arrayColorsAndNames[index][0]
        colorFromIndex = arrayColorsAndNames[index][1].lstrip("#")
        colorMapString += colorMapTemplate.format(nameFromIndex, colorFromIndex)

        colorString+= MaterialColorTemplate.format(nameFromIndex, CLASS_NAME)
        index += 1
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
    else:
        print("Couldn't create a {0} because it already has one in the current path.".format(FILE_NAME))

if __name__ == "__main__":
    init()
