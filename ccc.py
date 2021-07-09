import pandas as pd

df = pd.read_csv('q4_2019_6.xlsx')

print(df.tail())



print("-----------------------------------------------------------")
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
