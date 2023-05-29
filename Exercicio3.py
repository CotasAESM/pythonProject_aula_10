import tkinter as tk

def eh_perfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma == n

def verificar_perfeito():
    n = int(entrada.get())
    if eh_perfeito(n):
        label_resultado["text"] = f"{n} é um número perfeito"
    else:
        label_resultado["text"] = f"{n} não é um número perfeito"

def numeros_perfeitos_ate():
    n = int(entrada.get())
    resultado = ""
    for i in range(1, n+1):
        if eh_perfeito(i):
            resultado += f"{i}; "
    label_resultado["text"] = resultado

def criar_menu():
    janela = tk.Tk()
    janela.title("Números Perfeitos")

    global entrada
    entrada = tk.Entry(janela)
    entrada.grid(row=0, column=1)

    label_entrada = tk.Label(janela, text="Número:")
    label_entrada.grid(row=0, column=0)

    botao_verificar = tk.Button(janela, text="Verificar se é perfeito", command=verificar_perfeito)
    botao_verificar.grid(row=1, column=0)

    botao_mostrar = tk.Button(janela, text="Mostrar perfeitos até", command=numeros_perfeitos_ate)
    botao_mostrar.grid(row=1, column=1)

    global label_resultado
    label_resultado = tk.Label(janela, text="", width=50, font=("Arial", 12))
    label_resultado.grid(row=2, column=0, columnspan=2)

    janela.mainloop()

criar_menu()
