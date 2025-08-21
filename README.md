# Teste de Proficiência: Python e SQL

Este repositório contém as soluções para um teste de proficiência focado em análise de dados com Python e extração de dados com SQL. O projeto aborda desde a leitura e visualização de dados locais com Pandas e Matplotlib/Seaborn até a consulta a um banco de dados na nuvem (Google BigQuery) através da biblioteca `basedosdados`.

## Estrutura do Repositório

O projeto está dividido em três partes, cada uma em sua respectiva pasta:

* **/questao_1**: Contém um Jupyter Notebook com uma análise exploratória sobre os dados de blocos de carnaval do Rio de Janeiro em 2018.
* **/questao_2**: Contém um script Python interativo que permite ao usuário buscar blocos de carnaval por bairro e exportar o resultado para um arquivo CSV.
* **/questao_3**: Contém um script Python para extrair dados públicos da RAIS (Relação Anual de Informações Sociais) diretamente da plataforma Base dos Dados.

## Pré-requisitos

Antes de começar, garanta que você tenha os seguintes softwares instalados:
* Python 3.8 ou superior
* Git

Para a **Questão 3**, é necessário ter:
* O [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) instalado.
* Um projeto no Google Cloud Platform com uma conta de faturamento vinculada e a API do BigQuery ativa.

## Instalação e Configuração

Siga os passos abaixo para configurar o ambiente de desenvolvimento local.

**1. Clonar o Repositório:**
```bash
git clone [https://github.com/Leonardo-Bittencourt/repositorio-teste-proficiencia.git](https://github.com/Leonardo-Bittencourt/repositorio-teste-proficiencia.git)
cd repositorio-teste-proficiencia
