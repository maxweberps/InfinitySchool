CREATE DATABASE estoque;

USE estoque;

CREATE TABLE produtos (
	id_prod INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    descricao varchar(200),
    qtd_disp int,
    preco FLOAT
);

CREATE TABLE vendas (
	id_venda INT PRIMARY KEY AUTO_INCREMENT,
    qtd float,
    data_venda date,
    id_prod int,
    foreign key (id_prod) references produtos(id_prod)
);