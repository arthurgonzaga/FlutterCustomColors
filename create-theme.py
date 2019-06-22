import sys
import os.path

CLASS_NAME = "Colors" # Insert your class name here...
FILE_NAME = "Theme.dart" # Insert your file name here...

# Contain names at [0] and colors at [1]
arrayColorsAndNames = []

# Flutter templates
startTemplate = "import 'package:flutter/material.dart';\n\n"
classTemplate = "class {0}{{\n  {0}();\n"
colorTemplate = "\n  static const Map<int, Color> {0} = <int, Color>{{\n    500: Color(0xFF{1}),\n  }};\n"

# All the colors templates together from the array
colorString = ""

# The final flutter code
flutterCode = ""

# Current path
path = str(sys.argv[2])

# Call all the functions
def init():
    askColors()
    getAllColorsTogether(colorString, flutterCode)

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
            colors += str(raw_input()) 
        else:
            colors += str(raw_input()+ ",")
        index += 1
    splitArrayByString(colors)

    
# This function split what the user typed in the shell command to an array
def splitArrayByString(string):
    splittedArray = string.split(",")
    for splittedIndex in splittedArray:
        arrayColorsAndNames.append(splittedIndex.split(":"))


# Get all the colors Together
def getAllColorsTogether(colorString, flutterCode):
    index = 0
    while index < len(arrayColorsAndNames):
        nameFromIndex = arrayColorsAndNames[index][0]
        colorFromIndex = arrayColorsAndNames[index][1].lstrip("#")
        colorString += colorTemplate.format(nameFromIndex, colorFromIndex)
        index += 1
    createFlutterCode(colorString, flutterCode)

# Get all the templates together 
def createFlutterCode(colorString, flutterCode):
    flutterCode = startTemplate + classTemplate.format(CLASS_NAME) + colorString + "}"
    createFile(flutterCode)

# Create the Dart file
def createFile(string):
    if(os.path.isfile(FILE_NAME) != True):
        flutterFile = open(FILE_NAME, "a+")
        flutterFile.write(string)
        flutterFile.close()

if __name__ == "__main__":
    init()
