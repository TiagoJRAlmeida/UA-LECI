# Explicação das Features Implementadas

## Índice
1. [Comandos de Teste](#comandos-de-teste)
    - [Comandos Locais](#comandos-locais)
2. [Formato dos Dicionários](#formato-dos-dicionários)
    - [Organizations](#formato-do-dict-organizations-do-repositório)
    - [Sessions](#formato-do-dict-sessions-do-repositório)
3. [Formato dos Ficheiros](#formato-dos-ficheiros)
    - [Session File](#formato-session-file-json-do-client)
4. [Comandos Locais](#comandos-locais)
    - [REP_SUBJECT_CREDENTIALS](#funcionamento-do-rep_subject_credentials)
    - [REP_DECRYPT_FILE](#funcionamento-do-rep_decrypt_file)
5. [API Anônima](#anonymous-api-commands)
    - [REP_CREATE_ORG](#funcionamento-do-rep_create_org)
    - [REP_LIST_ORGS](#funcionamento-do-rep_list_orgs)
    - [REP_CREATE_SESSION](#funcionamento-do-rep_create_session)
    - [REP_GET_FILE](#funcionamento-do-rep_get_file)
6. [API Autenticada](#authenticated-api-commands)
    - [REP_LIST_SUBJECTS](#funcionamento-do-rep_list_subjects)
    - [REP_LIST_DOCS](#funcionamento-do-rep_list_docs)
7. [API Autorizada](#autherized-api-commands)
    - [REP_ADD_SUBJECT](#funcionamento-do-rep_add_subject)
    - [REP_SUSPEND_SUBJECT](#funcionamento-do-rep_suspend_subject)
    - [REP_ACTIVATE_SUBJECT](#funcionamento-do-rep_activate_subject)
    - [REP_ADD_DOC](#funcionamento-do-rep_add_doc)
    - [REP_GET_DOC_METADATA](#funcionamento-do-rep_get_doc_metadata)
    - [REP_GET_DOC_FILE](#funcionamento-do-rep_get_doc_file)
    - [REP_DELETE_DOC](#funcionamento-do-rep_delete_doc)


---

# Comandos de Teste
Para todos funcionarem, recomenda-se usar-los pela ordem que aparecem a seguir
## Comandos Locais
Estes comandos não necessitam de uma ligação ao repositório. <br>
Todos os exemplos de comandos apresentados supõem que são executados dentro da pasta "/delivery1"<br>
Para esta delivery foram implementados dois:
1. rep_subject_credentials <password> <credentials file>
    - Exemplo de uso:
        ```bash
        ./rep_subject_credentials 1234 my_keys.json
        ```
    - Comportamento esperado: 
        - Criação/alteração de um ficheiro chamado "my_keys.json" com um par de chaves publica e privada
        - A chave privada está cifrada com a password indicada (neste caso 1234)
2. rep_decrypt_file <encrypted file> <encryption metadata>
    - Ainda não implementado

## Comandos com a API
Estes comandos necessitam de uma ligação ao repositório. <br>
Para ligar o repositório deve executar o comando:<br>
```bash
python3 repository/repository.py
```
---
Agora com o repositório ligado, podemos realizar o resto dos comandos.<br>
O primeiro que devemos experimentar é o comando para criar uma organização. Podemos fazer isso com o comando:
- rep_create_org <organization> <username> <name> <email> <public key file>
    - Exemplo de uso:
        ```bash
        ./rep_create_org my_org tigs Tiago tigs@ua.pt my_keys.json
        ```
    - Este comando deve criar uma organization com o nome "my_org", em que o primeiro subject tem os atributos:
        - Username: tigs
        - Name: Tiago
        - Email: tigs@ua.pt
        - public_key: key publica dentro do ficheiro
Podemos agora verificar que a organization foi criada com o comando:
- rep_list_orgs
    - Exemplo de uso:
        ```bash
        ./rep_list_orgs
        ```
    - Este comando deve devolver todas as organizations existentes no repositorio. Neste momento só deve existir o que acabamos de criar.
Agora que temos uma organization e um subject lá dentro, podemos iniciar uma session entre os dois com o comando:
- rep_create_session <organization> <username> <password> <credentials file> <session file>
    - Exemplo de uso:
        ```bash
        ./rep_create_session my_org tigs 1234 my_keys.json my_session.json
        ```
    - Este comando vai guardar no ficheiro my_session.json todos o conteudo importante relativo á sessão.

Agora que temos uma sessão ativa, podemos usar outros tipos de comandos. Um exemplo é o comando:
- rep_add_subject <session file> <username> <name> <email> <credentials file>
    - Exemplo de uso:
        ```bash
        ./rep_subject_credentials 1234 joao_keys.json
        ./rep_add_subject my_session.json jhonny123 joao joao@ua.pt joao_keys.json
        ```
    - Este comando vai me permitir a mim, um subject já com uma sessao dentro da organization, a adicionar outro subject á organization

Podemos ver tambem os subjects dentro da organization com o commando:
- rep_list_subjects <session file> [username] 
    - Exemplo de uso:
        ```bash
        ./rep_list_subjects my_session.json
        ```
    - Para ver todos os subjects da organização ou:
        ```bash
        ./rep_list_subjects my_session.json jhonny123
        ```
    - Para procurar por um especifico subject especifico

Além disso, e para terminar o tópico dos subjects, também é possivel alterar os estado de um subject com os seguintes comandos:

1. rep_suspend_subject <session file> <username>
    - Exemplo de uso:
        ```bash
        ./rep_suspend_subject my_session.json jhonny123
        ./rep_list_subjects my_session.json jhonny123
        ```
    - Para alterar o estado de um subject para "suspended" (como podemos ver pelo output do comando rep_list_subjects)

2. rep_activate_subject <session file> <username>
    - Exemplo de uso:
        ```bash
        ./rep_activate_subject my_session.json jhonny123
        ./rep_list_subjects my_session.json jhonny123
        ```
    - Para alterar o estado de um subject para "active" (como podemos ver pelo output do comando rep_list_subjects)
    
Agora no que diz respeito aos documentos, para enviar um documento para o repositório, mencionando o ficheiro a ler, e o nome que queremos com que fique guardado no repositório é possivel usar o comando:
- rep_add_doc rep_add_doc <session file> <document name> <file>
    - Exemplo de uso:
        ```bash
        ./rep_add_doc my_session.json my_doc my_doc.txt
        ```
        - Para dar upload do ficheiro my_doc.txt no repositório com o nome my_doc

Podemos agora ver os documentos dentro da organização com a qual temos sessão estabelecida através do comando:
- rep_list_docs <session file> [-s username] [-d nt/ot/et date]
    - Exemplo de uso:
        ```bash
        ./rep_list_docs my_session.json
        ```
    - Para listar todos os documentos na organização ou:
        ```bash
        ./rep_list_docs my_session.json -s jhonny123 -d nt 15-11-2024
        ```
    - Para especificar os documentos de um criador mais recentes que a data mencionada

Como no repositório são guardados os metadados de cada ficheiro armazenado, é possível ir buscá-los com o comando:
- rep_get_doc_metadata <session file> <document name>
    - Exemplo de uso:
        ```bash
        ./rep_get_doc_metadata my_session.json my_doc
    - Para ir buscar os metadados do documento my_doc

Para além disso é possível "apagar" um ficheiro (na realidade apenas removemos o seu file_handle) do repositório com o comando:
- rep_delete_doc <session file> <document name>
    - Exemplo de uso:
        ```bash
        ./rep_delete_doc my_session.json my_doc
        ```
    - Para "apagar" o ficheiro my_doc do repositório

Por último, se quisermos ir buscar o conteúdo de um ficheiro (fazer download de um ficheiro) do repositório e, opcionalmente, escrever num ficheiro local podemos com o comando:
- rep_get_doc_file <session file> <document name> [file]
    - Exemplo de uso:
        ```bash
        ./rep_get_doc_file my_session.json
        ```
    - Para printar o conteúdo do ficheiro no stdout ou:
        ```bash
        ./rep_get_doc_file my_session.json my_doc
        ```
    - Para guardar o conteúdo num ficheiro my_doc local 
# Formato dos Dicionários
## Formato do dict "organizations" do repositório:
```json
organizations = {
    org1_name: {
        "SUBJECTS": {
            USERNAME1: {
                "ATTRIBUTES": [USERNAME1, FULLNAME1, EMAIL1, PUBLIC_KEY1],
                "STATUS": "ACTIVE",
                "ROLE": "IDK"
            },
            ...
        },
        "DOCS": {
            DOCUMENT_HANDLE1: {
                "DOCUMENT_HANDLE": DOCUMENT_HANDLE1,
                "NAME": doc_name1,
                "CREATE_DATE": time.strftime("%Y-%m-%d %H:%M:%S"),
                "CREATOR": username1,
                "FILE_HANDLE": file_handle1,
                "ACL": "IDK1",
                "DELETER": "IDK1",
                "ALG": "IDK1",
                "KEY": "IDK1"
            },
            ...
        }
    },
    ...
    }
}
```

## Formato do dict "sessions" do repositório:
```json
sessions = {
    session_id1: {
        "SUBJECT": username1, 
        "ORG_NAME": org1_name,
        "KEYS": {
            "ENCRYPTION_KEY": "base64-encoded-key",  // chave para encriptar/desencriptar mensagens
            "INTEGRITY_KEY": "base64-encoded-key",  // Chave para verificar integridade da mensagem (HMAC ou assinatura digital)
            "NONCE": "base64-encoded-value"
        },
        "EXPIRY_TIME": expiry_time1
    },
    ...
}
```


# Formato dos Ficheiros
## Formato session file (json) do client:
```json
{
  "SESSION_ID": session_id1,
  "ORG_NAME": org1_name,
  "USERNAME": username1,
  "KEYS": {
    "ENCRYPTION_KEY": "base64-encoded-key",  // chave para encriptar/desencriptar mensagens
    "INTEGRITY_KEY": "base64-encoded-key",  // Chave para verificar integridade da mensagem (HMAC ou assinatura digital)
    "NONCE": "base64-encoded-value"
  },
  "LIFETIME": {
    "START_TIME": "ISO-8601-timestamp",
    "EXPIRY_TIME": "ISO-8601-timestamp"
  },
  "STATUS": "active"
}
```


# Local commands
## Funcionamento do REP_SUBJECT_CREDENTIALS:
### Procolo
- Gera uma **chave privada** com RSA
- Deriva a **chave publica** da chave privada
- Cifra a **chave privada** com uma password
- Formata ambas as chaves no formato pem e guarda num ficheiro (que deve ser .pem)

## Funcionamento do REP_DECRYPT_FILE:
...


# Anonymous API commands:
## Funcionamento do REP_CREATE_ORG:
### Procolo
- Cliente cria um payload contendo o nome da nova organização, e a informação referente ao primeiro subject (Manager Subject)
- Cliente encripta o payload com a **chave publica do repositorio** e envia
- Repositorio (server) decripta o payload com a sua **chave privada**
- Repositorio (server) verifica se não existe uma organização igual e, caso não, guarda/cria a nova organização

## Funcionamento do REP_LIST_ORGS:
### Protocolo
- Cliente chama a função e faz o pedido ao Repositorio
- Repositorio (server) responde com uma lista de todos os nomes de organizações existentes

## Funcionamento do REP_CREATE_SESSION:
### Protocolo
- O cliente tem um par de chaves assimétricas
- O Repositório (server) tem um par de chaves assimétricas 
- O cliente cria uma chave simétrica aleatória, um NOUNCE, e um hash da chave 
- O cliente cifra a chave simétrica nova com a **publica do repositório**
- O cliente assina a mensagem composta pela nova chave simétrica, o NOUNCE e o hash com a sua **privada** e envia para o Repositorio (server) 
- O repositorio (server) decifra com a **publica do cliente** a mensagem, garantindo que foi enviado por ele.
- O repositorio (server) decifra com a sua **privada** a chave
- O repositorio (server) cria um hash e verifica se corresponde com o hash recebido
- O repositorio (server) verifica se a mensagem não foi intercetada com o NOUNCE
- Se estiver tudo correto, o repositorio (server) guarda a chave nova
- Agora ambos os lados tem a chave simétrica nova

## Funcionamento do REP_GET_FILE:
...


# Authenticated API commands:
## Funcionamento do REP_LIST_SUBJECTS:
### Protocolo
- Cliente pede a lista total dos subjects ou apenas 1 especifico
- O Repositorio (server) verifica se a sessão é valida
- O Repositorio (server) cria um payload com todos os subjects ou 1 especifico e o seu Status (active or suspend) e envia

## Funcionamento do REP_LIST_DOCS:
...

# Autherized API commands:
## Funcionamento do REP_ADD_SUBJECT:
...

## Funcionamento do REP_SUSPEND_SUBJECT:
### Protocolo
- Cliente pede para mudar o status de um subject para "suspended"
- O Repositorio (server) verifica se a sessão é valida
- O Repositorio (server) verifica se o subject existe
- O Repositorio (server) altera o status do subject para "suspended"

## Funcionamento do REP_ACTIVATE_SUBJECT:
### Protocolo
- Cliente pede para mudar o status de um subject para "suspended"
- O Repositorio (server) verifica se a sessão é valida
- O Repositorio (server) verifica se o subject existe
- O Repositorio (server) altera o status do subject para "suspended"

## Funcionamento do REP_ADD_DOC:
### Protocolo
- O cliente gera uma **chave aleatória simétrica**
- O cliente encripta o conteúdo do documento com essa chave aleatória
- O cliente encripta a **chave simétrica aleatória** e o **algoritmo usado para encriptar o ficheiro** com a chave da sessão
- O cliente envia o payload com toda a informação do ficheiro
- O servidor recebe essa informação
- O servidor desencripta o **algoritmo** e a **chave simétrica** com a chave da sessão
- O servidor encripta o **algoritmo** e a **chave simétrica** com a sua chave pública
- O servidor guarda o conteúdo do ficheiro em /docs/
- O servidor guarda os metadados do ficheiro no dicionário organizations["DOCS"]

## Funcionamento do REP_GET_DOC_METADATA:
...

## Funcionamento do REP_GET_DOC_FILE:
...

## Funcionamento do REP_DELETE_DOC:
...