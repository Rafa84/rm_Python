import string
import random

def geradordesenhas(tamanho);
    pontos = string.ponctuation
    letras = string.ascii_letters

    caracteres = pontos+letras

    senhas = ''.join(random.sample(caracteres, tamanho))
    return senha

geradordesenhas(15)
