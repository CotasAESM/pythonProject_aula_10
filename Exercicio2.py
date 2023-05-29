import random

lancamentos = [random.randint(1, 6) for _ in range(1000000)]

frequencias = {i: lancamentos.count(i) for i in range(1, 7)}

for numero, frequencia in frequencias.items():
    print(f"{numero}: {frequencia}")
