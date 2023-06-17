import pickle

import pandas as pd
from sklearn.metrics import accuracy_score

if __name__ == '__main__':
    X_test = pd.read_csv('./model/X_test.csv', index_col=0)
    y_test = pd.read_csv('./model/y_test.csv', index_col=0).squeeze()

    with open('./model/model.pkl', 'rb') as f:
        clf = pickle.load(f)

    predictions = clf.predict(X_test[clf.feature_names_in_])

    print('Accuracy:', accuracy_score(y_test, predictions))
