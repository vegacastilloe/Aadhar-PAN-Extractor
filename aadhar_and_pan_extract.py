import pandas as pd
import re
from tabulate import tabulate

# 🧩 Datos originales
df_raw = pd.read_excel(xl, header=1)
df_raw.columns = df_raw.columns.str.strip()
df_input = df_raw.iloc[:, :2].dropna(how='all')

# 📥 Renombrar columnas opcional
df_input.columns = ['Names', 'Strings']

# 🔍 Funciones para extraer identificadores
def extract_aadhar(text):
    match = re.search(r'\d{12}', text)
    return match.group(0) if match else ''

def extract_pan(text):
    match = re.search(r'[A-z]{5}\d{4}[A-z]', text)
    return match.group(0) if match else ''

# 🔣 Aplicar funciones
df_input['Aadhar'] = df_input['Strings'].apply(extract_aadhar).astype(str)
df_input['PAN'] = df_input['Strings'].apply(extract_pan)
df_input['Aadhar Given'] = df_raw.iloc[:, 2].copy().fillna('').astype(str).str.replace('.0', '', regex=False)
df_input['PAN Given'] = df_raw.iloc[:, 3].copy().fillna('')
df_input['Match1'] = df_input['Aadhar'] == df_input['Aadhar Given']
df_input['Match2'] = df_input['PAN'] == df_input['PAN Given']

# 📈 Mostrar resultado
print(tabulate(df_input.values, headers=df_input.columns, tablefmt='psql'))

# 💾 Exportación opcional
# df_input.to_excel("aadhar_and_pan_extract_output.xlsx", index=False)
