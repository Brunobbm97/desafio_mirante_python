import pytest
from unittest.mock import patch
from vendas_cli.cli import main


@patch("sys.argv", ["vendas-cli", "vendas.csv", "--format", "json"])
@patch("vendas_cli.cli.ler_csv_vendas")
def test_cli_fluxo_sucesso(mock_ler_csv):
    mock_ler_csv.return_value = []

    try:
        main()
    except SystemExit:
        pytest.fail("A execução falhou e chamou sys.exit, mas deveria ter sucesso.")


@patch("sys.argv", ["vendas-cli", "vendas.csv", "--start", "data-errada"])
def test_cli_formato_data_invalida():
    with pytest.raises(SystemExit) as error:
        main()

    assert error.value.code == 1