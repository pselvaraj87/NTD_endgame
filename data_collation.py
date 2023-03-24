import os
import pandas as pd

data_dir = '/Users/prashanthselvaraj/Desktop/NTD_endgame'
os.makedirs(os.path.join(data_dir, 'Processed'), exist_ok=True)
cols = ['scenario', 'espen_loc', 'measure_id', 'year_id', 'mean']

df_full = pd.DataFrame()

for f in os.listdir(data_dir):
    if '.csv' in f:
        df = pd.read_csv(os.path.join(data_dir, f), encoding='latin1')
        df.reset_index(inplace=True)

        seeds = ['draw_%i' %i for i in range(200)]
        df['mean'] = df[seeds].mean(axis=1)
        df = df[cols]

        df.to_csv(os.path.join(data_dir, 'Processed', f))

        df_full = pd.concat([df_full, df])

df_full.to_csv(os.path.join(data_dir, 'processed', 'all_countries.csv'))



