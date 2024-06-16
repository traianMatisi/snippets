#! /usr/bin/bash

# read with -prompt "this is a prompt" variable1 variable2
read -p "Hi, who'r'you? " name surname
# input are separated by white-spaces

echo "Hello, $name $surname ..."

echo $BASH
echo $BASH_VERSION
echo $HOME
echo $PWD
echo $? # "return value" variable