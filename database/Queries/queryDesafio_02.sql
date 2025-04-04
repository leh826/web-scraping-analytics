SELECT
  o.Razao_Social,
  SUM(f.VL_SALDO_FINAL) AS Total_Despesas
FROM
  dados_financeiros f
JOIN
  ans_operadoras o ON f.REG_ANS = o.Registro_ANS
WHERE
(f.DESCRICAO LIKE 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%' OR 
   f.CD_CONTA_CONTABIL='41181')  
  AND f.DATA BETWEEN '2024-01-01' AND '2024-10-1'
GROUP BY
  o.Razao_Social
ORDER BY
  Total_Despesas DESC
LIMIT 10;
--Quais as 10 operadoras com maiores despesas nessa categoria no último ano?