consumos = [10, 15, 13, 7, 8, 20, 16]
# economico > 11
for consumo in consumos:
    if consumo >= 11:
        print(f"{consumo} -> Este veiculo é economico!")
    else:
        print(f"{consumo} -> NÃO é economico!")