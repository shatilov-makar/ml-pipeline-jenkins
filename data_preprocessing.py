from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import os

PATH = "https://raw.githubusercontent.com/aksenov7/Kaggle_competition_group/master/adult.data.csv"
df = pd.read_csv(PATH)

if (not os.path.exists("train")):
    print("Folder 'train' was created")
    os.mkdir("train")

if (not os.path.exists("test")):
    print("Folder 'test' was created")
    os.mkdir("test")

columns = df.select_dtypes(include=(int, float)).columns

df[columns] = StandardScaler().fit_transform(df[columns])


X = df.select_dtypes(include=(int, float))
y = df.salary.apply(lambda salary: 0 if salary == '<=50K' else 1)

train, test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True, stratify=y)

train['target'] = y_train
test['target'] = y_test

train.to_csv('train/train.csv', sep=',')
test.to_csv('test/test.csv', sep=',')
