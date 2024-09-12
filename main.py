import tkinter as tk
from tkinter import ttk

# Cria a janela principal
root = tk.Tk()
root.title("Exercicio")
root.geometry("400x300")
count_ = 0

message = tk.Label(root, text=f"o número de cliques: {count_}", background="yellow")
message.pack(side="left", fill="both")


def button_count():
    global count_
    global message
    count_ += 1
    print(count_)
    message.config(text= f"o número de cliques: {count_}")


botao= ttk.Button(
   root,
   text="Demo Button",
   command=button_count
)
botao.pack()


def button_reset():
    global count_
    global message
    count_ = 0
    message.config(text= f"o número de cliques: {count_}")


botao_reset= ttk.Button(
   root,
   text="Resetar",
   command=button_reset
)
botao_reset.pack()


# Inicia o loop principal
root.mainloop()


