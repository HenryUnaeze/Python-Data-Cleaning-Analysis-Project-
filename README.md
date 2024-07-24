# Python-Data-Cleaning-Analysis-Project-
# 1.0  Description of Dataset 
The project looked at a messy data set of over one thousand unicorn companies across the globe. 
The data set containes list of company names, funding recieved, valuation, industry, Date Joined
city, year founded, country, continent and investors. 
# 2.0 Problem Statement 
Private companies with a valuation over $1 billion as of March 2022, including each 
company's current valuation, funding, country of origin, industry, select investors, and 
the years they were founded and became unicorns.
# 2.1 Recommended Analysis
1. Which unicorn companies have had the biggest return on investment?
2. How long does it usually take for a company to become a unicorn? Has it always 
been this way?
3. Which countries have the most unicorns? Are there any cities that appear to be 
industry hubs?
4. Which investors have funded the most unicorns?

Perform a basic exploratory data analysis of the features of the Unicorn Companies
dataset and come up with at least FOUR (4) data driven overall recommendations to help 
Unicorn Companies in creating good business models and making decisions that will 
focus on companies with high growth potential, diversify investment portfolio and 
prioritize companies with experienced leadership teams.

# Steps followed
 .Step 1: Open up Anacondo Navigator and launch Jupiter Notebook
 
 .Step 2: import the necessary libary for the analysis like;
 
 ![image](https://github.com/user-attachments/assets/a7fabcb7-8a1e-4a28-8abe-7719a3ec1696)
 
 .Step 3: Read the data set from local computer by compying the file path into pandas DataFrame and reading the data as shown below.

 ![image](https://github.com/user-attachments/assets/40d6a46c-f809-46c7-b59b-fdab5bcf8b93)
 
 . Step 4: Data exploration (to better undertand the characteristics of the dataset) 

 . Step 5: Ensure each column has the right datatype through coversion etc. e.g from object to datetime, string to integer etc. check below 

 . Step 6: Indentify columns or rows with missing  values.

 ![image](https://github.com/user-attachments/assets/90f17449-46a5-4831-ab6b-cbb57db8c916)

 . Step 7: Replacing empty columns with the right the city names missing 

 ![image](https://github.com/user-attachments/assets/f7040d7c-f12e-45fe-bc0d-219e61bf0237)
 . Step 8: Filling the column of missing select investors values through research. 

 ![image](https://github.com/user-attachments/assets/017a16ee-0c22-47ca-8385-bde1f9697f1e)

 . Step 9: Removing non-numeric characters from numerical columns like Valuation and Funding e.g, dollar sign and Billions

 ![image](https://github.com/user-attachments/assets/0bbbc7ea-949f-4999-9090-f4bbf01a7715)

 ![image](https://github.com/user-attachments/assets/d638bc24-8d54-4ac7-a183-dd60528698a2)
 
 . Step 10: Some companies have no funding and in order to compute for ROI, zero values are replaced by median value of funding. 
 
 ![image](https://github.com/user-attachments/assets/74358945-a4bd-4f1b-8ecd-091929203f49)

. Step 11: Creating Return on Investment (ROI) column and computing the value using this code

 ![image](https://github.com/user-attachments/assets/d5450a59-fade-4755-ba78-f8fa97e133cb)

. Step 12: Getting the number for days/years taken to become a unicorn company by substracting the year founded from the years joined. If in days the result is divided by 365.25 to covert to year.

 ![image](https://github.com/user-attachments/assets/e85dce53-9a04-4fb1-b807-235363022c4f)

. Step 13: Removing the string 'days' and converting string to integer using the code below:

 ![image](https://github.com/user-attachments/assets/825d3f9d-2d45-4e8f-91e6-ad0051ea9d48)

# Solution/ Insights to the problem statement:

## Question 1: Which Company has the highest RIO

![image](https://github.com/user-attachments/assets/2d75a80d-a998-43e7-bd1c-50ab7b8608ef)


 ## Plot showing Companies by ROI 
 
 ![image](https://github.com/user-attachments/assets/5f227811-5977-4a47-9c2c-74c122b63898)
 
## Insights: From the plot above , Zapier leads in the ROI with a value of 3999 followed the likes of Dunamu with 125, Workhuman at 110 etc

## Question 2: How long it takes for companies to become Unicorn and has that always been the trend?

![image](https://github.com/user-attachments/assets/da002c19-d54b-4ce8-bc82-e1e738fc7a5e)

![image](https://github.com/user-attachments/assets/6b1b0a2f-3034-44d4-b7f7-3f9f02cc459f)

![image](https://github.com/user-attachments/assets/be2cf118-eb6f-4252-a1bd-e3ceb1be3e0f)

![image](https://github.com/user-attachments/assets/105a9aab-ee26-4114-a587-76b3ee7b061e)

### Insights: From the plots above, in the past it takes the range of 13-37 years for a company to become a unicorn but in recent time it takes from 1-3 years for a company to be a unicorn

## Which countries have the most unicorns? Are there any cities that appear to be industry hub?

![image](https://github.com/user-attachments/assets/e48afd2a-121d-496a-a73d-fa20a59bc77b)

## Plot showing Companies and the number of unicorns 

![image](https://github.com/user-attachments/assets/f0a6ab32-36ac-4bb0-989a-6c628f79c869)

## Insights :3a; United States leads with 562 unicorns followed by China at 173 and India coming at 3rd place with 65 unicorns from the bar plot above 

![image](https://github.com/user-attachments/assets/08c33885-fe6d-4004-83df-be4cbbe4bfa2)

![image](https://github.com/user-attachments/assets/784ae0ca-3b47-4c3e-a1af-0533a5a88fa5)

 ## Insights :3b; Cities that appears to be hubs have more unicorns in them and they are; San Francisco with 153 unicorn companies followed by New York at 104 unicorns and Beijing having 63 as 3rd city. 

 ## Question 3: Which investors have funded the most unicorns?
 
 ![image](https://github.com/user-attachments/assets/322d501e-4d7d-4f2b-b888-9bbfca983c85)

 ![image](https://github.com/user-attachments/assets/1218c2ef-32c6-4ce5-90db-11871a7fc3da)

## Insights: Tiger Global Management, Sequoia Capital China, SIG Asia Investment, Sina Weibo, Soft bank Group etc are the to investors with highest funding 

 ## Question 4: Which Investors Team have better return on investement (ROI) demostrating experienced leadership ?

 ![image](https://github.com/user-attachments/assets/8e977d00-90be-4112-9306-c3cb1c4d5ce3)

![image](https://github.com/user-attachments/assets/bd50b7e2-a489-4e0b-8f81-402b144d5544)

## Insights:  4a; The above plot demonstrate that despite the less funding of just 1million dollars, Sequoia Capital, Bessemer Venture Partners, Threshold Ventures were able to identify opportunities in its investment portfolio and maximized them bringing ROI of nearly 4000. 

## Insights:  4b; Companies with great growth potential are those that achieved unicorn valuation in the shortest period of time. These companies include; Nexxi- 1- year, Phantom-1-year, Merama-1-year, Anyscale-2-years, Apna-2-years etc. Picking up investment portfolio from these companies ensures better ROI.
