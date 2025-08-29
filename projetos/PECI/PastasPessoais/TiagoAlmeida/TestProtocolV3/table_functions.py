import pandas as pd

def read_standard_table():
    df_standard = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Tabela_de_Agentes_Standardizados.csv', sep=';', low_memory=False)
    return df_standard


def read_departure_table():
    df = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Departure_Document_Data.csv', sep=';', low_memory=False)
    return df


def read_transport_table():
    df = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Transport_Document_Data.csv', sep=';', low_memory=False)
    return df