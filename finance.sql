CREATE TABLE IF NOT EXISTS contabilidade (
    data DATE,
    reg_ans VARCHAR(10),
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    vl_saldo_inicial NUMERIC(15,2),
    vl_saldo_final NUMERIC(15,2)
);

