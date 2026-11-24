import tkinter as tk  
import random
import string 
window = tk.Tk()
window.title('RandomPassword')
window.geometry ('300x400')
window.configure(bg='#2b2b2b')
password_entry = tk.Entry(window, font=('Arial', 14), justify='center')
password_entry.pack(fill= 'x', padx=10, pady=20,)
length_var = tk.StringVar(value='10')
length_menu = tk.OptionMenu(window, length_var, '6', '8', '10', '12', '16', '20')
use_symbols= tk.BooleanVar()
check_symbols= tk.Checkbutton(window, text= 'СпецСимволы', variable=use_symbols, bg='#2b2b2b', selectcolor='#4CAF50',  fg='white')
check_symbols.pack(pady=5)
length_menu.pack(pady=5)
def generate_password():
    chars = string.ascii_letters + string.digits
    if use_symbols.get():
        chars = chars + string.punctuation
    password = "".join(random.choices(chars, k=int(length_var.get())))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
def clear_password():
    password_entry.delete(0, tk.END)    
btn_clear = tk.Button(window, text='Стереть', command= clear_password)
btn_clear.pack(pady=5 , padx=10)
btn_random = tk.Button(window, text='Сгенереровать', command= generate_password, bg='#4CAF50',fg='white',font=('Arial', 12, 'bold'))
btn_random.pack(pady=5, padx=5)
def copy_password():
    window.clipboard_clear()
    password_entry.get()
    window.clipboard_append(password_entry.get())
btn_copy = tk.Button(window, text='Скопировать', command=copy_password)
btn_copy.pack(pady=5)

window.mainloop()


