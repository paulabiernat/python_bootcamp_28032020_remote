import tkinter
from tkinter import messagebox
def sumuj():
    try:
        val_a = int(a_entry.get())
        val_b = int(b_entry.get())
        val_c = int(c_entry.get())
        mnozenie = (val_a * val_b * val_c) /100
        wynik.configure(text=mnozenie)
    except ValueError:
        messagebox.showerror("Błędne dane!!", "Popraw dane!")
root = tkinter.Tk()
a_label = tkinter.Label(master=root, text="Paliwo")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()
b_label = tkinter.Label(master=root, text="Spalanie")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()
c_label = tkinter.Label(master=root, text="Dystans")
c_label.pack()
c_entry = tkinter.Entry(master=root)
c_entry.pack()
wynik_labl = tkinter.Label(master=root, text="Wynik:")
wynik = tkinter.Label(master=root, text="")
wynik_labl.pack()
wynik.pack()
submit = tkinter.Button(master=root, text="Policz", command=sumuj)
submit.pack()
root.mainloop()
print("Po mainloop")