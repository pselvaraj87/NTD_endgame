import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

data_dir = '/Users/prashanthselvaraj/Desktop/NTD_endgame'
os.makedirs(os.path.join(data_dir, 'figures'), exist_ok=True)

def write_individual_files():
    # Write individual files
    df = pd.read_csv(os.path.join(data_dir, 'processed', 'all_countries.csv'))

    # MDA files
    df_mda = df[df['measure_id']==1]
    df_mda.to_csv(os.path.join(data_dir, 'processed', 'mda1.csv'))

    df_mda = df[df['measure_id'] == 2]
    df_mda.to_csv(os.path.join(data_dir, 'processed', 'mda2.csv'))

    # Prevalence data
    df_mda = df[df['measure_id'] == 0]
    df_mda.to_csv(os.path.join(data_dir, 'processed', 'l3_prevalence.csv'))


def plot_prevalence():
    # GDX data
    # df = pd.read_csv(os.path.join(data_dir, 'processed', 'l3_prevalence.csv'))

    # Per's data
    df = pd.read_csv('/Users/prashanthselvaraj/Desktop/NTD_endgame/processed/lf_ihme_mean_iu_prev.csv')

    scenarios = df['scenario'].unique()

    # df_mda = pd.read_csv(os.path.join(data_dir, 'processed', 'mda2.csv'))
    # df_mda

    # scenario_key = {0: '0', 1: '1', 2: '2', 3: '3a', 4: '3b', 5: '3c', 6: '-1'}

    for s in scenarios:
        fig, axs = plt.subplots(1, 1)

        dftemp = df[df['scenario'] == s]
        df_overall_mean = dftemp.groupby(['year_id'])['prev_rate'].apply(np.mean).reset_index()

        for g, df_g in dftemp.groupby('IU_ID'):
            axs.plot(df_g['year_id'], df_g['prev_rate'], color='k', alpha=0.1, lw=0.5)

        axs.plot(df_overall_mean['year_id'], df_overall_mean['prev_rate'], color='r', alpha=1, lw=2)

        axs.set_title('Scenario %s' % s.split('_')[1])
        axs.set_xlabel('Year')
        axs.set_xlim([2018, 2040])
        axs.set_xticks([i for i in range(2020, 2041, 5)])

        plt.savefig(os.path.join(data_dir, 'figures', 'scenario_%s.png' % s.split('_')[1]))


if __name__ == '__main__':
    # write_individual_files()

    plot_prevalence()
