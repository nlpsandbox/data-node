#!/usr/bin/with-contenv bash

if [ ! -d "/data" ]
then
    echo "Downloading dataset files from Synapse"

    mkdir /data

    # Download the data from Synapse
    # python tools/main.py get-data

    # python main.py get-data
fi