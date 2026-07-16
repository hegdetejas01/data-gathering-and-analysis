### Importing Data from various methods ###
import pandas as pd
import numpy as np

filepath = '../numpy-pandas-learning/datasets/'

""" Comma Saperated Values - CSV """

# Fetching from local machine
df1 = pd.read_csv(filepath+'movies.csv')
print(df1.head())

# Fetching from url
df2 = pd.read_csv('https://raw.githubusercontent.com/m-mehdi/pandas_tutorials/main/weekly_stocks.csv')
print(type(df2.head()))

# sep parameter
df3 = pd.read_csv(filepath+'cities10.tsv') # since this is a tab saperated file, read_csv doesn't encounter any ',' and hence all gets imported as a single line
print("", df3, sep="\n")

df4 = pd.read_csv(filepath+'cities10.tsv', sep='\t') # saperator is tab
print("", df4, sep="\n")

# since this Data doesn't have any column name, the first row gets selected as a Column
# Therefore use name parameter
df5 = pd.read_csv(filepath+'cities10.tsv', sep='\t', names=['state','municipality','population','area'])
print("", df5, sep="\n")

# index_col
df6 = pd.read_csv(filepath+'movies.csv', index_col='title_x')
print("", df6.head(3), sep="\n")

print("", df1.set_index('title_x').head(3), sep="\n")


# header parameter
# i want to make my first row as my column name
df7 = pd.read_csv(filepath+'movies.csv', header=1)
print("", df7.head(3), sep="\n")


# use_cols parameter
df8 = pd.read_csv(filepath+'cities10.tsv', sep='\t', names=['state','municipality','population','area'], usecols=['municipality','area'])
print("", df8.head(3), sep="\n")


# skiprows
df9 = pd.read_csv(filepath+'movies.csv', skiprows=[1,3]) # row 0 in this file is column names
# the above line skips row number 1 and 3
print("", df9.head(5), sep="\n")

# nrows 
df10 = pd.read_csv(filepath+'movies.csv', nrows=100) # imports only 100 rows
print("", df10.shape[0], sep="\n")

# encoding
df11 = pd.read_csv(filepath+'cities10.tsv', sep="\t", encoding='utf8') 
# if the fle has different ecoding like latin-1 etc, use that in the encoding parameter to load the file

# skip bad lines
# on_bad_lines = 'skip' # skips those rows where the lines are not correct # 'skip', 'warn', 'error':default
df11 = pd.read_csv(filepath+'cities10.tsv', sep="\t", on_bad_lines='skip') 

# handling dates
df12 = pd.read_csv(filepath+'ipl-matches.csv', parse_dates=['Date'])
print(df12.info())

# convertors
def rename(name):
    if name == "Royal Challengers Bangalore": return "RCB"
    elif name == "Rajasthan Royals": return "RR"    
    else: return name

df13 = pd.read_csv(filepath+'ipl-matches.csv', converters={'Team1':rename, 'Team2':rename})
print("", df13[['Team1', 'Team2']], sep='\n')


# na_values
df14 = pd.read_csv(filepath+'time_series_covid19_confirmed_global.csv', na_values=['Male']) # this DF has nan values
# all males will be converted to NaN values


# Loading huge datasets in chunks
# deliveries has 179078 rows
dfs15 = pd.read_csv(filepath+'deliveries.csv', chunksize=5000)  # loads 5000 rows at a time
for chunk in dfs15:
    print(chunk.shape) # each chunk is a DF




""" Excel Sheets """

# pd.read_excel(filename)               # fetches the 1st sheet of the excel sheet
# pd.read_excel(filename, sheetname)    # fetches the mentioned sheet from the given excel document
# pd.read_excel('output.xlsx',sheet_name='Sheet_name_2')



""" From Text Files """

# you will use read_csv file
# check the file, if they are tab saperated then use

# pd.read_csv('question_answer_pairs.txt',sep='\t')



""" JSON File """
df16 = pd.read_json(filepath+'test.json')
df16.set_index('id', inplace=True)
print("", df16.head(3), sep="\n")


df17 = pd.read_json("https://api.exchangerate-api.com/v4/latest/INR")
print("", df17.head(3), sep="\n")





""" SQL """
import mysql.connector

# ip address of server, username, password, name of the database

# conn = mysql.connector.connect(host='localhost', user='root', password='', database='world')
# city = pd.read_sql_query('SELECT * FROM city', conn) # gets city table from world db
# country = pd.read_sql_query('SELECT * FROM country', conn) # gets country table from world db




#################################################################################
#################################################################################
#################################################################################
#################################################################################
#################################################################################

### EXPORTING DF ###


# df1.to_ : gives auto-suggestion to export


df1 = pd.read_csv(filepath+'deliveries.csv')
temp = df1.groupby('batsman')['batsman_runs'].sum().reset_index()
temp.to_csv('created/batsman_runs_created_in_csv.csv') # this also creates a index column
temp.to_csv('created/batsman_runs_2_created_in_csv.csv', index=False) # this eliminates the index

temp = df1.pivot_table(index="batsman", columns="bowling_team", values="batsman_runs", aggfunc='sum')
temp.to_csv('created/batsman_pivot_table_in_csv.csv')






df1 = pd.read_csv(filepath+'deliveries.csv')
temp1 = df1.groupby('batsman')['batsman_runs'].sum().reset_index()
temp1.to_excel('created/batsman_runs_created_in_excel.xlsx', index=False)

temp2 = df1.pivot_table(index="batsman", columns="bowling_team", values="batsman_runs", aggfunc='sum')
temp2.to_excel('created/batsman_pivot_table_in_excel.xlsx', sheet_name='pivot_table') # sheet in excel

# creating multiple sheets
with pd.ExcelWriter('created/batsman_in_excel.xlsx') as writer:
    temp1.to_excel(writer, sheet_name='batsman runs')
    temp2.to_excel(writer, sheet_name='pivot table')






temp = df1.query('batsman_runs == 6').pivot_table(index='over', columns='ball', values='batsman_runs', aggfunc='count')
temp.to_html('created/sixes_heatmap.html')





temp = df1.groupby(['batting_team', 'batsman'])['batsman_runs'].sum().unstack()
temp.to_json('created/ipl.json')
