import pandas as pd

def filter_standard():
    # Ler o ficheiro CSV
    df = pd.read_csv('~/Caso_de_Estudo_2/Tabela_de_Agentes_Standardizados.csv', sep=';', low_memory=False)
    
    # Manter apenas as colunas "name" e "identification_number"
    df_filtered = df[["name", "short_name", "identification_number"]]
    
    # Guardar o resultado num novo ficheiro CSV
    df_filtered.to_csv('~/Caso_de_Estudo_2/Filtro-Tabela_de_Agentes_Standardizados.csv', index=False, sep=";")
    
    print("Ficheiro filtrado guardado em: '~/Caso_de_Estudo_2/Filtro-Tabela_de_Agentes_Standardizados.csv'")



def filter_departure():
    # Ler o ficheiro CSV
    df = pd.read_csv('~/Caso_de_Estudo_2/Departure_Document_Data.csv', sep=';', low_memory=False)
    
    # Manter apenas as colunas "name" e "identification_number"
    df_filtered = df[["name", "identification_number"]]
    
    # Guardar o resultado num novo ficheiro CSV
    df_filtered.to_csv('~/Caso_de_Estudo_2/Filtro-Departure_Document_Data.csv', index=False, sep=";")
    
    print("Ficheiro filtrado guardado em: '~/Caso_de_Estudo_2/Filtro-Departure_Document_Data.csv.csv'")
    

def filter_transport():
    # Ler o ficheiro CSV
    df = pd.read_csv('~/Caso_de_Estudo_2/Transport_Document_Data.csv', sep=';', low_memory=False)
    
    # Manter apenas as colunas "name" e "identification_number"
    df_filtered = df[["name", "identification_number"]]
    
    # Guardar o resultado num novo ficheiro CSV
    df_filtered.to_csv('~/Caso_de_Estudo_2/Filtro-Transport_Document_Data.csv', index=False, sep=";")
    
    print("Ficheiro filtrado guardado em: '~/Caso_de_Estudo_2/Filtro-Transport_Document_Data.csv'")
    
    
filter_standard()
filter_transport()
filter_departure()