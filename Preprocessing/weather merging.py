import pandas as pd

df= pd.read_csv('./data/edit_Weather2020.csv')
df2 = pd.read_csv('./data/PatientInfo_수정.csv')
for i in range(len(df2)):
    for j in range(len(df)):
        if (df.iloc[j,1] == df2.iloc[i,4]) and (df.iloc[j,2] == df2.iloc[i,5]):
            df2.iloc[i, 7] = df.iloc[j, 3]
            df2.iloc[i, 8] = df.iloc[j, 4]
            df2.iloc[i, 9] = df.iloc[j, 5]
            df2.iloc[i, 10] = df.iloc[j, 6]
            df2.iloc[i, 11] = df.iloc[j, 7]
            df2.iloc[i, 12] = df.iloc[j, 8]
            df2.iloc[i, 13] = df.iloc[j, 9]
            break

df2.to_csv('PatientInfo_수정_날씨 추가.csv')