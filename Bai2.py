import pandas as pd
import requests
from io import BytesIO

url = 'https://docs.google.com/spreadsheets/d/1BnOzoEG0s6c8MpiUANZ0_pawXNHqdkid/export?format=xlsx'
response = requests.get(url)

excel_data = BytesIO(response.content)
df = pd.read_excel(excel_data)

filtered_df = df[
    (df['vpv2'] % 2 == 0) & 
    (df['pDisCharge'] % 2 == 0) & 
    (df['prec'] % 2 == 1)
].copy()

filtered_df['Sum_vBUS'] = filtered_df['vBus1'] + filtered_df['vBus2']

filtered_df.to_csv('Data_new.csv', index=False)

# ✅ In kết quả ra màn hình
print(filtered_df[['vpv2', 'pDisCharge', 'prec', 'vBus1', 'vBus2', 'Sum_vBUS']])
