**Aluno:** Paulo Almeida
**Disciplina:** Qualidade de Teste de Software

# Preparo do Ambiente

> Todos os comandos abaixo devem ser executados a partir desta pasta (onde
> este `README.md` e o `pytest.ini` estão localizados). O `pytest.ini` já
> configura o `pythonpath`, então não é necessário nenhum ajuste adicional de
> `PYTHONPATH` nem instalar o projeto como pacote.

Testado com Python 3.10+.

```sh
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/macOS
pip install -r requirements.txt
```

# Estrutura do Projeto

- `exercicio1/` — Parte 1: testes de unidade da classe `CustomStack` com 100% de cobertura.
- `exercicio2/` — Parte 2: classe `NumberAscOrder`, responsável por ordenar os números de uma `CustomStack`.

Cada pasta contém seu próprio `README.md` detalhando a solução.

# Execução dos Testes

Rodar tudo (os dois exercícios) com relatório de cobertura:

```sh
python -m pytest --cov=exercicio1/src --cov=exercicio2/src --cov-report=term-missing
```

Resultado esperado: 11 testes passando e 100% de cobertura em ambos os
exercícios.

Rodar apenas um exercício:

```sh
python -m pytest exercicio1/test --cov=exercicio1/src --cov-report=term-missing
python -m pytest exercicio2/test --cov=exercicio2/src --cov-report=term-missing
```
