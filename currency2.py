import requests
import json
from tkinter import *
from tkinter import Tk , ttk
from PIL import Image , ImageTk


# Converter function
def Converter():

    # url = "https://currency-converter18.p.rapidapi.com/api/v1/supportedCurrencies"
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    # url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    c1 = Combo1.get()
    c2 = Combo2.get()
    amnt = val_input.get()

    querystring = {"from":c1,"to":c2,"amount":amnt}

    # Making Logo Of Currency:
    if c2 == 'USD':
        sym = '$'      
    elif c2 == 'EUR':
        sym = '€'
    elif c2 == 'JPY':
        sym = '¥'
    elif c2 == 'GBP':
        sym = '£'
    elif c2 == 'AUD':
        sym = 'A$'
    elif c2 == 'CAD':
        sym = 'C$'
    elif c2 == 'CHF':
        sym = '₣'
    elif c2 == 'CNY':
        sym = '元'
    elif c2 == 'INR':
        sym = '₹'
    elif c2 == 'SGD':
        sym = 'S$'
    elif c2 == 'HKD':
        sym = 'HK$'
    elif c2 == 'SEK':
        sym = 'kr'
    elif c2 == 'NOK':
        sym = 'kr'
    elif c2 == 'DKK':
        sym = 'kr'
    elif c2 == 'NZD':
        sym = 'NZ$'
    elif c2 == 'ZAR':
        sym = 'R'
    elif c2 == 'BRL':
        sym = 'R$'
    elif c2 == 'RUB':
        sym = '₽'
    elif c2 == 'KRW':
        sym = '₩'
    elif c2 == 'MXN':
        sym = 'Mex$'
    elif c2 == 'KWD':
        # sym = 'KD'
        sym = 'د.ك'
    else:
        sym = ''
    
    head = {
	"X-RapidAPI-Key": "e021a002e9msh6218c60a48e1248p1628b9jsn5c170bb85457",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request("GET",url, headers=head,params=querystring)
    data = json.loads(response.text)
    converted_amnt = data['result']['convertedAmount']
    formatted = sym + " {:,.2f}" .format(converted_amnt)
    result['text'] = formatted
    print( formatted)
    # print(converted_amnt, formatted)

# GUI

app = Tk()
app.config(bg="#B2FF66")
app.geometry("400x450")
app.title("Currency Converter")
app.resizable(height=False, width=False)

#frames
frame1 = Frame(app, bg="#476628", height=60, width=400)
frame1.grid(row=0,column=0)

frame2 = Frame(app, bg="#476628", height=300, width=400)
frame2.grid(row=1,column=0)

# Icon
# Frame 1
img = Image.open('Currency72.png')
img = img.resize((40,40))
img = ImageTk.PhotoImage(img)
name = Label(frame1 , image=img , compound=LEFT , text = "Currency Converter" , height = 5 ,width = 370, padx = 15 , pady=30 , font= ('Arial 16 bold'), anchor=CENTER , bg = '#66b2ff' , fg = "#202635" )
name.place(x=0,y=0)

# Frame 2

result = Label(frame2 , text = " " , height = 2 ,width = 22 , pady=7 , font= ('Arial 16 bold'), relief="solid" , anchor=CENTER , bg = '#66b2ff' , fg = "#202635" )
result.place(x=50,y=50)

# from

from_ = Label(frame2 , text = "From:" , height = 1 ,width = 15 , pady=0 , padx=0 , font= ('Arial 10 bold'), relief="flat" , anchor=W , bg = '#B2FF66' , fg = "#202635" )
from_.place(x=50,y=150)

# insert Currency Here :-
currency = ["KWD" ,"USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "INR", "SGD", "HKD", "SEK", "NOK", "DKK", "NZD", "ZAR", "BRL", "RUB", "KRW", "MXN" , 
             "BTC"]

# Combo Box 1
Combo1 = ttk.Combobox(frame2,width=14,justify=CENTER,font=("arial 10 bold"))
Combo1['values'] = (currency)
Combo1.place(x=50 , y =175)

# Combo box 2
to_ = Label(frame2 , text = "To:" , height = 1 ,width = 15 , pady=0 , padx=0 , font= ('Arial 10 bold'), relief="flat" , anchor=W , bg = '#B2FF66' , fg = "#202635" )
to_.place(x=215,y=150)

Combo2 = ttk.Combobox(frame2,width=14,justify=CENTER,font=("arial 10 bold"))
Combo2['values'] = (currency)
Combo2.place(x=215 , y =175)


# Value Input 
val_input = Entry(frame2,width=32,textvariable="value", font=("Helvetica 13 bold") , relief=SOLID, justify=CENTER)
val_input.place(x=50 , y = 205 )

# Button 
button = Button(frame2 , text="Converter" , width= 19 , padx= 5 , height=1 , bg='#66b2ff', fg='Black' , font=("Helvetica 13 bold") , relief=SOLID , command=Converter)
button.place(x=90 , y = 235)
app.mainloop()