#!/bin/bash
function create-theme(){
	PATH_FOLDER=~/Development/Desktop/Python/FlutterCustomColors
    python $PATH_FOLDER/create-theme.py $1 $PWD
}