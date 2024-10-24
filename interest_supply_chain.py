# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:47:27 2024

@author: keith
"""
#interest rates
import pandas as pd
#link to the interest rate data
interest_csv_raw = "https://github.com/awrubes/AdvProg_Project/raw/refs/heads/main/interest%20rate%20FRB_H15.csv"
#read in the interest rate data
interest_df2 = pd.read_csv(interest_csv_raw)
#view data
interest_df2.head()
#remove the first 4 rows of metadata
interest_df = interest_df2.iloc[4:]
#rename the columns to the first row strings
interest_df.columns = interest_df.iloc[0] 
#view data frame
interest_df.head()
#ensure the federal funds effective rate are treated as numeric values
interest_df['RIFSPFF_N.D'] = pd.to_numeric(interest_df['RIFSPFF_N.D'], errors='coerce')
#view the data frame
interest_df.head()


#remove the first row that contains an NaN
interest_df = interest_df[1:] 
#view the data frame
interest_df.head()    
#make the column time period labeled as a date.         
interest_df['Time Period'] = pd.to_datetime(interest_df['Time Period'], errors='coerce')

#plotting the data
import matplotlib.pyplot as plt
#plot time period/date as the x axis and the interest rate as y axis  
plt.plot(interest_df['Time Period'], interest_df['RIFSPFF_N.D'])  

#label the axis and give title
plt.xlabel('Date')
plt.ylabel('Effective rate')
plt.title(' Effective Interest Rate vs. Date')

#tilt the dates for readability 
plt.xticks(rotation=45)
#dipslay plot
plt.show()
#basic statistics on interest rates.
interest_df['RIFSPFF_N.D'].describe()

#supply chain


supply_pressure_csv = "https://github.com/awrubes/AdvProg_Project/raw/refs/heads/main/gscpi_data_global_supply_chain_pressure_index.csv"
#supply chain pressure index put into data frame
supply_pressure_df = pd.read_csv(supply_pressure_csv)
#view data
supply_pressure_df.head()
 # rename column names to avoid errors
new_column_names = ['Date', 'GSCPI', 'Column3', 'Column4', 'Column5', 'Column6', 'Column7', 'Column8', 'Column9', 'Column10', 'Column11']
#assign the new column names
supply_pressure_df.columns = new_column_names
#ensure the data frame has only the columns of interest
supply_pressure_df = supply_pressure_df[['Date', 'GSCPI']] 
#remove the blank space/NaN at top of data frame
supply_pressure_df = supply_pressure_df[4:]
#view data frame of supply chain pressure index
supply_pressure_df.head() 
#ensure that the date is read as a date
supply_pressure_df['Date'] = pd.to_datetime(supply_pressure_df['Date'], errors='coerce')
#view data frame
supply_pressure_df.head()
#plotting the global supply chain pressure index vs the date
plt.plot(supply_pressure_df['Date'], supply_pressure_df['GSCPI'])  
#label the plot and give it a title
plt.xlabel('Date')
plt.ylabel('GSCPI')
plt.title(' Global Supply Chain Pressure Index vs. Date')
#tilt the x axis labels for readability
plt.xticks(rotation=45)
#display plot
plt.show()
#show basic statistics of global supply chain pressure index
supply_pressure_df['GSCPI'].describe()


