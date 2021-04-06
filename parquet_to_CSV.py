import pandas as pd

parquet_file = r"C:\Users\everis\Desktop\UserData\userdata1.parquet"

# Lee TODOS los Archivos de esa Localidad.
#parquet_file = r"C:\Users\everis\Desktop\UserData"

df =  pd.read_parquet(parquet_file, engine='auto')

print(df)

# Convertimos a CSV
df.to_csv(r"C:\Users\everis\Desktop\UserData\userdata1.csv")