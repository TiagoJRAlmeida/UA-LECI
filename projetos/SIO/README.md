# 🔐 Secure Document Repository System

## 📋 Project Overview

This project was developed as part of the Information Security in Organizations (SIO) course. The goal is to implement a secure document repository service for organizations that enables controlled sharing of documents among authorized personnel. The system implements a robust role-based access control mechanism with three distinct API tiers providing varying levels of access, comprehensive encryption, and sophisticated session management.

---

## 🎯 System Objectives

- Provide a secure document management system for organizational use
- Implement granular access control through role-based permissions with cryptographic protection
- Support secure document upload, download, and deletion operations with encryption at rest
- Enable organizational management with subject and role administration
- Maintain secure session management with protection against eavesdropping, impersonation, manipulation, and replay attacks

---

## ⚙️ System Architecture

### Core Components

The repository is implemented as a Python Flask backend with a RESTful API interface. The client communicates with the repository through well-defined API endpoints organized into three security tiers:

### 1. Anonymous API

Endpoints accessible without authentication:

- ```Create organization``` - Register new organizations
- ```List organizations``` - Browse available organizations
- ```Create session``` - Establish authenticated sessions
- ```Download file``` - Access files with known handles (encrypted content only)

### 2. Authenticated API

Endpoints requiring valid session tokens:

- ```Assume session role``` - Activate specific roles for operations
- ```Release session role``` - Deactivate currently assumed roles
- ```List session roles``` - View available roles for current session
- ```List subjects - Browse``` subjects within the organization
- ```List roles``` - View roles defined in the organization
- ```List subjects in role``` - View membership of specific roles
- ```List roles of subject``` - View role assignments for specific subjects
- ```List permissions in role``` - View permissions granted to roles
- ```List roles with permission``` - Find roles with specific permissions
- ```List documents``` - Browse documents with filtering capabilities

### 3. Authorized API

Endpoints requiring both session authentication and specific role assignments:

- ```Add subject``` - Register new users in the organization
- ```Change subject status``` - Suspend or reactivate user accounts
- ```Add role``` - Create new organizational roles
- ```Change role status``` - Activate or deactivate roles
- ```Manage role membership``` - Add/remove subjects from roles
- ```Manage role permissions``` - Add/remove permissions to roles
- ```Upload document``` - Add new documents to the repository
- ```Download document metadata``` - Access document information
- ```Delete document``` - Remove documents from the repository
- ```Change document ACL``` - Modify document access control lists

---

## 🔐 Security Architecture

### Cryptographic Implementation

- Session Key Exchange: Hybrid encryption (RSA + AES) with digital signatures
- Document Encryption: AES-CBC for file content encryption
- File Identification: SHA-256 hashing combined with organization name for unique file handles
- Communication Security: HMAC for message authentication, NONCE for replay protection

### Security Protocols

- Session Establishment: Secure key exchange with forward secrecy properties
- Message Integrity: HMAC verification on all communications
- Replay Protection: NONCE-based mechanism with session identifiers
- Freshness Guarantees: Timestamp validation with expiration mechanisms

### Access Control Model

- Role-Based Access Control (RBAC) - Permissions assigned to roles, not individual users
- Document ACLs: Fine-grained permissions (DOC_READ, DOC_DELETE, DOC_ACL) per role per document
- Organization Management: Administrative permissions (ROLE_ACL, SUBJECT_NEW, SUBJECT_DOWN, SUBJECT_UP, DOC_NEW)
- Role Management: Role manipulation permissions (ROLE_NEW, ROLE_DOWN, ROLE_UP, ROLE_MOD)

### Session Management

- Secure Authentication: Session establishment with strong credentials
- Multiple Sessions: Support for simultaneous sessions across different organizations
- Attack Protection: Robust against eavesdropping, impersonation, manipulation, and replay attacks
- Session Lifetime: Configurable expiration based on inactivity

--- 

## 📊 Permission Matrix

### Document Permissions

| Permission  | Description                                         |
|-------------|-----------------------------------------------------|
| DOC_READ    | Read encrypted file content and decrypt with proper key |
| DOC_DELETE  | Clear file_handle (soft delete)                     |
| DOC_ACL     | Modify document access control list                 |

### Organization Permissions

| Permission    | Description                        |
|---------------|------------------------------------|
| ROLE_ACL      | Modify organization ACL            |
| SUBJECT_NEW   | Add new subjects to organization   |
| SUBJECT_DOWN  | Suspend subjects                   |
| SUBJECT_UP    | Reactivate suspended subjects      |
| DOC_NEW       | Add new documents to organization  |

### Role Management Permissions

| Permission | Description                              |
|------------|------------------------------------------|
| ROLE_NEW   | Create new roles                         |
| ROLE_DOWN  | Suspend roles                            |
| ROLE_UP    | Reactivate roles                         |
| ROLE_MOD   | Modify role membership and permissions   |

--- 

## ✅ Validation & Testing

A set of commands are provided to interact with the repository. A test script is also included. To execute it, run:

```bash
./run_test
```

This script demonstrates the utilization of all available commands. Note: The explanation provided is in Portuguese.

After testing, you can remove the files created by the run_test command using:

```bash
./run_files
```

<!-- # Explicação das Features Implementadas

## Índice
1. [Comandos de Teste](#comandos-de-teste)
2. [Formato dos Dicionários](#formato-dos-dicionários)
    - [Organizations](#formato-do-dict-organizations-do-repositório)
    - [Sessions](#formato-do-dict-sessions-do-repositório)
3. [Formato dos Ficheiros](#formato-dos-ficheiros)
    - [Session File](#formato-session-file-json-do-client)


---

# Comandos de Teste
Para todos funcionarem, recomenda-se usar-los pela ordem que aparecem a seguir
## Comandos Locais
Estes comandos não necessitam de uma ligação ao repositório. <br>
Todos os exemplos de comandos apresentados supõem que são executados dentro da pasta "/delivery2"<br>
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
    - Este comando é chamado dentro do comando rep_get_doc_file e desencripta um ficheiro encriptado conhecendo os seus dados de encriptação (*encryption metadata*).

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

Ao criar uma organização, a **API** cria automaticamente a **role** de **Manager** e dá acesso ao subject para poder assumir essa **role**.

Assim, depois de criar a organização e de estabelecer uma sessão, o criador da org pode executar o comando:

- rep_assume_role <session file> <role>
    - Exemplo de uso: 
    ```bash
    ./rep_assume_role my_session.json MANAGER
    ```
    - Para assumir a role de **Manager** nessa sessão. Isto aplica-se a todos os subjects que estabeleçam sessão na organização. No entanto, um subject só pode assumir uma **role** à qual tenha direito (isto é, essa role tem de estar na sua lista de **roles** às quais tem acesso).<br><br>

Agora que temos uma sessão ativa, podemos usar outros tipos de comandos. Um exemplo é o comando:
- rep_add_subject <session file> <username> <name> <email> <credentials file>
    - Exemplo de uso:
        ```bash
        ./rep_subject_credentials 1234 joao_keys.json
        ./rep_add_subject my_session.json jhonny123 joao joao@ua.pt joao_keys.json
        ```
    - Este comando vai me permitir a mim, um subject já com uma sessao dentro da organization, a adicionar outro subject à organization. Para o subject poder executar este comando precisa de ter ativa uma role que tenha a permissão de **"SUBJECT_NEW"**.


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

Um subject que tenha assumido uma **role** com permissão **"SUBJECT_DOWN"** e **"SUBJECT_UP** pode suspender e ativar um subject, respetivamente. No caso atual, a **role** de **Manager** já tem todas a permissões, então não há necessidade. No entanto, podemos criar uma **role** e adicionar permissões (por exemplo **"SUBJECT_UP"** e **"SUBJECT_DOWN"**) com os seguintes comandos:

- rep_add_role <session file> <role>
    - Exemplo de uso:
    ```bash
    ./rep_add_role my_session.json ADMIN
    ```

    - Para criar a role de **Admin** na organização.

- rep_add_permission <session file> <role> <username>
    ```bash
    ./rep_add_permission my_session.json ADMIN SUBJECT_DOWN
    ./rep_add_permission my_session.json ADMIN SUBJECT_UP
    ```
    - Para que a role **Admin** ganhe a permissão **"SUBJECT_DOWN"** e **"SUBJECT_UP"**. Para executar este comando é necessário ter assumido uma **role** com a permissão **"ROLE_MOD"**. Uma vez que temos a role **Manager**, não há problemas.

Para além disso, o comando rep_add_permission também permite dar a um subject a permissão de assumir uma certa role:

- Exemplo de uso:
    ```bash
    ./rep_add_permission my_session.json ADMIN tigs
    ./rep_add_permission my_session.json ADMIN jhonny123
    ```
    - Agora, os subjects **tigs (nós)** e **jhonny123** podem assumir a **role** de **Admin**:
        ```bash
        ./rep_assume_role my_session.json ADMIN
        ```

Tal como podemos adicionar permissões e subjects, também podemos removê-los com o comando:

- rep_remove_permission <session file> <username>
    - Exemplos de uso:
    ```bash
    ./rep_remove_permission my_session.json ADMIN SUBJECT_DOWN
    ./rep_remove_permission my_session.json ADMIN SUBJECT_UP
    ./rep_remove_permission my_session.json ADMIN jhonny123
    ```
    - Para reverter o que foi feito há instantes. No entanto, vamos permitir novamente que o **jhonny123** assuma a **role** de **Admin**_

    ```bash
    ./rep_add_permission my_session.json ADMIN jhonny123
    ```

<br>

Se algum subject quiser ver as roles que assumiu na sua sessão, pode fazê-lo com o comando:

- ./rep_list_roles <session file>
    - Exemplo de uso:
    ```bash
    ./rep_list_roles my_session.json
    ```
    - Para listar todas as roles que assumiu na sessão, e o seu estado: **"ACTIVE"** ou **"SUSPENDED"**.

<br>

Quando um subject quer remover uma role que tem ativada na sua sessão atual (é importante mencionar que continua a ter acesso a essa role, e apenas está a removê-la da sua sessão atual. Pode recuperá-la correndo o comando de assumir a **role** novamente), pode fazê-lo com o comando:

- ./rep_drop_role <session file> <role>
    - Exemplo de uso:
    ```bash
    ./rep_drop_role my_session.json ADMIN
    ```
    - Para perder a **role** de ADMIN na sessão atual.
    

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

No que diz respeito a permissões, um subject pode ver as permissões de uma certa **role** e as **roles** que têm uma certa permissão com os comandos (respetivamente):

- rep_list_role_permissions <session file> <role>
    - Exemplo de uso:
    ```bash
    ./rep_list_role_permissions my_session.json ADMIN
    ```
    - Para ver as permissões da **role** **Admin**.

- rep_list_permission_roles <session file> <permission>
    - Exemplo de uso:
    ```bash
    ./rep_list_permission_roles my_session.json SUBJECT_UP
    ./rep_list_permission_roles my_session.json DOC_READ
    ```
    - Para ver as roles que têm a permissão **"SUBJECT_UP"**. Se for especificada uma permissão relativa a documentos (e.g. **"DOC_READ"**) são apresentadas todas as **roles** que têm essa permissão associados aos documentos onde têm essa permissão.

Qualquer subject que tenha uma **role** com a permissão **"ROLE_DOWN"** e **"ROLE_UP"** pode suspender e reativar uma role, mudando o seu estado de **"ACTIVE"** para **"SUSPENDED"** e vice-versa:

- rep_suspend_role <session file> <role>
    - Exemplo de uso:
    ```bash
    ./rep_suspend_role my_session.json ADMIN
    ./rep_list_subject_roles my_session.json tigs
    ```
    - Para suspender a **role** **Admin** e verificar se a role realmente foi suspensa (se o subject **tigs** tiver a **role** Admin, deverá agora aparecer com o estado **"SUSPENDED"**).

- rep_reactivate_role <session file> <role>
    - Exemplo de uso:
    ```bash
    ./rep_reactivate_role my_session.json ADMIN
    ./rep_list_subject_roles my_session.json tigs
    ```

Uma vez que a secção seguinte diz respeito aos documentos, vamos adicionar a permissão **"DOC_NEW"** à **role** **Admin**:
```bash
./rep_add_permission my_session.json ADMIN DOC_NEW
```

E vamos iniciar uma sessão no lugar do **jhonny123** , assumindo a **role** de **Admin**:
```bash
./rep_create_session my_org jhonny123 1234 joao_keys.json joao_session.json
./rep_assume_role joao_session.json ADMIN
```
<br>

Agora no que diz respeito aos documentos, para enviar um documento para o repositório, mencionando o ficheiro a ler, e o nome que queremos com que fique guardado no repositório é possivel usar o comando:
- rep_add_doc rep_add_doc <session file> <document name> <file>
    - Exemplo de uso:
        ```bash
        ./rep_add_doc joao_session.json my_doc my_doc.txt
        ```
    - Para dar upload do ficheiro my_doc.txt no repositório com o nome my_doc. Para o subject poder executar este comando precisa de ter assumido uma **role** que tenha a permissão de **"DOC_NEW"**.

<br>

Por *default*, ao criarmos um documento, a **ACL** desse documento apenas dá permissão ao **Manager** para fazer tudo com esse documento. Uma vez que o subject **tigs** tem a **role** de **Manager**, tem a permissão de **"DOC_ACL"** no documento que o **jhonny123** acabou de adicionar, e pode alterar as permissões de qualquer role neste documento:

- rep_acl_doc <session file> <document name> [+/-] <role> <permission>
    - Exemplos de uso:
    ```bash
    ./rep_acl_doc my_session.json my_doc + ADMIN DOC_READ
    ./rep_acl_doc my_session.json my_doc + ADMIN DOC_ACL
    ./rep_acl_doc my_session.json my_doc - ADMIN DOC_ACL
    ```
    - Para, respetivamente, permitir que a **role** **Admin** possa ler o documento, permitir que a **role** **Admin** possa modificar a **ACL** do documento e, de seguida, remover essa permissão.


Podemos agora ver os documentos dentro da organização com a qual temos sessão estabelecida através do comando:
- rep_list_docs <session file> [-s username] [-d nt/ot/et date]
    - Exemplo de uso:
        ```bash
        ./rep_list_docs my_session.json
        ```
    - Para listar todos os documentos na organização ou:
        ```bash
        ./rep_list_docs my_session.json -s jhonny123
        ./rep_list_docs my_session.json -s jhonny123 -d nt 18-12-24
        ./rep_list_docs my_session.json
        ./rep_list_docs my_session.json -s jhonny123 -d od 30-12-24
        ./rep_list_docs my_session.json -s jhonny123 -d et 27-12-24
        ```
    - Para especificar os documentos, especificando o criador do documento, e a data (*newer than*, *older than*, *equal to*).

Como no repositório são guardados os metadados de cada ficheiro armazenado, é possível ir buscá-los com o comando:
- rep_get_doc_metadata <session file> <document name>
    - Exemplo de uso:
        ```bash
        ./rep_get_doc_metadata joao_session.json my_doc
    - Para ir buscar os metadados do documento my_doc. Para o subject poder executar este comando precisa de ter ativa uma role que tenha a permissão de **"DOC_READ"** neste documento.

Se quisermos ir buscar o conteúdo de um ficheiro (fazer download de um ficheiro) do repositório e, opcionalmente, escrever num ficheiro local podemos com o comando:
- rep_get_doc_file <session file> <document name> [file]
    - Exemplo de uso:
        ```bash
        ./rep_get_doc_file my_session.json my_doc
        ```
    - Para printar o conteúdo do ficheiro no stdout ou:
        ```bash
        ./rep_get_doc_file my_session.json my_doc new_doc.txt
        ```
    - Para guardar o conteúdo num ficheiro my_doc.txt local. Para o subject poder executar este comando precisa de ter ativa uma role que tenha a permissão de **"DOC_READ"** neste documento.

Para além disso é possível "apagar" um ficheiro (na realidade apenas removemos o seu **file_handle**) do repositório com o comando:
- rep_delete_doc <session file> <document name>
    - Exemplo de uso:
        ```bash
        ./rep_delete_doc my_session.json my_doc
        ```
    - Para "apagar" o ficheiro my_doc do repositório

Agora podemos ver que se tentar-mos ir buscar o conteúdo do ficheiro, não é possivel apenas com o nome:
```bash
./rep_get_doc_file my_session.json my_doc
```

# Formato dos Dicionários
## Formato do dict "organizations" do repositório:
```json
organizations = {
    org1_name: {
        "SUBJECTS":
            USERNAME1: {
                "FULL_NAME": "FULLNAME1",
                "EMAIL": "EMAIL1",
                "PUBLIC_KEY": "PUBLIC_KEY1",
                "STATUS": "ACTIVE",
                "ROLES": ["MANAGER"]
            },
        "ACL": {
            "MANAGER": {
                "PERMISSIONS": [
                    "ROLE_ACL",
                    "SUBJECT_NEW",
                    "SUBJECT_DOWN",
                    "SUBJECT_UP",
                    "DOC_NEW",
                    "ROLE_NEW",
                    "ROLE_DOWN",
                    "ROLE_UP",
                    "ROLE_MOD"
                ],
                "STATUS": "ACTIVE"
            }
        },
        "SESSION_IDS": [],
        "DOCUMENT_HANDLES": [],
        ...
    },
    ...
}
```

## Formato do dict "documents" do repositório:
```json
documents = {
    DOCUMENT_HANDLE1: {
        "NAME": doc_name1,
        "CREATION_DATE": time.strftime("%d-%m-%y %H:%M:%S"),
        "CREATOR": username1,
        "ORG_NAME": organization_name1,
        "FILE_HANDLE": file_handle1,
        "ACL": {
            "MANAGER": ["DOC_ACL", "DOC_READ", "DOC_DELETE"]
        },
        "DELETER": "IDK1",
        "ALG": "IDK1",
        "KEY": "IDK1",
        "IV": "IDK1"
    },
    ...
}
```

## Formato do dict "sessions" do repositório:
```json
sessions = {
    session_id1: {
        "SUBJECT": username1, 
        "ORG_NAME": org1_name,
        "ROLES": [],
        "KEYS": {
            "ENCRYPTION_KEY": "base64-encoded-key",  // chave para encriptar/desencriptar mensagens
            "INTEGRITY_KEY": "base64-encoded-key",  // Chave para verificar integridade da mensagem (HMAC ou assinatura digital)
            "NONCE": ["base64-encoded-value"]
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
    "NONCE": ["base64-encoded-value"]
  },
  "ROLES": [],
  "EXPIRY_TIME": "ISO-8601-timestamp",
}
``` -->