import pandas as pd

df_transport = pd.read_csv("D:/Projeto PECI/Transport_Document_Data.csv",sep=";")
df_departure = pd.read_csv("D:/Projeto PECI/Departure_Document_Data.csv",sep=";")

unique_words = {i for i in df_transport["name"]}
unique_words.update({i for i in df_departure["name"]})

print(len(unique_words))

with open("UniqueNames.txt","w",encoding="utf-8") as file:
    file.write("".join({i + '\n' for i in unique_words}))