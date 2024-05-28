import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df['Contact Start Date Time'] = pd.to_datetime(df['Contact Start Date Time'])
    df['Contact Start Date'] = pd.to_datetime(df['Contact Start Date'])
    df['Contact Agent Name'].fillna('unnamed agent', inplace=True)
    return df

def extract_time_features(df):
    df['Hour of Day'] = df['Contact Start Date Time'].dt.hour
    df['Day of Week'] = df['Contact Start Date Time'].dt.day_name()
    return df

def plot_peak_call_times(df):
    df = extract_time_features(df)
    heatmap_data = df.pivot_table(index='Day of Week', columns='Hour of Day', values='Contact ID', aggfunc='count')
    heatmap_data = heatmap_data.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='.1f')  # Use float format for annotations
    plt.title('Heatmap of Call Volumes by Hour and Day of Week')
    plt.xlabel('Hour of Day')
    plt.ylabel('Day of Week')
    plt.show()

def plot_seasonal_decomposition(df):
    df.set_index('Contact Start Date Time', inplace=True)
    df_resampled = df.resample('D').size()
    
    decomposition = seasonal_decompose(df_resampled, model='additive')
    fig = decomposition.plot()
    fig.set_size_inches(12, 8)
    plt.show()

def plot_call_volume_forecast(df):
    df_resampled = df.resample('D').size()
    model = ExponentialSmoothing(df_resampled, trend='add', seasonal='add', seasonal_periods=7)
    fit = model.fit()
    forecast = fit.forecast(30)
    
    plt.figure(figsize=(12, 6))
    plt.plot(df_resampled, label='Observed')
    plt.plot(forecast, label='Forecast', color='red')
    plt.title('Call Volume Forecast')
    plt.xlabel('Date')
    plt.ylabel('Number of Calls')
    plt.legend()
    plt.show()

def plot_hold_time_vs_call_duration(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='HoldTime(Seconds)', y='Call Time(Minutes)', data=df)
    plt.title('Hold Time vs. Call Duration')
    plt.xlabel('Hold Time (Seconds)')
    plt.ylabel('Call Time (Minutes)')
    plt.show()


def call_duration_dist(df):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Call Time(Minutes)'], bins=30, kde=True)
    plt.title('Distribution of Call Durations')
    plt.xlabel('Call Time (Minutes)')
    plt.ylabel('Frequency')
    plt.show()
    
def hold_to_call_time(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='HoldTime(Seconds)', y='Call Time(Minutes)', data=df)
    plt.title('Hold Time vs. Call Duration')
    plt.xlabel('Hold Time (Seconds)')
    plt.ylabel('Call Time (Minutes)')
    plt.show()


def plot_peak_call_times(df):
    df = extract_time_features(df)
    heatmap_data = df.pivot_table(index='Day of Week', columns='Hour of Day', values='Contact ID', aggfunc='count')
    heatmap_data = heatmap_data.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='.1f')  # Use float format for annotations
    plt.title('Heatmap of Call Volumes by Hour and Day of Week')
    plt.xlabel('Hour of Day')
    plt.ylabel('Day of Week')
    plt.show()

def plot_seasonal_decomposition(df):
    df.set_index('Contact Start Date Time', inplace=True)
    df_resampled = df.resample('D').size()
    
    decomposition = seasonal_decompose(df_resampled, model='additive')
    fig = decomposition.plot()
    fig.set_size_inches(12, 8)
    plt.show()


def plot_call_volume_forecast(df):
    df_resampled = df.resample('D').size()
    model = ExponentialSmoothing(df_resampled, trend='add', seasonal='add', seasonal_periods=7)
    fit = model.fit()
    forecast = fit.forecast(30)
    
    plt.figure(figsize=(12, 6))
    plt.plot(df_resampled, label='Observed')
    plt.plot(forecast, label='Forecast', color='red')
    plt.title('Call Volume Forecast')
    plt.xlabel('Date')
    plt.ylabel('Number of Calls')
    plt.legend()
    plt.show()



