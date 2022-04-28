import streamlit as st
import pandas as pd


# load pickle
@st.cache(suppress_st_warning=True)
def load_data():
    df = pd.read_pickle("a_file.pkl")
    return df


def stations_description(data, data_station):
    st.title("Bikes in Edinburgh")
    st.write(f"We have {len(data_station.index)} bike stations in Edinburgh.")
    st.map(data_station)
    station_names = data_station.name.drop_duplicates()
    station = st.selectbox(f"Select your station for more info:",
                           station_names)
    station_info(data, data_station, station)


def station_info(data, data_station, station):
    if station:
        selected_df = data_station[
            data_station.name == station
            ].reset_index()[["id", "description", "lat", "lon"]]
        if len(selected_df.index) > 1:
            st.markdown(f"Selected station has {len(selected_df.index)} "
                        f"habitats")
        st.markdown("### Station info:")
        for i, value in enumerate(selected_df.description):
            for n, lat in enumerate(selected_df.lat):
                for o, lon in enumerate(selected_df.lon):
                    if i == n and n == o:
                        st.write(f"The {station} is near <b>{value}</b>",
                                 unsafe_allow_html=True)
                        st.write(f"- Latitude: {lat}")
                        st.write(f"- Longitude: {lon}")


def run_app():
    df = load_data()
    df_st = bike_stations(df)
    stations_description(df, df_st)


def bike_stations(data):
    df_stations = data.drop_duplicates('start_station_id').sort_values(
        by="start_station_name")
    df_stations = df_stations.drop(
        columns=["index", "started_at", "ended_at", "duration",
                 "end_station_id", "end_station_name",
                 "end_station_description", "end_station_latitude",
                 "end_station_longitude"])
    df_stations = df_stations.rename(
        columns={"start_station_name": "name",
                 "start_station_id": "id",
                 "start_station_description": "description",
                 "start_station_latitude": "lat",
                 "start_station_longitude": "lon"})
    return df_stations


