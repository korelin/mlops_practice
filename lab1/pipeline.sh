#!/bin/bash
python3 -m pip install -r requirements.txt
python3 data_creation.py
python3 data_preprocessing.py
python3 model_preparation.py
python3 model_testing.py
