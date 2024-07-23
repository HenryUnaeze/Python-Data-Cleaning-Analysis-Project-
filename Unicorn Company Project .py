#!/usr/bin/env python
# coding: utf-8

# In[56]:


import numpy as np
import pandas as pd

#visuals 
import matplotlib.pyplot as plt 
import seaborn as sns 


# In[57]:


dfc = pd.read_csv(r"C:\Users\Henry Unaeze\OneDrive\Desktop\Personal Data Analyst Projects\Python For DAT\Python Assignments\Unicorn_Companies.csv")
dfc


# In[58]:


dfc.shape


# In[59]:


dfc.info()


# In[60]:


dfc.describe()


# In[61]:


dfc['Date Joined'] = pd.to_datetime(dfc['Date Joined'], errors='coerce')
dfc['Year Founded'] = pd.to_datetime(dfc['Year Founded'], format='%Y')


# In[62]:


dfc


# In[63]:


dfc.info()


# In[64]:


dfc.info()


# In[65]:


dfc.isna().sum()


# In[66]:


dfc


# ## Identify rows with missing values 
# 

# In[67]:


dfc[dfc.isna().any(axis=1)]


# In[68]:


dfc.loc[12,'City']='Antigua'
dfc.loc[170,'City']='Singapore'
dfc.loc[242,'City']='Noida'
dfc.loc[251,'City']='Singapore'
dfc.loc[382,'City']='Singapore'
dfc.loc[325,'City']='Hong Kong'
dfc.loc[541,'City']='Singapore'
dfc.loc[629,'City']='Singapore'
dfc.loc[811,'City']='Singapore'
dfc.loc[848,'City']='Singapore'
dfc.loc[889,'City']='Singapore'
dfc.loc[893,'City']='New York'
dfc.loc[880,'City']='Singapore'
dfc.loc[980,'City']='San Francisco'
dfc.loc[986,'City']='Singapore'
dfc.loc[994,'City']='Singapore'
dfc.loc[1061,'City']='Hong Kong'



# In[69]:


dfc[dfc.isna().any(axis=1)]


# In[70]:


dfc.loc[629, 'Select Investors'] = ', '.join(['Northern Light Venture Capital', 'Haitong Kaiyuan Investment', 'SeptWolves Ventures'])


# In[71]:


dfc


# In[72]:


dfc.isna().sum()


# In[73]:


dfc.loc[629,'Select Investors']= ','.join(['Northern Light Venture Capital', 'Haitong Kaiyuan Investment', 'SeptWolves Ventures'])


# In[74]:


dfc.isna().sum()


# In[75]:


dfc.info()


# In[76]:


dfc


# ## Removing non-numeric characters from numerical columns like Valuation and Funding e.g, dollar sign and Billions

# In[78]:


# Define a function to convert funding values
def convert_funding(value):
    if isinstance(value, (int, float)):
        return value
    try:
        value = value.replace('$', '')  # Remove dollar sign
        if 'M' in value:
            return float(value.replace('M', '')) * 1e6  # Convert millions to numeric
        elif 'B' in value:
            return float(value.replace('B', '')) * 1e9  # Convert billions to numeric
        else:
            return float(value)  # If no suffix, return as float
    except ValueError:
        return np.nan  # Return NaN for any conversion error

# Apply the conversion function to the 'Funding' column
dfc['Funding'] = dfc['Funding'].apply(convert_funding)
dfc


# In[80]:


# Define a function to convert funding values
def convert_funding(value):
    if isinstance(value, (int, float)):
        return value
    try:
        value = value.replace('$', '')  # Remove dollar sign
        if 'B' in value:
            return float(value.replace('B', '')) * 1e9  # Convert Billions to numeric
        else:
            return float(value)  # If no suffix, return as float
    except ValueError:
        return np.nan  # Return NaN for any conversion error

# Apply the conversion function to the 'Funding' column
dfc['Valuation'] = dfc['Valuation'].apply(convert_funding)
dfc


# In[81]:


dfc


# In[82]:


dfc[dfc.isna().any(axis=1)]


# In[ ]:





# In[83]:


# Replace zero funding with NaN
dfc['Funding'].replace(0, np.nan, inplace=True)

# Impute NaN values in 'Funding' with the median value of the funding column
median_funding = dfc['Funding'].median()

dfc['Funding'].fillna(median_funding, inplace=True)


# In[84]:


dfc


# In[85]:


dfc.isna().sum()


# In[86]:


dfc


# In[107]:


dfc['ROI'] = (dfc['Valuation'] - dfc['Funding']) / dfc['Funding']


# In[108]:


dfc


# In[109]:


dfc.info()


# In[110]:


dfc['Uni_Corn_days'] = dfc['Date Joined']-dfc['Year Founded']
dfc['Uni_Corn_days']


# In[111]:


dfc


# In[112]:


dfc.columns


# In[113]:


dfc1=dfc[['Company', 'Valuation', 'Date Joined', 'Industry', 'City', 'Country',
       'Continent', 'Year Founded', 'Funding', 'Select Investors', 'ROI','Uni_Corn_days']]
dfc1


# In[114]:


dfc1.info()


# In[115]:


dfc1['Uni_Years'] = dfc1['Uni_Corn_days']/365.25
dfc1['Uni_Years'] 


# In[116]:


dfc1


# In[117]:


dfc1.info()


# In[118]:


dfc1['Uni_Years']= dfc1['Uni_Years'].astype(str)
dfc1['Uni_Years']


# In[119]:


dfc1.info()


# In[120]:


dfc1['Num_Years'] = dfc1['Uni_Years'].str.extract(r'(\d+)').astype(int)
dfc1['Num_Years'] 


# In[121]:


dfc1


# In[122]:


dfc1.columns


# In[123]:


dfc2=dfc1[['Company', 'Valuation', 'Date Joined', 'Industry', 'City', 'Country',
       'Continent', 'Year Founded', 'Funding', 'Select Investors', 'ROI','Num_Years']]
dfc2


# ### Question 1: Which Company has the highest RIO

# In[129]:


Comp_HROI=dfc2.groupby(['Company'])['ROI'].max().sort_values(ascending=True)
Comp_HROI


# In[130]:


# Group by Company and get the max ROI, then sort
Comp_HROI = dfc2.groupby('Company')['ROI'].max().sort_values(ascending=False)

# Select the top 50 companies
top_50_Comp_HROI = Comp_HROI.head(50)

# Plot using Seaborn
plt.figure(figsize=(12, 10))
sns.barplot(x=top_50_Comp_HROI, y=top_50_Comp_HROI.index, palette='Spectral')
plt.xlabel('ROI')
plt.ylabel('Company')
plt.title('Top 50 Companies by Highest ROI')
plt.tight_layout()
plt.show()


# ## From the plot above , Zapier leads in the ROI with a value of 3999 followed the likes of Dunamu with 125, workhuman at 110 etc

# In[ ]:





# ## Question 2: How long it takes for companies to become Unicorn and has that always been the trend?

# ### Ans: Filter companies with valuation of 1billion Dollars

# In[104]:


# Number of top companies to display
top_n = 50

# Filter the dataset to only include companies with a valuation of $1 billion
filtered_df = dfc2[dfc2['Valuation'] == 1e9]

# Group by company and calculate the sum of the number of years to reach the $1 billion valuation
Val_Num_Yrs = filtered_df.groupby('Company')['Num_Years'].sum().sort_values(ascending=False)

# Select the top N companies
top_val_num_yrs = Val_Num_Yrs.head(top_n)

# Plotting
plt.figure(figsize=(12, 8))
ax = sns.barplot(x=top_val_num_yrs.values, y=top_val_num_yrs.index, palette='viridis')

# Adding title and labels
plt.title(f'Top {top_n} Companies by Time Taken to Reach $1 Billion Valuation', fontsize=16, weight='bold')
plt.xlabel('Number of Years', fontsize=14, weight='bold')
plt.ylabel('Company', fontsize=14, weight='bold')

# Adding values on the bars
for i, v in enumerate(top_val_num_yrs.values):
    ax.text(v + 0.1, i, f'{v:.2f}', va='center', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()


# ### Checking the bottom 50 companies to determine trend on how long it takes to become a unicorn 

# In[182]:


# Number of bottom companies to display
bottom_n = 50

# Filter the dataset to only include companies with a valuation of $1 billion
filtered_df = dfc2[dfc2['Valuation'] == 1e9]

# Group by company and calculate the sum of the number of years to reach the $1 billion valuation
Val_Num_Yrs = filtered_df.groupby('Company')['Num_Years'].sum().sort_values()

# Select the bottom N companies
bottom_val_num_yrs = Val_Num_Yrs.head(bottom_n)

# Plotting
plt.figure(figsize=(12, 8))
ax = sns.barplot(x=bottom_val_num_yrs.values, y=bottom_val_num_yrs.index, palette='rocket')

# Adding title and labels
plt.title(f'Bottom {bottom_n} Companies by Time Taken to Reach $1 Billion Valuation', fontsize=16, weight='bold')
plt.xlabel('Number of Years', fontsize=14, weight='bold')
plt.ylabel('Company', fontsize=14, weight='bold')

# Adding values on the bars
for i, v in enumerate(bottom_val_num_yrs.values):
    ax.text(v + 0.1, i, f'{v:.2f}', va='center', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()


# ## Answers: From the plot above, in the past it takes the range of 13-37 years for a company to become a unicorn but in recent time it takes from 1-3 years for a company to be a unicorn

# ## Which countries have the most unicorns? Are there any cities that appear to be industry hub?
# 

# In[ ]:


Ctry_Mst_Uni=dfc2['Country'].value_counts()
Ctry_Mst_Uni


# In[192]:


Ctry_Mst_Uni = dfc2['Country'].value_counts()

# Get the top 50 cities
top_50 = Ctry_Mst_Uni.head(50)

# Convert the series to a DataFrame for easier plotting with Seaborn
df = top_50.reset_index()
df.columns = ['Country', 'Count']

# Define a new vibrant color palette
palette = sns.color_palette("inferno", len(df))

# Plotting
plt.figure(figsize=(16, 10))
ax = sns.barplot(x='Country', y='Count', data=df, palette=palette)

# Adding title and labels
ax.set_title('Top 50 Countries by Count', fontsize=16, weight='bold')
ax.set_xlabel('Country', fontsize=14, weight='bold')
ax.set_ylabel('Count', fontsize=14, weight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)

# Adding bar labels
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()


# ## Answers 3a: United States leads with 562 unicorns followed by China at 173 and India coming at 3rd place with 65 unicorns from the bar plot above 

# In[ ]:


# Plotting
plt.figure(figsize=(12, 8))
sns.barplot(x='Count', y='Country', data = Ctry_Mst_Uni, palette='viridis')

# Adding title and labels
plt.title('Distribution of Counts by Country')
plt.xlabel('Count')
plt.ylabel('Country')

# Show the plot
plt.show()


# ## Cities that appears to be a hub must be a city with the highest number of unicorn companies in them. 

# In[ ]:


Cty_Mst_Uni=dfc2['City'].value_counts()
Cty_Mst_Uni


# In[151]:


Cty_Mst_Uni = dfc2['City'].value_counts()

# Get the top 50 cities
top_75 = Cty_Mst_Uni.head(50)

# Convert the series to a DataFrame for easier plotting with Seaborn
df = top_75.reset_index()
df.columns = ['City', 'Count']

# Define a new vibrant color palette
palette = sns.color_palette("flare", len(df))

# Plotting
plt.figure(figsize=(16, 10))
ax = sns.barplot(x='City', y='Count', data=df, palette=palette)

# Adding title and labels
ax.set_title('Top 75 Cities by Count', fontsize=16, weight='bold')
ax.set_xlabel('City', fontsize=14, weight='bold')
ax.set_ylabel('Count', fontsize=14, weight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)

# Adding bar labels
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()


# ## Answer 3b: Cities that appears to be hubs have more unicorns in them and they are; San Francisco with 153 unicorn companies followed by New York at 104 unicorns and Beijing having 63 as 3rd city.   

# ### Which investors have funded the most unicorns?

# In[160]:


Inv_Most_Fnd =dfc2.groupby(['Select Investors'])['Funding'].max().sort_values(ascending=False)
Inv_Most_Fnd


# In[185]:


# Group by Company and get the max ROI, then sort
Inv_Most_Fnd = dfc2.groupby('Select Investors')['Funding'].max().sort_values(ascending=False)

# Select the top 15 companies
top_30_Inv_Most_Fnd= Inv_Most_Fnd.head(30)

# Plot using Seaborn
plt.figure(figsize=(12, 10))
sns.barplot(x=top_30_Inv_Most_Fnd, y=top_30_Inv_Most_Fnd.index, palette='twilight_shifted_r')
plt.xlabel('Funding')
plt.ylabel('Select Investors')
plt.title('Top 30 Companies by Highest Funding')
plt.tight_layout()
plt.show()


# ## Which Investors Team have better return on investement (ROI) demostrating experienced leadership ?

# In[191]:


# Investors with highest ROI
Inv_High_ROI = dfc2.groupby('Select Investors')['ROI'].sum().sort_values(ascending=False)

# Select the top 15 companies
top_15_Inv_High_ROI = Inv_High_ROI.head(15)

# Plot using Seaborn
plt.figure(figsize=(12, 10))
sns.barplot(x=top_15_Inv_High_ROI, y=top_15_Inv_High_ROI.index, palette='afmhot')
plt.xlabel('ROI')
plt.ylabel('Select Investors')
plt.title('Top 15 Investors by Highest ROI')
plt.tight_layout()
plt.show()


# ## Answer: The above plot demonstrate that despite the less funding of just 1million dollars, Sequoia Capital, Bessemer Venture Partners, Threshold Ventures were able to identify opportunities in its investment portfolio and maximized them bringing ROI of nearly 4000. 

# ## Companies with great growth potential are those that achieved unicorn valuation in the shortest period of time. These companies include; Nexxi- 1- year, Phantom-1-year, Merama-1-year, Anyscale-2-years, Apna-2-years etc. Picking up investment portfolio from these companies ensures better ROI.

# In[ ]:




