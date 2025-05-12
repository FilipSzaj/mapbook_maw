from cProfile import label
from tkinter import *

import tkintermapview

users:list = [{"name": "Filip", "surname": "xxx", "location": "Ciechanów", "post": 100}]

def add_user():
    imie = entry_name.get()
    nazwisko = entry_surname.get()
    posty = entry_post.get()
    miejscowosc = entry_location.get()
    users.append(
        {
            "name": imie,
            "surname": nazwisko,
            "location": miejscowosc,
            "post": posty
        })
    print(users)
    entry_name.delete(0, END)
    entry_surname.delete(0, END)
    entry_post.delete(0, END)
    entry_location.delete(0, END)
    entry_name.focus()
    show_users()

def show_users():
    listbox_lista_obiektow.delete(0, END)
    for idx, user in enumerate(users):
        listbox_lista_obiektow.insert(idx, f"{idx+1}. {user['name']} {user['surname']} {user['location']} {user['post']}")

def delete_user():
    idx=listbox_lista_obiektow.index(ACTIVE)
    users.pop(idx)
    show_users()

def user_details():
    idx=listbox_lista_obiektow.index(ACTIVE)
    label_name_szczegoly_obiektu_wartosc.configure(text=users[idx]["name"])
    label_surname_szczegoly_obiektu_wartosc.configure(text=users[idx]["surname"])
    label_posts_szczegoly_obiektu_wartosc.configure(text=users[idx]["post"])
    label_location_szczegoly_obiektu_wartosc.configure(text=users[idx]["location"])

def edit_user():
    idx=listbox_lista_obiektow.index(ACTIVE)
    entry_name.insert(0, users[idx]["name"])
    entry_surname.insert(0, users[idx]["surname"])
    entry_post.insert(0, users[idx]["post"])
    entry_location.insert(0, users[idx]["location"])

    buttton_dodaj_obiekt.configure(text="Zapisz", command=lambda:update_users(idx))

def update_users(idx):
    name=entry_name.get()
    surname=entry_surname.get()
    location=entry_location.get()
    post=entry_post.get()
    users[idx]["name"]=name
    users[idx]["surname"]=surname
    users[idx]["location"]=location
    users[idx]["post"]=post

    buttton_dodaj_obiekt.configure(text="Dodaj", command=add_user)
    entry_name.delete(0, END)
    entry_surname.delete(0, END)
    entry_post.delete(0, END)
    entry_location.delete(0, END)
    entry_name.focus()
    show_users()









root = Tk()
root.title("mapbook_FS")
root.geometry("1024x768")

#RAMKI
ramka_lista_obiektow= Frame(root)
ramka_formularz= Frame(root)
ramka_szczegol_obiektow= Frame(root)
ramka_mapa= Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegol_obiektow.grid(row=1, column=0)
ramka_mapa.grid(row=2, column=0, columnspan=2)

#RAMKA LISTA OBIEKTÓW
label_lista_obiektow= Label(ramka_lista_obiektow, text="Lista obiektów:")
label_lista_obiektow.grid(row=0, column=0, columnspan=3)
listbox_lista_obiektow= Listbox(ramka_lista_obiektow)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly= Button(ramka_lista_obiektow, text="Pokaż Szczegóły", command=user_details)
button_pokaz_szczegoly.grid(row=2, column=0)
button_edytuj_obiekt= Button(ramka_lista_obiektow, text="Edytuj obiekt", command=edit_user)
button_edytuj_obiekt.grid(row=2, column=1)
button_usun_obiekt= Button(ramka_lista_obiektow, text="Usuń obiekt", command=delete_user)
button_usun_obiekt.grid(row=2, column=2)
button_usun_obiekt.grid(row=2, column=2)

#RAMKA FORMULARZ
label_formularz= Label(ramka_formularz, text="Formularz: ")
label_formularz.grid(row=0, column=0, columnspan=2,)
label_name= Label(ramka_formularz, text="Imię: ")
label_name.grid(row=1, column=0, sticky=W)
label_surname= Label(ramka_formularz, text="Nazwisko: ")
label_surname.grid(row=2, column=0, sticky=W)
label_post= Label(ramka_formularz, text="Liczba postów: ")
label_post.grid(row=3, column=0, sticky=W)
label_location= Label(ramka_formularz, text="Miejscowość: ")
label_location.grid(row=4, column=0, sticky=W)

entry_name= Entry(ramka_formularz)
entry_name.grid(row=1, column=1,)
entry_surname= Entry(ramka_formularz)
entry_surname.grid(row=2, column=1,)
entry_post= Entry(ramka_formularz)
entry_post.grid(row=3, column=1,)
entry_location= Entry(ramka_formularz)
entry_location.grid(row=4, column=1,)

buttton_dodaj_obiekt= Button(ramka_formularz, text="Dodaj", command=add_user)
buttton_dodaj_obiekt.grid(row=5, column=1, columnspan=2)

#RAMKA SZCZEGÓŁY OBIEKTÓW
label_szczegoly_obiektu= Label(ramka_szczegol_obiektow, text="Szczegóły użytkownika: ")
label_szczegoly_obiektu.grid(row=0, column=0,sticky=W)

label_name_szczegoly_obiektu= Label(ramka_szczegol_obiektow, text="Imię: ")
label_name_szczegoly_obiektu.grid(row=1, column=0,)

label_name_szczegoly_obiektu_wartosc= Label(ramka_szczegol_obiektow, text="....")
label_name_szczegoly_obiektu_wartosc.grid(row=1, column=1,)

label_surname_szczegoly_obiektu= Label(ramka_szczegol_obiektow, text="Nazwisko: ")
label_surname_szczegoly_obiektu.grid(row=1, column=2,)

label_surname_szczegoly_obiektu_wartosc= Label(ramka_szczegol_obiektow, text="....")
label_surname_szczegoly_obiektu_wartosc.grid(row=1, column=3,)

label_posts_szczegoly_obiektu= Label(ramka_szczegol_obiektow, text="Postów: ")
label_posts_szczegoly_obiektu.grid(row=1, column=4,)

label_posts_szczegoly_obiektu_wartosc= Label(ramka_szczegol_obiektow, text="....")
label_posts_szczegoly_obiektu_wartosc.grid(row=1, column=5,)

label_location_szczegoly_obiektu= Label(ramka_szczegol_obiektow, text="Miejscowość: ")
label_location_szczegoly_obiektu.grid(row=1, column=6,)

label_location_szczegoly_obiektu_wartosc= Label(ramka_szczegol_obiektow, text="....")
label_location_szczegoly_obiektu_wartosc.grid(row=1, column=7,)

#RAMKA MAPA
map_widget= tkintermapview.TkinterMapView(ramka_mapa, width=1024, height=400)
map_widget.set_position(52.23, 21)
map_widget.set_zoom(5)
map_widget.grid(row=0, column=0, columnspan=8)




root.mainloop()