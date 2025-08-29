import pandas as pd
import json 

# Lê o CSV com uso eficiente da memória
df_standard = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Tabela_de_Agentes_Standardizados.csv', sep=';', low_memory=False)
print("Tabela de agentes standardizados lida!\n")

# Dicionário que contem key = NIF e value = ["id", "name", "organization_id"]
NIFData = {}
NIFData["NIFsRepetidos"] = []

# Dicionário que contém key = name e value = NIF
NameNIF = {}
NameNIF["NomesRepetidos"] = []

# Itera pelas linhas do DataFrame
for _, row in df_standard.iterrows():
    id = str(row["id"])  # Converte para string para evitar problemas com NaN
    name = str(row["name"])  # Converte para string para garantir consistência
    nif = str(row["identification_number"])
    organization_id = str(row["organization_id"])
    
    
    # <--- Atualizar o NIFData --->
    if nif in NIFData:
        print(f"NIF REPETIDO: {nif}")
        NIFData["NIFsRepetidos"].append(nif)
    else:    
        NIFData[nif] = [id, name, organization_id]
    # <---------------------------->
    
    
    # <--- Atualizar o NameNIF --->
    if name in NameNIF:
        print(f"NOME REPETIDO: {name}")
        NameNIF["NomesRepetidos"].append(name)
    else:
        NameNIF[name] = nif
    # <--------------------------->

# Escreve para ficheiros JSON
with open("Standard_NIF_Data_relation.json", "w", encoding="utf-8") as f:
    json.dump(NIFData, f, ensure_ascii=False, indent=4)

print(f"Ficheiro JSON gerado em: Standard_NIF_Data_relation.json")

with open("Standard_Name_NIF_relation.json", "w", encoding="utf-8") as f:
    json.dump(NameNIF, f, ensure_ascii=False, indent=4)

print(f"Ficheiro JSON gerado em: Standard_Name_NIF_relation.json")


# df_departure = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Departure_Document_Data.csv', sep=';', low_memory=False)
# print("Tabela de departure lida!\n")