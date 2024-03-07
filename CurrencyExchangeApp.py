
import tkinter as tk
from tkinter import ttk

#ttkthemes module downloaded from https://github.com/TkinterEP/ttkthemes , under GNU General Public License v3 (GPLv3) (GPLv3).
from ttkthemes import ThemedTk 

import datetime as dt   
import requests
from functools import partial




#Conversion procedure
def convert(entry, label, dropdown1, dropdown2):
    
    initial_amount = int(entry.get())
    initial_currency = dropdown1.get()
    final_currency = dropdown2.get()
    

    if(initial_currency != '---' and final_currency != '---' and initial_amount >= 0):

        if(initial_currency == final_currency or initial_amount == 0):
            label.config(text = initial_amount)

        else:
            response = requests.get(f"https://api.frankfurter.app/latest?amount={initial_amount}&from={initial_currency}&to={final_currency}")

            label.config(text = f"{response.json()['rates'][final_currency]}")

#Clear procedure
def clear(entry, label, dropdown1, dropdown2):

    entry.delete(0, 'end')
    label.config(text='-----Final Amount-----')
    dropdown1.set('---')
    dropdown2.set('---')


#GUI Widgets
window_main = ThemedTk()
window_main.geometry('700x370')
window_main.title('Currency Exchange App')
font_type = 'Arial'
font_type_size1 = 'Arial', 30
font_type_size2 = 'Arial', 20 

style = ttk.Style(window_main)
style.theme_use("arc")


label_main = ttk.Label(window_main,
                       text = "Currency Exchange",
                       font = font_type_size1)
label_main.pack(pady=30)

frame_main = ttk.Frame(window_main)
frame_main.pack(pady=20)

label_from = ttk.Label(frame_main,
                  text = "From: ",
                  font = font_type_size2)
label_from.grid(row = 0,
            column = 0,
            padx = 20,
            pady = (20,10))

label_to = ttk.Label(frame_main,
                  text = "To: ",
                  font = font_type_size2)
label_to.grid(row = 1,
            column = 0,
            padx = 20,
            pady = (10,20))

entry_amt = ttk.Entry(frame_main,
                      font=font_type_size2)
entry_amt.grid(row = 0,
            column = 1,
            padx = (10,20),
            pady = (20,10))

label_amt = ttk.Label(frame_main,
                      text = '-----Final Amount-----',
                      font = font_type_size2)
label_amt.grid(row = 1,
            column = 1,
            padx = (10,20),
            pady = (10,20))



pressed_to = tk.StringVar()

currency_list = ['AUD', 'BRL', 'GBP', 'BGN', 'CAD', 'CNY', 'CZK', 'DKK', 'EUR', 'HKD', 'HUF', 'ISK', 'INR',
                 'IDR', 'JPY', 'MYR', 'MXN', 'NZD', 'NOK', 'PHP', 'PLN', 'RON', 'SGD', 'ZAR', 'KRW', 'SEK',
                 'CHF', 'THB', 'TRY', 'USD']

drop_to = ttk.OptionMenu(frame_main, pressed_to, '---', *currency_list)
#pressed_from.set("---")
drop_to.grid(row = 1, 
             column = 2, 
             padx = (0,20), 
             pady = (10,20))

pressed_from = tk.StringVar()

drop_from = ttk.OptionMenu(frame_main, pressed_from, '---', *currency_list)
#pressed_to.set("---")
drop_from.grid(row = 0, 
             column = 2, 
             padx = (0,20), 
             pady = (20,10))

buttonCall_cvt = partial(convert, entry_amt, label_amt, pressed_from, pressed_to)

button_cvt = ttk.Button(window_main,
                         text = "CONVERT",
                         command = buttonCall_cvt)

button_cvt.pack(pady=10)


buttonCall_clear = partial(clear, entry_amt, label_amt, pressed_from, pressed_to)

button_clear = ttk.Button(window_main,
                         text = "CLEAR",
                         command = buttonCall_clear)

button_clear.pack(pady=5)


#Appearance Menu
menu1 = tk.Menu(window_main)
window_main.config(menu=menu1)

appear_menu = tk.Menu(menu1)
menu1.add_cascade(label="Appearance",
                  menu=appear_menu)

appear_menu.add_command(label='Light',
                        command= lambda t="arc": change_appearance(t))

appear_menu.add_command(label='Dark',
                        command= lambda t="black": change_appearance(t))



def change_appearance(theme):
    style.theme_use(theme)

    if(theme == "black"):
        window_main.config(bg = "black")
    else:
        window_main.config(bg = "systemWindowBackgroundColor")





window_main.mainloop()



