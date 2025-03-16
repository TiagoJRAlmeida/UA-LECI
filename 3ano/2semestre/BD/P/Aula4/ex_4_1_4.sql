CREATE TABLE Medicine_Medico(
    ID int NOT NULL PRIMARY KEY,
    Especialidade varchar(256) NOT NULL,
    Nome varchar(256) NOT NULL
)
GO

CREATE TABLE Medicine_Paciente(
    Medico_ID int NOT NULL REFERENCES Medicine_Medico (ID),
    Numero_Utente int NOT NULL PRIMARY KEY,
    Endereco varchar(256) NOT NULL,
    Nome varchar(256) NOT NULL
)
GO

CREATE TABLE Medicine_Prescricao(
    Utente_Numero_Utente int NOT NULL REFERENCES Medicine_Paciente (Numero_Utente),
    Medico_ID int NOT NULL REFERENCES Medicine_Medico (ID),
    ID int NOT NULL,
    [Data] date NOT NULL,
    PRIMARY KEY (Utente_Numero_Utente, Medico_ID, ID)
)
GO

CREATE TABLE Medicine_Farmacias(
    Endereco varchar(256) NOT NULL,
    Telefone int NOT NULL,
    NIF int NOT NULL,
    PRIMARY KEY (Endereco, Telefone, NIF)
)
GO

CREATE TABLE Medicine_Companhia_Farmaceutica(
    Numero_Registo_Nacional int NOT NULL PRIMARY KEY,
    Endereco varchar(256),
    Telefone int NOT NULL,
    Nome varchar(256)
)
GO

CREATE TABLE Medicine_Farmaco(
    CF_Numero_Registo_Nacional int NOT NULL REFERENCES Medicine_Companhia_Farmaceutica (Numero_Registo_Nacional),
    Nome_Comercial varchar(256) NOT NULL,
    Formula varchar(256) NOT NULL,
    PRIMARY KEY (CF_Numero_Registo_Nacional, Nome_Comercial)
)
GO