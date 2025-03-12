import json


dicionario = {
    'SerieHistoricaDesistencia':'''
SELECT uf.ano_saida, uf.status, count(*) FROM ufc AS uf
    WHERE uf.status = 'Cancelado' AND uf.ano_saida !='xx'
GROUP BY uf.ano_saida, uf.status;
'''
}

with open('json/queries.json', 'w') as f:
    json.dump(dicionario, f)