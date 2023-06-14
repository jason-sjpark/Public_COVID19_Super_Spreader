import pandas as pd
data=pd.read_csv("PatientInfo_수정_날씨 추가.csv", encoding='cp949')

data['sex'] = [1 if (s=='male') else 0 for s in data['sex']]

#0s: 0, 10s: 1, 20s: 2,... 100s: 10으로 치환
data.replace('10s',1,inplace=True)
data.replace('20s',2,inplace=True)
data.replace('30s',3,inplace=True)
data.replace('40s',4,inplace=True)
data.replace('50s',5,inplace=True)
data.replace('60s',6,inplace=True)
data.replace('70s',7,inplace=True)
data.replace('80s',8,inplace=True)
data.replace('90s',9,inplace=True)
data.replace('100s',10,inplace=True)
data.replace('0s',0,inplace=True)

#Korea면 1, Korea가 아니면 0으로 치환
data.replace('Korea',1,inplace=True)
data.replace('Bangladesh',0,inplace=True)
data.replace('Canada',0,inplace=True)
data.replace('China',0,inplace=True)
data.replace('France',0,inplace=True)
data.replace('Germany',0,inplace=True)
data.replace('Indonesia',0,inplace=True)
data.replace('Mongolia',0,inplace=True)
data.replace('Spain',0,inplace=True)
data.replace('Switzerland',0,inplace=True)
data.replace('Thailand',0,inplace=True)
data.replace('United Kingdom',0,inplace=True)
data.replace('United States',0,inplace=True)
data.replace('Vietnam',0,inplace=True)
data.replace('Foreign',0,inplace=True)
#print(data)

#province치환
data.replace('Seoul',0,inplace=True)
data.replace('Busan',1,inplace=True)
data.replace('Daegu',2,inplace=True)
data.replace('Gwangju',3,inplace=True)
data.replace('Incheon',4,inplace=True)
data.replace('Daejeon',5,inplace=True)
data.replace('Ulsan',6,inplace=True)
data.replace('Sejong',7,inplace=True)
data.replace('Gyeonggi-do',8,inplace=True)
data.replace('Gangwon-do',9,inplace=True)
data.replace('Chungcheongbuk-d',10,inplace=True)
data.replace('Chungcheongnam-do',11,inplace=True)
data.replace('Chungcheongbuk-do',12,inplace=True)
data.replace('Jeollabuk-do',13,inplace=True)
data.replace('Jeollanam-do',14,inplace=True)
data.replace('Gyeongsangbuk-do',15,inplace=True)
data.replace('Gyeongsangnam-do',16,inplace=True)
data.replace('Jeju-do',17,inplace=True)

data.to_csv('Data범주화.csv', encoding='cp949')



