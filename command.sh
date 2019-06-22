#!/bin/bash
function create-theme(){
	PATH=~/Development/Desktop/Python/FlutterCustomColors
    python $PATH/create-theme.py $1 $PWD
}