import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer

train = pd.read_csv("titanic/train.csv")
test = pd.read_csv("titanic/test.csv")
imputer = SimpleImputer()
imputedTrain = imputer.fit_transform(train)
train = train.dropna()
test = test.dropna()
print(train.head())

y = train["Survived"]

features = ["Pclass", "Sex", "Age", "SibSp", "Parch"]
X = pd.get_dummies(train[features])
X_test = pd.get_dummies(test[features])

model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test.PassengerId, 'Survived': predictions})
output.to_csv('submission.csv', index=False)
print("Your submission was successfully saved!")