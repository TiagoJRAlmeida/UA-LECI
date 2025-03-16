CREATE TABLE ConferenceManager_Instituicao (
    ID_Instituicao INT PRIMARY KEY,
    Nome VARCHAR(256) NOT NULL,
    Endereco VARCHAR(256) NOT NULL UNIQUE
);
GO

CREATE TABLE ConferenceManager_Autor (
    ID_Autor INT PRIMARY KEY,
    Nome VARCHAR(256) NOT NULL,
    Email VARCHAR(256) NOT NULL UNIQUE,
    ID_Instituicao INT NOT NULL,
    FOREIGN KEY (ID_Instituicao) REFERENCES ConferenceManager_Instituicao(ID_Instituicao)
);
GO

CREATE TABLE ConferenceManager_Artigo_Cientifico (
    Numero_Registo VARCHAR(128) PRIMARY KEY,
    Titulo VARCHAR(256) NOT NULL
);
GO

CREATE TABLE ConferenceManager_Tem (
    Numero_Registo VARCHAR(128) NOT NULL,
    ID_Autor INT NOT NULL,
    PRIMARY KEY (Numero_Registo, ID_Autor),
    FOREIGN KEY (Numero_Registo) REFERENCES ConferenceManager_Artigo_Cientifico(Numero_Registo),
    FOREIGN KEY (ID_Autor) REFERENCES ConferenceManager_Autor(ID_Autor)
);
GO

CREATE TABLE ConferenceManager_Participante (
    ID_Participante INT PRIMARY KEY,
    Nome VARCHAR(256) NOT NULL,
    Email VARCHAR(256) NOT NULL UNIQUE,
    Morada VARCHAR(256) NOT NULL,
    Data_Inscricao DATE NOT NULL,
    ID_Instituicao INT NOT NULL,
    FOREIGN KEY (ID_Instituicao) REFERENCES ConferenceManager_Instituicao(ID_Instituicao)
);
GO

CREATE TABLE ConferenceManager_Estudante (
    ID_Participante INT PRIMARY KEY,
    Local_Comprovativo VARCHAR(256) NOT NULL,
    FOREIGN KEY (ID_Participante) REFERENCES ConferenceManager_Participante(ID_Participante)
);
GO

CREATE TABLE ConferenceManager_Nao_Estudante (
    ID_Participante INT PRIMARY KEY,
    Referencia_Transacao VARCHAR(256) NOT NULL,
    FOREIGN KEY (ID_Participante) REFERENCES ConferenceManager_Participante(ID_Participante)
);
GO
