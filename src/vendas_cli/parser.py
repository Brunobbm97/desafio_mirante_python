import csv
import logging
from datetime import datetime
from typing import List, Dict, Any

logger = logging.getLogger(__name__)


def ler_csv_vendas(caminho_arquivo: str) -> List[Dict[str, Any]]:
    """Lê o arquivo CSV de vendas e retorna uma lista de dicionários tipados."""
    vendas = []
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                try:
                    venda = {
                        "data": datetime.strptime(linha["data"], "%Y-%m-%d").date(),
                        "produto": linha["produto"].strip(),
                        "quantidade": int(linha["quantidade"]),
                        "valor_unitario": float(linha["valor_unitario"])
                    }
                    vendas.append(venda)
                except (ValueError, KeyError) as e:
                    logger.warning(f"Erro ao processar linha {linha}: {e}")
        logger.info(f"{len(vendas)} registros lidos com sucesso de {caminho_arquivo}.")
    except FileNotFoundError:
        logger.error(f"Arquivo não encontrado: {caminho_arquivo}")
        raise
    except Exception as e:
        logger.error(f"Erro inesperado ao ler CSV: {e}")
        raise

    return vendas