from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql+pymysql://student2:eh2BjVEpYmDcT96E@data.engeto.com:3306/data_academy_02_2022")
query = 'SELECT * FROM edinburgh_bikes'

df = pd.read_sql(sql=query, con=engine)
df.to_pickle("a_file.pkl")
