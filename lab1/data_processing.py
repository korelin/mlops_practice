import pandas as pd


def delete_NaNs(df: pd.DataFrame) -> pd.DataFrame:
    '''Чистим датафрейм от Nanов'''

    return df.dropna()


train = pd.read_csv('./train/train.csv',
                    sep='\t',
                    encoding='utf-8',
                    usecols=['A', 'B', 'C', 'Y'])

train = delete_NaNs(train)

train.to_csv('./train/train.csv',
             sep='\t',
             encoding='utf-8')

test = pd.read_csv('./test/test.csv',
                   sep='\t',
                   encoding='utf-8',
                   usecols=['A', 'B', 'C', 'Y'])

test = delete_NaNs(test)

test.to_csv('./test/test.csv',
            sep='\t',
            encoding='utf-8')
