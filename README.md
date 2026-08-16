# Gerador de Relatório de Vendas

Esta é uma aplicação de Interface de Linha de Comando (CLI) desenvolvida em Python para processar arquivos CSV de vendas e gerar relatórios detalhados[cite: 1]. O projeto foca em código limpo, modularidade e boas práticas de engenharia de software[cite: 1].

## Funcionalidades

- **Leitura de CSV:** Ingestão de dados segura com tratamento de erros linha a linha[cite: 1].
- **Cálculos Consolidados:** Relatórios com o total de vendas por produto, valor total geral e identificação do produto mais vendido[cite: 1].
- **Filtros Temporais:** Capacidade de filtrar os relatórios por um intervalo de datas específico[cite: 1].
- **Múltiplos Formatos:** Suporte para saída em texto plano (tabela) ou em formato JSON[cite: 1].

## Pré-requisitos

- Python 3.8 ou superior.

## Instalação

Recomenda-se a instalação da ferramenta utilizando um ambiente virtual para isolar as dependências.

1. Clone o repositório:
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd vendas-cli
```

2. Crie e ative um ambiente virtual:
- **Linux/macOS:**
```bash
python -m venv venv
source venv/bin/activate
```
- **Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

3. Instale a CLI no ambiente:
```bash
pip install .
```

## Como usar

Após a instalação, o comando `vendas-cli` estará disponível no seu terminal[cite: 1].

**1. Gerar relatório em formato de texto (padrão)[cite: 1]:**
```bash
vendas-cli vendas.csv --format text
```

**2. Gerar relatório em formato JSON[cite: 1]:**
```bash
vendas-cli vendas.csv --format json
```

**3. Filtrar vendas por um intervalo de datas[cite: 1]:**
```bash
vendas-cli vendas.csv --format json --start 2025-01-01 --end 2025-03-31
```

## Executando os Testes

Este projeto possui testes unitários desenvolvidos com `pytest` para garantir a confiabilidade das regras de negócio[cite: 1].

1. Instale as dependências de teste:
```bash
pip install pytest pytest-cov
```

2. Execute a suíte de testes com o relatório de cobertura de código:
```bash
pytest --cov=vendas_cli
```

## Arquitetura do Projeto

A solução foi estruturada de forma modular[cite: 1], garantindo o Princípio de Responsabilidade Única (SOLID):
- `parser.py`: Responsável exclusivamente pela leitura e validação dos dados do CSV[cite: 1].
- `core.py`: Contém as lógicas de negócio, cálculos de agregação e filtros de data[cite: 1].
- `output.py`: Formata e serializa os dados para o terminal ou JSON[cite: 1].
- `cli.py`: Orquestra o fluxo de dados e gerencia os argumentos do usuário via terminal.