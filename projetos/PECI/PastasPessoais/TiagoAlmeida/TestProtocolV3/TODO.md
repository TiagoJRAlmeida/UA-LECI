# TODO

## 1. Clustering
- Avaliar qual abordagem gera melhores resultados:
    - Clustering com **MinHash**
    - Clustering com **Cosine Similarity**

- Aplicar limpeza de palavras ideal para minimizar erros.

---

## 2. Avaliação de Clustering (Accuracy)

- Confirmar se o **F1 Score** é suficiente como métrica de avaliação ou se deve ser substituído/melhorado.
  
- **Opções para cálculo da accuracy**:
  
  1. **Clusterização total com sinónimos**  
        - Transformar o dicionário de sinónimos em clusters.
        - Usar **todos os nomes únicos** do dicionário para criar novos clusters - Do zero.
        - Comparar os clusters criados com os clusters do dicionário.  
        *(Rápido)*

  2. **Clusterização parcial com sinónimos**  
        - Igual ao anterior, mas usando apenas **uma percentagem** dos nomes únicos.
        - Comparar os clusters correspondentes.  
        *(Muito rápido)*

  3. **Clusterização total com datasets**  
        - Transformar o dicionário de sinónimos em clusters.
        - Criar clusters com **todos os nomes únicos** dos três datasets.
        - Utilizar os **nomes standard** como ground truth para iniciar novos clusters, **exceto os nomes standard que aparecem no dicionário**.
        - Comparar apenas os clusters de sinónimos.  
        *(Muito lento)*

  4. **Clusterização parcial com datasets**  
        - Transformar o dicionário de sinónimos em clusters.
        - Criar clusters com **todos os nomes únicos** dos três datasets.
        - Usar ground truth dos nomes standard, mas ignorando uma **percentagem** dos nomes standard do dicionário
        - Comparar apenas os clusters de sinónimos.    
        *(Muito lento)*

  5. **Comparação parcial apenas com sinónimos removidos**  
        - Transformar o dicionário de sinónimos em clusters.
        - Criar clusters com todos os nomes únicos dos três datasets.
        - Usar ground truth dos nomes standard, mas ignorando uma **percentagem** dos nomes standard do dicionário.
        - Comparar apenas os clusters correspondentes aos nomes removidos.  
        *(Muito lento)*

---

## 3. Criação do Dicionário de Sinónimos
- Melhorar a função `clean_name` para obter resultados mais consistentes.

- Encontrar uma forma de estimar/classificar a **accuracy esperada**.
