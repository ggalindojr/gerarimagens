from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

# ISSO É APENAS UM TESTE
# ISSO É APENAS UM TESTE
# ISSO É APENAS UM TESTE

tela = Tk()
tela.title('App de geração de imagens')
tela.configure(bg='black')
# tela.geometry('400x200+0+0')

style = ttk.Style()
style.configure("BW.TLabel", background="SteelBlue", foreground="white", font="Verdana 13", width=7, anchor=W)

width_of_window = 513
height_of_window = 250

screen_width = tela.winfo_screenwidth()
screen_height = tela.winfo_screenheight()

x_coordinate = (screen_width/2) - (width_of_window/2)
# y_coordinate = (screen_height/2) - (height_of_window/2)

tela.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, 200))

tela.resizable(width=False, height=False)

def selectNome():
    tela.filename = filedialog.askopenfilename(initialdir="C:\\Dev\\Python-Dev\\02projeto\\imgsite", 
                                               title="Selecione o arquivo", 
                                               filetypes=(("Arquivos txt", "*.txt"),("Todos os arquivos", "*.*")))
    label4.config(text=tela.filename)
    label4['bg']="blue"
    label4['fg']="yellow"

def selectImg():
    tela.filename = filedialog.askopenfilename(initialdir="C:\\Dev\\Python-Dev\\02projeto\\imgsite", 
                                               title="Selecione o arquivo", 
                                               filetypes=(("Arquivos png", "*.png"),("Arquivos jpg", "*.jpg"),("Arquivos jpeg", "*.jpeg")))
    label5.config(text=tela.filename)
    label5['bg']= "blue"
    label5['fg']= "yellow"

def selectPasta():
    tela.filename = filedialog.askdirectory(initialdir="C:\\Dev", title="Selecione a pasta")
    path = tela.filename
    caminho = path.replace("/","\\")
    os.chdir(caminho)
    label6.config(text=path)
    label6['bg']= "blue"
    label6['fg']= "yellow"

def gerarArquivo():
    with open(label4['text'], "r") as rf:
        data = rf.readlines()
    i = 0
    for nome in data:
        with open(label5['text'], "rb") as rf:
            with open(nome.replace("\n","").replace('/', '-') + ".png", "wb") as wf:
                for line in rf:
                    wf.write(line)
        i += 1
        label7['text']= i
        label7['bg']= "blue"
        label7['fg']= "yellow"

label1 = Label(tela, text="Nome", bg="blue", fg="white", font="Verdana 13 bold", width=7, anchor=W)
label1.grid(row=0, column=0)

btn1 = ttk.Button(tela, text="Selecione", style="BW.TLabel", command=selectNome)
btn1.grid(row=1, column=0, sticky=W+E)

label2 = Label(tela, text="Imagem", bg="blue", fg="white", font="Verdana 13 bold", width=7, anchor=W)
label2.grid(row=2, column=0)

btn2 = ttk.Button(tela, text="Selecione", style="BW.TLabel", command=selectImg)
btn2.grid(row=3, column=0, sticky=W+E)

label3 = Label(tela, text="Pasta", bg="blue", fg="white", font="Verdana 13 bold", width=7, anchor=W)
label3.grid(row=4, column=0)

btn3 = ttk.Button(tela, text="Selecione", style="BW.TLabel", command=selectPasta)
btn3.grid(row=5, column=0, sticky=W+E)

label4 = Label(tela, text="Caminho", bg="grey11", bd=3, relief="sunken", fg="white", font="Verdana 11", width=46, anchor=W)
label4.grid(row=0, column=1)

label5 = Label(tela, text="Caminho", bg="grey11", bd=3, relief="sunken", fg="white", font="Verdana 11", width=46, anchor=W)
label5.grid(row=2, column=1)

label6 = Label(tela, text="Caminho", bg="grey11", bd=3, relief="sunken", fg="white", font="Verdana 11", width=46, anchor=W)
label6.grid(row=4, column=1)

btn4 = Button(tela, text="Gerar", background="SteelBlue", foreground="white", font="Verdana 13", width=7, anchor=CENTER, command=gerarArquivo)
btn4.place(relx=0.5, rely=0.85, anchor=CENTER)

label7 = Label(tela, text="Quantidade", bg="grey11", bd=3, relief="sunken", fg="white", font="Verdana 11 bold", width=15)
label7.place(relx=0.5, rely=0.7, anchor=CENTER)

tela.mainloop()