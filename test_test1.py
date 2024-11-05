#import unittest
#import test1 as t
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# date = np.array(['t','r','e','w'])
# myseries=pd.Series(date,index= [ 10,20,30,40])
# print(myseries[30])

# date= {'first':'ali', 'sec':'mari', 'thired':'sara'}
# ser=pd.Series(date,index=['a','b','c'])
# print(ser)
# date_1=pd.Series([20,3,4,5],index=['a','b','c','f'])
# date_2=pd.Series([6,3,52,28],index=['a','b','c','f'])
# print(date_1.add(date_2))
# print(date_1.sub(date_2))
# print(date_1.mul(date_2))
# print(date_1.div(date_2))
# print(date_1.pow(date_2))
#loc , iloc
# print(myseries.iloc[0])
# print(myseries.loc[10])
# mylist=['e','r','r']
# df= pd.DataFrame(mylist)
# print(df)
# date={'name':['ali','reza','hosein'],'age':[25,20,35]}
# df=pd.DataFrame(date)
# print(df)
# date={'name':['ali',np.nan,'reza'],'age':[20,30,32], 'city':['theran','karaj',np.nan],'teching':['pandas','numpy','scipy']}


# df=pd.DataFrame(date)
# print(df[df['age']==30])
 #isnull , notnull
# print(df.fillna(0))
# dropna
# print(df.dropna())

# df=pd.read_csv('./file.csv')
# print(df)
# import os
# print("Current Directory:", os.getcwd())
# df = pd.read_csv('pythonhome/file.csv')
# print(df)
#read_csv , read_exel , read_html . ExcellFilePorse(), to_csv
# print(df.shape)
# print(df.count())
# print(type(df.values))
# print(df.describe())
# print(df.set_index('maryam'))
# mysort=df.sort_values('maryam',axis=0,inplace=False,ascending=True,na_position='last')
# print(mysort)
# df['20'].plot()
# plt.show()
# df_1=pd.DataFrame({'name':['ali','omid','hamid'],'gread': [20,19,36],'qulity':['low','mid','high']})


# df_2=pd.DataFrame({'name':['zahra','sara','hamid'],'gread': [60,35,18],'qulity':['high','mid','low']})


# df_3=pd.DataFrame({'name':['ali','sara','hamid'],'gread': [49,89,399],'emil':['teset1','teset2','teset3']})

# print(pd.merge(df_1,df_2,on='name'))
# df_1.set_index('name',inplace=True)

# df_3.set_index('name',inplace=True)


# myjoin=df_1.join(df_3,lsuffix='_left')
# print(myjoin)

#outer inner left

# merge=pd.merge(df_1,df_2,on='name',how='outer')
# merge.set_index('name',inplace=True)
# print(merge)

# mygp=df.groupby('maryam')



# print(mygp.groups)
# print(df)
# def myfunc(self):
#     return df.loc[self].maryam>df.loc[self].karaj
# print(df.groupby(myfunc).groups)
# print(mygp['20'].agg(np.mean))
# for maryam,group in mygp:
#     print('maryam')
#     print(group)
# getgp=mygp.get_group('sara')
# print(getgp)
# print(pd.concat([df_1,df_2]))
# print(pd.to_datetime('2019-05-15 3:45pm'))
# print(pd.to_datetime(['2019-02-09','2010-05-08']))
# print(pd.to_datetime('2/25/10', format='%m/%d/%y'))