# 🚀 Desafio: ETL Reutilizável

Este repositório contém a solução para o **Desafio de ETL Reutilizável**. O objetivo principal do projeto é construir um pipeline de Extração, Transformação e Carga (ETL) que seja genérico, configurável e extensível, permitindo processar diferentes fontes de dados com o mínimo de alteração no código core.


---

## 📖 Sobre o Projeto

Em ambientes de engenharia de dados, a duplicação de código para criar pipelines semelhantes é um problema comum. Este projeto resolve isso aplicando padrões de projeto (Design Patterns) para criar um **Framework de ETL Reutilizável**. 

O pipeline é capaz de ler dados de múltiplos formatos (ex: CSV, JSON, APIs), aplicar regras de limpeza e validação dinâmicas, e salvar o resultado em diferentes destinos (ex: Bancos de Dados, Data Lakes, Arquivos Parquet).

---

## 🏗️ Arquitetura e Design

O projeto foi desenhado seguindo os princípios do **SOLID** e padrões como **Factory** e **Strategy**:

* **Extractors (Extração):** Interfaces modulares para leitura de dados de diferentes origens.
* **Transformers (Transformação):** Classes responsáveis por manipulação, tipagem e enriquecimento dos dados.
* **Loaders (Carga):** Módulos desacoplados para gravação dos dados transformados no destino final.

---

## 🛠️ Tecnologias Utilizadas

* **[Python](https://www.python.org/):** Linguagem principal do projeto.
* **[Pandas](https://pandas.pydata.org/) / [Polars](https://pola.rs/):** Para manipulação e transformação eficiente de dados.
* **[Pydantic](https://docs.pydantic.dev/):** Para validação de schemas e garantia de qualidade dos dados.
* **[Python-dotenv](https://pypi.org/project/python-dotenv/):** Gerenciamento de variáveis de ambiente.
* **[Pytest](https://docs.pytest.org/):** Framework para testes unitários e de integração.

