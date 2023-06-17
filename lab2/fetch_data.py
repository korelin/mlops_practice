from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split


if __name__ == '__main__':
    phoneme = fetch_openml('phoneme', parser='liac-arff', version=1)
    X_train, X_test, y_train, y_test = train_test_split(
        phoneme['data'], phoneme['target'], test_size=0.2, random_state=42)

    X_train.to_csv('./data/X_train.csv')
    X_test.to_csv('./data/X_test.csv')
    y_train.to_csv('./data/y_train.csv')
    y_test.to_csv('./data/y_test.csv')
