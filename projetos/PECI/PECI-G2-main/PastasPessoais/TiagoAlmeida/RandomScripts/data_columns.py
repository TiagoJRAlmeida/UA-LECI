import pandas as pd


# Print ás colunas standard
standard_df = pd.read_csv('~/Caso_de_Estudo_2/Tabela_de_Agentes_Standardizados.csv', sep=';', nrows=5)

standard_columns = standard_df.columns
""" print("-"*50)
print("\tTabelas de Dados Standard\n")
print(f"Numero de colunas: {len(standard_columns)}")

print("Colunas: ")
for column in standard_columns:
    print(column) """


# Print ás colunas de departure
departure_df = pd.read_csv('~/Caso_de_Estudo_2/Departure_Document_Data.csv', sep=';', nrows=5)

departure_columns = departure_df.columns
""" print("-"*50)
print("\tTabelas de Dados Departure\n")
print(f"Numero de colunas: {len(departure_columns)}")

print("Colunas: ")
for column in departure_columns:
    print(column) """
    
    
# Print ás colunas de tranport
transport_df = pd.read_csv('~/Caso_de_Estudo_2/Transport_Document_Data.csv', sep=';', nrows=5)

transport_columns = transport_df.columns
""" print("-"*50)
print("\tTabelas de Dados Transport\n")
print(f"Numero de colunas: {len(transport_columns)}")

print("Colunas: ")
for column in transport_columns:
    print(column) """
    
    
# Print ás colunas comuns entre standard e Departure
print("\n")
print("-"*50)
print("\nColunas em comum entre Standard e Departure\n")
comum_standard_departure = [column for column in standard_columns if column in departure_columns]
print(f"Numero de colunas: {len(comum_standard_departure)}")
print("Colunas: ")
for column in comum_standard_departure:
    print(column)


# Print ás colunas comuns entre standard e Transport
print("\n")
print("-"*50)
print("\nColunas em comum entre Standard e Transport\n")
comum_standard_transport = [column for column in standard_columns if column in transport_columns]
print(f"Numero de colunas: {len(comum_standard_transport)}")
print("Colunas: ")
for column in comum_standard_transport:
    print(column)
    
    
# Print ás colunas comuns entre Departure e Transport
print("\n")
print("-"*50)
print("\nColunas em comum entre Departure e Transport\n")
comum_departure_transport = [column for column in departure_columns if column in transport_columns]
print(f"Numero de colunas: {len(comum_departure_transport)}")
print("Colunas: ")
for column in comum_departure_transport:
    print(column)
    