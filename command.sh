#!/bin/bash
function create-theme(){
	PATH_FOLDER=$PWD
    NUMBER_OF_COLORS=$1
    if [ -n "$NUMBER_OF_COLORS" ]
    then
        python $PATH_FOLDER/create-theme.py $NUMBER_OF_COLORS $PWD
    else
        echo "Try using: create-theme <number of colors>"
    fi
}
