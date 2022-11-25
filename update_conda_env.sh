#!/bin/bash

ENV_NAME=$1
FILE_NAME=$2

echo "Env name: " $ENV_NAME
echo "File name: " $file

read -p "Do you want to proceed? [y/n] " yn

case $yn in 
	y ) echo ok, we will proceed;;
	n ) echo exiting...;
		exit;;
	* ) echo invalid response;
		exit 1;;
esac

conda deactivate
conda env remove --name $ENV_NAME 
conda env create --name $ENV_NAME --file=$FILE_NAME

conda activate $ENV_NAME
conda env export --no-builds > environment.yml
