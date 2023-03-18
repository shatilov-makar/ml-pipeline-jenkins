import pickle
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

train = pd.read_csv('train/train.csv', index_col=0)

y = np.array(train.pop('target'))
X = np.array(train)

logreg = LogisticRegression(random_state=42)
logreg.fit(X, y)


model_name = 'model.sav'
pickle.dump(logreg, open(model_name, 'wb'))
