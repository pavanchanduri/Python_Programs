import pandas as pd

## Series
##A Pandas Series is a one-dimensional array-like object that 
# can hold any data type. It is similar to a column in a table.
data=[1,2,3,4,5, "Test", (1,2,3,4)]
series=pd.Series(data)
print("Series \n",series)
print(type(series))

## Create a Series from dictionary
data={'a':1,'b':2,'c':3}
series_dict=pd.Series(data)
print(series_dict)

## Map data with a given index to form a series
data=[10,20,30]
index=['a','b','c']
series_mapped=pd.Series(data,index=index)
print(series_mapped)

## Dataframe
## create a Dataframe from a dictionary of list
data={
    'Name':['Krish','John','Jack'],
    'Age':[25,30,45],
    'City':['Bangalore','New York','Florida']
}
df=pd.DataFrame(data)
print(df)
print(type(df))

## Dataframe from list of dictionaries
data = [
    {'Name':'Krish', 'Age':25, 'City':'Bangalore'},
    {'Name':'John', 'Age':30, 'City':'New York'},
    {'Name':'Jack', 'Age':45, 'City':'Florida'}
]
df=pd.DataFrame(data)
print(df)
print(type(df))
print(df.columns)  # Display column names
print(df.loc[0])  # Display first row
print(df.iloc[2])  # Display second row
print(df.at[2, 'Name']) # Display Name of third row
df['Salary'] = [50000, 60000, 70000] ## Add Salary column
print(df)

## Remove a column
df.drop('Salary',axis=1,inplace=True)
print(df)

#Remove row
df.drop(0,axis=0,inplace=True)
print(df)


## Read data from csv
df = pd.read_csv('src/sales_data.csv')
print(df.head(5))  # Display first 5 rows
print(df.tail(5))  # Display last 5 rows
print(df['Product Category'].head(5)) # Display first 5 rows of 'Product Category' column

# Display the data types of each column
print("Data types:\n", df.dtypes)

# Describe the DataFrame
print("Statistical summary:\n", df.describe())