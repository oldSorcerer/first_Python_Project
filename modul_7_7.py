import pandas as pd
data = pd.read_csv('programm.csv')
print(data.sort_values(by="name", ascending=True))