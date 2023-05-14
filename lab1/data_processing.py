import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess_df(df: pd.DataFrame) -> pd.DataFrame:
    '''Проводим предобработку данных (чистка Nan и стандартизация)'''
    df = df.dropna()

    scaler = StandardScaler()
    df = scaler.fit_transform(df)
    df = pd.DataFrame(df, columns=train.columns)

    return df


train = pd.read_csv('./train/train.csv', sep='\t', encoding='utf-8',
                    usecols=['A', 'B', 'C', 'Y'])

train = preprocess_df(train)
train.to_csv('./train/train.csv', sep='\t', encoding='utf-8', index=False)

test = pd.read_csv('./test/test.csv', sep='\t', encoding='utf-8',
                   usecols=['A', 'B', 'C', 'Y'])

test = preprocess_df(test)
test.to_csv('./test/test.csv', sep='\t', encoding='utf-8', index=False)
