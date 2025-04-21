# Gerador de senha simples 😁

import string
import numpy
import numpy.random


q = input("Sugerir senha forte? ")



def gerar():
    letras = string.ascii_letters
    num = string.digits
    cac = string.punctuation
    alg = (letras+num+cac)

    senha = numpy.random.choice(list(alg),20)
    print("".join(senha))


if q == "sim" or q == "Sim":
    gerar()
else:
    None