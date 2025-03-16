CREATE TABLE ATL_Professor(
    CC int NOT NULL PRIMARY KEY,
    Nome varchar(256) NOT NULL,
    Morada varchar(256) NOT NULL,
    Data_Nascimento date NOT NULL,
    Telefone int NOT NULL,
    Email varchar(256) NOT NULL,
    Num_Funcionario int NOT NULL
)
GO

CREATE TABLE ATL_Turma(
    Professor_CC int NOT NULL REFERENCES ATL_Professor (CC),
    ID int NOT NULL,
    Classe int NOT NULL,
    Ano_Letivo int NOT NULL,
    Designacao varchar(256) NOT NULL,
    Alunos_Maximo int NOT NULL,
    PRIMARY KEY (ID)
)
GO

CREATE TABLE ATL_Enc_Edu(
    CC int NOT NULL PRIMARY KEY,
    Nome varchar(256) NOT NULL,
    Relacao_Aluno varchar(64) NOT NULL,
    Email varchar(256) NOT NULL,
    Telefone int NOT NULL,
    Data_Nasicmento date NOT NULL,
    Morada varchar(256) NOT NULL
)
GO

CREATE TABLE ATL_Atividade(
    ID int NOT NULL PRIMARY KEY,
    Designacao varchar(256) NOT NULL,
    Custo int NOT NULL
)
GO

CREATE TABLE ATL_Aluno(
    Atividade_ID int REFERENCES ATL_Atividade(ID),
    Turma_ID int NOT NULL REFERENCES ATL_Turma (ID),
    Enc_Edu_CC int NOT NULL REFERENCES ATL_Enc_Edu (CC),
    CC int NOT NULL PRIMARY KEY,
    Morada varchar(256) NOT NULL,
    Data_Nascimento date NOT NULL,
    Nome varchar(256) NOT NULL
)
GO

CREATE TABLE ATL_Autorizados(
    Aluno_CC int NOT NULL REFERENCES ATL_Aluno (CC),
    CC int NOT NULL PRIMARY KEY,
    Nome int NOT NULL,
    Relacao_Aluno varchar(64) NOT NULL,
    Email varchar(256) NOT NULL,
    Telefone int NOT NULL,
    Data_Nascimento date NOT NULL,
    Morada varchar(256) NOT NULL
)
GO