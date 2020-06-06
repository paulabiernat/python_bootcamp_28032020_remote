import tkinter

from pogoda import get_location_id, get_location_weather, report


def get_report():
    location_name = a_entry.get()
    location_id = get_location_id(location_name)
    weather = get_location_weather(location_id)
    rep = report(weather, location_name)
    wynik.configure(text=rep)

root = tkinter.Tk()
a_label = tkinter.Label(master=root, text="Miasto")
a_label.pack()
a_entry = tkinter.Entry(master=root)
a_entry.pack()
wynik_labl = tkinter.Label(master=root, text="Dane o pogodzie: ")
wynik = tkinter.Label(master=root, text="")
wynik_labl.pack()
wynik.pack()



submit = tkinter.Button(master=root, text="Znajdz", command=get_report)
submit.pack()

root.mainloop()
