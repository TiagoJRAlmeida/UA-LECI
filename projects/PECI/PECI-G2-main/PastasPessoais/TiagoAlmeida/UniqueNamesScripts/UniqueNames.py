import pandas as pd
import json

def getStandardUniqueNames():
    print("\nReading Standard Table...")
    df = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Tabela_de_Agentes_Standardizados.csv', sep=';', low_memory=False)
    print("Standard Table read!")
    print(f"Number of rows: {len(df)}")
    
    row_count = 0
    unique_names = {}
    unique_names_file = open("Standard-Unique_Names.json", "w", encoding="utf-8")
    for _, row in df.iterrows():
        row_count += 1
        row_name = str(row["name"])

        if row_name not in unique_names:
            unique_names[row_name] = 1
        else:
            unique_names[row_name] += 1

        print(f"\rCurrent Row: {row_count}", end="")
        
    
    sorted_Unique_Names = dict(sorted(unique_names.items(), key=lambda item: item[1], reverse=True))
    json.dump(sorted_Unique_Names, unique_names_file, ensure_ascii=False, indent=4)
    print("\nStandard Table Unique Names Saved on file Standard-Unique_Names.json\n")


def getDepartureUniqueNames():
    print("\nReading Departure Table...")
    df = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Departure_Document_Data.csv', sep=';', low_memory=False)
    print("Departure Table read!")
    print(f"Number of rows: {len(df)}")

    row_count = 0
    unique_names = {}
    unique_names_file = open("Departure-Unique_Names.json", "w")
    for _, row in df.iterrows():
        row_count += 1
        row_name = str(row["name"])

        if row_name not in unique_names:
            unique_names[row_name] = 1
        else:
            unique_names[row_name] += 1

        print(f"\rCurrent Row: {row_count}", end="")
        
    
    sorted_Unique_Names = dict(sorted(unique_names.items(), key=lambda item: item[1], reverse=True))
    json.dump(sorted_Unique_Names, unique_names_file, ensure_ascii=False, indent=4)
    print("\nDeparture Table Unique Names Saved on file Departure-Unique_Names.json\n")



def getTransportUniqueNames():
    print("\nReading Transport Table...")
    df = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Transport_Document_Data.csv', sep=';', low_memory=False)
    print("Transport Table read!")
    print(f"Number of rows: {len(df)}")
    
    row_count = 0
    unique_names = {}
    unique_names_file = open("Transport-Unique_Names.json", "w")
    for _, row in df.iterrows():
        row_count += 1
        row_name = str(row["name"])

        if row_name not in unique_names:
            unique_names[row_name] = 1
        else:
            unique_names[row_name] += 1
        
        print(f"\rCurrent Row: {row_count}", end="")
        
    
    sorted_Unique_Names = dict(sorted(unique_names.items(), key=lambda item: item[1], reverse=True))
    json.dump(sorted_Unique_Names, unique_names_file, ensure_ascii=False, indent=4)
    print("\nTransport Table Unique Names Saved on file Transport-Unique_Names.json\n")



getStandardUniqueNames()
print("-"*50)
getDepartureUniqueNames()
print("-"*50)
getTransportUniqueNames()