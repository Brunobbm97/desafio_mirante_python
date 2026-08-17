import pytest
from datetime import date
from vendas_cli.core import filtrar_vendas, calcular_resumo


# Fixture: cria uma massa de dados falsa que será injetada nos testes
@pytest.fixture
def vendas_mock():
    return [
        {"data": date(2025, 1, 10), "produto": "Notebook", "quantidade": 2, "valor_unitario": 3500.00},
        {"data": date(2025, 2, 15), "produto": "Mouse", "quantidade": 5, "valor_unitario": 100.00},
        {"data": date(2025, 3, 20), "produto": "Teclado", "quantidade": 1, "valor_unitario": 250.00},
        {"data": date(2025, 1, 25), "produto": "Notebook", "quantidade": 1, "valor_unitario": 3500.00},
    ]


def test_filtrar_vendas_sem_data(vendas_mock):
    """Garante que se nenhuma data for passada, todas as vendas retornam."""
    resultado = filtrar_vendas(vendas_mock, data_inicio=None, data_fim=None)
    assert len(resultado) == 4


def test_filtrar_vendas_com_data_inicio(vendas_mock):
    """Testa o filtro a partir de uma data de início."""
    data_inicio = date(2025, 2, 1)
    resultado = filtrar_vendas(vendas_mock, data_inicio=data_inicio, data_fim=None)
    assert len(resultado) == 2  # Deve retornar apenas a venda de Fev e Março


def test_filtrar_vendas_com_intervalo_completo(vendas_mock):
    """Testa o filtro respeitando um intervalo (start e end)."""
    data_inicio = date(2025, 1, 1)
    data_fim = date(2025, 1, 31)
    resultado = filtrar_vendas(vendas_mock, data_inicio=data_inicio, data_fim=data_fim)
    assert len(resultado) == 2  # Deve retornar as duas vendas de Janeiro


def test_calcular_resumo(vendas_mock):
    """Testa se os cálculos principais estão corretos[cite: 1]."""
    resumo = calcular_resumo(vendas_mock)

    # 1. Total de vendas por produto[cite: 1]
    assert resumo["vendas_por_produto"]["Notebook"] == 10500.00  # (2 * 3500) + (1 * 3500)
    assert resumo["vendas_por_produto"]["Mouse"] == 500.00  # (5 * 100)

    # 2. Valor total de todas as vendas[cite: 1]
    assert resumo["total_geral"] == 11250.00

    # 3. Produto mais vendido (em quantidade)[cite: 1]
    assert resumo["produto_mais_vendido"] == "Mouse"  # 5 unidades


def test_calcular_resumo_lista_vazia():
    """Garante que a função não quebre caso receba uma lista vazia."""
    resumo = calcular_resumo([])
    assert resumo["total_geral"] == 0.0
    assert resumo["vendas_por_produto"] == {}
    assert resumo["produto_mais_vendido"] is None