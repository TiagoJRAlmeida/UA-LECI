import pandas as pd
import sys 

def filter_rows_by_string(csv_file, search_string):
    # Ler o ficheiro CSV para um DataFrame
    df = pd.read_csv(csv_file, sep=';', low_memory=False)
    
    # Filtrar linhas onde "name" ou "short_name" contém a string fornecida
    filtered_df = df[df["name"].str.contains(search_string, case=False, na=False) | 
                      df["short_name"].str.contains(search_string, case=False, na=False)]
    
    return filtered_df


def filter_rows_by_string2(csv_file, search_string):
    # Ler o ficheiro CSV para um DataFrame
    df = pd.read_csv(csv_file, sep=';', low_memory=False)
    
    # Garantir que os valores nulos são substituídos por strings vazias antes de aplicar str.split()
    df["name"] = df["name"].fillna("")
    df["short_name"] = df["short_name"].fillna("")
    
    # Converter a string de pesquisa para minúsculas
    search_string = search_string.lower()
    
    # Filtrar linhas onde "name" ou "short_name" tem a string como palavra isolada
    filtered_df = df[
        df["name"].str.split().apply(lambda words: search_string in [word.lower() for word in words]) |
        df["short_name"].str.split().apply(lambda words: search_string in [word.lower() for word in words])
    ]
    
    return filtered_df



# Exemplo de uso
csv_file = "~/Caso_de_Estudo_2/Filtro-Tabela_de_Agentes_Standardizados.csv"
method = input("Escolhe o metodo a usar(1/2): ")
search_string = input("Introduz a string a procurar: ")

if method == "1":
    result_df = filter_rows_by_string(csv_file, search_string)
elif method == "2":
    result_df = filter_rows_by_string2(csv_file, search_string)
else:
    print("Method not allowed.")
    sys.exit(1)

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
