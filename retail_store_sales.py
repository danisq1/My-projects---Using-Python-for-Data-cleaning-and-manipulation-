# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 19:08:01 2023

@author: danis
"""

import pandas as pd

# file_name = pd.read_csv('file.csv')  <-------format of read_csv


data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

#summary of the data
data.info()

#working with calculations

# Defining variables 

CostPerItem = 11.73

SellingPricePerItem = 21.11

NumberOfItemsPurchased = 6 

#Mathematical Operations in Pyton

ProfitPerItem = 21.11 - 11.73

ProfitPerItem = SellingPricePerItem - CostPerItem 

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem 
CostPerTransaction = CostPerItem * NumberOfItemsPurchased
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased

#CostPerTransaction Column Calculation 

#CostPerTransaction = CostPerItem * NumberOfItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']

NumberOfItemsPurchased = data['NumberOfItemsPurchased']

CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#adding a new column to a dataframe

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']


# Sales per Transaction 

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#Profit Calculation = Sales - Cost 

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction'] 

# Markup = (Sales - Cost) / Cost 

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

data['Markup'] = data['ProfitPerTransaction']  / data['CostPerTransaction']

#Rounding Markup

roundmarkup = round(data['Markup'] , 2)

data['Markup'] = round(data['Markup'] , 2)

#combining data fields 

my_name = 'danish' + 'Qayoom'

my_data = 'Day'+'-'+'Month'+'-'+'Year'


# checking colums data type 

print(data['Day'].dtype)


# Change colums type 

day = data ['Day'].astype(str)
year = data['Year'].astype(str)


print(day.dtype)
print(year.dtype)
       
       
my_date = day + '-' + data['Month']+'-' + year

data['date'] = my_date

#using iloc to view specific colums/rows 

data.iloc[0]  # views the row with index = 0 


data.iloc[0:3] #first 3 rows 


data.iloc[-5:] #last 5 rows 

data.head(5) #brings in first 5 rows 

data.iloc[:,2] # brings in all rows on 2nd column 

data.iloc[4,2] # brings in 4th row, 2nd column 

#using split to split the client keywords field 

# new_var = column.str.split('sep', expend = True)

split_col = data['ClientKeywords'].str.split(',' , expand=True)

#creating new columns for the split colums in Client Keywords 

data['ClientAge'] = split_col[0]

data['ClientType'] = split_col[1]

data['LenghtofContract'] = split_col[2]

#using the replace function 

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')

data['LenghtofContract'] = data['LenghtofContract'].str.replace(']' , '')

#using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()


# how to merge files 
# bringing in new dataset 

seasons = pd.read_csv('sales_analysis_seasons.csv', sep=';')

#merging file: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns 

#df = df.drop('columnname' , axis = 1)

data = data.drop('ClientKeywords' , axis = 1)

data = data.drop('Day', axis = 1)

#data = data.drop('Day', axis = 1)

data = data.drop(['Year', 'Month'],  axis = 1)

#data = data.drop(['Season_x', 'Season_y'],  axis = 1)

#export into a csv

data.to_csv('retail_store_sales_cleaned.csv' , index = False)









