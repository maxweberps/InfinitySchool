"""
1. Considere a seguinte lista de velocidades obtidas por um radar = [60, 55, 67, 53, 38, 45, 70, 81],
utilize for para percorrer a lista e imprimir apenas as velocidades acima da permitida (velocidade permitida = 50)
"""

radar = [60, 55, 67, 53, 38, 45, 70, 81]
for velocidade in radar:
    if velocidade > 50:
        print(velocidade)
