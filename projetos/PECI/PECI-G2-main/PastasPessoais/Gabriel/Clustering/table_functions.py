import pandas as pd

def read_standard_table():
    print("\nReading Standard Table...")
    df = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Tabela_de_Agentes_Standardizados.csv', sep=';', low_memory=False)
    print("Standard Table read!")
    print(f"Number of rows: {len(df)}")
    return df


def read_departure_table():
    print("\nReading Departure Table...")
    df = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Departure_Document_Data.csv', sep=';', low_memory=False)
    print("Departure Table read!")
    print(f"Number of rows: {len(df)}")
    return df


def read_transport_table():
    print("\nReading Transport Table...")
    df = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Transport_Document_Data.csv', sep=';', low_memory=False)
    print("Transport Table read!")
    print(f"Number of rows: {len(df)}")
    return df