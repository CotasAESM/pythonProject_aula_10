def calcular_e_imprimir_soma_da_expressao():
    n = -1  # Inicializa n com um valor negativo para entrar no loop while

    while n <= 0:
        n = int(input("Digite um valor positivo para n: "))
        if n <= 0:
            print("Entrada inválida. Por favor, digite um valor positivo.")

    # Calcula e imprime as parcelas da expressão
    soma_expressao = 0
    m = 3  # Inicializa o denominador m com o valor inicial
    expressao_string = ""
    for i in range(2, n + 1):
        parcela = f"{i}/{m}"
        expressao_string += parcela
        soma_expressao += i / m
        m += 2

        if i != n + 1:
            expressao_string += " + "

    # Imprime a representação final da soma
    representacao_soma = f"{expressao_string} = {soma_expressao}"
    print(representacao_soma)

print("Vamos tratar uma função que retorna o valor da expressão: 2/3 + 3/5 + 4/7 + 5/9 +…+n/m.")
calcular_e_imprimir_soma_da_expressao()
