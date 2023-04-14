import string
import random
import pyperclip
import tkinter as tk

def generate_password(length, special_chars=False, uppercase=False):
    chars = string.digits
    if special_chars:
        chars += string.punctuation
    if uppercase:
        chars += string.ascii_uppercase

    password = ''.join(random.choice(chars) for _ in range(length))

    return password

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        status_label.config(text="Contraseña copiada al portapapeles")
    else:
        status_label.config(text="No se puede copiar una contraseña vacía")

def generate():
    length = length_entry.get()
    if length.isdigit():
        special_chars = special_chars_var.get()
        uppercase = uppercase_var.get()
        password = generate_password(int(length), special_chars, uppercase)
        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly")
        status_label.config(text="")
    else:
        status_label.config(text="La longitud debe ser un número")

window = tk.Tk()
window.title("Generador de Contraseñas")

length_label = tk.Label(text="Longitud de la contraseña (sólo números):")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

special_chars_var = tk.BooleanVar()
special_chars_var.set(False)
special_chars_checkbutton = tk.Checkbutton(window, text="¿Incluir caracteres especiales?", variable=special_chars_var)
special_chars_checkbutton.pack()

uppercase_var = tk.BooleanVar()
uppercase_var.set(False)
uppercase_checkbutton = tk.Checkbutton(window, text="¿Incluir letras mayúsculas?", variable=uppercase_var)
uppercase_checkbutton.pack()

generate_button = tk.Button(window, text="Generar contraseña", command=generate)
generate_button.pack()

password_label = tk.Label(text="Contraseña generada:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()
password_entry.config(state="readonly")

copy_button = tk.Button(window, text="Copiar al portapapeles", command=copy_to_clipboard)
copy_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()
