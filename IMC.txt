peso=float(input('Digite seu peso! '))
altura=float(input('Digite sua altura! '))
imc = peso / (altura ** 2)
print (' O IMC  dessa pessoa e: {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso')
if imc >= 18.5 and imc <25:
    print('Peso normal')
if imc >= 25 and imc <30:
    print('Sobrepeso')
if imc >= 30 and imc <39.9:
    print('Obesidade')
    if imc > 40:
        print('Morbida')