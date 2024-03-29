import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

 
data = pd.read_csv('main_data.csv')
st.title ('Dashboard Bike Sharing Dataset')

tab1, tab2 = st.tabs(['Data', 'Analisis Data'])

with tab1:
        
    st.write(data)

    total=data.cnt.sum()
    st.metric("Total Sewa", value=total)

with tab2:
    monthly_usage = data.groupby(data['dteday'])['cnt'].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(monthly_usage.index, monthly_usage.values, marker='o', linestyle='-')
    ax.set_title('Seasonal patterns of bicycle use')
    ax.set_xlabel('Month')
    ax.set_ylabel('Number of Bikes shared')
    ax.tick_params(axis='x', rotation=5)
    ax.grid(True)
    st.title('Seasonal patterns of bicycle use')
    st.pyplot(fig)

    data['day_of_week'] = pd.to_datetime(data['dteday']).dt.dayofweek
    daily_usage_weekday = data.groupby('day_of_week')['cnt'].mean()
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(days_of_week, daily_usage_weekday)
    ax.set_title('Differences in bicycle shared patterns between weekdays and weekends')
    ax.set_xlabel('Day in a week')
    ax.set_ylabel('Average Number of Bikes Borrowed')
    ax.set_ylim(0, max(daily_usage_weekday) * 1.1)
    ax.grid(axis='y')
    st.title('Differrent patterns of bicycle use')
    plt.tight_layout()
    st.pyplot(fig)

st.caption('copyright (c) Arya Putra Nugraha 2024')

