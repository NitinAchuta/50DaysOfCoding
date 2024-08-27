from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f'{km}')
    

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height = 100)
window.config(padx=20,pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1,row=0)

Miles_label = Label(text='Miles')
Miles_label.grid(column=2,row=0)

miles_label = Label(text='is equal to')
miles_label.grid(column=0,row=1)

km_label = Label(text='Km')
km_label.grid(column=2,row=1)

km_result_label = Label(text='')
km_result_label.grid(column=1,row=1)


convert_button = Button(text = 'Calculate', command=miles_to_km)
convert_button.grid(column=1,row=2)




window.mainloop()