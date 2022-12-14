# -*- coding: utf-8 -*-
"""Zomato EDA

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WZWwRLR2u_j4Q3xt9BefvaLRBPxB8lL_
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

df = pd.read_csv('/content/zomato.csv',encoding='latin-1')

df.head()

df.shape

df.columns

df.info()

df.describe()

df.isnull().sum()

sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')

df_country = pd.read_excel('/content/Country-Code.xlsx')

df_country.head()

final_df = pd.merge(df,df_country,on='Country Code',how='left')

final_df.head()

final_df.dtypes

country_names=final_df.Country.value_counts().index

country_val=final_df.Country.value_counts().values

plt.pie(country_val[:3],labels=country_names[:3],autopct='%1.2f%%')

final_df.columns

ratings=final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating Counts'})

ratings.head()

plt.rcParams['figure.figsize']=(12,6)
sns.barplot(x='Aggregate rating', y = 'Rating Counts', data = ratings)

sns.barplot(x='Aggregate rating', y = 'Rating Counts', data = ratings,hue='Rating color',palette=['white','red','orange','yellow','green','green'])

sns.countplot(x='Rating color',data=ratings,palette=['white','red','orange','yellow','green','green'],order=df.deck.value_counts().iloc[:3].index)

final_df.groupby(['Aggregate rating','Country']).size().reset_index()

final_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()

final_df.columns

final_df[final_df['Has Online delivery']=='Yes'].Country.value_counts()

final_df[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()

final_df.City.value_counts().index

city_values = final_df.City.value_counts().values
city_labels = final_df.City.value_counts().index

plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.2f%%')

