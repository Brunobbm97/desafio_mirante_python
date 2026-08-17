import pytest
from datetime import date
from vendas_cli.parser import ler_csv_vendas


def test_ler_csv_vendas_sucesso(tmp_path):
    arquivo_csv = tmp_path / "vendas_teste.csv"
    arquivo_csv.write_text(
        "data,produto,quantidade,valor_unitario\n2025-01-15,Notebook,2,3500.00\n",
        encoding="utf-8"
    )

    resultado = ler_csv_vendas(str(arquivo_csv))

    assert len(resultado) == 1
    assert resultado[0]["produto"] == "Notebook"
    assert resultado[0]["quantidade"] == 2
    assert resultado[0]["valor_unitario"] == 3500.00
    assert resultado[0]["data"] == date(2025, 1, 15)


def test_ler_csv_vendas_arquivo_nao_encontrado():
    with pytest.raises(FileNotFoundError):
        ler_csv_vendas("caminho_inexistente.csv")