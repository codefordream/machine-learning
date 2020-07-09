import pandas as pd

#creating DataFrame 
data = {"Month":pd.Series(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]),
"Rainfall":pd.Series([1.05,3.22,14.2,8.2,4.5,1.05,3.22,14.2,8.2,4.5,4.2,1.2]),}
df = pd.DataFrame(data)

#read csv file
dfc = pd.read_csv(r'./rain.csv')
print(dfc)

#read json file
dfj = pd.read_json(r'./rain.json')
print(dfj)

#fill in the missing values (e.g., october)
dfzero = dfj.fillna(0) #fill the value by 0
print(dfzero)

#drop the row with missing values
dfclean = dfj.dropna(0)
print(dfclean)


#count the all rows containing Nans
count = 0
for i,row in dfj.iterrows():
    if any(row.isnull()):
        count +=1
print("\n Number of Nan row:" + str(count))

#calculate mean
print("\n Mean:"+ str(dfclean.mean())) #mean of all columns
print("\n Mean of Rainfall:"+ str(dfclean['Rainfall'].mean())) #mean of 'Rainfall' column
print("\n Mean of Rainfall and top three row:"+ str(dfclean['Rainfall'][0:3].mean())) #mean of 'Rainfall' column and top three row

#find median
print("\n Median:"+ str(dfclean.median())) #median of all columns
print("\n Median:"+ str(dfclean['Rainfall'].median())) #median of 'Rainfall' column

#calculate Standard Deviation
print("\n Standard Deviation:"+ str(dfclean.std())) #Standard Deviation of all columns
print("\n Standard Deviation:"+ str(dfclean['Rainfall'].std())) #Standard Deviation of 'Rainfall' column

#Data retrieval
#retrieve row by index using iloc
print(dfclean.iloc[4])

#set index column then use Month value to retrieve data of that month
dfindex = dfclean.set_index('Month')
print(dfindex.loc['Mar'])