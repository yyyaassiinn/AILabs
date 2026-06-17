import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
df = pd.read_csv(r'C:\Users\Yassin\Downloads\Fish.csv')
print(df.head())

df['Species'] = df['Species'].astype('category').cat.codes

x = df.drop('Species',axis = 1)
y = df[['Species']]
X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size = 0.2, random_state=42)
model = SVC()
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)

print(accuracy_score(Y_test, Y_pred))