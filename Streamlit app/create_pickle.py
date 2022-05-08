from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql+pymysql://student2:eh2BjVEpYmDcT96E@data.engeto.com:3306/data_academy_02_2022")
query = 'SELECT * FROM edinburgh_bikes'

data = pd.read_sql(sql=query, con=engine)

# change start-time column to datetime format
data['started_at'] = pd.to_datetime(
    data['started_at'])
# change end-time column to datetime format
data['ended_at'] = pd.to_datetime(
    data['ended_at'])

data.to_pickle("a_file.pkl")
