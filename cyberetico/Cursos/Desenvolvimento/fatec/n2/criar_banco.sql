CREATE DATABASE IF NOT EXISTS `duck_tech`
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE `duck_tech`;

CREATE TABLE IF NOT EXISTS `funcionarios` (
    `id`           INT AUTO_INCREMENT PRIMARY KEY,
    `nome`         VARCHAR(100) NOT NULL,
    `endereco`     VARCHAR(150),
    `numero`       VARCHAR(10),
    `complemento`  VARCHAR(100),
    `celular`      VARCHAR(20),
    `bairro`       VARCHAR(100),
    `cep`          VARCHAR(10),
    `cidade`       VARCHAR(100),
    `uf`           VARCHAR(2),
    `email`        VARCHAR(100),
    `cargo`        VARCHAR(50),
    `usuario`      VARCHAR(50) UNIQUE NOT NULL,
    `senha`        VARCHAR(255) NOT NULL,
    `departamento` VARCHAR(50)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
