[Back to main Logbook Page](../hci_logbook.md)

---
# C. Requirement Definition
>	Based on all the gathered context, including an understanding of current practices, competitors, and user feedback and expectations: 
>	- summarize the user characteristics, context, and motivations using Personas
>	- explain your vision for a novel solution that will target user motivations using Scenarios
>	- identify requirements

# Personas

## Persona: [António Sousa] 
### Summary 
| Attribute        | Details                                       |
| ---------------- | --------------------------------------------- |
| **Photo**        | ![António Sousa](personas/persona1v2.jpg)  |
| **Name**         | António Sousa                                 |
| **Age**          | 45 anos                                       |
| **Occupation**   | Consumidor com Intolerância Alimentar         |
| **Location**     | Aveiro, Portugal                               |
| **Goals**        | Quer comprar de forma prática e segura        |
| **Pain Points**  | Falta de informação e clareza nas aplicações  |
| **Motivation**   | "Quero fazer as minhas compras de forma prática e segura para evitar riscos e garantir o melhor custo-benefício." |
| **Full Profile** | [📄 Read More](personas/persona1_template.md) |

---
## Persona: [Paulo Gomes] 
### Summary 
| Attribute        | Details                                       |
| ---------------- | --------------------------------------------- |
| **Photo**        | ![Paulo Gomes](personas/persona2v2.jpg)        |
| **Name**         | Paulo Gomes                                   |
| **Age**          | 33 anos                                       |
| **Occupation**   | Funcionário de Supermercado                   |
| **Location**     | Aveiro, Portugal                              |
| **Goals**        | Ter uma plataforma intuitiva que lhe facilite o trabalho           |
| **Pain Points**  | Dificuldade em fazer uma constante atualização de preços/promoções  |
| **Motivation**   | "Preciso de uma plataforma confiável e de fácil utilização para garantir que os preços e promoções estejam sempre corretos para manter a competitividade do supermercado e oferecer uma boa experiência aos clientes."               |
| **Full Profile** | [📄 Read More](personas/persona2_template.md) |

---

## Persona: [Joana Silva] 
### Summary 
| Attribute        | Details                                       |
| ---------------- | --------------------------------------------- |
| **Photo**        | ![Joana Silva](personas/persona3v2.jpg)        |
| **Name**         | Joana Silva                                   |
| **Age**          | 19 anos                                       |
| **Occupation**   | Estudante Universitária                       |
| **Location**     | Aveiro, Portugal                              |
| **Goals**        | Encontrar supermercados na sua zona e poupar o máximo possível           |
| **Pain Points**  | Dificuldades em encontrar supermercados e poupar dinheiro             |
| **Motivation**   | "Preciso de economizar tempo e dinheiro, então quero encontrar rapidamente os melhores preços e promoções antes de sair para as compras."                |
| **Full Profile** | [📄 Read More](personas/persona3_template.md) |

---

## Persona: [Manuel Ferreira] 
### Summary 
| Attribute        | Details                                       |
| ---------------- | --------------------------------------------- |
| **Photo**        | ![Manuel Ferreira](personas/persona4v2.jpg)    |
| **Name**         | Manuel Ferreira                               |
| **Age**          | 72 anos                                       |
| **Occupation**   | Reformado                                     |
| **Location**     | Aveiro, Portugal                              |
| **Goals**        | Encontrar produtos baratos e acessíveis sem precisar de sair de casa frequentemente.|
| **Pain Points**  | Dificuldade de locomoção e desafios com tecnologia.    |
| **Motivation**   | "Preciso de encontrar os melhores preços sem perder tempo e esforço. Uma ferramenta simples que me ajude nisso faz toda a diferença para o meu dia a dia."            |
| **Full Profile** | [📄 Read More](personas/persona4_template.md) |



# Scenarios


## Scenario 1: António procura, segundo as suas restrições alimentares, os melhores preços da zona onde se encontra

António Sousa, sempre atento à alimentação da sua família e às suas restrições alimentares, decide usar a plataforma para facilitar as compras. Antes de sair de casa, ele abre o *website* SmartPrecos e pesquisa por leite sem lactose. Em segundos, a plataforma mostra o supermercado com o melhor preço, juntamente com uma comparação de preços noutras lojas da região.

Enquanto planeia as compras, António seleciona, nos filtros, as suas intolerâncias à lactose e ao glúten, garantindo que todos os produtos sugeridos são adequados para ele. Além disso, verifica as campanhas e promoções ativas, aproveitando descontos em alguns dos seus produtos habituais.

No fim, o *website* mantém um histórico do que o António pesquisou, tornando a experiência cada vez mais rápida e eficiente.

## Scenario 2: Paulo atualiza os preços do supermercado

Paulo Gomes inicia mais um dia de trabalho no supermercado, garantindo que todas as informações de preços estejam corretas. Ao ligar o computador, abre a plataforma de gestão de preços e verifica as atualizações de preços da concorrência. Ele percebe que um dos principais produtos em promoção precisa de ser ajustado para manter a competitividade.

Com poucos cliques, Paulo insere o novo preço na plataforma, que sincroniza automaticamente com o *website* da SmartPrecos. Agora, qualquer consumidor que pesquisar esse produto verá o preço atualizado em tempo real.

Durante o dia, ele recebe uma notificação sobre uma nova campanha promocional que precisa ser de aplicada a diversos produtos. Como está longe do escritório, usa o smartphone para ajustar rapidamente as promoções no *website* da SmartPrecos, garantindo que a informação esteja disponível para quem pesquise.

Ao fim do dia, Paulo revê todos os preços e promoções estão corretos para o dia seguinte. Com os preços sempre atualizados e alinhados com a concorrência, ele garante que o supermercado continue competitivo e atrativo para os consumidores.

---


# Requirements





## C.1. Functional requirements
Comparação de Preços – A plataforma deve permitir que os utilizadores pesquisem produtos e comparem preços entre diferentes supermercados na região.

Exibição do Melhor Preço – A plataforma deve destacar o supermercado que oferece o preço mais barato para um determinado produto.

Consulta de Promoções – A plataforma deve listar campanhas promocionais e descontos ativos nos supermercados.

Mapa Interativo – A plataforma deve exibir a localização dos supermercados com base nos produtos pesquisados.

Informação Nutricional – A plataforma deve fornecer detalhes nutricionais dos produtos disponíveis.

Filtros Personalizados – O utilizador deve poder filtrar os produtos com base em intolerâncias alimentares, localização e faixa de preço.

Gestão de Conta do Utilizador – A plataforma deve permitir que os utilizadores criem uma conta para personalizar suas preferências e guardar filtros.

Atualização de Dados em Tempo Real – Os preços e promoções devem ser atualizados dinamicamente para garantir informações precisas.

## C.2. Non-functional requirements
Desempenho – A plataforma deve exibir os resultados de pesquisa rapidamente.

Escalabilidade – A plataforma deve suportar um grande número de utilizadores simultâneos sem comprometer o seu funcionamento responsivo.

Usabilidade – A interface deve ser intuitiva e acessível para diferentes perfís de utilizador, incluindo idosos e pessoas com pouca familiaridade com tecnologia.

Segurança – Os dados dos utilizador devem ser protegidos através de autenticação segura e criptografia.

Compatibilidade Web - A plataforma deve ser acessível a uma grande maioria dos  *browsers* mais populares 

Personalização – A plataforma deve oferecer recomendações personalizadas com base nas preferências e no histórico do utilizador.

Acessibilidade – Deve incluir suporte a leitores de tela e opções de contraste para melhorar a experiência de utilizadores com deficiência visual.

Manutenção e Atualizações – O sistema deve permitir a implementação de atualizações sem interromper o serviço.

---
[Back to main Logbook Page](hci_logbook.md)