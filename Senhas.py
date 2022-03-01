import string
import random

def geradordesenhas(tamanho):
    pontos = string.punctuation
    letras = string.ascii_letters
    caracteres = pontos + letras
    senha = ''.join(random.sample(caracteres, tamanho))
    return senha

password = geradordesenhas(15)
print(password)