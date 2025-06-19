import os
import tkinter as tk
from tkinter import messagebox, ttk
import subprocess
import glob
import time

# Função para atualizar a barra de progresso
def atualizar_barra_progresso(valor):
    progress_bar['value'] = valor
    root.update_idletasks()

# Função para extrair AFs
def extrair_afs():
    script_path = r'C:\Users\Visitante\Desktop\teste AF\extrair afs.py'
    atualizar_barra_progresso(0)
    
    # Simulando progresso
    for i in range(0, 101, 10):  # Incrementando de 10 em 10
        atualizar_barra_progresso(i)
        time.sleep(0.1)  # Simula o tempo de execução do script
    subprocess.run(['python', script_path])
    
    atualizar_barra_progresso(100)
    messagebox.showinfo("Info", "Extração de AFs concluída!")

# Função para mesclar AFs
def mesclar_afs():
    script_path = r'C:\Users\Visitante\Desktop\teste AF\mesclar AF com NF.py'
    atualizar_barra_progresso(0)
    
    # Simulando progresso
    for i in range(0, 101, 10):  # Incrementando de 10 em 10
        atualizar_barra_progresso(i)
        time.sleep(0.1)  # Simula o tempo de execução do script
    subprocess.run(['python', script_path])
    
    atualizar_barra_progresso(100)
    messagebox.showinfo("Info", "Mesclagem de AFs concluída!")

# Função para importar os arquivos
def importar_os():
    script_path = r'C:\Users\Visitante\Desktop\teste AF\mesclados\mesclar.py'
    atualizar_barra_progresso(0)
    
    # Simulando progresso
    for i in range(0, 101, 10):  # Incrementando de 10 em 10
        atualizar_barra_progresso(i)
        time.sleep(0.1)  # Simula o tempo de execução do script
    subprocess.run(['python', script_path])
    
    atualizar_barra_progresso(100)
    messagebox.showinfo("Info", "Importação concluída!")

# Função para excluir PDFs e TXTs
def excluir_arquivos():
    folder_path = r'C:\Users\Visitante\Desktop\teste AF'
    exclude_folders = ['Mesclado +', 'informe', 'SEM AF']
    
    atualizar_barra_progresso(0)
    
    # Excluir todos os PDFs e TXTs no diretório, exceto os das pastas excluídas
    total_files = sum(1 for root_dir, _, files in os.walk(folder_path) 
                      for filename in files if filename.endswith(('.pdf', '.txt')) 
                      and not any(exclude in root_dir for exclude in exclude_folders))
    
    if total_files == 0:
        messagebox.showinfo("Info", "Não há arquivos para excluir!")
        return
    
    removed_files = 0
    for root_dir, _, files in os.walk(folder_path):
        if any(exclude in root_dir for exclude in exclude_folders):
            continue
        for filename in files:
            if filename.endswith('.pdf') or filename.endswith('.txt'):
                file_path = os.path.join(root_dir, filename)
                os.remove(file_path)
                removed_files += 1
                atualizar_barra_progresso((removed_files / total_files) * 100)
    
    messagebox.showinfo("Info", "Todos os PDFs e TXTs foram excluídos!")

# Configuração da janela
root = tk.Tk()
root.title("Gerenciador de AFs")
root.geometry("400x300")
root.configure(bg="#2e2e2e")

# Estilo da barra de progresso
style = ttk.Style()
style.theme_use('clam')
style.configure("TProgressbar", background="#4caf50", troughcolor="#bdbdbd", thickness=20)

# Botões
btn_extrair = tk.Button(root, text="Extrair AFs", command=extrair_afs, bg="#3e3e3e", fg="#ffffff")
btn_extrair.pack(pady=10, padx=10, fill='x')

btn_mesclar = tk.Button(root, text="Mesclar AF com NF", command=mesclar_afs, bg="#3e3e3e", fg="#ffffff")
btn_mesclar.pack(pady=10, padx=10, fill='x')

btn_importar = tk.Button(root, text="Mesclar tudo", command=importar_os, bg="#3e3e3e", fg="#ffffff")
btn_importar.pack(pady=10, padx=10, fill='x')

btn_excluir = tk.Button(root, text="Excluir Todos os PDFs", command=excluir_arquivos, bg="#3e3e3e", fg="#ffffff")
btn_excluir.pack(pady=10, padx=10, fill='x')

# Barra de progresso
progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progress_bar.pack(pady=20)

# Iniciar a interface
root.mainloop()
