Crie uma função que substitui as vogais de uma palavra por símbolos especiais. Os símbolos que substituem as vogais são:

vogais: a e i o u

símbolos: @ & ! # *

Para testar se a função está correta, faça os seguintes testes:

```
print(trocar_vogais('luar')) 
# imprime l*@r

print(trocar_vogais('bocejo')) 
# imprime b#c&j#

print(trocar_vogais('tranquilo')) 
# imprime tr@nq*!l#
```

A função não precisa considerar vogais maiúsculas (A, E, I, O, U) ou com acentos (á, é, à, ó, ô, etc). Caso alguma palavra seja usada vogais maiúsculas ou acentos, elas podem ser ignoradas. Exemplo:

```
print(trocar_vogais('tédio')) 
# imprime téd!#

print(trocar_vogais('Amanhã')) 
# imprime Am@nhã
```

Crie um arquivo chamado `resolucao.py` que contenha a função que você implementou.
