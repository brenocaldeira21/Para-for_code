## análise_lab

## descrição do programa 
o programa processa os dados do inventário de um laboratório contendo 30 frascos de reagentes qumicos com nome do composto, "modelo" e pureza o programa executa em etapas
o 'set()' identifica os tipos únicos de reagentes. eliminando as duplicatas
o 'zip()' + 'list()' combina as três listas em uma tupla 
o 'for' com unpacking gera relatório formado por todos os 30 frascos
list comprehension com if filtra apenas os lotes que tem pureza =>98.0

## respostas do README

### 1. Levando em consideração a estrutura do nosso inventário, por que seria incorreto usar a função dict() para transformar o resultado do nosso zip() em um dicionário, utilizando o nome do reagente como "Chave" e o lote como "Valor"?
Dicionários não permitem chaves duplicadas, 
No inventário, existem múltiplos frascos do mesmo reagente — por exemplo, `'Etanol'` aparece 8 vezes, cada um com um lote diferente. 
Se usássemos `dict(zip(reagentes, lotes))`, cada nova ocorrência de `'Etanol'` sobrescreveria a anterior.
terminaríamos com apenas 7 entradas no dicionário (uma por tipo de composto), perdendo os dados de 23 frascos.

### 2. O que a função zip() gera na memória do Python antes de usarmos a função list() para forçar a visualização dos dados?
O zip não gera nenhuma lista na memória, pelo que entendi ele apenas combina as duas listas elemento a elemento.
Cada tupla só é gerada no momento em que é solicitada A função `list()` é o que força o `zip` a trabalhar de uma vez.
Materializando todas as tuplas na memória como uma lista concreta.

### 3. Observando o seu código final, de que forma o List Comprehension substitui a necessidade de criar uma lista vazia e usar a estrutura de repetição for tradicional acompanhada do método .append()?
Com o list comprehension fica apenas uma linha 
Acredito que com append ficaria 
lotes_aprovados = []
for reagente, lote, pureza in inventario:
    if pureza >= 98.0:
        lotes_aprovados.append(lote)
A execuçaõ fica mais rápida que usar for + append 
