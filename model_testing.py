
import pickle
import pandas as pd
import numpy as np


model_name = 'model.sav'

test = pd.read_csv('test/test.csv', index_col=0)

y = np.array(test.pop('target'))
X = np.array(test)

model = pickle.load(open(model_name, 'rb'))
result = model.score(X, y)
print(result)
