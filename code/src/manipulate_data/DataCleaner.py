## The original data contained issues or rather like most real world data, this data was dirty. Some rows had all features marked as NaN. In some rows, the 'tm' and 'ph' feature columns had been swapped.
## This code file takes care of both of those issues.

## Imports
import numpy as np
import pandas as pd

import os
from IPython.display import display

## First read the data
train_df = pd.read_csv("/Users/riyazachariah/Thermostability_Prediction/data/raw/train.csv")

## Now explore the data
print(train_df.describe())

## Look for entries where the pH and tm values have been swapped
swap_mask = train_df['pH']>14

## Create a temp column to store the tm values temporarily
train_df['tm_temp'] = train_df['tm']

## Do the swap
train_df.loc[swap_mask, 'tm'] = train_df.loc[swap_mask, 'pH']
train_df.loc[swap_mask, 'pH'] = train_df.loc[swap_mask, 'tm_temp']

## Alternatively, I can also use the numpy.where() function
## train_df['tm'] = np.where(train_df['pH']>14, train_df['pH'], train_df['tm'])

## Look for missing/NaN values
nan_mask = train_df.isnull()
train_missing = train_df[nan_mask]
columns_with_missing = train_df.columns[nan_mask.any()]

## Drop rows that are missing values in either sequence or tm columns
train_df = train_df.dropna(subset=['protein_sequence', 'tm'], inplace=True)

## An interactive look at the corrected dataframe
display(train_df)

## Compare with the updated training set provided by the team
