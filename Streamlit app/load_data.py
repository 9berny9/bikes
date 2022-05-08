def load_data():
    df = pd.read_pickle("a_file.pkl")
    return df


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


df = load_data()
df_st = bike_stations(df)
