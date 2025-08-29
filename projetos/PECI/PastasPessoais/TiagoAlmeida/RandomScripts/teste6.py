import pandas as pd


def read_transport_table():
    print("\nA ler Tabela de Transport")
    df = pd.read_csv('~/Caso_de_Estudo_2/Filtro-Transport_Document_Data.csv', sep=';', low_memory=False, nrows=20)
    print("Tabela de Transport lida!")
    print(f"Numero de linhas da tabela Transport: {len(df)}")
    return df


df = read_transport_table()
nanTest = df.loc[3]['identification_number']
print(pd.isna(nanTest))

# sinesCount = 0
# current_row = 0

# for _, row in df.iterrows():
#     row_name = str(row["name"])
#     flag = False
#     for word in row_name.split():
#         if word.lower() == "sines":
#             flag = True
#     if flag == True:
#         sinesCount += 1

#     print(f"\rCurrent Row: {current_row}", end="")
#     current_row += 1


# print(f"\nSines Count: {sinesCount}")
