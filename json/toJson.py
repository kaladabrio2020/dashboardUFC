import json


dicionario = {
    'SerieHistoricaDesistencia':'''
SELECT uf.ano_saida, uf.status, count(*) FROM ufc AS uf
    WHERE uf.status = 'Cancelado' AND uf.ano_saida !='xx'
GROUP BY uf.ano_saida, uf.status;
''','TootipsSerieHistoricaDesistencia':'''
SELECT uf.nome_unidade, count(*) FROM ufc AS uf
    WHERE uf.status = 'Cancelado' AND uf.ano_saida !='xx' AND CAST(uf.ano_saida AS INT) = ano1 
GROUP BY uf.ano_saida, uf.nome_unidade 
ORDER BY count DESC
LIMIT 5;
''',
    'Forma de entrada':'''
SELECT u.status, u.forma_ingresso, count(*) FROM ufc AS u
    WHERE u.status LIKE ANY (ARRAY['%%d1%%', '%%d2%%', '%%d3%%', '%%d4%%']) AND
          u.ano_ingresso   BETWEEN ano1_ and ano2_ AND
          u.forma_ingresso LIKE ANY (ARRAY['%%c1%%', '%%c2%%'])
    GROUP BY u.status, forma_ingresso;
''',
    'PorSexo':'''
SELECT u.sexo, u.forma_ingresso, u.status, count(*) FROM ufc AS u
    WHERE u.status LIKE ANY (ARRAY['%%d1%%', '%%d2%%', '%%d3%%', '%%d4%%']) AND
          u.ano_ingresso   BETWEEN ano1_ and ano2_ AND
          u.forma_ingresso LIKE ANY (ARRAY['%%c1%%', '%%c2%%'])
    GROUP BY u.sexo, forma_ingresso, u.status;
''',

    'MediaAprovados':'''
SELECT uf.status, uf.forma_ingresso, ROUND(AVG(ABS(uf.ano_ingresso - CAST( uf.ano_saida AS BIGINT))), 2) AS media FROM ufc as uf
    WHERE uf.ano_saida != 'xx' AND
        uf.ano_ingresso   BETWEEN ano1_ and ano2_ AND
        uf.forma_ingresso LIKE ANY (ARRAY['%%c1%%', '%%c2%%'])
    GROUP BY uf.status, uf.forma_ingresso;
    ''',

    'TaxaCancelados':'''
WITH tabela AS (
    SELECT u.nome_curso, count(u.status)::FLOAT AS total FROM ufc AS u
        WHERE u.ano_ingresso BETWEEN ano1_ and ano2_ AND
              u.forma_ingresso LIKE ANY (ARRAY['%%c1%%', '%%c2%%'])
    GROUP BY u.nome_curso
),
 tabela2 AS (
    SELECT u.nome_curso, count(*)::FLOAT AS desistencia FROM ufc AS u
        WHERE u.status = 'Cancelado' AND
              u.ano_ingresso BETWEEN ano1_ and ano2_ AND 
              u.forma_ingresso LIKE ANY (ARRAY['%%c1%%', '%%c2%%'])
    GROUP BY u.nome_curso
) SELECT t1.nome_curso, ROUND((t2.desistencia / t1.total)::DECIMAL*100 , 2) AS taxa_cancelamento FROM tabela AS t1
    INNER JOIN tabela2 AS t2
        ON t1.nome_curso = t2.nome_curso
    ORDER BY taxa_cancelamento DESC LIMIT 10;
''', 

    'CancelamentoMatricularModalidade':'''
SELECT  CAST(u.ano_saida AS INT), u.nome_mobilidadade_considerada, u.modalidade_considerada, count(*) FROM ufc AS u
    WHERE u.nome_mobilidadade_considerada !='xx' AND
          u.status = 'Cancelado' AND
          u.ano_saida !='xx'
    GROUP BY CAST(u.ano_saida AS INT), u.nome_mobilidadade_considerada, u.modalidade_considerada;
''',

    'TempoCancelamento':'''
WITH tabela AS (
    SELECT ABS(CAST(u.ano_ingresso AS INT) - CAST(u.ano_saida AS INT)) AS anos, u.nome_mobilidadade_considerada, u.modalidade_considerada, count(*) FROM ufc AS u
        WHERE u.nome_mobilidadade_considerada !='xx' AND
              u.status = 'Cancelado' AND
              u.ano_saida !='xx'
        GROUP BY anos, u.nome_mobilidadade_considerada, u.modalidade_considerada
) SELECT CASE 
    WHEN anos = 0 THEN 'No mesmo ano'  
    WHEN anos = 1 THEN 'Primeiro ano'
    WHEN anos = 2 THEN 'Segundo ano'
    WHEN anos = 3 THEN 'Terceiro ano'
    WHEN anos = 4 THEN 'Quarto ano'
    WHEN anos = 5 THEN 'Quinto ano'
    ELSE 'Sexto ano'
END ano_de_cancelamento, nome_mobilidadade_considerada, modalidade_considerada, count
FROM tabela;
'''
}

with open('json/queries.json', 'w') as f:
    json.dump(dicionario, f)