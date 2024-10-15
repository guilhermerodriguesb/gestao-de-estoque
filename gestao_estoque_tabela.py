import tkinter as tk
from tkinter import ttk, messagebox

# Dicionário para armazenar produtos
estoque = {}

# Função para cadastrar produto
def cadastrar_produto():
    nome = entry_nome.get()
    quantidade = entry_quantidade.get()
    preco = entry_preco.get()
    localizacao = entry_localizacao.get()

    if nome and quantidade.isdigit() and preco.replace('.', '', 1).isdigit() and localizacao:
        estoque[nome] = {
            'quantidade': int(quantidade),
            'preco': float(preco),
            'localizacao': localizacao
        }
        atualizar_tabela()
        limpar_campos()
        messagebox.showinfo("Sucesso", f"Produto '{nome}' cadastrado!")
    else:
        messagebox.showwarning("Erro", "Preencha os campos corretamente!")

# Função para procurar produto
def procurar_produto():
    nome = entry_nome.get()
    if nome in estoque:
        produto = estoque[nome]
        mensagem = (
            f"Nome: {nome}\n"
            f"Quantidade: {produto['quantidade']}\n"
            f"Preço: R$ {produto['preco']}\n"
            f"Localização: {produto['localizacao']}"
        )
        messagebox.showinfo("Produto Encontrado", mensagem)
    else:
        messagebox.showwarning("Erro", "Produto não encontrado.")

# Função para excluir produto
def excluir_produto():
    nome = entry_nome.get()
    if nome in estoque:
        del estoque[nome]
        atualizar_tabela()
        messagebox.showinfo("Sucesso", f"Produto '{nome}' excluído!")
        limpar_campos()
    else:
        messagebox.showwarning("Erro", "Produto não encontrado.")

# Função para atualizar a tabela com os produtos
def atualizar_tabela():
    # Limpa a tabela antes de inserir os novos dados
    for item in tabela.get_children():
        tabela.delete(item)

    # Preenche a tabela com os produtos do dicionário
    for nome, dados in estoque.items():
        tabela.insert("", tk.END, values=(nome, dados['quantidade'], dados['preco'], dados['localizacao']))

# Função para limpar os campos de entrada
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_localizacao.delete(0, tk.END)

# Criação da janela principal
root = tk.Tk()
root.title("Gestão de Estoque")
root.geometry("600x400")

# Widgets de entrada
frame_campos = tk.Frame(root)
frame_campos.pack(pady=10)

tk.Label(frame_campos, text="Nome").grid(row=0, column=0)
entry_nome = tk.Entry(frame_campos)
entry_nome.grid(row=0, column=1)

tk.Label(frame_campos, text="Quantidade").grid(row=1, column=0)
entry_quantidade = tk.Entry(frame_campos)
entry_quantidade.grid(row=1, column=1)

tk.Label(frame_campos, text="Preço (R$)").grid(row=2, column=0)
entry_preco = tk.Entry(frame_campos)
entry_preco.grid(row=2, column=1)

tk.Label(frame_campos, text="Localização").grid(row=3, column=0)
entry_localizacao = tk.Entry(frame_campos)
entry_localizacao.grid(row=3, column=1)

# Botões de ações
frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=10)

btn_cadastrar = tk.Button(frame_botoes, text="Cadastrar Produto", command=cadastrar_produto)
btn_cadastrar.grid(row=0, column=0, padx=5)

btn_procurar = tk.Button(frame_botoes, text="Procurar Produto", command=procurar_produto)
btn_procurar.grid(row=0, column=1, padx=5)

btn_excluir = tk.Button(frame_botoes, text="Excluir Produto", command=excluir_produto)
btn_excluir.grid(row=0, column=2, padx=5)

# Tabela para exibir os produtos
frame_tabela = tk.Frame(root)
frame_tabela.pack(pady=10)

colunas = ("Nome", "Quantidade", "Preço (R$)", "Localização")
tabela = ttk.Treeview(frame_tabela, columns=colunas, show="headings")

# Configuração das colunas
for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna, width=100)

tabela.pack()

# Inicia o loop principal da interface
root.mainloop()
