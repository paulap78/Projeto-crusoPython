# Projeto-crusoPython
Resolução de um dos projetos do curso Python. 

O projeto utiliza lista bi-dimensional com altura e largura não necessariamente iguais contendo apenas 0's e 1's. Cada 1 representa um pedaço de rio, enquanto os 0's representam terra. Rios são compostos por 1's adjacentes horizontalmente ou verticalmente (mas não diagonalmente). O número de 1's adjacentes representa o tamanho do rio.

Os rios podem fazer curvas, isto é, rios podem ter formato de L ou até mesmo de cruz e são considerados um rio só.

O objetivo era criar um algoritmo que receba esta lista bi-dimensional e retorne uma lista com os tamanhos dos rios dentro dessa estrutura. Os tamanhos de rios dentro da lista resposta não precisam ter uma ordem específica.

O projeto utiliza lista bi-dimensional com altura e largura não necessariamente iguais contendo apenas 0's e 1's. Cada 1 representa um pedaço de rio, enquanto os 0's representam terra. Rios são compostos por 1's adjacentes horizontalmente ou verticalmente (mas não diagonalmente). O número de 1's adjacentes representa o tamanho do rio.

Os rios podem fazer curvas, isto é, rios podem ter formato de L ou até mesmo de cruz e são considerados um rio só.

O objetivo era criar um algoritmo que receba esta lista bi-dimensional e retorne uma lista com os tamanhos dos rios dentro dessa estrutura, os tamanhos de rios dentro da lista resposta não precisam ter uma ordem específica.

Exemplo de entrada:

matrix = [
[1, 0, 0, 1, 0],
[1, 0, 1, 0, 0],
[0, 0, 1, 0, 1],
[1, 0, 1, 0, 1],
[1, 0, 1, 1, 0],
]
Saída esperada:

[1, 2, 2, 2, 5] # Note que os números poderiam estar em qualquer ordem dentro da lista
podemos visualizar os rios claramente na seguinte estrutura:

[1, , , 1, ]
[1, , 1, , ]
[ , , 1, , 1]
[1, , 1, , 1]
[1, , 1, 1, ]
