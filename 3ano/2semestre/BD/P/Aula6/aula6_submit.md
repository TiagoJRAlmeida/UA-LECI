# BD: Guião 6

## Problema 6.1

### *a)* Todos os tuplos da tabela autores (authors);

```
SELECT * FROM authors;
```

### *b)* O primeiro nome, o último nome e o telefone dos autores;

```
SELECT au_fname, au_lname, phone FROM authors;
```

### *c)* Consulta definida em b) mas ordenada pelo primeiro nome (ascendente) e depois o último nome (ascendente); 

```
SELECT au_fname, au_lname, phone FROM authors ORDER BY au_fname, au_lname;
```

### *d)* Consulta definida em c) mas renomeando os atributos para (first_name, last_name, telephone); 

```
SELECT au_fname AS first_name, au_lname AS last_name, phone AS telephone FROM authors ORDER BY au_fname, au_lname;
```

### *e)* Consulta definida em d) mas só os autores da Califórnia (CA) cujo último nome é diferente de ‘Ringer’; 

```
SELECT au_fname AS first_name, au_lname AS last_name, phone AS telephone FROM authors WHERE state LIKE 'CA' AND au_lname NOT LIKE 'Ringer' ORDER BY au_fname, au_lname;
```

### *f)* Todas as editoras (publishers) que tenham ‘Bo’ em qualquer parte do nome; 

```
SELECT * FROM publishers WHERE pub_name LIKE '%Bo%';
```

### *g)* Nome das editoras que têm pelo menos uma publicação do tipo ‘Business’; 

```
SELECT pub_name FROM publishers INNER JOIN titles ON titles.pub_id = publishers.pub_id WHERE type LIKE 'Business';
```

### *h)* Número total de vendas de cada editora; 

```
SELECT publishers.pub_name, sum(ytd_sales) AS sales
FROM titles 
INNER JOIN publishers ON titles.pub_id = publishers.pub_id 
GROUP BY publishers.pub_name;
```

### *i)* Número total de vendas de cada editora agrupado por título; 

```
SELECT titles.title, publishers.pub_name, sum(ytd_sales) AS sales
FROM titles 
INNER JOIN publishers ON titles.pub_id = publishers.pub_id 
GROUP BY publishers.pub_name, titles.title; 
```

### *j)* Nome dos títulos vendidos pela loja ‘Bookbeat’; 

```
SELECT title 
FROM titles 
JOIN sales ON titles.title_id = sales.title_id
JOIN stores ON sales.stor_id = stores.stor_id
WHERE stores.stor_name = 'Bookbeat'
```

### *k)* Nome de autores que tenham publicações de tipos diferentes; 

```
SELECT authors.au_id, COUNT(titles.type) AS types FROM authors
INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN titles ON titles.title_id = titleauthor.title_id
GROUP BY authors.au_id, titles.type
HAVING COUNT(titles.type) > 1
```

### *l)* Para os títulos, obter o preço médio e o número total de vendas agrupado por tipo (type) e editora (pub_id);

```
SELECT 
    [type], 
    pub_id, 
    AVG(price) AS avg_price, 
    SUM(ytd_sales) AS total_sales
FROM titles
GROUP BY [type], pub_id;
```

### *m)* Obter o(s) tipo(s) de título(s) para o(s) qual(is) o máximo de dinheiro “à cabeça” (advance) é uma vez e meia superior à média do grupo (tipo);

```
SELECT [type]
FROM titles
GROUP BY [type]
HAVING MAX(advance) > 1.5*AVG(advance);
```

### *n)* Obter, para cada título, nome dos autores e valor arrecadado por estes com a sua venda;

```
SELECT titles.title, au_fname AS Author_first_name, au_lname AS Author_last_name, titles.ytd_sales AS Sales
FROM authors
INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN titles ON titleauthor.title_id = titles.title_id;
```

### *o)* Obter uma lista que incluía o número de vendas de um título (ytd_sales), o seu nome, a faturação total, o valor da faturação relativa aos autores e o valor da faturação relativa à editora;

```
SELECT 
	title, 
	ytd_sales, 
	price*ytd_sales AS faturacao, 
	price*ytd_sales*royalty/100 AS auths_revenue, 
	price*ytd_sales*(100-royalty)/100 AS publisher_revenue
FROM titles;
```

### *p)* Obter uma lista que incluía o número de vendas de um título (ytd_sales), o seu nome, o nome de cada autor, o valor da faturação de cada autor e o valor da faturação relativa à editora;

```
SELECT title, ytd_sales, price*ytd_sales AS faturacao, 
concat(au_fname,' ',au_lname) AS author, price*ytd_sales*royalty*royaltyper*1/10000 AS auth_revenue, price*ytd_sales*(100-royalty)*1/100 AS publisher_revenue
FROM ((titles JOIN titleauthor ON titles.title_id=titleauthor.title_id) JOIN authors ON titleauthor.au_id=authors.au_id)
ORDER BY title;
```

### *q)* Lista de lojas que venderam pelo menos um exemplar de todos os livros;

```
SELECT stor_name, count(title) as n_titles
FROM stores 
INNER JOIN sales on stores.stor_id=sales.stor_id
INNER JOIN titles on sales.title_id=titles.title_id
GROUP by stor_name
HAVING count(title) >= count(titles.title_id);
```

### *r)* Lista de lojas que venderam mais livros do que a média de todas as lojas;

```
SELECT stores.stor_name, SUM(sales.qty) AS total_books_sold
FROM stores
INNER JOIN sales ON stores.stor_id = sales.stor_id
GROUP BY stores.stor_id, stores.stor_name
HAVING SUM(sales.qty) > (
    SELECT AVG(total_sales)
    FROM (
        SELECT SUM(sales.qty) AS total_sales
        FROM sales
        GROUP BY sales.stor_id
    ) AS avg_sales_per_store
);
```

### *s)* Nome dos títulos que nunca foram vendidos na loja “Bookbeat”;

```
SELECT titles.title
FROM titles
WHERE titles.title_id NOT IN (
    SELECT DISTINCT sales.title_id
    FROM sales
    INNER JOIN stores ON sales.stor_id = stores.stor_id
    WHERE stores.stor_name = 'Bookbeat'
);
```

### *t)* Para cada editora, a lista de todas as lojas que nunca venderam títulos dessa editora; 

```
SELECT publishers.pub_id, publishers.pub_name, stores.stor_id, stores.stor_name
FROM publishers
CROSS JOIN stores
WHERE NOT EXISTS (
    SELECT 1 
    FROM sales
    JOIN titles ON sales.title_id = titles.title_id
    WHERE titles.pub_id = publishers.pub_id
    AND sales.stor_id = stores.stor_id
)
ORDER BY publishers.pub_name, stores.stor_name;
```

## Problema 6.2

### ​5.1

#### a) SQL DDL Script
 
[a) SQL DDL File](ex_6_2_1_ddl.sql "SQLFileQuestion")

#### b) Data Insertion Script

[b) SQL Data Insertion File](ex_6_2_1_data.sql "SQLFileQuestion")

#### c) Queries

##### *a)*

```
SELECT distinct Fname, Minit, Lname
FROM employee
JOIN works_On
ON Ssn=Essn
JOIN project
ON Pno=Pnumber;
```

##### *b)* 

```
SELECT Fname, Minit, Lname 
FROM employee WHERE Super_ssn =(
SELECT Ssn
FROM employee
WHERE Fname='Carlos' AND Minit='D' AND Lname='Gomes');
```

##### *c)* 

```
SELECT Pname, SUM(Hourss) as total_hours
FROM employee
JOIN works_On
ON Ssn=Essn
JOIN project
ON Pno=Pnumber
GROUP BY Pname;
```

##### *d)* 

```
SELECT Fname, Minit, Lname
FROM employee
JOIN works_On
ON Ssn=Essn
JOIN project
ON Pno=Pnumber
WHERE Dno=3 AND Pname='Aveiro Digital' AND Hourss > 20;
```

##### *e)* 

```
SELECT Fname, Minit, Lname
FROM employee
FULL OUTER JOIN works_On
ON Ssn=Essn
WHERE Hourss IS NULL;
```

##### *f)* 

```
SELECT Dname, AVG(Salary)
FROM
(SELECT *
FROM department
JOIN employee
ON Dnumber=DNo
WHERE Sex='F') AS A
GROUP BY Dname;
```

##### *g)* 

```
SELECT Essn
FROM dependents
JOIN employee
ON Essn=Ssn
GROUP BY Essn
HAVING COUNT(Essn) > 2;
```

##### *h)* 

```
SELECT Mgr_ssn FROM 
(SELECT *
FROM dependents
FULL OUTER JOIN department
ON Essn=Mgr_ssn) AS E
WHERE E.Essn IS NULL;
```

##### *i)* 

```
SELECT DISTINCT Fname, Minit, Lname, Addresss
FROM employee
JOIN works_On
ON Ssn=Essn
JOIN project
ON Pno=Pnumber
JOIN dept_Locations
ON Dno=Dnumber
WHERE Plocation='Aveiro' AND Dlocation!='Aveiro';
```

### 5.2

#### a) SQL DDL Script
 
[a) SQL DDL File](ex_6_2_2_ddl.sql "SQLFileQuestion")

#### b) Data Insertion Script

[b) SQL Data Insertion File](ex_6_2_2_data.sql "SQLFileQuestion")

#### c) Queries

##### *a)*

```
SELECT *
FROM Fornecedor
FULL OUTER JOIN Encomenda
ON Fornecedor=Nif
WHERE Numero IS NULL;
```

##### *b)* 

```
SELECT Nome, AVG(item.Unidades) AS avg_units_order FROM item
JOIN Produto
ON Codigo=CodProd
GROUP BY Nome;
```


##### *c)* 

```
SELECT AVG(Aa) AS avg_number_diff_items_per_order
FROM
(SELECT CAST(COUNT(*) AS FLOAT) AS Aa FROM item
GROUP BY NumEnc) AS a;
```


##### *d)* 

```
SELECT Fornecedor.Nome, Produto.Nome, SUM(Item.Unidades) FROM Encomenda
JOIN Fornecedor
ON Fornecedor=Nif
JOIN Item
ON NumEnc=Numero
JOIN Produto
ON Codigo=CodProd
GROUP BY Fornecedor.Nome, Produto.Nome;
```

### 5.3

#### a) SQL DDL Script
 
[a) SQL DDL File](ex_6_2_3_ddl.sql "SQLFileQuestion")

#### b) Data Insertion Script

[b) SQL Data Insertion File](ex_6_2_3_data.sql "SQLFileQuestion")

#### c) Queries

##### *a)*

```
SELECT *
FROM Paciente
WHERE NSNS
NOT IN (SELECT DISTINCT NSNS FROM Prescricao);
```

##### *b)* 

```
SELECT Especialidade, COUNT(*) AS prescricoes FROM medico
JOIN Prescricao
ON medico.nid=Prescricao.nid
GROUP BY Especialidade;
```


##### *c)* 

```
SELECT COUNT(*) AS processed_no FROM Prescricao
WHERE Data_proc IS NOT NULL;
```


##### *d)* 

```
SELECT * FROM Presc_farmaco
FULL OUTER JOIN Farmaco
ON Nome=Nome_farmaco
WHERE Nreg=906
AND Num_presc IS NULL;
```

##### *e)* 

```
SELECT Nome_farmacia, Num_reg_farm, COUNT(*) AS sold_farma FROM Prescricao
JOIN Presc_farmaco
ON Num_presc=Nuni
WHERE Nome_farmacia IS NOT NULL
GROUP BY Nome_farmacia, Num_reg_farm;
```

##### *f)* 

```
SELECT NSNS FROM prescricao
GROUP BY NSNS
HAVING COUNT(DISTINCT NID) > 1;
```
