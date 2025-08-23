from itertools import combinations

def max_intersection(lists):
    max_result = set()
    best_sequence = []
    
    # Gerar todas as combinações possíveis de interseção
    for r in range(2, len(lists) + 1):
        for combo in combinations(lists, r):
            intersection_result = set(combo[0])
            sequence = [combo[0]]
            
            for lst in combo[1:]:
                intersection_result &= set(lst)
                sequence.append(lst)
                
                # Atualiza a melhor interseção encontrada
                if len(intersection_result) > len(max_result):
                    max_result = intersection_result
                    best_sequence = sequence[:]
    
    return best_sequence, max_result

# Exemplo de uso:
palavra = "PSA SINES HONG"

psa = [
        "PSA Sines - Terminais De Contentores, S.A."
]

sines = [
        "PSA Sines - Terminais De Contentores, S.A.",
        "Clube Nautico De Sines",
        "Pioneiro Do Rio Sines",
        "Americold Sines",
        "APS - Administração dos Portos de Sines e do Algarve, S.A.",
        "Hospital Particular do Alentejo, Sines",
        "PORTUGS Sines - Reboques Marítimos, Unipessoal Lda",
        "MEDTUG Sines, S.A."
    ]

hong = [
        "COSCO HONG KONG SHIPPING LTD",
        "Fml Hong Kong",
        "Maersk Shipping Hong Kong Ltd",
        "Asia Maritime Pacific (Hong Kong) Limited",
        "OCEAN BASE SHIPPING (HONG KONG) LIMITED",
        "Chang Ye Shipping (Hong Kong) Limited",
        "Chellaram Shipping (Hong Kong) Ltd.",
        "Worldtrans Marine Hong Kong Co Ltd",
        "Yangtze Navigation (Hong Kong) Co., Ltd"
    ]

lists = [psa, sines, hong]

sequence, result = max_intersection(lists)
print("Melhor sequência de interseção:", sequence)
print("\nResultado da interseção:", result)