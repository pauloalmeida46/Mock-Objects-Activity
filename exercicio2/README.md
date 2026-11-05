# Exercício 2 — `NumberAscOrder`

## Objetivo

Implementar uma classe que recebe uma `CustomStack` com os números sorteados da
Mega Sena (na ordem em que foram sorteados) e devolve uma `list()` ordenada de
forma ascendente.

## Implementação (`src/number_asc_order.py`)

- `NumberAscOrder.sort(custom_stack)`:
  - Valida que o parâmetro recebido é de fato uma `CustomStack` (`TypeError`
    caso contrário).
  - Desempilha todos os elementos usando apenas os métodos já existentes de
    `CustomStack` (`is_empty()` e `pop()`) — nenhum método novo foi adicionado
    à classe `CustomStack`.
  - Ordena a lista resultante em ordem ascendente e a retorna.

## Testes (`test/number_asc_order_test.py`)

Seguindo a proposta de **Mock Object**, a `CustomStack` é simulada com
`unittest.mock`/`pytest-mock` (`mocker.Mock(spec=CustomStack)`), controlando o
comportamento de `is_empty()` e `pop()` sem depender da implementação real da
pilha:

- **Pilha com 6 números sorteados (aleatórios)**: mock configurado para
  simular 6 elementos antes de esvaziar; verifica que o resultado é a lista
  ordenada dos números originais e que `pop()`/`is_empty()` foram chamados o
  número esperado de vezes.
- **Pilha vazia**: mock configurado para já estar vazio; verifica que o
  resultado é `[]` e que `pop()` nunca é chamado.
- **Parâmetro inválido**: verifica que passar algo que não é `CustomStack`
  lança `TypeError`.

## Resultado

```
Name                                 Stmts   Miss  Cover
------------------------------------------------------------------
exercicio2\src\number_asc_order.py        10      0   100%
```
