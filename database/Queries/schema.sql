
CREATE TABLE IF NOT EXISTS ans_operadoras (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(10),
    cnpj VARCHAR(14),
    razao_social TEXT,
    nome_fantasia TEXT,
    modalidade VARCHAR(50),
    logradouro TEXT,
    numero VARCHAR(20),
    complemento TEXT,
    bairro VARCHAR(50),
    cidade VARCHAR(50),
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(3),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico TEXT,
    representante TEXT,
    cargo_representante VARCHAR(50),
    regiao_comercializacao INTEGER,
    data_registro_ans DATE
);
