import numpy as np
import pandas as pd

df = pd.read_csv('../datasets/churn_dataset.csv')

print("********* base function in python ************")
# index of the Tabular data
print(df.index)

# columns of the Tabular data
print(df.columns)
# both axis, columns of the Tabular data
print (df.axes)

# values of the each row in list as 2d (tabular data)
print(df.values)
#  cols abd datatypes
print(df.dtypes)
#  return df of selected datatypes, which is float
print(df.select_dtypes(float))
print(df.info())
print(df.describe())
print(df.describe().loc['min', ])
print(df.describe().loc['min', ]['Total Spend'])
print(df)
df = df.convert_dtypes()
print(df.info())

# deep copy
dfc = df.copy()
# retrives first 20 rows of the data frame
df_20 = df.head(20)

print(df_20)

print("********* base function in python ************")

print ("************ The ways of adding and deleting -columns in df********* START")
df_20.insert(2,"custid" ,range(100,100+len(df_20)))
print(df_20)
df_20.drop(columns=['custid'],inplace=True)
print(df_20)
df_20['custid'] = range(100,100+len(df_20))
print(df_20)
df_20.pop('custid')
print(df_20)

df_20['2x_Spend'] = 2 * df_20.loc[:,'Total Spend']
print(df_20)

df_20['3x_Spend']= df['Total Spend'].apply(lambda x : x*3)
print(df_20)

df_20 = df_20.assign(FiveX_Spend = lambda x : x['2x_Spend'] + x['3x_Spend'])
print(df_20)

df_20['customer_type'] = 'invester'
print (df_20)

df_20.drop(columns = ['customer_type','FiveX_Spend','3x_Spend','2x_Spend'], inplace=True)
print (df_20)

print ("************ The ways of adding and deleting -columns in df********* END")