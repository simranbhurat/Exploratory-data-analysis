#  Importing essential libraries



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


## Importing datasets

Ipl=pd.read_csv('matches.csv')

## Analyse the Dataset

Ipl.head()

Ipl.shape

Ipl.info()

Ipl.describe()

Ipl.isnull().sum()

# Frequency of man of the Match award

Ipl['player_of_match'].value_counts()

## Top 5 players with Man of the match award

Ipl['player_of_match'].value_counts().head(5)

list(Ipl['player_of_match'].value_counts()[0:5].keys())

## Data Visualisation of Player_of_match

plt.bar(list(Ipl['player_of_match'].value_counts()[0:5].keys()),list(Ipl['player_of_match'].value_counts()[0:5]),color=['violet','indigo','blue','green','yellow'])
plt.show()

# The graph above shows that Chris Gayle is the most successful player in Ipl

