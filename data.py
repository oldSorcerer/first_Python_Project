import pandas as pd

data = pd.read_csv("programm.csv")
print(data)

name1 = "Ivan"

answ2 = data[data["name"] == name1].values

print(answ2)

#print(" ".join(answ2[0]))