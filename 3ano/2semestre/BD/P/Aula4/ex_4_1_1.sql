CREATE TABLE RentACar_Cliente(
NIF varchar(9) NOT NULL,
Nome varchar(256) NOT NULL,
Endereco varchar(512) NOT NULL,
numCarta varchar(16) NOT NULL,
PRIMARY KEY (NIF))
GO

CREATE TABLE RentACar_Balcao(
Numero int NOT NULL,
Nome varchar(256) NOT NULL,
Endereco varchar(256) NOT NULL,
PRIMARY KEY (Numero))
GO

CREATE TABLE RentACar_TipoVeiculo(
Codigo int NOT NULL,
Designacao varchar(128) NOT NULL,
ArCondicionado bit NOT NULL,
PRIMARY KEY (Codigo))
GO

CREATE TABLE RentACar_Veiculo(
Matricula varchar(8) NOT NULL,
Marca varchar(32),
Ano int,
TipoVeiculo_Codigo int,
PRIMARY KEY (Matricula),
FOREIGN KEY (TipoVeiculo_Codigo) REFERENCES RentACar_TipoVeiculo (Codigo))
GO

CREATE TABLE RentACar_Aluguer(
Numero int NOT NULL PRIMARY KEY,
Duracao int NOT NULL,
[Data] date NOT NULL,
Cliente_NIF varchar(9) NOT NULL REFERENCES RentACar_Cliente (NIF),
Balcao_Numero int NOT NULL REFERENCES RentACar_Balcao (Numero),
Veiculo_Matricula varchar(8) NOT NULL REFERENCES RentACar_Veiculo (Matricula))
GO


CREATE TABLE RentACar_Pesado(
Peso int NOT NULL,
Passageiros int NOT NULL,
Codigo int NOT NULL REFERENCES RentACar_TipoVeiculo (Codigo),
PRIMARY KEY (Codigo))
GO

CREATE TABLE RentACar_Ligeiro(
NumLugares int NOT NULL,
Portas int NOT NULL,
Combustivel int NOT NULL,
Codigo int NOT NULL REFERENCES RentACar_TipoVeiculo (Codigo),
PRIMARY KEY (Codigo))
GO