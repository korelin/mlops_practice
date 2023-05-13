import pickle
import pandas as pd
#from sklearn.metrics import r2_score


pkl_filename = 'pickle_model.pkl'

with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

df = pd.read_csv('./test/test.csv',
                 sep='\t',
                 encoding='utf-8',
                 usecols=['A', 'B', 'C', 'Y'])

test_y = df['Y']
test_X = df.drop('Y', axis=1)

#predict = pickle_model.predict(test_X)

#r2 = r2_score(test_y, predict)
score = pickle_model.score(test_X, test_y)

print("Model test accuracy is: {0:.2f} %".format(100 * score))
#print("Model test r2_score: {0:.2f} %".format(100 * r2))
