import os
import numpy as np
import pandas as pd


def data_generator(sample_size: int) -> pd.DataFrame:
    '''
    Создаем синтетический датасет
    '''
    np.random.seed(1)

    feature_A = 20 * np.random.randn(sample_size) + 100
    feature_B = 30 * np.random.randn(sample_size) + 200
    feature_C = 5 * np.random.randn(sample_size) + 20

    result = 2 * feature_A\
             + 8 * feature_B\
             + feature_C\
             + 25 * np.random.randn(sample_size) + 30

    df = pd.DataFrame(list(zip(feature_A, feature_B, feature_C, result)),
                      columns=['A', 'B', 'C', 'Y'])

    # Зашумляем какой-нибудь столбец Nan
    idx = np.random.randint(0, sample_size, round(sample_size * 0.1))

    df['A'].iloc[idx] = np.NaN

    return df


if not os.path.exists('./train'):
    os.makedirs('./train')

if not os.path.exists('./test'):
    os.makedirs('./test')

train_data = data_generator(10000)
train_data.to_csv('./train/train.csv', sep='\t', encoding='utf-8')

test_data = data_generator(1000)
test_data.to_csv('./test/test.csv', sep='\t', encoding='utf-8')
