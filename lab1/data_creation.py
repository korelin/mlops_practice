import os
import numpy as np
import pandas as pd


def data_generator(sample_size: int) -> pd.DataFrame:
    '''Создаем синтетический датасет'''

    feature_A = 20 * np.random.randn(sample_size) + 100
    feature_B = 30 * np.random.randn(sample_size) + 200
    feature_C = 5 * np.random.randn(sample_size) + 20

    result = 2 * feature_A \
             + 8 * feature_B \
             + feature_C \
             + 25 * np.random.randn(sample_size) + 30

    df = pd.DataFrame({
        'A': feature_A,
        'B': feature_B,
        'C': feature_C,
        'Y': result})

    # Зашумляем какой-нибудь столбец Nan
    idx = np.random.randint(0, sample_size, round(sample_size * 0.1))
    df.loc[idx, 'A'] = np.NaN

    return df


os.makedirs('./train', exist_ok=True)
train_data = data_generator(10000)
train_data.to_csv('./train/train.csv', sep='\t', encoding='utf-8', index=False)

os.makedirs('./test', exist_ok=True)
train_data = data_generator(1000)
train_data.to_csv('./test/test.csv', sep='\t', encoding='utf-8', index=False)
