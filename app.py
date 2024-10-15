import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np
import pydeck

'''
# Your Ride:
'''
d = st.date_input(
    "Current date",
    datetime.date.today())

t = st.time_input(
    'Current Time', datetime.datetime.now())

combined_datetime = datetime.date(2019, 8, 1)
if st.button('Submit date and time'):
    combined_datetime = datetime.datetime.combine(d, t)

pickup_longitude = st.number_input('Insert pickup longitude')
pickup_latitude = st.number_input('Insert pickup latitude')
dropoff_longitude = st.number_input('Insert dropoff longitude')
dropoff_latitude = st.number_input('Insert dropoff latitude')

passenger_count = st.number_input('Insert number of passengers', value=0)

url = 'https://taxifare-1010595293132.europe-west1.run.app/predict/'

params = {"pickup_datetime": combined_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count}

fare = 0

if st.button('Get Fare'):
    response = requests.get(url,params)
    fare = response.json()['fare']
    st.write(f'${round(fare,2)}')

df = pd.DataFrame(
    [[pickup_longitude, pickup_latitude], [dropoff_longitude, dropoff_latitude]],
    columns=["lat", "lon"],
)
st.map(df)
df
view_state = pydeck.ViewState(
    latitude=40, longitude=74, controller=True, zoom=2.4, pitch=30
)
