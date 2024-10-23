# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:47:27 2024

@author: keith
"""
#interest rates
import pandas as pd
#link to the interest rate data
interest_csv_raw = "https://github.com/division-zero/Data-602project/raw/refs/heads/main/interest%20rate%20FRB_H15.csv"
#read in the interest rate data
interest_df2 = pd.read_csv(interest_csv_raw)
interest_df2.head()

interest_df = interest_df2.iloc[4:]
interest_df.head()

import matplotlib.pyplot as plt
interest_df.columns = interest_df.iloc[0]  
interest_df = interest_df[1:]              
interest_df['Time Period'] = pd.to_datetime(interest_df['Time Period'], errors='coerce')

plt.figure(figsize=(10, 6))  
plt.plot(interest_df['Time Period'], interest_df['RIFSPFF_N.D'])  


plt.xlabel('Date')
plt.ylabel('Effective rate')
plt.title(' Effective Interest Rate vs. Date')


plt.xticks(rotation=45)

plt.show()
interest_df['RIFSPFF_N.D'].describe()

#supply chain
supply_csv_raw = "https://github.com/division-zero/Data-602project/raw/refs/heads/main/Supply_Chain_Shipment_Pricing_Dataset.csv"
supply_price_df = pd.read_csv(supply_csv_raw)
supply_pressure_csv = "https://github.com/division-zero/Data-602project/raw/refs/heads/main/gscpi_data_global_supply_chain_pressure_index.csv"
supply_pressure_df = pd.read_csv(supply_pressure_csv)
supply_price_df.head()
supply_pressure_df.head()
supply_pressure_df.columns = interest_df.iloc[0]  
supply_pressure_df = supply_pressure_df[4:]
supply_pressure_df.head() 

supply_pressure_df['Date'] = pd.to_datetime(supply_pressure_df['Date'], errors='coerce')

             

plt.figure(figsize=(10, 6))  
plt.plot(supply_pressure_df['Date'], supply_pressure_df['GSCPI'])  


plt.xlabel('Date')
plt.ylabel('GSCPI')
plt.title(' Global Supply Chain Pressure Index vs. Date')


plt.xticks(rotation=45)

plt.show()
supply_pressure_df['GSCPI'].describe()
