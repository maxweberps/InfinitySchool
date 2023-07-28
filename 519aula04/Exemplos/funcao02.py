def calculaIMC(altura: float, peso: float):
    imc = peso / altura ** 2
    print(f'Sei IMC é: {imc:.2f}')


calculaIMC(1.72, 71.4)
