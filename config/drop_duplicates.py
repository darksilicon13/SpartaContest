import pandas as pd
df=pd.read_csv('20220513PlayList.csv')
df1=df['채널명'].unique()
df.drop_duplicates(subset='썸네일',inplace=True)
df['채널명']=df1
print(df)