-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           10.6.17-MariaDB - mariadb.org binary distribution
-- OS do Servidor:               Win64
-- HeidiSQL Versão:              12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para loja
DROP DATABASE IF EXISTS `loja`;
CREATE DATABASE IF NOT EXISTS `loja` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci */;
USE `loja`;

-- Copiando estrutura para tabela loja.categoria_produto
DROP TABLE IF EXISTS `categoria_produto`;
CREATE TABLE IF NOT EXISTS `categoria_produto` (
  `categoria_id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `descricao` text DEFAULT NULL,
  PRIMARY KEY (`categoria_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela loja.categoria_produto: ~10 rows (aproximadamente)
DELETE FROM `categoria_produto`;
INSERT INTO `categoria_produto` (`categoria_id`, `nome`, `descricao`) VALUES
	(1, 'Eletrônicos', 'Produtos relacionados a eletrônicos, como smartphones, notebooks, câmeras, etc.'),
	(2, 'Móveis', 'Itens de mobiliário para casa ou escritório, incluindo sofás, mesas, cadeiras, etc.'),
	(3, 'Vestuário', 'Roupas e acessórios, incluindo camisetas, calças, jaquetas, bolsas, etc.'),
	(4, 'Eletrodomésticos', 'Grandes e pequenos aparelhos para facilitar as tarefas domésticas'),
	(5, 'Livros', 'Livros de todos os gêneros e para todas as idades'),
	(6, 'Artigos Esportivos', 'Equipamentos e roupas para prática de esportes'),
	(7, 'Brinquedos', 'Brinquedos educativos e para diversão de crianças de todas as idades'),
	(8, 'Jardinagem', 'Ferramentas, insumos e decorações para jardinagem e cuidados com plantas'),
	(9, 'Informática', 'Produtos de informática incluindo hardware, software e acessórios'),
	(10, 'Beleza e Saúde', 'Produtos para cuidados pessoais, saúde e beleza');

-- Copiando estrutura para tabela loja.cliente
DROP TABLE IF EXISTS `cliente`;
CREATE TABLE IF NOT EXISTS `cliente` (
  `cliente_id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `endereco` text DEFAULT NULL,
  PRIMARY KEY (`cliente_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela loja.cliente: ~10 rows (aproximadamente)
DELETE FROM `cliente`;
INSERT INTO `cliente` (`cliente_id`, `nome`, `email`, `telefone`, `endereco`) VALUES
	(1, 'Luisa Fernandes', 'luisa.fernandes@gmail.com', '21987654321', 'Av. das Américas, 500, Rio de Janeiro - RJ'),
	(2, 'Ricardo Almeida', 'ricardo.almeida@email.com', '11987654321', 'Alameda Santos, 100, São Paulo - SP'),
	(3, 'Gabriela Souza', 'gabriela.souza@gmail.com', '31987650004', 'Rua das Laranjeiras, 123, Belo Horizonte - MG'),
	(4, 'Carlos Andrade', 'carlos.andrade@gmail.com', '85987650005', 'Av. Beira Mar, 456, Fortaleza - CE'),
	(5, 'Fernanda Lima', 'fernanda.lima@gmaill.com', '21987650009', 'Av. das Palmeiras, 234, Niterói - RJ'),
	(6, 'Tiago Gomes', 'tiago.gomes@email.com', '11987650010', 'Rua dos Pinheiros, 567, São Paulo - SP'),
	(7, 'Juliana Moraes', 'juliana.moraes@email.com', '21987651111', 'Av. Maracanã, 789, Rio de Janeiro - RJ'),
	(8, 'Rafael Costa', 'rafael.costa@email.com', '11987652222', 'Praça da Sé, 321, São Paulo - SP'),
	(9, 'Patricia Barbosa', 'patricia.barbosa@email.com', '31987653333', 'Av. Afonso Pena, 456, Belo Horizonte - MG'),
	(10, 'Eduardo Pereira', 'eduardo.pereira@email.com', '41987654444', 'Rua XV de Novembro, 123, Curitiba - PR');

-- Copiando estrutura para tabela loja.fornecedor
DROP TABLE IF EXISTS `fornecedor`;
CREATE TABLE IF NOT EXISTS `fornecedor` (
  `fornecedor_id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `contato` varchar(255) DEFAULT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `endereco` text DEFAULT NULL,
  PRIMARY KEY (`fornecedor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela loja.fornecedor: ~9 rows (aproximadamente)
DELETE FROM `fornecedor`;
INSERT INTO `fornecedor` (`fornecedor_id`, `nome`, `contato`, `telefone`, `endereco`) VALUES
	(1, 'EletroTech', 'Márcia Lima', '11987650001', 'Rua Eletrônica, 400, São Paulo - SP'),
	(2, 'DecorCasa', 'Túlio Borges', '21987650002', 'Av. dos Decoradores, 750, Rio de Janeiro - RJ'),
	(3, 'FashionStyle', 'Carla Dias', '31987650003', 'Alameda da Moda, 320, Belo Horizonte - MG'),
	(4, 'HighTech Equipamentos', 'Paulo Santos', '11987650006', 'Av. das Indústrias, 789, São Paulo - SP'),
	(5, 'HomeSweetHome Decorações', 'Sílvia Pereira', '21987650007', 'Rua das Flores, 1012, Rio de Janeiro - RJ'),
	(6, 'UrbanFashion Roupas', 'Renata Moura', '31987650008', 'Alameda Fashion, 303, Belo Horizonte - MG'),
	(7, 'ConfortoCasa Eletro', 'Claudia Silva', '11987650011', 'Av. dos Eletrodomésticos, 890, Campinas - SP'),
	(8, 'LeituraTotal Livraria', 'Marcelo Pires', '21987650012', 'Rua dos Livros, 345, Salvador - BA'),
	(9, 'AtletaEquip Esportes', 'Roberto Carvalho', '31987650013', 'Alameda dos Esportes, 678, Belo Horizonte - MG'),
	(10, 'Brinca Mundo', 'Sonia Ferreira', '11987655555', 'Av. Brigadeiro Faria Lima, 1571, São Paulo - SP'),
	(11, 'Verde Vida Jardinagem', 'Marco Tulio', '21987656666', 'Rua Barão do Amazonas, 352, Niterói - RJ'),
	(12, 'Tech Solutions', 'Ana Carolina', '31987657777', 'Av. do Contorno, 6594, Belo Horizonte - MG'),
	(13, 'Estética & Bem-Estar', 'Luciana Souza', '41987658888', 'Rua das Flores, 890, Curitiba - PR');

-- Copiando estrutura para tabela loja.produto
DROP TABLE IF EXISTS `produto`;
CREATE TABLE IF NOT EXISTS `produto` (
  `produto_id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `descricao` text DEFAULT NULL,
  `preco` decimal(10,2) NOT NULL,
  `estoque` int(11) DEFAULT 0,
  `fornecedor_id` int(11) DEFAULT NULL,
  `categoria_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`produto_id`),
  KEY `fornecedor_id` (`fornecedor_id`),
  CONSTRAINT `produto_ibfk_1` FOREIGN KEY (`fornecedor_id`) REFERENCES `fornecedor` (`fornecedor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela loja.produto: ~26 rows (aproximadamente)
DELETE FROM `produto`;
INSERT INTO `produto` (`produto_id`, `nome`, `descricao`, `preco`, `estoque`, `fornecedor_id`, `categoria_id`) VALUES
	(1, 'Smartphone XZ2', 'Smartphone XZ2, 128GB, tela 6.1"', 2800.00, 150, 1, 1),
	(2, 'Mesa de Centro', 'Mesa de centro em vidro, 90x50 cm', 450.00, 40, 2, 2),
	(3, 'Camiseta Polo', 'Camiseta polo algodão, cor azul, tamanho M', 120.00, 200, 3, 3),
	(4, 'Notebook Pro 15', 'Notebook Pro 15, i7, 16GB RAM, SSD 1TB', 7800.00, 60, 1, 1),
	(5, 'Cadeira Gamer', 'Cadeira gamer ergonômica com apoio', 1300.00, 30, 2, 2),
	(6, 'Vestido Floral', 'Vestido floral verão, tamanho G', 89.99, 120, 3, 3),
	(7, 'Teclado Mecânico', 'Teclado mecânico RGB, layout ABNT2', 350.00, 100, 4, 1),
	(8, 'Tapete Persa', 'Tapete persa 2x3 metros, 100% lã', 2000.00, 15, 5, 2),
	(9, 'Jaqueta Jeans', 'Jaqueta jeans azul, tamanho P', 250.00, 75, 6, 3),
	(10, 'Smartwatch 8Gen', 'Smartwatch 8ª Geração, monitora saúde', 1200.00, 90, 4, 1),
	(11, 'Poltrona Reclinável', 'Poltrona reclinável, couro, preta', 1800.00, 20, 5, 2),
	(12, 'Calça Legging', 'Calça legging esportiva, preta, M', 99.90, 150, 6, 3),
	(13, 'Liquidificador PowerMix', 'Liquidificador 5 velocidades, 700W potência', 180.00, 80, 7, 4),
	(14, 'Guerra dos Tronos - Livro', 'Primeiro volume da saga As Crônicas de Gelo e Fogo', 49.90, 120, 8, 5),
	(15, 'Bicicleta Speed', 'Bicicleta speed com quadro de alumínio e 21 marchas', 1200.00, 40, 9, 6),
	(16, 'Micro-ondas QuickCook', 'Micro-ondas 30L com função descongelar', 350.00, 60, 7, 4),
	(17, '1984 - George Orwell', 'Clássico da literatura distópica', 29.90, 150, 8, 5),
	(18, 'Kit de Halteres', 'Conjunto de halteres ajustáveis, até 20kg', 300.00, 75, 9, 6),
	(19, 'Cubo Mágico', 'Cubo Mágico profissional 3x3x3', 25.90, 200, 10, 7),
	(20, 'Kit Jardinagem', 'Kit Jardinagem com 5 ferramentas básicas', 120.00, 80, 11, 8),
	(21, 'Mouse Gamer', 'Mouse Gamer com fio, 7200 DPI ajustáveis', 89.99, 150, 12, 9),
	(22, 'Creme Hidratante Facial', 'Creme hidratante facial, 50g', 59.90, 100, 13, 10),
	(23, 'Quebra-Cabeça 1000 peças', 'Quebra-cabeça temático, 1000 peças', 49.90, 150, 10, 7),
	(24, 'Vaso Decorativo', 'Vaso decorativo em cerâmica, 30cm', 85.00, 60, 11, 8),
	(25, 'Teclado Mecânico RGB', 'Teclado mecânico RGB, switches azuis', 250.00, 75, 12, 9),
	(26, 'Kit Maquiagem Básico', 'Kit maquiagem com itens essenciais', 180.00, 90, 13, 10);

-- Copiando estrutura para tabela loja.venda
DROP TABLE IF EXISTS `venda`;
CREATE TABLE IF NOT EXISTS `venda` (
  `venda_id` int(11) NOT NULL AUTO_INCREMENT,
  `cliente_id` int(11) DEFAULT NULL,
  `data_hora` datetime DEFAULT current_timestamp(),
  `valor_total` decimal(10,2) NOT NULL,
  PRIMARY KEY (`venda_id`),
  KEY `cliente_id` (`cliente_id`),
  CONSTRAINT `venda_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `cliente` (`cliente_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela loja.venda: ~6 rows (aproximadamente)
DELETE FROM `venda`;
INSERT INTO `venda` (`venda_id`, `cliente_id`, `data_hora`, `valor_total`) VALUES
	(1, 1, '2023-10-05 10:30:00', 2890.00),
	(2, 2, '2023-10-06 14:45:00', 7800.00),
	(3, 3, '2023-10-07 09:15:00', 649.90),
	(4, 4, '2023-10-08 16:00:00', 2299.90),
	(5, 5, '2023-10-09 10:20:00', 229.90),
	(6, 6, '2023-10-10 15:30:00', 1529.90),
	(7, 7, '2023-10-11 10:00:00', 255.89),
	(8, 8, '2023-10-12 14:30:00', 335.90),
	(9, 5, '2023-10-13 16:45:00', 215.00),
	(10, 6, '2023-10-14 11:15:00', 584.89);

-- Copiando estrutura para tabela loja.venda_produto
DROP TABLE IF EXISTS `venda_produto`;
CREATE TABLE IF NOT EXISTS `venda_produto` (
  `venda_id` int(11) NOT NULL,
  `produto_id` int(11) NOT NULL,
  `quantidade` int(11) DEFAULT NULL,
  `preco_unitario` decimal(10,2) NOT NULL,
  PRIMARY KEY (`venda_id`,`produto_id`),
  KEY `produto_id` (`produto_id`),
  CONSTRAINT `venda_produto_ibfk_1` FOREIGN KEY (`venda_id`) REFERENCES `venda` (`venda_id`),
  CONSTRAINT `venda_produto_ibfk_2` FOREIGN KEY (`produto_id`) REFERENCES `produto` (`produto_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

-- Copiando dados para a tabela loja.venda_produto: ~15 rows (aproximadamente)
DELETE FROM `venda_produto`;
INSERT INTO `venda_produto` (`venda_id`, `produto_id`, `quantidade`, `preco_unitario`) VALUES
	(1, 1, 1, 2800.00),
	(1, 3, 1, 120.00),
	(2, 4, 1, 7800.00),
	(3, 7, 1, 350.00),
	(3, 9, 2, 250.00),
	(4, 8, 1, 1200.00),
	(4, 10, 1, 1800.00),
	(4, 12, 1, 99.90),
	(5, 13, 1, 180.00),
	(5, 15, 1, 49.90),
	(6, 14, 1, 1200.00),
	(6, 16, 1, 29.90),
	(6, 18, 1, 300.00),
	(7, 19, 2, 25.90),
	(7, 21, 1, 89.99);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
