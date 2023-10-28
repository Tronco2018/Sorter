import tkinter as tk

#font
font = ("Arial", 13, "bold")
button = ("Arial", 13, "bold")
button2 = ("Arial", 13, "bold")
button3 = ("Arial", 13, "bold")
title = ("Arial", 16, "bold")

#Creating window
win = tk.Tk()
win.title("Sorter")
win.geometry("400x300")

#text string
label2 = tk.Label(win, text="Sorter 1.1", font=title)
label2.pack()

#creating user input
user_input = tk.Entry(win)
user_input.pack()

#setting inputbox size
user_input.config(width=50)

label1 = tk.Label(win, text="")
#def' function "sort"
def sort():

    global sorted_list
    testo = user_input.get()
    words_list = testo.split()

    # sort the list of words
    sorted_list = sorted(words_list)

    # Print list
    label1 = tk.Label(win, text=sorted_list, font=font, fg="black")
    label1.pack()
    

#Creating label and button
button = tk.Button(win, text="Sort", font=button, command=sort)
button.pack()
#button size
button.config(height=1, width=5)

# Definisci una funzione per copiare sorted_list negli appunti
def copy_sorted_list():
    text_to_copy = ' '.join(sorted_list)  # Converte la lista ordinata in una stringa
    win.clipboard_clear()  # Pulisce il contenuto degli appunti
    win.clipboard_append(text_to_copy)  # Aggiunge il testo negli appunti
    win.update()  # Aggiorna la finestra principale

# Crea un pulsante per copiare sorted_list negli appunti
copy_button = tk.Button(win, text="copy", font=button2, command=copy_sorted_list)
copy_button.pack()
copy_button.config(height=1, width=5)






#loop
win.mainloop()