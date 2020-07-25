# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 20:36:03 2020

@author: haria
"""

import pandas as pd
import bar_chart_race as bcr

file_path = r'C:\Users\haria\Desktop\Development\Python\Projects\Python Tutorial\Bar Chart Race'

data = pd.read_csv(file_path + '\\annual_co2_emisson.csv')

table = pd.pivot_table(data, values='Annual CO2 emissions (tonnes )',columns='Entity',index='Year')

table = table.fillna(0)
table.index = pd.to_datetime(table.index, format='%Y')
#to-do - remove columns of world and continents
df = table

df.drop(['World','Africa','Americas (other)','Europe (other)','EU-28','Asia and Pacific (other)','Middle East','International transport'],axis=1,inplace=True)

bcr.bar_chart_race(
    df=df.loc['1800':],
    filename='annual_co2_emissions.mp4',
    orientation='h',
    sort='desc',
    n_bars=15,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=10,
    interpolate_period=False,
    label_bars=True,
    bar_size=.95,
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    period_fmt='%Y',
    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                      's': f'Total annual emissions: {v.sum():,.0f}',
                                      'ha': 'right', 'size': 8, 'family': 'Courier New'},
    #perpendicular_bar_func='max',
    period_length=250,
    figsize=(10, 5),
    dpi=300,
    cmap='tab20c',
    title='Annual CO2 emissions (tonnes) by country',
    title_size='',
    bar_label_size=4,
    tick_label_size=4,
    shared_fontdict={'family' : 'Helvetica', 'color' : '.1'},
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=True)