import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np

BG_COLOR = "#2c3e50"
BTN_COLOR = "#27ae60"
TXT_COLOR = "#ecf0f1"

def perform_analysis():
    raw_input = user_input.get()
    
    if not raw_input:
        messagebox.showwarning("Aviso", "O campo está vazio!")
        return

    try:
        val_list = [float(n.strip()) for n in raw_input.split(',')]
        data_series = pd.Series(val_list)
        
        avg = data_series.mean()
        med = data_series.median()
        std_dev = data_series.std()
        
        res_display = f"Média: {avg:.2f}\nMediana: {med:.2f}\nDesvio Padrão: {std_dev:.2f}"
        result_label.config(text=res_display)
        
    except ValueError:
        messagebox.showerror("Erro de Formato", "Use apenas números e vírgulas!")
    except Exception as err:
        messagebox.showerror("Erro", f"Algo deu errado: {err}")

root = tk.Tk()
root.title("StatsCalc - Analisador de Dados")
root.geometry("420x350")
root.configure(bg=BG_COLOR)

tk.Label(root, text="Insira sua sequência de dados:", 
         fg="white", bg=BG_COLOR, font=("Arial", 11)).pack(pady=(20, 5))

user_input = tk.Entry(root, font=("Consolas", 13), width=35)
user_input.pack(pady=10)

run_btn = tk.Button(root, text="GERAR ESTATÍSTICAS", 
                    command=perform_analysis,
                    bg=BTN_COLOR, fg="white", 
                    font=("Arial", 10, "bold"),
                    padx=10, pady=5)
run_btn.pack(pady=25)

result_label = tk.Label(root, text="", font=("Courier New", 12), 
                        bg=BG_COLOR, fg=TXT_COLOR, justify="left")
result_label.pack(pady=10)

if __name__ == "__main__":
    root.mainloop()
