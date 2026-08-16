from typing import List, Dict, Any, Optional
from datetime import date


def filtrar_vendas(vendas: List[Dict[str, Any]], data_inicio: Optional[date], data_fim: Optional[date]) -> List[
    Dict[str, Any]]:
    """Filtra as vendas com base em um intervalo de datas."""
    vendas_filtradas = vendas
    if data_inicio:
        vendas_filtradas = [v for v in vendas_filtradas if v["data"] >= data_inicio]
    if data_fim:
        vendas_filtradas = [v for v in vendas_filtradas if v["data"] <= data_fim]
    return vendas_filtradas


def calcular_resumo(vendas: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Realiza os cálculos principais: total por produto, total geral e mais vendido."""
    total_geral = 0.0
    vendas_por_produto: Dict[str, float] = {}
    quantidade_por_produto: Dict[str, int] = {}

    for venda in vendas:
        valor_total_item = venda["quantidade"] * venda["valor_unitario"]
        produto = venda["produto"]

        total_geral += valor_total_item
        vendas_por_produto[produto] = vendas_por_produto.get(produto, 0.0) + valor_total_item
        quantidade_por_produto[produto] = quantidade_por_produto.get(produto, 0) + venda["quantidade"]

    produto_mais_vendido = max(quantidade_por_produto.items(), key=lambda x: x[1])[
        0] if quantidade_por_produto else None

    return {
        "vendas_por_produto": vendas_por_produto,
        "total_geral": total_geral,
        "produto_mais_vendido": produto_mais_vendido
    }