def trocar_vogais(arg):
    troca = {
        "a": "@",
        "e": "&",
        "i":"!",
        "o":"#",
        "u":"*"
    }
    txt = arg
    for x in troca:
        txt = txt.replace(x, troca[x])
    return txt
print(trocar_vogais('aeiou'))
