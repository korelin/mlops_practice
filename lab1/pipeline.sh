#!/bin/bash
scriptdir="$( dirname -- "$BASH_SOURCE"; )";

pip install tensorflow Pillow

python3 "$scriptdir/data_creation.py" > /dev/null 2>&1
python3 "$scriptdir/data_preprocessing.py" > /dev/null 2>&1
python3 "$scriptdir/model_preparation.py" > /dev/null 2>&1
python3 -W ignore "$scriptdir/model_testing.py" 2>/dev/null | grep 'Model test accuracy is'