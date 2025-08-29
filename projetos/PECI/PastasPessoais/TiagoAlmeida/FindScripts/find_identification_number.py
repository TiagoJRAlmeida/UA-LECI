import pandas as pd

def filter_rows_by_number(csv_file, search_number):
    # Ler o ficheiro CSV para um DataFrame
    df = pd.read_csv(csv_file, sep=';', low_memory=False)
    
    # Filtrar linhas onde "Name" ou "short_name" contém a string fornecida
    filtered_df = df[df["identification_number"] ==  search_number]
    
    return filtered_df

# Exemplo de uso
csv_file = "~/Caso_de_Estudo_2/Filtro-Tabela_de_Agentes_Standardizados.csv"
search_string = input("Introduz o identification_number a procurar: ")

result_df = filter_rows_by_number(csv_file, search_string)

# Mostrar o resultado
print("\n")
print("-"*90)
print("Found names:\n")
for name in result_df["name"]:
    print(name)

print("\n")
print("-"*90)
print("Found short_name:\n")
for short_name in result_df["short_name"]:
    print(short_name)

print("\n")
print("-"*90)
print("\n")
print(result_df)

print(result_df)
