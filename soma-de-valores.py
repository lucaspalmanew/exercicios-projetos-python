n = 0
cont = 0
soma = 0
while True:
    n = int(input('Digite um valor (999) para parar: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados {cont} números e soma foi {soma}')
