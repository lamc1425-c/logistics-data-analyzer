# Importamos pandas y le asignamos un alias "pd"
import pandas as pd

# En la variable df se guardará la lectura del archivo o ruta
df = pd.read_csv("data/orders.csv")

print(df.head())
