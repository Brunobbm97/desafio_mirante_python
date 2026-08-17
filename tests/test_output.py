import json
from vendas_cli.output import gerar_saida_texto, gerar_saida_json


def test_gerar_saida_texto():
    resumo_mock = {
        "vendas_por_produto": {"Notebook": 3500.0},
        "total_geral": 3500.0,
        "produto_mais_vendido": "Notebook"
    }
    resultado = gerar_saida_texto(resumo_mock)

    assert "RELATÓRIO DE VENDAS" in resultado
    assert "Notebook" in resultado
    assert "3,500.00" in resultado


def test_gerar_saida_json():
    resumo_mock = {
        "vendas_por_produto": {"Mouse": 100.0},
        "total_geral": 100.0,
        "produto_mais_vendido": "Mouse"
    }
    resultado = gerar_saida_json(resumo_mock)

    dados = json.loads(resultado)
    assert dados["total_geral"] == 100.0
    assert dados["produto_mais_vendido"] == "Mouse"