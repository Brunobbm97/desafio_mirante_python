import pytest
from datetime import date
from vendas_cli.core import filtrar_vendas, calcular_resumo


@pytest.fixture
def vendas_mock():
    return [
        {"data": date(2025, 1, 10), "produto": "Notebook", "quantidade": 2, "valor_unitario": 3500.00},
        {"data": date(2025, 2, 15), "produto": "Mouse", "quantidade": 5, "valor_unitario": 100.00},
        {"data": date(2025, 3, 20), "produto": "Teclado", "quantidade": 1, "valor_unitario": 250.00},
        {"data": date(2025, 1, 25), "produto": "Notebook", "quantidade": 1, "valor_unitario": 3500.00},
    ]


def test_filtrar_vendas_sem_data(vendas_mock):
    resultado = filtrar_vendas(vendas_mock, data_inicio=None, data_fim=None)
    assert len(resultado) == 4


def test_filtrar_vendas_com_data_inicio(vendas_mock):
    data_inicio = date(2025, 2, 1)
    resultado = filtrar_vendas(vendas_mock, data_inicio=data_inicio, data_fim=None)
    assert len(resultado) == 2


def test_filtrar_vendas_com_intervalo_completo(vendas_mock):
    data_inicio = date(2025, 1, 1)
    data_fim = date(2025, 1, 31)
    resultado = filtrar_vendas(vendas_mock, data_inicio=data_inicio, data_fim=data_fim)
    assert len(resultado) == 2


def test_calcular_resumo(vendas_mock):
    resumo = calcular_resumo(vendas_mock)

    assert resumo["vendas_por_produto"]["Notebook"] == 10500.00
    assert resumo["vendas_por_produto"]["Mouse"] == 500.00

    assert resumo["total_geral"] == 11250.00

    assert resumo["produto_mais_vendido"] == "Mouse"


def test_calcular_resumo_lista_vazia():
    resumo = calcular_resumo([])
    assert resumo["total_geral"] == 0.0
    assert resumo["vendas_por_produto"] == {}
    assert resumo["produto_mais_vendido"] is None