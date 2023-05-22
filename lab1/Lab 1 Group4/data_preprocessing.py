#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# %% Импорт
import sys
import argparse
import sklearn
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler


scaler = StandardScaler()
def transforms(data,data_path,name):
    """
    Обработка данных и сохранение их в новый файл
    """
    file_path = ""
    try:
        dt = pd.read_csv(data, sep=',')
        file_path = ""
        print(scaler.fit(dt))
        StandardScaler(copy=True, with_mean=True, with_std=True)
        print(scaler.mean_)
        print(scaler.transform(dt))   
        file_path = name + 'trans'+'.csv'
        data.to_csv(file_path, index=False)
        return data

    except:
        print(f"Ошибка сохранения файла {file_path}")
        return None
