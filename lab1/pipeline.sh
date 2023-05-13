#!/bin/bash

pip install pandas
pip install numpy
pip install scikit-learn

python3 data_creation.py
python3 data_processing.py
python3 model_preparation.py
python3 model_testing.py
