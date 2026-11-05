# Exercício 1 — Testes de unidade da `CustomStack`

## Objetivo

Elevar a cobertura de testes da classe `CustomStack` de 79% para 100%, analisando
a efetividade do teste já existente.

## Bug encontrado

Em `push()`, a condição de pilha cheia comparava o **método** `self.size` (sem
chamá-lo) com `self.limit`:

```python
if (self.size == self.limit):   # sempre False: método != int
```

Isso fazia com que `StackFullException` nunca fosse lançada, mesmo com a pilha
cheia — e, por consequência, essa linha nunca podia ser coberta por nenhum
teste, não importa o que fosse testado. A correção foi chamar o método:

```python
if (self.size() == self.limit):
```

## Testes implementados (`test/custom_stack_test.py`)

- `push` em pilha vazia atualiza `size`, `top` e `is_empty`.
- Pilha recém-criada está vazia (`is_empty` e `size`).
- `push` de múltiplos elementos atualiza `size`/`top` corretamente.
- `push` além do limite lança `StackFullException` e não altera o `size`.
- `pop` remove e retorna o último elemento.
- `pop` em pilha vazia lança `StackEmptyException`.
- `top` em pilha vazia lança `StackEmptyException`.
- `top` não remove o elemento do topo.

## Resultado

```
Name                                   Stmts   Miss  Cover
--------------------------------------------------------------------
exercicio1\src\custom_stack_class.py      24      0   100%
```
