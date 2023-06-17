import pickle

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFpr


if __name__ == '__main__':
    X_train = pd.read_csv('./data/X_train.csv', index_col=0)
    y_train = pd.read_csv('./data/y_train.csv', index_col=0).squeeze()

    feature_selector = SelectFpr().set_output(transform='pandas')
    X_train = feature_selector.fit_transform(X_train)

    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)

    with open('./model/model.pkl', 'wb') as f:
        pickle.dump(clf, f)
