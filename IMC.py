peso=float(input('Digite seu peso! '))
altura=float(input('Digite sua altura! '))
imc = peso / (altura ** 2)
print (' O IMC  dessa pessoa e: {:.1f}'.format(imc))
if imc < 18.5:
    print('ANOREXIA')
elif 18.5 <= imc < 25:
    print('NORMAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
elif imc >= 40:
    print('MORBIDO')
