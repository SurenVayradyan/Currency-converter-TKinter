from tkinter import *
from tkinter import messagebox # Окно сообщений
from tkinter import ttk
import urllib.request
import json


root = Tk()
root.title('Convector')
root.geometry('300x250+550+300')
root.resizable(False, False)

START_AMOUNT = 100 # Стартовая сумма

def exchange():
    e_usd.delete(0, END)
    e_eur.delete(0, END)
    try:
        e_usd.insert(0, round(float(e_uah.get()) / float (JSON_object[0] ['sale']), 2))
        e_eur.insert(0, round(float(e_uah.get()) / float (JSON_object[1] ['sale']), 2))
        
    except:
        messagebox.showerror('Warning', 'Проверьте веденную сумму')



try:
    html = urllib.request.urlopen('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    data = html.read()
    JSON_object = json.loads(data)
except:
    messagebox.showerror('Error', 'Ошибка получения курсов  курсов валют')
    root.destroy()
    

header_frame = Frame(root)
header_frame.pack(fill = X)
header_frame.grid_columnconfigure(0, weight = 1) # grid_columnconfigure стобцы создания(позиция), weight ширина
header_frame.grid_columnconfigure(1, weight = 1)
header_frame.grid_columnconfigure(2, weight = 1)


h_currency = Label(header_frame, text = 'Валюта', bg = '#ccc', font = 'Arial 12 bold')
h_currency.grid(row = 0, column = 0, sticky = EW)
h_buy = Label(header_frame, text = 'Покупка', bg = '#ccc', font = 'Arial 12 bold')
h_buy.grid(row = 0, column = 1, sticky = EW)
h_sale = Label(header_frame, text = 'Продажа', bg = '#ccc', font = 'Arial 12 bold')
h_sale.grid(row = 0, column = 2, sticky = EW)


#USD
usd_currency = Label(header_frame, text = 'USD', font = 'Arial 10')
usd_currency.grid(row = 1, column = 0, sticky = EW)
usd_buy = Label(header_frame, text = JSON_object[0] ['buy'], font = 'Arial 10')
usd_buy.grid(row = 1, column = 1, sticky = EW)
usd_sale = Label(header_frame, text = JSON_object[0] ['sale'], font = 'Arial 10')
usd_sale.grid(row = 1, column = 2, sticky = EW)


#EUR
eur_currency = Label(header_frame, text = 'EUR', font = 'Arial 10')
eur_currency.grid(row = 2, column = 0, sticky = EW)
eur_buy = Label(header_frame, text = JSON_object[1] ['buy'], font = 'Arial 10')
eur_buy.grid(row = 2, column = 1, sticky = EW)
eur_sale = Label(header_frame, text = JSON_object[1] ['sale'], font = 'Arial 10')
eur_sale.grid(row = 2, column = 2, sticky = EW)


calc_frame = Frame(root, bg = '#fff')
calc_frame.pack(expand = 1, fill = BOTH)
calc_frame.grid_columnconfigure(1, weight = 1)


l_uah = Label(calc_frame, text = 'Гривна', bg = '#fff', font = 'Arial 10')
l_uah.grid(row = 0, column = 0, padx = 10)
e_uah = ttk.Entry(calc_frame, justify = CENTER, font = 'Arial 10')
e_uah.grid(row = 0, column = 1, columnspan = 2, pady =10, padx = 10, sticky = EW)
e_uah.insert(0, START_AMOUNT)

# Кнопка
btn_calc = ttk.Button(calc_frame, text = 'Обмен', command = exchange)
btn_calc.grid(row = 1, column = 1, columnspan = 2, padx = 10, sticky = EW)

#Результат
res_frame = Frame(root)
res_frame.pack(expand = 1, fill = BOTH, pady = 5)
res_frame.grid_columnconfigure(1, weight = 1)


l_usd = Label(res_frame, text = 'USD', font = 'Arial 10 bold')
l_usd.grid(row = 3, column = 0)
e_usd = ttk.Entry(res_frame, justify = CENTER, font = 'Arial 10')
e_usd.grid(row = 3, column = 1, columnspan = 2, padx = 10, sticky = EW)
e_usd.insert(0, round(START_AMOUNT / float (JSON_object[0] ['sale']), 2))



l_eur = Label(res_frame, text = 'EUR', font = 'Arial 10 bold')
l_eur.grid(row = 4, column = 0)
e_eur = ttk.Entry(res_frame, justify = CENTER, font = 'Arial 10')
e_eur.grid(row = 4, column = 1, columnspan = 2, padx = 10, sticky = EW)
e_eur.insert(0, round(START_AMOUNT / float (JSON_object[1] ['sale']), 2))


root.mainloop()