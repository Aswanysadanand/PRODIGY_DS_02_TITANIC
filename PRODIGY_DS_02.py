#!/usr/bin/env python
# coding: utf-8

# PRODIGY INFOTECH DATA SCIENCE INTERNSHIP

# MAY 2024

# AUTHOR: ASWANY SADANAND

# TASK 02

# Perform data cleaning and exploratory data analysis (EDA) on a dataset of your choice, such as the Titanic dataset from Kaggle. Explore the relationships between variables and identify patterns and trends in the data.

# #importing necessary libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# #loading datasets

# In[2]:


df=pd.read_csv('Downloads/train.csv')


# In[3]:


df


# #checking sum of null values

# In[4]:


df.isnull().sum()


# In[5]:


# Separate categorical and numerical columns
categorical_columns = df.select_dtypes(include=['object', 'category']).columns
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

# Print the lists of categorical and numerical columns
print("Categorical columns:", categorical_columns)
print("Numerical columns:", numerical_columns)


# #removing unwanted columns

# In[6]:


cols_to_drop=['Name','PassengerId','Ticket','Cabin']


# In[7]:


df.drop(cols_to_drop,axis=1,inplace=True)


# In[8]:


df


# In[18]:


df['Pclass'].value_counts()


# In[19]:


df['SibSp'].value_counts()


# In[20]:


df['Parch'].value_counts()


# In[21]:


df['Pclass'].value_counts()


# EXPLORATORY DATA ANALYSIS

# #plotting survived Vs Passengerclass

# In[9]:


# Plots

sns.countplot(data=df, x="Survived")
plt.show()

sns.countplot(data=df, x="Pclass")
plt.show()


# In[10]:


sns.countplot(data=df, x="Pclass", hue="Survived")
plt.show()


# #plotting sex versus passenger count

# In[11]:


sns.countplot(data=df, x="Sex")
plt.show()


# #plotting sex versus survived

# In[12]:


sns.countplot(data=df, x="Sex", hue="Survived")
plt.show()


# #plotting embarked versus survived

# In[13]:


sns.countplot(data=df, x="Embarked")
plt.show()

sns.countplot(data=df, x="Embarked", hue="Survived")
plt.show()


# #plotting siblings/spouses versus survived

# In[15]:


sns.countplot(data=df, x="SibSp")
plt.show()

sns.countplot(data=df, x="SibSp", hue="Survived")
plt.show()


# #plotting parents/children versus survived

# In[16]:


sns.countplot(data=df, x="Parch")
plt.show()

sns.countplot(data=df, x="Parch", hue="Survived")
plt.show()


# #CONCLUSION
# 
# 1.Passengers in class 1 survived more when compared to class 2 and 3.
# 2.Male passengers survived more when compared to female passengers.
# 3.Passengers embarked from port Southampton survived more when compared to port Queenstown and port Cherbourg.
# 4.Most of the siblings/spouses died compared to survived ones.
# 5.Most of the parents died compared to the survived ones.
