#!/bin/bash

cd /app

if [ ! -f mlCloudDetect.ini ]; then
    echo "Error: config file not found!"
    exit 1
fi

if [ ! -f /data/keras_model.h5 -o ! -f /data/labels.txt ]; then
    echo "ERROR: model not found, you must download or train a model and place it in the ./data directory"
    exit 1
fi

python3 mlCloudDetect.py
