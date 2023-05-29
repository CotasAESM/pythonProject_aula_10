import tkinter as tk

def celsius_para_fahrenheit():
    temp = float(entrada.get())
    fahrenheit = (temp * 9/5) + 32
    label_resultado["text"] = f"{round(fahrenheit, 2)} °F"

def fahrenheit_para_celsius():
    temp = float(entrada.get())
    celsius = (temp - 32) * 5/9
    label_resultado["text"] = f"{round(celsius, 2)} °C"

def criar_menu():
    janela = tk.Tk()
    janela.title("Conversor de Temperatura")

    global entrada
    entrada = tk.Entry(janela)
    entrada.grid(row=0, column=1)

    label_entrada = tk.Label(janela, text="Temperatura:")
    label_entrada.grid(row=0, column=0)

    botao_celsius = tk.Button(janela, text="Celsius para Fahrenheit", command=celsius_para_fahrenheit)
    botao_celsius.grid(row=1, column=0)

    botao_fahrenheit = tk.Button(janela, text="Fahrenheit para Celsius", command=fahrenheit_para_celsius)
    botao_fahrenheit.grid(row=1, column=1)

    global label_resultado
    label_resultado = tk.Label(janela, text="", width=50, font=("Arial", 12))
    label_resultado.grid(row=2, column=0, columnspan=2)

    janela.mainloop()

criar_menu()
