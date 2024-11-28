USE eventus;

-- Script para criar a tabela 'especies'
CREATE TABLE eventos (
    evento_id INT AUTO_INCREMENT PRIMARY KEY,
    titulo_evento VARCHAR(80) NOT NULL,
    descricao VARCHAR(255),
    data_evento VARCHAR(10),
);


-- Inserir uma espécie com ID auto-incrementado
INSERT INTO eventos (titulo_evento, descricao, data_evento)
VALUES ('Futebol várzea 2024', 'O evento acontecerá na unaerp, com valor de R$100.000.00', '24/11/2024');

-- Exibir os registros da tabela especies
SELECT * FROM evento;


-- DELETE FROM evento WHERE animal_id IN (3, 4);

