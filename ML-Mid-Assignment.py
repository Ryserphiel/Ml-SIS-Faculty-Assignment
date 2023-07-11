#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the required library
import pandas as pd


# In[2]:


# To display all rows
pd.set_option('display.max_rows', None)

# To display all coloumns
pd.set_option('display.max_columns', None) 


# In[3]:


# Load the data
df = pd.read_excel('SIS_Faculty-List.xlsx')


# In[4]:


# Display the columns name
df.columns


# In[5]:


# Display some information of each column in the dataset
df.info()


# In[6]:


# Show its contents
print(df)


# ### Drop the “LWD”, “Highest Qualification” and “DOCUMENT OTHER PROFESSIONAL CERTIFICATION CRITIERA Five Years Work Experience Teaching Excellence Professional Certifications” columns

# In[7]:


df.drop('LWD', axis=1, inplace=True)


# In[8]:


df.drop('Highest Qualification', axis=1, inplace=True)


# In[9]:


df.drop('DOCUMENT OTHER PROFESSIONAL CERTIFICATION CRITIERA Five Years Work Experience Teaching Excellence Professional Certifications', axis=1, inplace=True)


# In[10]:


# Check to see if they have been dropped
df.columns


# ### Rename the “Courses Taught- Term 201510” column to “Courses Taught - Term Oct 2015”

# In[11]:


df.rename(columns={'Courses Taught- Term 201510': 'Courses Taught - Term Oct 2015'}, inplace=True)


# In[12]:


# Display the columns name to check if the column name has been changed
df.columns


# ### Change Columns name to title case format

# In[13]:


df.rename(columns={'All Qualifications from Profile': 'All Qualifications From Profile'}, inplace=True)


# In[14]:


df.rename(columns={'MAJOR TEACHING FIELD': 'Major Teaching Field'}, inplace=True)


# In[15]:


# Rename Join\nDate and Highest\Qualification\nLevel to eliminate the line break
df.rename(columns={'Join\nDate': 'Join Date', 'Highest\nQualification\nLevel': 'Highest Qualification Level'}, inplace=True)


# In[16]:


# Display the columns to check if the columns name has been changed
df.columns


# ### Change the date to UK format

# In[17]:


# Convert the 'Join Date' column to the UK format
df['Join Date'] = df['Join Date'].dt.strftime('%d-%m-%Y')

print(df['Join Date'])


# ### Replace the missing data “NaN” with “Unknown”

# In[18]:


df.fillna("Unknown", inplace=True)


# In[19]:


# Check to see if the count for all the columns contain 284 entries
df.describe(include = 'O')


# ### Removing all the line break characters “\n” from the dataset

# In[20]:


# Replacing the line breaks character in the "Courses Taught - Term Oct 2015" column with a comma
df['Courses Taught - Term Oct 2015'] = df['Courses Taught - Term Oct 2015'].str.replace("\n", ", ", regex=True)


# In[21]:


print(df['Courses Taught - Term Oct 2015'])


# In[22]:


# Cleaning up individual cells
value = df['Courses Taught - Term Oct 2015'][114]
print(value)


# In[23]:


df.at[114, 'Courses Taught - Term Oct 2015'] = "BUS2403 - Innovation & Entrepreneurship"


# In[24]:


# Verifying that the specific cell is cleaned up
value = df['Courses Taught - Term Oct 2015'][114]
print(value)


# ### Remove duplicate rows

# In[25]:


# Check for duplicates in the "Name" column
duplicates = df.duplicated('Name')

# Subset the dataframe to retrieve only the rows that are duplicates based on the "Name" column
duplicate_rows = df[duplicates]

# Print the duplicate rows
print(duplicate_rows)


# In[26]:


# Check to see if the duplicated name are duplicate or unique by comparing it with the other columns
name_to_search = "Amanda Hobson"  

# Generate a boolean mask by comparing the values in the 'Name' column with the specific name you wish to search for
mask = df['Name'] == name_to_search

# Utilise the boolean mask to apply a filter to the dataframe, allowing you to retrieve the records that match the specified name
records_with_name = df[mask]

# Display the records with the specified name
print(records_with_name)


# In[27]:


# Check to see if the duplicated name are duplicate or unique by comparing it with the other columns
name_to_search = "Zikida Koudou"  

# Generate a boolean mask by comparing the values in the 'Name' column with the specific name you wish to search for
mask = df['Name'] == name_to_search

# Utilise the boolean mask to apply a filter to the dataframe, allowing you to retrieve the records that match the specified name
records_with_name = df[mask]

# Display the records with the specified name
print(records_with_name)


# ### Standardise the “University” column by removing the few entries that contain the country name

# In[28]:


# Display the "University" column so that I can note down the rows that need cleaning
print(df['University'])


# In[29]:


value = df['University'][102]
print(value)


# In[30]:


value = df['University'][160]
print(value)


# In[31]:


value = df['University'][72]
print(value)


# In[32]:


# Removing the country name at the end of the university name; Standardising the formatting

df.at[3, 'University'] = "The University of Swansea"
df.at[4, 'University'] = "New York University"
df.at[23, 'University'] = "Jackson State University"
df.at[49, 'University'] = "Michigan State University"
df.at[50, 'University'] = "University of Nebraska"

df.at[51, 'University'] = "Girne American University"
df.at[53, 'University'] = "Nova Southeastern University"
df.at[54, 'University'] = "International Islamic University"
df.at[55, 'University'] = "University of Salento"
df.at[56, 'University'] = "Paul Cezannel University"

df.at[57, 'University'] = "University of Paris 1 Pantheon-Sorbonne"
df.at[58, 'University'] = "Colorada State University"
df.at[67, 'University'] = "University of Wales"
df.at[69, 'University'] = "Massachusetts Institute of Technology"
df.at[75, 'University'] = "Temple University School of Law"

df.at[82, 'University'] = "Southern New Hampshire University"
df.at[102, 'University'] = "University of Mediterranean, University of Tunis El Manar"
df.at[103, 'University'] = "Amman Arab University"
df.at[104, 'University'] = "University of Tunis"
df.at[105, 'University'] = "University of Manchester"

df.at[106, 'University'] = "Rutgers University"
df.at[107, 'University'] = "Pennsylvania State University"
df.at[120, 'University'] = "Karnataka State Open University"
df.at[132, 'University'] = "Capella University"
df.at[133, 'University'] = "University of Nebraska"

df.at[134, 'University'] = "Hult Internationl Business School"
df.at[136, 'University'] = "JRN Rajasthan Vidyapeeth University"
df.at[140, 'University'] = "University Negros Occidental-Recoleto"
df.at[153, 'University'] = "School for International Training"
df.at[157, 'University'] = "University of National And World Economic"

df.at[160, 'University'] = "American University, University of Kansas"
df.at[170, 'University'] = "Hult Internationl Business School"
df.at[172, 'University'] = "University of Louisville"
df.at[178, 'University'] = "Birla Institute of Tech & School"
df.at[179, 'University'] = "Nova Southern University"

df.at[200, 'University'] = "Northcentral University"
df.at[201, 'University'] = "Walden University"
df.at[205, 'University'] = "Nelson Mandela Metropolitan University"
df.at[209, 'University'] = "University of Pretoria"
df.at[210, 'University'] = "Argosy University"

df.at[225, 'University'] = "University of Nice"
df.at[226, 'University'] = "Tbilisi State University"
df.at[227, 'University'] = "Capella University"
df.at[228, 'University'] = "Grenoble Ecole de Management"
df.at[229, 'University'] = "Universitidad Azteca"

df.at[230, 'University'] = "Cardiff Metropolian University"
df.at[247, 'University'] = "Philippine Christian University"
df.at[248, 'University'] = "Amman Arab University"
df.at[249, 'University'] = "Panteion University"
df.at[256, 'University'] = "The University of Western Australia"

df.at[267, 'University'] = "Birla Institute of Tech & School"
df.at[269, 'University'] = "Birla Institute of Tech & School"
df.at[278, 'University'] = "Durham University"
df.at[279, 'University'] = "South East European University"
df.at[280, 'University'] = "University of Economics"

df.at[281, 'University'] = "University of Mauritus"
df.at[282, 'University'] = "University of San Paulo"
df.at[283, 'University'] = "Virginia Commonwealth University"
df.at[24, 'University'] = "University of Paris Sud 11"
df.at[37, 'University'] = "Thunderbird School of Global Management"
df.at[72, 'University'] = "Institute of Banking Studies, University of Jordan"


# In[33]:


# Display the "University" column for one final check
print(df['University'])


# ### Standardise the qualification in the “Highest Qualification Level” column

# In[34]:


# Display the "Highest Qualification Level" column so that I can note down the rows that need cleaning
print(df['Highest Qualification Level'])


# In[35]:


# Moving all Doctorate to the Ph.D category
df['Highest Qualification Level'].replace('Doctorate', 'Ph.D', inplace=True)

df.at[72, 'Highest Qualification Level'] = "Masters"
df.at[75, 'Highest Qualification Level'] = "Ph.D"
df.at[108, 'Highest Qualification Level'] = "Masters"
df.at[134, 'Highest Qualification Level'] = "Masters"
df.at[154, 'Highest Qualification Level'] = "Ph.D"

df.at[160, 'Highest Qualification Level'] = "Masters"
df.at[193, 'Highest Qualification Level'] = "Bachelor"
df.at[241, 'Highest Qualification Level'] = "Masters"
df.at[243, 'Highest Qualification Level'] = "Ph.D"
df.at[253, 'Highest Qualification Level'] = "Masters"

df.at[261, 'Highest Qualification Level'] = "Masters"
df.at[263, 'Highest Qualification Level'] = "Ph.D"
df.at[274, 'Highest Qualification Level'] = "Ph.D"
df.at[277, 'Highest Qualification Level'] = "Ph.D"


# In[36]:


# Checking the quality of the data cleaning
print(df['Highest Qualification Level'])


# In[37]:


# Display the entire dataset to check the quality of the cleaned data
print(df)


# In[38]:


# Formatting some missed cells
df.at[132, 'Location'] = "Cardiff"
df.at[133, 'Location'] = "Cardiff"
df.at[216, 'Title'] = "Faculty - Business, Comp & Math"


# In[39]:


print(df)


# In[ ]:




