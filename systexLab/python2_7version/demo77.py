#encoding=UTF-8
import pandas as pd
data = pd.read_csv('data\\data4.csv')
print data.columns
print data.head()
group1 = data[['處分字號','違反勞動基準法條款','違反法規內容']].groupby(['違反勞動基準法條款','違反法規內容']).count()
sorted_group1 = group1.sort_values('處分字號',ascending=False)
print sorted_group1.head(n=30)