nota1 = float(input("Aí quebrada, fala essa primeira nota aí: "))

while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Nota invalida truta, fala a de verdade aí carai: "))

nota2 = float(input("Suave parça, agora fala essa segundinha aí: "))

while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Essa segunda nota tá boa não, digita uma outra aí na malandragem: "))

media = (nota1 + nota2) / 2

print("Aí cocozão no short, a média dessas sua nota aí é: ", media)