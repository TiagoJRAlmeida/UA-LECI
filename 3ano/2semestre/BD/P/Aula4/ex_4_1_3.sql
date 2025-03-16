CREATE TABLE StockManager_Tipo_Fornecedor(
    ID int NOT NULL PRIMARY KEY,
    Designacao varchar(64) NOT NULL,
    Endereco varchar(256) NOT NULL,
    Nome varchar(256) NOT NULL,
    Numero_Fax int NOT NULL
)
GO

CREATE TABLE StockManager_Fornecedor(
    NIF int NOT NULL,
    ID_Tipo_Fornecedor int NOT NULL REFERENCES StockManager_Tipo_Fornecedor(ID),
    Condicoes_Pagamento varchar(512) NOT NULL,
    Endereco varchar(256) NOT NULL,
    Nome varchar(256) NOT NULL,
    Numero_Fax int NOT NULL
    PRIMARY KEY (NIF, ID_Tipo_Fornecedor)
)
GO

CREATE TABLE StockManager_Encomenda(
    Numero int NOT NULL,
    NIF int NOT NULL,
    ID_Fornecedor int NOT NULL,
    FOREIGN KEY (NIF, ID_Fornecedor) REFERENCES StockManager_Fornecedor (NIF, ID_Tipo_Fornecedor),
    PRIMARY KEY (Numero)
)
GO

CREATE TABLE StockManager_Produto(
    Numero_Encomenda int NOT NULL REFERENCES StockManager_Encomenda (Numero),
    Codigo int NOT NULL,
    Nome varchar(256) NOT NULL,
    Quantidade_Armazem int NOT NULL,
    Preco int NOT NULL,
    IVA int NOT NULL,
    PRIMARY KEY (Numero_Encomenda, Codigo)
)
GO