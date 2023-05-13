import pandas as pd
from sklearn.preprocessing import StandardScaler

def delete_NaNs(df: pd.DataFrame) -> pd.DataFrame:
    '''Чистим датафрейм от Nanов'''

    return df.dropna()

train = pd.read_csv('./train/train.csv',
                    sep='\t',
                    encoding='utf-8',
                    usecols=['A', 'B', 'C', 'Y'])
train = delete_NaNs(train)

scaler = StandardScaler ()
train_scaler = scaler.fit_transform(train)
train_scaler_df = pd.DataFrame(train_scaler, columns=train.columns)

train_scaler_df.to_csv('./train/train.csv', sep='\t', encoding='utf-8', index=False)

test = pd.read_csv('./test/test.csv',
                    sep='\t',
                    encoding='utf-8',
                    usecols=['A', 'B', 'C', 'Y'])
test = delete_NaNs(test)

scaler = StandardScaler ()
test_scaler = scaler.fit_transform(test)
test_scaler_df = pd.DataFrame(test_scaler, columns=test.columns)

test_scaler_df.to_csv('./test/test.csv', sep='\t', encoding='utf-8', index=False)