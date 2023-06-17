from pathlib import Path

import pandas as pd
from sklearn.preprocessing import StandardScaler


if __name__ == '__main__':

    train_datasets = [f.name for f in Path('train').iterdir() if f.name.endswith('.csv')]
    test_datasets = [f.name for f in Path('test').iterdir() if f.name.endswith('.csv')]
    common_datasets = set(train_datasets).intersection(test_datasets)

    train = pd.concat([pd.read_csv(f'train/{dataset}') for dataset in common_datasets], axis=1)
    test = pd.concat([pd.read_csv(f'test/{dataset}') for dataset in common_datasets], axis=1)

    scaler = StandardScaler()
    train_scaled = pd.DataFrame(scaler.fit_transform(train), columns=train.columns)
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns)

    train_scaled.to_csv('train/scaled.csv', index=False)
    test_scaled.to_csv('test/scaled.csv', index=False)
