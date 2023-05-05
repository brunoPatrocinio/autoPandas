import tkinter as tk
import pandas as pd
from tkinter import ttk
from tkinter.filedialog import askopenfilename

#obs para ler arq. xls com o urso pandas, instale a dependência do openpyxl

#dataframe declarado
dtFrame = ""

#tuplas dos tipos de arquivos
csvFile = ("csv files", "*.csv"), ("only csv", "*.csv")
xlsFile = ("xls files", "*.xls"), ("Only xls", "*.xls")
pdfFile = ("pdf Files", "*.pdf"), ("Only pdf", "*.pdf")

listaOpcoes = ["csv", "xls", "pdf"]
janela = tk.Tk()

#Funções
def selecaoFile(): #função carrega arquivo
    tipoArqSelecionado = comboBoxSelecao.get()
    if(tipoArqSelecionado == "csv"):
        caminho = askopenfilename(title="Selecione um arquivo...", filetypes=csvFile)
        #print(tipoArqSelecionado)
        dtFrame = pd.read_csv(caminho)
        print(dtFrame)

    elif(tipoArqSelecionado == "xls"):
        caminho = askopenfilename(title="Selecione um arquivo...", filetypes=xlsFile)
        print(tipoArqSelecionado)
        dtFrame = pd.read_excel(caminho)
    elif(tipoArqSelecionado == "pdf"):
        caminho = askopenfilename(title="Selecione um arquivo...", filetypes=pdfFile)
        print(tipoArqSelecionado)
    else:
        print("Nenhum arquivo suportado selecionado")

#END Funções

janela.title("Ferramenta Beta Analise")
labelCabecalho = tk.Label(text="Análise Proto Beta 0.1V", borderwidth=2, relief="solid", font=16) # com borda de 2px e solido
labelCabecalho.grid(row=0, column=0, padx=10, pady=10, sticky="nswe", columnspan=6)

labelText1 = tk.Label(text="Selecione o caminho do arquivo...", font=10)#label Seleção
labelText1.grid(row=1, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

labelText2 = tk.Label(text="Selecione o Tipo de Arquivo:", font=10) #label seleção combobox
labelText2.grid(row=1, column=3, padx=10, pady=10, sticky="nswe", columnspan=2)

comboBoxSelecao = ttk.Combobox(values=listaOpcoes)
comboBoxSelecao.grid(row=1, column=5, padx=10, pady=10, sticky="nswe")

selecaoButton = tk.Button(text="Arquivo...", command=selecaoFile)
selecaoButton.grid(row=2, column=0, padx=2, pady=2)


janela.mainloop()