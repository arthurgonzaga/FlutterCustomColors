### Install: 
```bash
git clone "https://github.com/arthurgonzaga/FlutterCustomColors.git"
cd FlutterCustomColors
```
Open command.sh in a text editor and change the PATH_FOLDER variable to this project folder
```
...
PATH_FOLDER=~/path/to/FlutterCustomColors
...
```
Then type the following command:
```bash
source ~/command.sh
```
>You can find how to make the command available in the Terminal [here](https://medium.com/devnetwork/how-to-create-your-own-custom-terminal-commands-c5008782a78e#b79f).
>
Then go to create-theme.py and set the CLASSNAME and FILENAME if you want.

```python
CLASS_NAME = "Colors" # Insert your class name here...
FILE_NAME = "Theme.dart" # Insert your file name here...
```

### Usage:
To run the script type in:
```bash
create-theme <number of colors>
```

Then:
```bash
<colorname>:<HEX>
```
<<<<<<< HEAD
>**This will generate a dart code from your current path**
=======
>This will generate a dart code from your current path 
>>>>>>> 8f84bf0d5a93cd5a67d4a795859349217204423d
