from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('./전처리 최종완료.csv')

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=1)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


model = LogisticRegression()
model.fit(X_train, Y_train)
print(model.score(X_train, Y_train))
print(model.score(X_test, Y_test))