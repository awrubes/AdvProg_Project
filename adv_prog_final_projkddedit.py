# -*- coding: utf-8 -*-
"""Adv Prog_Final Proj.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qnd8BoykFZvhqvYNuoUfDRnnuxWsssHF
"""

#global libraries
import pandas as pd
import numpy as np
import seaborn as sns
from IPython.display import display
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# ALLIE
# Inflation Indicators from World Bank Data

# Filtered by top 8 GDP countries, 2014 onward (2023)


cpi_df = pd.read_csv('https://raw.githubusercontent.com/awrubes/AdvProg_Project/main/inflation_consumerprices.csv', skiprows=2)

cpi_long = cpi_df.melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
                  var_name='Year',
                  value_name='Indicator Value')
total_missing = cpi_long.isna().sum()

missing_by_year = cpi_long[cpi_long['Indicator Value'].isna()].groupby('Year').size()
#print(missing_by_year)

missing_by_country = cpi_long[cpi_long['Indicator Value'].isna()].groupby('Country Name').size()

#filter out countries with less than 5 NaN values
no_na_country = missing_by_country[missing_by_country < 5].index

#filter the dataframe using this list
countries_to_keep = cpi_long[cpi_long['Country Name'].isin(no_na_country)]

#drop rows with unnamed values
countries_to_keep = countries_to_keep[~countries_to_keep['Year'].astype(str).str.contains('Unnamed')]

#keep 2014 onward
countries_to_keep = countries_to_keep[countries_to_keep['Year'] >= '2014']

all_countries_inflation = countries_to_keep

#Top countries by GDP
# United States: $25.43 trillion
# China: $14.72 trillion
# Japan: $4.25 trillion
# Germany: $3.85 trillion
# India: $3.41 trillion
# United Kingdom: $2.67 trillion
# France: $2.63 trillion
# Canada: $2.16 trillion
# Italy: $2.04 trillion

top_gdp = ['United States', 'China', 'Japan', 'Germany', 'India', 'United Kingdom', 'France', 'Russia', 'Canada', 'Italy']
top_gdp_df = countries_to_keep[countries_to_keep['Country Name'].isin(top_gdp)]

#get the countries with the highest inflation
mean_inflation = countries_to_keep['Indicator Value'].mean()
std_inflation = countries_to_keep['Indicator Value'].std()
high_inflation_threshold = mean_inflation + std_inflation
high_inflation_countries = countries_to_keep[countries_to_keep['Indicator Value'] > high_inflation_threshold].sort_values(by='Indicator Value', ascending=False)

mean_high = high_inflation_countries.groupby('Country Name').agg({'Indicator Value': 'mean'}).sort_values(by='Indicator Value', ascending=False)

#visualize using seaborn the top 10 countries
ax = (
    sns.lineplot(data=top_gdp_df, x='Year', y='Indicator Value', hue='Country Name')
)
ax.legend_.set_bbox_to_anchor((1.05, 1))
plt.title('Inflation Rates for Top 8 GDP Nations')
plt.show()

#Highest inflation rates
#Sudan                    120.672016
# Turkiye                   63.084122
# Suriname                  50.466966
# Sri Lanka                 49.721102

highest = ['Sudan', 'Turkiye', 'Suriname', 'Sri Lanka']
highest_df = countries_to_keep[countries_to_keep['Country Name'].isin(highest)]

ax2 = (
    sns.lineplot(data=highest_df, x='Year', y='Indicator Value', hue='Country Name')
)
ax2.legend_.set_bbox_to_anchor((1.05, 1))
plt.show()

combined = pd.concat([top_gdp_df, highest_df])
ax2 = (
    sns.lineplot(data=combined, x='Year', y='Indicator Value', hue='Country Name')
)
ax2.legend_.set_bbox_to_anchor((1.05, 1))
plt.show()

new_combined = combined[combined['Country Name'] != 'Sudan']

ax2 = (
    sns.lineplot(data=new_combined, x='Year', y='Indicator Value', hue='Country Name')
)
ax2.legend_.set_bbox_to_anchor((1.05, 1))
plt.show()

# DHANYA
# CPI , by Country, years : 2014 to 2023

# Downloaded all countries CPI data for last 10 years( 2014- 2023) from International Monetary Fund(IMF)
# https://data.imf.org/?sk=4ffb52b2-3653-409a-b471-d47b46d904b5&sid=1485878855236

# uploaded the same into github

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read raw data
cpi_raw = pd.read_excel('https://raw.githubusercontent.com/datanerddhanya/DATA602/refs/heads/main/Consumer_Price_Index_CPI.xlsx')

cpi_years = cpi_raw.melt(id_vars=['Country'],
                  var_name='Year',
                  value_name='CPI')


# to remove the text like 'Republic of ', 'Kingdom of ', 'Federative Republic of ',
# 'Islamic Republic of ', 'Democratic Republic of ', 'Commonwealth of '
cpi_years['Country'] = cpi_years['Country'].str.split(',').str[0].str.strip()

#as it has many decimals, rounding to 2
cpi_years['CPI'] = cpi_years['CPI'].round(2)

cpi_years

# Plot the data
plt.figure(figsize=(10, 6))
sns.lineplot(data=cpi_years, x='Year', y='CPI', marker='o',errorbar=None)

# Customize the plot
plt.title('Annual CPI for countries over Ten Years', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('CPI Value', fontsize=12)
plt.legend(title='Countries', bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside
plt.xticks(rotation=45)  # Rotate x-axis labels to 45 degrees
plt.grid(True)

# Display the plot
plt.show()


# 1. Convert both country names to lowercase for case-insensitive matching
cpi_years['Country'] = cpi_years['Country'].str.lower()

countries_to_track = ['united states', 'canada', 'brazil', 'united kingdom',
                 'france', 'germany', 'russia', 'italy','mexico', 'china', 'japan',
                 'india', 'australia', 'south africa']
countries_to_track = [country.lower() for country in countries_to_track]

# Plot the data
plt.figure(figsize=(10, 6))
sns.lineplot(data=cpi_years[cpi_years['Country'].isin(countries_to_track)], x='Year', y='CPI', hue ='Country', marker='o',errorbar=None)

# Customize the plot
plt.title('Annual CPI for countries over Ten Years', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('CPI Value', fontsize=12)
plt.legend(title='Countries', bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside
plt.xticks(rotation=45)  # Rotate x-axis labels to 45 degrees
plt.grid(True)

# Display the plot
plt.show()

# DHANYA
# CPI for USA, various expense categories,  years : 2014 to 2023

# Downloaded USA CPI data by various expense categories for last 10 years( 2014- 2023) from International Monetary Fund(IMF)
# https://data.imf.org/?sk=4ffb52b2-3653-409a-b471-d47b46d904b5&sid=1485878802128

# uploaded the same into github

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read raw data
cpi_expense_category_raw = pd.read_excel('https://raw.githubusercontent.com/datanerddhanya/DATA602/refs/heads/main/Country_Indexes_by_expenditurecategory.xlsx',skiprows=1)


cpi_expense_category_years = cpi_expense_category_raw.melt(id_vars=['Expenditure Category'],
                   var_name='MonthYear',
                   value_name='CPI')

# Convert '2014M01' to '2014' and '01'
cpi_expense_category_years['Year'] = cpi_expense_category_years['MonthYear'].str.split('M').str[0]
cpi_expense_category_years['Month'] = cpi_expense_category_years['MonthYear'].str.split('M').str[1]

# Dropping 'MonthYear' variable as we no longer need it
cpi_expense_category_years = cpi_expense_category_years.drop(columns=['MonthYear'])

# Convert 'Year' to a numerical type for proper plotting on the x-axis
cpi_expense_category_years['Year'] = pd.to_numeric(cpi_expense_category_years['Year'])

# Convert 'Month' to a numerical type for proper plotting on the x-axis
cpi_expense_category_years['Month'] = pd.to_numeric(cpi_expense_category_years['Month'])

# as it has many decimals, rounding to 2
cpi_expense_category_years['CPI'] = cpi_expense_category_years['CPI'].round(2)

# Check for NA or null values
cpi_expense_category_years.isna().sum()

# Plot the data
plt.figure(figsize=(10, 6))
sns.lineplot(data=cpi_expense_category_years, x='Year', y='CPI', hue = 'Expenditure Category', marker='o',errorbar=None)

# Customize the plot
plt.title('Annual CPI for US by expense categories over Ten Years', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('CPI Value', fontsize=12)
plt.legend(title='Expenditure Category', bbox_to_anchor=(1.05, 1), loc='upper left')  # Move legend outside
plt.xticks(rotation=45)  # Rotate x-axis labels to 45 degrees
plt.grid(True)

# Display the plot
plt.show()

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
print(interest_df['RIFSPFF_N.D'].describe())
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
print(supply_pressure_df['GSCPI'].describe())

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

real_income_csv = "https://github.com/awrubes/AdvProg_Project/raw/refs/heads/main/real%20median%20household%20income%20MEHOINUSA672N.csv"
#real median household income put into data frame
real_income_df = pd.read_csv(real_income_csv)
#view data
real_income_df.head()

median_income_csv = "https://github.com/awrubes/AdvProg_Project/raw/refs/heads/main/median%20household%20income%20MEHOINUSA646N.csv"
#median household income put into data frame
median_income_df = pd.read_csv(median_income_csv)
#view data
median_income_df.head()

plt.plot(real_income_df['DATE'], real_income_df['MEHOINUSA672N'])

#label the axis and give title
plt.xlabel('Date')
plt.ylabel('Real Median Household Income ($)')
plt.title(' Real Median Household Income vs. Date')

#tilt the dates for readability
plt.xticks(rotation=45)
#dipslay plot
plt.show()
real_income_df.describe()

plt.plot(median_income_df['DATE'], median_income_df['MEHOINUSA646N'])

#label the axis and give title
plt.xlabel('Date')
plt.ylabel('Median Household Income ($)')
plt.title(' Real Median Household Income vs. Date')

#tilt the dates for readability
plt.xticks(rotation=45)
#dipslay plot
plt.show()
median_income_df.describe()

#interest by country
country_interest_excel = "https://github.com/awrubes/AdvProg_Project/raw/refs/heads/main/interest_by_country_IMF-IFS.xlsx"
#median household income put into data frame
country_interest_df = pd.read_excel(country_interest_excel)
#view data
print(country_interest_df.head())
country_interest_df.describe()

#GDP per Capita by country

GDP_capita = "https://github.com/awrubes/AdvProg_Project/raw/refs/heads/main/GDP%20per%20capita%20WITS-Country-Timeseries.xlsx"
gdp_capita_df = pd.read_excel(GDP_capita)
#view data
print(gdp_capita_df.head())
gdp_capita_df.describe()

#GNI per capita by country (income)
GNI_capita = "https://github.com/awrubes/AdvProg_Project/raw/refs/heads/main/GNI%20per%20capita%20WITS-Country-Timeseries%20(1).xlsx"
gni_capita_df = pd.read_excel(GNI_capita)
#view data
print(gni_capita_df.head())
gni_capita_df.describe()

#median income yearly data converted to a linear interpolation of data


# Ensure DATE column is datetime
median_income_df['DATE'] = pd.to_datetime(median_income_df['DATE'], errors='coerce')

# Ensure MEHOINUSA646N column is numeric
median_income_df['MEHOINUSA646N'] = pd.to_numeric(median_income_df['MEHOINUSA646N'], errors='coerce')

# Set Month_year as index
median_income_df['Month_year'] = median_income_df['DATE']
median_income_df.set_index('Month_year', inplace=True)

# Drop the DATE column
median_income_df.drop(columns=['DATE'], inplace=True)

# Resample to monthly and interpolate
median_income_df_monthly = median_income_df.resample('MS').interpolate(method='linear')

# Debug: Check the interpolated values
print(median_income_df_monthly)

#real income yearly data converted to a linear interpolation of data
# Ensure DATE column is datetime
real_income_df['DATE'] = pd.to_datetime(real_income_df['DATE'], errors='coerce')

# Ensure MEHOINUSA672N column is numeric
real_income_df['MEHOINUSA672N'] = pd.to_numeric(real_income_df['MEHOINUSA672N'], errors='coerce')

# Set Month_year as index
real_income_df['Month_year'] = real_income_df['DATE']
real_income_df.set_index('Month_year', inplace=True)

# Drop the DATE column
real_income_df.drop(columns=['DATE'], inplace=True)

# Resample to monthly and interpolate
real_income_df_monthly = real_income_df.resample('MS').interpolate(method='linear')

# Debug: Check the interpolated values
print(real_income_df_monthly)

#merging GSCPI with Interest for global dataset

common_dates = set(interest_df['Time Period']).intersection(supply_pressure_df['Date'])
interest_df = interest_df[interest_df['Time Period'].isin(common_dates)]
supply_pressure_df = supply_pressure_df[supply_pressure_df['Date'].isin(common_dates)]

global_merged_df = pd.merge(interest_df, supply_pressure_df, left_on='Time Period', right_on='Date', how='inner')

global_merged_df = global_merged_df.drop("Time Period", axis=1)
global_merged_df.head(10)

#need to make this comparable to country dataframe, so either mean or December of each year so it's by year

global_merged_df['Year'] = global_merged_df['Date'].apply(lambda x: x.year)

global_merged_df_grouped = global_merged_df.groupby('Year')

global_merged_df_means = global_merged_df_grouped.mean()

global_merged_df_grouped.head(5)

global_merged_df_means = global_merged_df_means.drop("Date", axis=1)

global_merged_df_means.head(5)

gdp_capita_df.columns
gdp_long = gdp_capita_df.melt(
    id_vars=['Country Name', 'Indicator Name'],  # Columns to keep
    var_name='Year',  # New column for years
    value_name='GDP per Capita'
)
gni_long = gni_capita_df.melt(
    id_vars=['Country Name', 'Indicator Name'],  # Columns to keep
    var_name='Year',  # New column for years
    value_name='GNI per capita '  # New column for GDP values
)

gni_long.rename(columns={'Country Name' : 'Country'}, inplace=True)
gdp_long.rename(columns={'Country Name' : 'Country'}, inplace=True)
all_countries_inflation.rename(columns={'Country Name':'Country'}, inplace=True)
all_countries_inflation.rename(columns={'Indicator Value':'Inflation'}, inplace=True)
gdp_long = gdp_long.drop('Indicator Name', axis=1)
gni_long = gni_long.drop('Indicator Name', axis=1)

#clean inflation dataframe remove unnecessary columns
all_countries_inflation = all_countries_inflation.drop(["Country Code", "Indicator Code", "Indicator Name"], axis=1)

#strip whitespace and set to lowercase
gdp_long['Country'] = gdp_long['Country'].str.lower().str.strip()
gni_long['Country'] = gni_long['Country'].str.lower().str.strip()
cpi_years['Country'] = cpi_years['Country'].str.lower().str.strip()
all_countries_inflation['Country'] = all_countries_inflation['Country'].str.lower().str.strip()

#all global dataframes for merging
all_countries_inflation.head(2)

gdp_long.head(2)

cpi_years.head(2)

gni_long.head(2)

#now merging datasets by country and year (non global values)

common_countries = set(cpi_years['Country'].str.lower()) & set(all_countries_inflation['Country'].str.lower()) & set(gdp_long['Country'].str.lower()) & set(gni_long['Country'].str.lower())
cpi_years = cpi_years[cpi_years['Country'].str.lower().isin(common_countries)]
all_countries_inflation = all_countries_inflation[all_countries_inflation['Country'].str.lower().isin(common_countries)]
gdp_long = gdp_long[gdp_long['Country'].str.lower().isin(common_countries)]
gni_long = gni_long[gni_long['Country'].str.lower().isin(common_countries)]


country_merged_df = pd.merge(cpi_years, all_countries_inflation, on=['Country', 'Year'], how='inner')
country_merged_df = pd.merge(country_merged_df, gdp_long, on=['Country', 'Year'], how='inner')
country_merged_df = pd.merge(country_merged_df, gni_long, on=['Country', 'Year'], how='inner')

#ALLIE/KEITH TO DO:
# Need to look at GDP/GNI unit of measurement, domestic currency needs to be converted to US Dollars (check common_countries)

#Merged Dataframes

country_merged_df.head(5)
#contains, GDP, GNI, CPI, Inflation

#still has NaN values for some metrics such as GNI/GDP

country_merged_df.isna().sum().sum()

country_merged_na = country_merged_df[country_merged_df.isna().any(axis=1)]

country_merged_na.head(10)

#ALLIE TO DO:
#drop suriname from merged data frame

#Merged Dataframes

global_merged_df_means.head(10)
#merging Global datasets for GSCPI and Interest

#keith correlations

#relevant dataframes country_merged_df(CPI, inflation, GDP per capita, GNI per capita) global_merged_df_means (GSPI and interest)
import seaborn as sns
import matplotlib.pyplot as plt



#CPI is most dependent on inflation rather than GNI/GDP


correlation_global = global_merged_df_means.corr(numeric_only=True)

# Create the heatmap
sns.heatmap(correlation_global, annot=True, cmap='coolwarm')
plt.show()

print(country_merged_df.head()) #CPI inflation GDP per capita GNI per capita
print(global_merged_df_means.head())

# Reset the index to make 'Year' a regular column
global_merged_df_means = global_merged_df_means.reset_index()

# Year converted from index to column display
print(global_merged_df_means.head())

#merge global_merged_df_means and country_merged_df.head() by year

#first make sure Year from both dataframes are the same type.
country_merged_df['Year'] = country_merged_df['Year'].astype(int)  # Convert to string
global_merged_df_means['Year'] = global_merged_df_means['Year'].astype(int)  # Convert to string

#make sure the types have changed
print(country_merged_df.dtypes)
print(global_merged_df_means.dtypes)

# Merging on the 'year' column
country_global_df = pd.merge(country_merged_df, global_merged_df_means , on='Year')
#successfully merged
print(country_global_df.head())
print(country_global_df.columns)
#remove the unnecessary columns if the above is run more than once
#country_global_df = country_global_df.drop(['level_0', 'index'], axis=1)

#correlations between CPI, inflation, interest, GNI per capita, GDP per capita, Global supply chain index all countries treated as one
correlation_all = country_global_df.corr(numeric_only=True)

# correlation heatmap of all countries treated as one
sns.heatmap(correlation_all, annot=True, cmap='coolwarm')
plt.show()

# Select only numeric columns for correlation matrix
numeric_cols = country_global_df.select_dtypes(include=['int64', 'float64']).columns

# Group by country and calculate correlation matrix for each country
correlations_country = country_global_df.groupby('Country')[numeric_cols].corr()

#view the correlations
print(correlations_country.columns)
print(correlations_country)

#selecting the correlations for one country
print(correlations_country.loc['united states'])

# Loop through each country and plot the correlation matrix
for country, corr_matrix in correlations_country.groupby(level=0):
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
    plt.title(f'Correlation Matrix for {country}')
    plt.show()





'''
# Function to calculate correlation for each country
def calculate_interest_correlation(df, Country):
    country_df = df[df['Country'] == Country]
    interest_correlation = country_df[['RIFSPFF_N.D', 'CPI']].corr()
    return interest_correlation.loc['RIFSPFF_N.D', 'CPI']

# List of unique countries
countries = country_global_df['Country'].unique()

# Calculating correlation for each country
interest_CPI_correlations = {Country: calculate_interest_correlation(country_global_df, Country) for Country in countries}

# Displaying results
print(interest_CPI_correlations)



def calculate_interest_correlation(df, Country):
    country_df = df[df['Country'] == Country]
    interest_correlation = country_df[['RIFSPFF_N.D', 'CPI']].corr()
    return interest_correlation.loc['RIFSPFF_N.D', 'CPI']

# List of unique countries
countries = country_global_df['Country'].unique()

# Calculating correlation for each country
interest_CPI_correlations = {Country: calculate_interest_correlation(country_global_df, Country) for Country in countries}

# Displaying results
print(interest_CPI_correlations)

correlation_country = country_global_df.corr(numeric_only=True)

# Create the heatmap
sns.heatmap(correlation_country, annot=True, cmap='coolwarm')
plt.show()

'''