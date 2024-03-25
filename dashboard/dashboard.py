import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

#ambil data day dan hour

data_df = pd.read_csv("https://raw.githubusercontent.com/hamzic05/Submission-Bike-Exploratory-Data-Analysis/main/dashboard/all_data.csv")
data_df

st.title('Submissions Dicoding')
date_columns = ["dteday"]

for column in date_columns:
    data_df[column] = pd.to_datetime(data_df[column])

min_date = data_df["dteday"].min()
max_date = data_df["dteday"].max()
with st.sidebar:
  # Mengambil start_date & end_date dari date_input
  start_date, end_date = st.date_input(
    label='Rentang Waktu',min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
  )

main_df = data_df[(data_df["dteday"] >= str(start_date)) & (data_df["dteday"] <= str(end_date))]

st.subheader("1. Total Penyewa Sepeda Harian")
seasonal_data = data_df.groupby('season_daily')['cnt_daily'].mean()
season_names = ['Spring', 'Summer', 'Fall', 'Winter']
plt.bar(season_names, seasonal_data)
plt.xlabel('Musim')
plt.ylabel('Re-rata Jumlah Sewa Harian')
st.pyplot(plt)

st.subheader("2. perbedaan penyewa sepeda harian saat hari kerja (workingday) dengan hari libur (holiday)")
plt.figure(figsize=(8, 5))
sns.boxplot(x="workingday_daily", y="cnt_daily", data=data_df)
plt.xlabel("Workingday")
plt.ylabel("Jumlah Sewa Sepeda Harian")
st.pyplot(plt)

