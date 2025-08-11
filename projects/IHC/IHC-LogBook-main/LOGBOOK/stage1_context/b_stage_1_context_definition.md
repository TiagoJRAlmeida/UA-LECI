[Back to main Logbook Page](../hci_logbook.md)

---
# B. Stage 1 - Context Definition


# B.1. Competitor Identification
>	The competitor analysis will entail an identification of all competitors, with brief descriptions and a collection of the look and feel of their solutions, e.g., with screenshots, etc. It will also include a detailed analysis of the competitor deemed the best or more representative. It ends with a summary of the main findings including an HCI SWOT analysis



## B.1a. Competitors


| **Competitor**    | **Description**                             |
| ----------------- | ------------------------------------------- |
| KuantoKusta    | Plataforma *online* (*web* e *mobile* ) para comparação de preços e compra de produtos, especialmente eletrónicos
| Kabaz | Plataforma *web* *online* para comparação de preços de produtos de supermercado, nomeadamente produtos alimentares  |                                     




## B.1b. Detailed Competitor Analysis
>	Choose the most notable competitor and do a more thorough analysis of their interactive solution

O **KuantoKusta** é uma plataforma web na qual um utilizador pode procurar por produtos, principalmente, mas não só, informáticos (telemóveis, eletrodomésticos, televisões, consolas), e comparar o seu preço em várias lojas para encomenda. Nesta plataforma também é possível ver o custo dos portes em cada loja, e até mesmo fazer encomendas pelo website da KuantoKusta, podendo assim ser usado como um intermediário.

Por outro lado, a **Kabaz** foca-se em comparar preços de produtos de supermercado, principalmente produtos alimentares. O utilizador pode introduzir o seu código postal e um raio de distância, em quilómetros, onde deseja incluir os supermercados para comparação. De seguida, pesquisando por um produto, é-lhe apresentado o preço desse produto nos supermercados dentro desse raio. Ao contrário da KuantoKusta, nesta plataforma não é possível efetuar compras diretamente pelo website, pelo que o “carrinho” é substituído por uma ferramenta “cabaz” que serve como um bloco de notas onde ficam guardadas as comparações de todos os produtos que o utilizador lá adicionar.

Dada a maior semelhança que a **Kabaz** apresenta dentro do contexto do problema que se pretende resolver, por ser direcionada especificamente a produtos alimentares de supermercados, a análise de concorrentes focar-se-á nesta plataforma.


### - Heuristic Evaluation

#### Method
De modo a fazer uma análise relevante do concorrente, o grupo procurou responder a algumas perguntas enquanto simulava uma utilização normal da plataforma web:

1) **A plataforma resolve o problema inicial?**
2) **A plataforma é fácil de usar?**
3) **A plataforma é acessível ao maior número de utilizadores possível?**
4) **A plataforma tem todas as funcionalidades extra úteis ao utilizador?**

Com isto, cada membro do grupo procurou utilizar a plataforma casualmente, de forma a ter uma experiência mais fidedigna possível, anotando os pontos mais relevantes.
No fim das simulações seguiu-se uma breve discussão sobre a utilização de cada membro, e criou-se uma tabela onde foram anotados todos os problemas encontrados na usabilidade do website.

Para cada um dos pontos foi feita uma avaliação do ponto de vista das heurísticas de Nielsen. Cada membro deu uma nota de 0 a 4 a cada um dos problemas e, em conjunto, associou-se cada um dos mesmos a uma das 10 heurísticas da usabilidade de Nielsen.


#### Individual Evaluations
<!-- For the individual heuristic evaluations by each member of the group, you can use the templates below, grouping problems by heuristic OR each evaluator can have a table listing all the detected problems with the number of the violated heuristics on the second column. Whichever your choice, you should have a list of problems, the severity, and a recommendation to mitigate it -->



- [expert1_heuristic_evaluation_workbook](heuristic_evaluations/expert1_heuristic_evaluation_workbook.md)

- [expert2_heuristic_evaluation_workbook](heuristic_evaluations/expert2_heuristic_evaluation_workbook.md)

- [expert3_heuristic_evaluation_workbook](heuristic_evaluations/expert3_heuristic_evaluation_workbook.md)

- [expert4_heuristic_evaluation_workbook](heuristic_evaluations/expert4_heuristic_evaluation_workbook.md)


#### Consensus

>	After the individual analysis by each expert, all results should be gathered in a consensus table. If an expert has not found any of the problems found by other experts, they should analyse it, at this point, and give it a severity.

| **Issue**       | **Tiago Costa** | **Tiago Almeida** | **Pedro Mariano** | **Diogo Coutinho** | **Median** |
| --------------- | ------------ | -------- | -------- | ------------------------------------------- | ------ |
| Falta de um botão de saída para o leitor do código de barras | 1           | 2       | 3        | 3| 2.5|
| Imagens da comida sem embalagem em vez de imagens da embalagem   | 2            | 1        | 1       |2 | 1.5|
| Histórico de pesquisa não disponível |  1            |  1        |   2       |2  | 1.5|
| O website não tem possibilidade de criar uma conta pessoal | 2| 2| 2|3 | 2|
| Falta de um filtro de faixa de preço |3 |3 | 2| 3| 3|
| Barra de categorias com visibilidade reduzida |2 | 3| 1| 3| 2.5|
| Falta de informação relativa à localização dos supermercados |2 | 2| 2| 2| 2|
| Falta de filtro e informação de intolerâncias | 3|3 | 4| 4| 3.5|
| Falta de informação nutricional em cada produto | 3| 3| 4| 3| 3|



---
### - Cognitive Walkthrough

#### Method
[Briefly described  the method you used for the Cognitive Walkthrough analysis. ]

#### Task Selection and Task Analysis

[Which tasks did you select and why. What are the subtasks entailed for each ]


| Task                        | Subtasks                               |
| --------------------------- | -------------------------------------- |
| **1. Encontrar a loja com a coca cola mais barata** | Procurar "Coca Cola" na barra de pesquisa     |
|                             | Selecionar o tipo de "Coca Cola" que queremos |
|                             | Escolher a loja perto de mim com o preço mais baixo |
|                             | Adicionar ao carrinho |


| Task                          | Subtasks                                |
| ----------------------------- | --------------------------------------- |
| **1. Encontrar a bebida mais barata que não seja água** | Pesquisar por categoria "Bebidas" |
|                               | Aplicar filtro de mostrar os mais baratos primeiro |
|                               | Descer na página até encontrar uma bebida que não seja água |


#### Results

Task: Encontrar a bebida mais barata que não seja água

| Step # | Task/Action to Perform | Will User Know What to do at this step? (Yes/No) | Notes | If the user does the right thing, will they know it is progressing towards goal? (Yes/No) | Notes | Is Action Successful? (Yes/No) | Suggestions for Improvement |     |
| ------ | ---------------------- | ------------------------------------------------ | ----- | ----------------------------------------------------------------------------------------- | ----- | ------------------------------ | --------------------------- | --- |
| 1      | Pesquisar por categoria "Bebidas"   | Sim                                         | Talvez não, caso não veja a barra de categorias, que é pequena      | Sim                                                                                  |       | Sim                       | Modificar a barra de categorias de forma a ser mais visivel e facil de usar              |     |
| 2      | Aplicar filtro de mostrar os mais baratos primeiro   | Sim                                         |       | Sim                                                                                  |       | Sim                       | Um filtro para mostrar produtos dentro de uma faixa de preços seria bastante útil              |     |
| 3      | Descer na página até encontrar uma bebida que não seja água   | Sim                                         |       | Sim                                                                                  |       | Sim                       | Melhorar o filtro para ser possivel "retirar" certos produtos. Neste caso ter de procurar uma bebida que não seja água é incomodo e imprático                 |     |


## B.1c. Overall Analysis

[Here, you should summarize the main findings for the competitor panorama, listing key points that are valuable to inform the design of your solution, and also make an HCI SWOT analysis for the main competitor, taking into consideration what you learned from the heuristic evaluation, cognitive walkthrough, online reviews, user feedback, etc.]


---

# B.2. Users
>	For the users, there are two goals: 1) understand the current status of users in the domain you are addressing. How do they manage, what are the main tasks they do, if they use some tool for the purpose, what are current challenges, what might be improved, what might be new features, ...


## B.2a. Method

As entrevistas realizadas foram feitas dentro da sala de aula com estudantes, colegas de turma. O objetivo das entrevistas realizadas foi principalmente receber opinião sobre a importancia do problema, confirmar se a nossa abordagem de resolução do mesmo estava correta e por fim receber sujestões de como podemos melhorar.
Para obter os melhores resultados possiveis, o grupo segui-o a seguinte estrutura de entrevista:
1) **Contextualização do problema**
2) **Primeira Pergunta: Ponto de vista do entrevistado sobre a possivel solução ideal**
3) **Contextualização da solução pensada pelo grupo**
4) **Segunda Pergunta: Opinião do entrevistado sobre a implementação do grupo**
5) **Terceira Pergunta: Se o entrevistado achou alguma funcionalidade a mais e se tinha alguma que gostaria de acrescentar**
6) **Quarta Pergunta: Se o entrevistado utilizaria ou conhece alguém que faria uso da solução e com que frequência**
7) **Quinta Pergunta: Quais os filtros que valoriza mais quando procura produtos num website**


## B.2b. Results

>	This section tracks all informal user interviews, summarizing key insights and linking to detailed notes for each session. 

### Interview List 
| Date       | Participant / Role | Key Insights                                                    | Link to Notes                |     |
| ---------- | ------------------ | --------------------------------------------------------------- | ---------------------------- | --- |
| 25-02-2025 | Gabriel / estudante | Gostaria de uma solução que reúna várias funcionalidades numa só plataforma. Acharia útil de desse para encomendar produtos.  | [📄 Notes](interviews/interview-Gabriel.md) |     |
| 25-02-2025 | Gonçalo / estudante | Gostaria que fosse em formato web e que reúna todos os preços | [📄 Notes](interviews/interview-Goncalo.md) |     |
| 25-02-2025 | Rafael / estudante | Gostaria que reúna todos os preços, promoções e campanhas. Acharia útil que mostrasse o stock físico de um produto em loja. | [📄 Notes](interviews/interview-Rafael.md) |     |

### Common Themes & Patterns 

- **Recurring Problems:** 
	- Conseguir reunir todos os diferentes preços para o mesmo produto numa só plataforma 
	- Conseguir identificar qual a loja com as melhores ofertas
- **Frequently Used Tools:** 
	- Filtro de preço
	- Filtro de distancia
- **Desired Features / Solutions:** 
	- Possibilidade de encomendar produtos
	- Possibilidade de verificar o stock fisico da loja
- --- 



---
[Back to main Logbook Page](../hci_logbook.md)

---
