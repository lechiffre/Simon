#!/usr/bin/env python
# coding: utf-8

# In[1]:


# STEP 1
# IMPORT SIMON P&L2022

import pandas as pd
import numpy as np
from statsmodels.robust.scale import mad

#import the file with raw data
simonProfitAndLoss_df = pd.read_csv('Simon2022_ProfitAndLoss.csv', sep=";", header = None, skiprows=[0],names=["Date", "PaL", "PaL Sum"])

simonProfitAndLoss_df['Date'] = pd.to_datetime(simonProfitAndLoss_df['Date'], infer_datetime_format=True)


#add id to each row starting from 0
#simonProfitAndLoss_df['id'] = pd.RangeIndex(0, len(simonProfitAndLoss_df)) + 1

#replace "," for "." for conversion
simonProfitAndLoss_df['PaL'] = simonProfitAndLoss_df['PaL'].apply(lambda x: float(x.split()[0].replace(',', '.')))
#convert to integer
simonProfitAndLoss_df['PaL'] = simonProfitAndLoss_df['PaL'].astype(int)

#replace "," for "." for conversion
simonProfitAndLoss_df['PaL Sum'] = simonProfitAndLoss_df['PaL Sum'].apply(lambda x: float(x.split()[0].replace(',', '.')))
#convert to integer
simonProfitAndLoss_df['PaL Sum'] = simonProfitAndLoss_df['PaL Sum'].astype(int)
simonProfitAndLoss_df = simonProfitAndLoss_df.drop('PaL Sum', axis=1)



with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(simonProfitAndLoss_df)
