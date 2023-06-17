import os
from typing import Optional

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def create_data(n_samples: int, noise: int = 0, random_state: Optional[int] = None) -> pd.DataFrame:
    np.random.seed(random_state)
    X = np.linspace(0, 2 * np.pi, n_samples)
    y = np.sin(X) + noise * np.random.normal(0, 1, n_samples)
    return pd.DataFrame({'X': X, 'y': y})


if __name__ == '__main__':

    n_samples = 365
    n_datasets = int(os.getenv('DATASETS_NUMBER'))
    noise_frac = 0.1
    n_anomalies = int(n_samples * 0.05)

    data_sets = [create_data(n_samples, noise=noise_frac, random_state=n) for n in range(n_datasets)]
    anomalies = np.random.choice(len(data_sets[-1]), size=n_anomalies, replace=False)
    data_sets[-1].loc[anomalies, 'y'] = data_sets[-1].loc[anomalies, 'y'] ** 2

    for i, data in enumerate(data_sets):
        train, test = train_test_split(data, test_size=0.2, random_state=i)

        os.makedirs('train', exist_ok=True)
        os.makedirs('test', exist_ok=True)

        train.to_csv(f'train/{i}.csv', index=False)
        test.to_csv(f'test/{i}.csv', index=False)
