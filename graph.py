
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('accidents_2022.csv')
df.head()
# List of columns names
list(df.columns)

# Dataframe info : column name and types, null values, and memory usage.
df.info()
import numpy as np

# Apparently, there are not null values.
df.isnull().sum().any()
# False
# meaning there are not null values.

# replace Unknown with n.a
df.replace('Unknown',np.nan, inplace=True)

# Now, There are null values
df.isnull().sum().any()
# True

# Access number of null values using the .info() method.
df.info()

df.drop(['Drugs Involved','Stats Area','Suburb','LGA Name','Postcode','Area Speed','Position Type','Horizontal Align','Vertical Align','Other Feat','Road Surface','Moisture Cond','Weather Cond','DayNight','Crash Typr','Unit Resp','Entiity Code','CSEF Severity','Traffic Ctrl','DUI Involved','ACCLOC_X','ACCLOC_Y','UNIQUE_LOC'],axis=1 ,inplace=True)

# Columns after dropping.
df.columns

list(df.month.unique())
# ['October','September','December','July','May','June','January','April','March','November','February','August']

# Month names to int
month_to_int = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
# Convert month names into numbers
df['month'].replace(month_to_int,inplace=True)
df.date.dtypes
# dtype('<M8[ns]')
# Obtain new month names
list(df.month.unique())
df.rename(columns=lambda x:x.replace(' ','_').lower(), inplace=True)

accidents_hour_day = df.groupby([df['date'].dt.hour.rename('hour'),df['date'].dt.dayofweek.rename('day')]).count().date

accidents_hour_day.unstack().plot(kind='barh', figsize=(16,26))

# title and x,y labels
plt.legend(labels=[calendar.day_name[x] for x in range(0,7)],fontsize=16)
plt.title('Accidents in Australia',fontsize=20)
plt.xlabel('Number of accidents',fontsize=16)
plt.ylabel('Hour',fontsize=16);