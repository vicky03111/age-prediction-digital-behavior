import pandas as pd
import numpy as np


def aggregate_visits(visits):
    if len(visits[visits.duplicated()]) > 0:
        visits = visits.drop_duplicates()
    visits_agg = visits.groupby('user_id').agg(
        total_visits=('session_id', 'count'),
        favorite_daytime=('daytime', lambda x: x.mode().iloc[0]),
        favorite_category=('website_category', lambda x: x.mode().iloc[0]),
        category_count=('website_category', 'nunique'),
        date_count=('date', 'nunique')
    )
    time_agg = visits.groupby(['user_id', 'daytime']).size().unstack(fill_value=0)
    time_agg.columns = ['visits_' + col for col in time_agg.columns]
    category_agg = visits.groupby(['user_id', 'website_category']).size().unstack(fill_value=0)
    category_agg.columns = ['cat_' + col.replace(' ', '_') for col in category_agg.columns]
    visits_agg = visits_agg.merge(time_agg, on='user_id')
    visits_agg = visits_agg.merge(category_agg, on='user_id')

    visits_agg['pct_вечер'] = visits_agg['visits_вечер'] / visits_agg['total_visits']
    visits_agg['pct_день'] = visits_agg['visits_день'] / visits_agg['total_visits']
    visits_agg['pct_ночь'] = visits_agg['visits_ночь'] / visits_agg['total_visits']
    visits_agg['pct_утро'] = visits_agg['visits_утро'] / visits_agg['total_visits']
    visits_agg = visits_agg.drop(columns=['visits_вечер', 'visits_день', 'visits_ночь', 'visits_утро'])
    return visits_agg


def edit_visits_cats(df):
    df['log_total_visits'] = np.log1p(df['total_visits'])
    web_cats = [col for col in df.columns if 'Category' in col]
    for col in web_cats:
        df['log_' + col] = np.log1p(df[col])
    df = df.drop(columns=(web_cats + ['total_visits']))
    return df


def merge_dfs(dfs, on='user_id', how='outer'):
    df = dfs[0]
    for i in dfs[1:]:
        df = df.merge(i, on=on, how=how)
    return df