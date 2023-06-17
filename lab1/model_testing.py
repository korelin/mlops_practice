import pickle
import pandas as pd
from sklearn.metrics import mean_squared_error

if __name__ == '__main__':

    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)

    test = pd.read_csv('test/scaled.csv')

    pred = model.predict(test[['X']])
    mse = mean_squared_error(test['y'], pred)

    print(f'Model test MSE is: {round(mse, 4)}')
