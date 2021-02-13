# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.


v = float(input('Qual foi sua velocidade?'))
if v > 80 :
    m = (v - 80) * 7
    print('voce foi multado em R$ {:.2f}'.format(m))
else:
    print('voce estava dentro do limite de velocidade')