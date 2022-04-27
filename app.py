import streamlit as st
import pandas as pd


# load pickle
@st.cache(suppress_st_warning=True)
def load_data():
    df = pd.read_pickle("a_file.pkl")
    return df


def head_app(data_station):
    st.title("Bikes in Edinburgh")
    st.write(f"We have {len(data_station.index)} stations in Edinburgh.")
    st.map(data_station)
    st.selectbox(f"Select your station for more info:",
                 data_station.start_station_name.sort_values())


def run_app():
    df = load_data()
    df_st = bike_stations(df)
    head_app(df_st)


def bike_stations(data):
    df_stations = data.drop_duplicates('start_station_name').sort_values(
        by="start_station_name")
    df_stations = df_stations.drop(
        columns=["index", "started_at", "ended_at", "duration",
                 "end_station_id", "end_station_name",
                 "end_station_description", "end_station_latitude",
                 "end_station_longitude"]).reset_index()
    df_stations = df_stations.rename(
        columns={"start_station_latitude": "lat",
                 "start_station_longitude": "lon"})
    return df_stations


run_app()
