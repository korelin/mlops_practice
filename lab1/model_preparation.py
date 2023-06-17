import pickle

import pandas as pd
from sklearn.linear_model import LinearRegression

if __name__ == '__main__':
    train = pd.read_csv('train/scaled.csv')
    model = LinearRegression()
    model.fit(train[['X']], train['y'])

    with open('model.pkl', 'wb') as file:
        pickle.dump(model, file)
