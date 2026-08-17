import json
from typing import Dict, Any


def gerar_saida_texto(resumo: Dict[str, Any]) -> str:
    linhas = []
    linhas.append("=" * 40)
    linhas.append("RELATÓRIO DE VENDAS".center(40))
    linhas.append("=" * 40)

    linhas.append("\nTOTAL DE VENDAS POR PRODUTO:")
    for produto, total in resumo["vendas_por_produto"].items():
        linhas.append(f" - {produto.ljust(20)}: R$ {total:,.2f}")

    linhas.append("-" * 40)
    linhas.append(f"VALOR TOTAL DE VENDAS : R$ {resumo['total_geral']:,.2f}")

    mais_vendido = resumo['produto_mais_vendido'] or 'N/A'
    linhas.append(f"PRODUTO MAIS VENDIDO  : {mais_vendido}")
    linhas.append("=" * 40)

    return "\n".join(linhas)


def gerar_saida_json(resumo: Dict[str, Any]) -> str:
    return json.dumps(resumo, indent=4, ensure_ascii=False)