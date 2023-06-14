import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from imblearn.over_sampling import SMOTE

# 데이터 가져오기
SS = pd.read_csv('data/SuperSpreader.csv')
S = pd.read_csv('data/Spreader.csv')
categorical_feature_names1 = [
                              "sex",
                              "age",
                             "country",
                             "province"
                             ]
# test데이터에서 범주형으로 만들어줄 컬럼 지정 (이 컬럼들은 test데이터에 있는 컬럼들)
categorical_feature_names2 = [
                              "sex",
                              "age",
                             "country",
                             "province"
                             ]

# 위의 컬럼들 범주형으로 변환
for var in categorical_feature_names1:
    SS[var] = SS[var].astype("category")
for var in categorical_feature_names2:
    S[var] = S[var].astype("category")

SS_features = SS[['sex', 'age', 'country', 'province', '7_avg_temp', '7_min_temp', '7_max_temp', '7_max_wind_speed', '7_avg_relative_humidity']]
SS_super = SS['bool']
S_features = S[['sex', 'age', 'country', 'province', '7_avg_temp', '7_min_temp', '7_max_temp', '7_max_wind_speed', '7_avg_relative_humidity']]
S_super = S['bool']
SS_X_train, SS_X_test, SS_y_train, SS_y_test = train_test_split(SS_features,SS_super,test_size=0.5,random_state=42)
S_X_train, S_X_test, S_y_train, S_y_test = train_test_split(S_features,S_super,test_size=0.5,random_state=42)

X_train = pd.concat([SS_X_train, S_X_train])
print(X_train.head())
X_test = pd.concat([SS_X_test, S_X_test])
y_train = pd.concat([SS_y_train, S_y_train])
print(y_train.head())
y_test = pd.concat([SS_y_test, S_y_test])
smote = SMOTE(ratio = 0.3, random_state=42)

X_train_over,y_train_over = smote.fit_resample(X_train,y_train)
X_train_over = pd.DataFrame(X_train_over, columns=['sex', 'age', 'country', 'province', '7_avg_temp', '7_min_temp', '7_max_temp', '7_max_wind_speed', '7_avg_relative_humidity'])
y_train_over = pd.DataFrame(y_train_over, columns = ['bool'])
train = pd.concat([X_train_over, y_train_over],axis=1)
test = pd.concat([X_test, y_test],axis=1)
# train = pd.read_csv('./data/train.csv')
# test = pd.read_csv('./data/test.csv')

# 범주형으로 만들어줄 컬럼 지정 (이 컬럼들은 train데이터 안에 있는 컬럼들)
# categorical_feature_names1 = [
#                               "sex",
#                               "age",
#                              "country",
#                              "province"
#                              ]
# # test데이터에서 범주형으로 만들어줄 컬럼 지정 (이 컬럼들은 test데이터에 있는 컬럼들)
# categorical_feature_names2 = [
#                               "sex",
#                               "age",
#                              "country",
#                              "province"
#                              ]
#
# # 위의 컬럼들 범주형으로 변환
# for var in categorical_feature_names1:
#     train[var] = train[var].astype("category")
# for var in categorical_feature_names2:
#     test[var] = test[var].astype("category")

train.to_csv("train.csv")
test.to_csv("test.csv")

X_train = train.iloc[:, :-1].values
y_train = train.iloc[:, -1].values
X_test = test.iloc[:,:-1].values
y_test = test.iloc[:,-1].values



# 컬럼들 중 시행착오를 거쳐 최상의 성능을 보이는 조합의 컬럼들만 사용
feature_names = [
                    "sex",
                    "age",
                    "country",
                    "province",
                    "7_avg_temp",
                    "7_min_temp",
                    "7_max_temp",
                    "7_max_wind_speed",
                    "7_avg_relative_humidity",
                    # "count"
                 ]
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from keras import layers, models

# 각 레이어의 가중치와 바이어스를 초기화하는 옵션이 있음
# keras.initializers.RandomNormal(mean=0.0, stddev=0.05, seed=None)
# keras.initializers.RandomUniform(minval=-0.05, maxval=0.05, seed=None)

clf = models.Sequential([
    layers.Dense(units=16, kernel_initializer='uniform', input_dim=9, activation='relu'),
    layers.Dense(units=18, kernel_initializer='uniform', activation='relu'),
    # layers.Dropout(0.25),
    layers.Dense(5, kernel_initializer='uniform', activation='relu'),
    # layers.Dense(24, kernel_initializer='uniform', activation='relu'),
    layers.Dense(1, kernel_initializer='uniform', activation='sigmoid')
])

clf.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
clf.summary()

clf.fit(X_train, y_train, batch_size=50, epochs=10)
score = clf.evaluate(X_test, y_test, verbose=0)
print(clf.metrics_names)
print(score)