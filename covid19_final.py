import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing

import warnings
warnings.filterwarnings("ignore")

### importing data files
df_confirmed = pd.read_csv('global_covid_confirmed_daily_updates.csv', index_col=0)
df_death = pd.read_csv('global_covid_deaths_daily_updates.csv', index_col=0)

print('confirmed cases dataset shape: ', df_confirmed.shape)
print('death cases dataset shape: ', df_death.shape)


### converting date columns to datetime index
df_confirmed.columns = pd.to_datetime(df_confirmed.columns)
df_confirmed.columns.freq = 'D'

df_death.columns = pd.to_datetime(df_death.columns)
df_death.columns.freq = 'D'


### Prediction
confirm = pd.DataFrame()
death = pd.DataFrame()

print('Running predictions for next date...')

for n in range(0,188):
    model_1 = ExponentialSmoothing(endog=df_confirmed.iloc[n],trend='add').fit()
    model_2 = ExponentialSmoothing(endog=df_death.iloc[n],trend='add').fit()
    fcast1 = model_1.forecast(1)
    fcast2 = model_2.forecast(1)
    fcast1 = round(fcast1, 1)
    fcast2 = round(fcast2, 1)
    confirm = pd.concat([confirm, fcast1])
    death = pd.concat([death, fcast2])
    
confirm.columns = ['Confirmed']
death.columns = ['Deaths']
confirm.set_index(df_confirmed.index, inplace=True)
death.set_index(df_confirmed.index, inplace=True)

print('Generating submission file...')

submission = pd.merge(confirm,death, on=confirm.index)
submission.rename(columns={'key_0': 'Country/Region'}, inplace=True)
submission.to_excel("submission_covid-19.xlsx", index=False)

print('DONE!')