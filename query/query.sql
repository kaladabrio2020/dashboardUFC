-- Status 
SELECT u.status, u.forma_ingresso, count(*) FROM ufc AS u
    WHERE u.status LIKE ANY (ARRAY['%%Cancelado%%', '%%Ativo%%', '%%Trancado%%', '%%Concluído%%']) AND
          u.ano_ingresso   BETWEEN 2010 and 2023 AND
          u.forma_ingresso LIKE ANY (ARRAY['%%VESTIBULAR%%', '%%SISU%%'])
    GROUP BY u.status, forma_ingresso;


SELECT u.sexo, u.forma_ingresso, u.status, count(*) FROM ufc AS u
    WHERE u.status LIKE ANY (ARRAY['%%Cancelado%%', '%%Ativo%%', '%%Mobilidade%%', '%%Trancado%%']) AND
          u.ano_ingresso   BETWEEN 2010 and 2024 AND
          u.forma_ingresso LIKE ANY (ARRAY['%%VESTIBULAR%%', '%%SISU%%'])
    GROUP BY u.sexo, forma_ingresso, u.status;

SELECT u.nome_curso, u.forma_ingresso, u.status, count(*) FROM ufc AS u
    WHERE u.status LIKE ANY (ARRAY['%%Cancelado%%', '%%Ativo%%', '%%Mobilidade%%', '%%Trancado%%']) AND
          u.ano_ingresso   BETWEEN 2010 and 2024 AND
          u.forma_ingresso LIKE ANY (ARRAY['%%VESTIBULAR%%', '%%SISU%%'])
    GROUP BY u.nome_curso, forma_ingresso, u.status
    ORDER BY u.count DESC;

SELECT uf.status, uf.forma_ingresso, ROUND(AVG(ABS(uf.ano_ingresso - CAST( uf.ano_saida AS BIGINT))), 2) as media FROM ufc as uf
    WHERE uf.ano_saida != 'xx' AND
        uf.ano_ingresso   BETWEEN 2010 and 2024 AND
        uf.forma_ingresso LIKE ANY (ARRAY['%%VESTIBULAR%%', '%%SISU%%'])
    GROUP BY uf.status, uf.forma_ingresso;
SELECT MIN(DISTINCT ano_ingresso) FROM ufc
WHERE modalidade_considerada LIKE '%%Cota%%';


SELECT count(DISTINCT nome_curso) FROM ufc
    WHERE ano_ingresso BETWEEN 2010 and 2020;


-- top 5 curso com maior taxa de saida

WITH tabela AS (
    SELECT u.nome_curso, count(u.status)::FLOAT AS total FROM ufc AS u
        WHERE u.ano_ingresso BETWEEN 2023 and 2023 AND
              u.forma_ingresso LIKE ANY (ARRAY['%%VESTIBULAR%%', '%%SISU%%'])
    GROUP BY u.nome_curso
),
 tabela2 AS (
    SELECT u.nome_curso, count(*)::FLOAT AS desistencia FROM ufc AS u
        WHERE u.status = 'Cancelado' AND
              u.ano_ingresso BETWEEN 2023 and 2023 AND 
              u.forma_ingresso LIKE ANY (ARRAY['%%VESTIBULAR%%', '%%SISU%%'])
    GROUP BY u.nome_curso
) SELECT t1.nome_curso, ROUND((t2.desistencia / t1.total)::DECIMAL*100 , 2) AS taxa_cancelamento FROM tabela AS t1
    INNER JOIN tabela2 AS t2
        ON t1.nome_curso = t2.nome_curso
    ORDER BY taxa_cancelamento DESC LIMIT 5;

-- 2017
SELECT  CAST(u.ano_saida AS INT), u.nome_mobilidadade_considerada, u.modalidade_considerada, count(*) FROM ufc AS u
    WHERE u.nome_mobilidadade_considerada !='xx' AND
          u.status = 'Cancelado' AND
          u.ano_saida !='xx'
    GROUP BY CAST(u.ano_saida AS INT), u.nome_mobilidadade_considerada, u.modalidade_considerada;


SELECT MIN(DISTINCT ano_ingresso) FROM ufc

SELECT * FROM ufc AS u
    WHERE u.nome_curso ='Historia';

-- Série historica de desistencias
SELECT uf.ano_saida, uf.status, count(*) FROM ufc AS uf
    WHERE uf.status = 'Cancelado' AND uf.ano_saida !='xx'
GROUP BY uf.ano_saida, uf.status;

