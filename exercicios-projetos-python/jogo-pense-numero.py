from random import randint
from time import sleep
computador = randint(0, 5)
print('_*_' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('_*_' * 20)
print('PENSANDO...')
sleep(2)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('EU GANHEI!, pensei no número {}'.format(computador))
