import pandas as pd

def read_standard_table():
    print("\nA ler Tabela de agentes standardizados")
    df_standard = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Tabela_de_Agentes_Standardizados.csv', sep=';', low_memory=False)
    print("Tabela de agentes standardizados lida!")
    return df_standard


def read_departure_table():
    print("\nA ler Tabela de Departure")
    df = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Departure_Document_Data.csv', sep=';', low_memory=False)
    print("Tabela de Departure lida!")
    print(f"Numero de linhas da tabela Departure: {len(df)}")
    return df


def read_transport_table():
    print("\nA ler Tabela de Transport")
    df = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Transport_Document_Data.csv', sep=';', low_memory=False)
    print("Tabela de Transport lida!")
    print(f"Numero de linhas da tabela Transport: {len(df)}")
    return df