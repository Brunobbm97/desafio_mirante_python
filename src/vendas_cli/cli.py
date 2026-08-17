import argparse
import logging
import sys
from datetime import datetime
from .parser import ler_csv_vendas
from .core import filtrar_vendas, calcular_resumo
from .output import gerar_saida_texto, gerar_saida_json


def configurar_logs():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


def main():
    configurar_logs()

    parser = argparse.ArgumentParser(description="Gerador de Relatório de Vendas Avançado")
    parser.add_argument("arquivo", help="Caminho do arquivo CSV de vendas")
    parser.add_argument("--format", choices=["text", "json"], default="text",
                        help="Formato de saída (text ou json)")
    parser.add_argument("--start", help="Data de início (YYYY-MM-DD)")
    parser.add_argument("--end", help="Data de término (YYYY-MM-DD)")

    args = parser.parse_args()

    try:
        data_inicio = datetime.strptime(args.start, "%Y-%m-%d").date() if args.start else None
        data_fim = datetime.strptime(args.end, "%Y-%m-%d").date() if args.end else None
    except ValueError:
        logging.error("Formato de data inválido. Use YYYY-MM-DD.")
        sys.exit(1)

    try:
        # Pipeline principal (muito fácil de explicar na apresentação!)
        vendas = ler_csv_vendas(args.arquivo)
        vendas = filtrar_vendas(vendas, data_inicio, data_fim)
        resumo = calcular_resumo(vendas)

        if args.format == "json":
            print(gerar_saida_json(resumo))
        else:
            print(gerar_saida_texto(resumo))

    except Exception as e:
        logging.error("Falha na execução da CLI.")
        sys.exit(1)


if __name__ == "__main__":
    main()