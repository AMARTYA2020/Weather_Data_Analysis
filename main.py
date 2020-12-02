          # Contributer: Amartya Pandey

import pandas as pd
data = pd.read_csv(r"E:\Data_analysis\Weather Data analysis\Weather_Data.csv")
# print(data)  # This prints entire rows and columns present in the dataset
x = data.head()
#print(x)    #This by default displays first 5 rows
y = data.shape
print(y)
z = data.columns  #This will represent all the column/attribute fiels in tuple
print(z)
a = data.dtypes # This will represent all the datatypes of data in columns
print(a)
b = data['Weather'].unique() # This will represent all the unique items present in Weather attribute
print(b)
c = data.nunique() # This will represent the total number of unique values in each column/attribute
print(c)
d = data.info() # Provides basic acknowledgement of the given dataframe
print(d)

      # QUESTIONS AFTER ANALYZING THE ABOVE DATASETS::

# Q1). FIND ALL THE UNIQUE 'WIND SPEED' FROM THE GIVEN DATA FRAME :
# SOLUTION:
e = data['Wind Speed_km/h'].nunique()
print(e)


# Q2). FIND THE NUMBER OF TIMES WHEN THE 'WEATHER IS EXCATLY CLEAR' :
# SOLUTION:
f = data.Weather.value_counts()
print(f)
  # Basically there are two other ways to manipulate this :
  # 1). using filter  data[data.Weather == clear]       2). using groupby()     data.groupby('Weather').get_group('clear')


# Q3). FIND OUT THE VARIANCE OF 'Relative Humidity' in this dataset :
# SOLUTION:
j = data['Rel Hum_%'].var()
print(j)


# Q4). FIND THE NUMBER OF TIMES WHEN 'WIND SPEED WAS EXACTLY 4KM/H' :
#SOLUTION:
g = data['Wind Speed_km/h'] == 4
print(g)


# Q5). FIND OUT ALL THE NULL VALUES IN THE DATA :
#SOLUTION:
h = data.isnull()
print(h)


# Q6). Change the name of attribute "Weather" to "Weather condition" in the dataset:
#SOLUTION:
i = data.rename(columns= {'Weather':'Weather condition'},inplace=True)
print(i)
    # now we print the dataset upto 2 rows for confirmation of rename :)
I = data.head(2)
print(I)


# Q7). FIND OUT THE MEAN VALUE OF VISIBILITY ::
#SOLUTION:
k = data.Visibility_km.mean()
print(k)


# Q8). FIND OUT THE STANDARD DEVIATION OF 'Pressure' in the dataset:
#SOLUTION:
l = data.Press_kPa.std()
print(l)


# Q9).FIND OUT ALL THE INSTANCES WHEN 'Rain' was recorder:
#SOLUTION:
m = data[data['Weather condition']== 'Snow']  # if code is data['Weather condition']=='Snow' then output interms of T/F
print(m)


# Q10).FIND OUT ALL THE CONDITIONS WHEN 'weather is Clear' or 'Visibility is above 40':
#SOLUTION:
n = data[(data['Weather condition'] == 'Clear') | (data['Visibility_km'] > 40)]
print(n)


# Q11).FIND OUT ALL THE CONDITIONS WHEN 'Weather is clear' and 'Relative humidity is greater then 50':
#SOLUTION:
p = data[(data['Weather condition'] == 'clear') & (data['Rel Hum_%'] > 50)]
print(p)




