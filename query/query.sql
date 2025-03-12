SELECT u.status, u.forma_ingresso, count(*) FROM ufc AS u
    WHERE u.status LIKE ANY (ARRAY['%%Cancelado%%', '%%Ativo%%', '%%Mobilidade%%', '%%Trancado%%']) AND
          u.ano_ingresso  BETWEEN 2010 and 2020 AND
          u.forma_ingresso LIKE ANY (ARRAY['%%VESTIBULAR%%', '%%SISU%%'])
    GROUP BY u.status, forma_ingresso;




SELECT MIN(DISTINCT ano_ingresso) FROM ufc
WHERE modalidade_considerada LIKE '%%Cota%%';


SELECT count(DISTINCT nome_curso) FROM ufc
    WHERE ano_ingresso BETWEEN 2010 and 2020;


-- Série historica de desistencias
SELECT uf.ano_saida, uf.status, count(*) FROM ufc AS uf
    WHERE uf.status = 'Cancelado' AND uf.ano_saida !='xx'
GROUP BY uf.ano_saida, uf.status;