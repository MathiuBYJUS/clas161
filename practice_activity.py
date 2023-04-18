from tkinter import*
from PIL import ImageTk ,Image
from tkinter import filedialog
import os

root=Tk()
root.geometry("500x500")

imagen1=ImageTk.PhotoImage(Image.open("abrir.png"))
imagen2=ImageTk.PhotoImage(Image.open("guardar.png"))
imagen3=ImageTk.PhotoImage(Image.open("salir.jpg"))

name=""

def thanos():
    root.destroy()

def openFile():
    global name
    texto.delete(1.0, END)
    input1.delete(0, END)
    text_file = filedialog.askopenfilename(title="Abrir el archivo de texto", filetypes=(("Archivos de texto", "*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    input1.insert(END,formated_name)
    root.title(formated_name)
    text_file = open(name,'r')
    paragraph=text_file.read()
    texto.insert(END,paragraph)
    text_file.close()
    
def save():
    a=input1.get()
    b=open(a+".txt","w")
    c=texto.get("1.0",END)
    print(c)
    b.write(c)
    texto.delete(0,END)
    name.delete(1.0,END)
    messagebox.showinfo("Ya se guardo","Exito")
    

    
    










input1=Entry(root)
input1.place(relx=0.7 , rely=0.1, anchor=CENTER)
boton1=Button(root,image=imagen1,command=openFile)
boton1.place(relx=0.05,rely=0.1,anchor=CENTER)
boton2=Button(root,image=imagen2,command=save)
boton2.place(relx=0.15,rely=0.1,anchor=CENTER)
boton3=Button(root,image=imagen3,command=thanos)
boton3.place(relx=0.25,rely=0.1,anchor=CENTER)
label1=Label(root,text="Titulo del Archivo")
label1.place(relx=0.48,rely=0.1,anchor=CENTER)
texto=Text(root,width=50,height=20)
texto.place(relx=0.5,rely=0.5,anchor=CENTER)



root.mainloop()