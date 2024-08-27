from tkinter import *
#initilaize the window
window = Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


#Label
my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)
# my_label['text'] = "New Text"
# my_label.config(text='New Text')
my_label.config(padx=50,pady=50)

#Button
def button_clicked():
    print('I got clicked')
    my_label['text'] = input.get()

button = Button(text = 'Click Me', command=button_clicked)
button.grid(column=1,row=1)

new_button = Button(text = 'New Button')
new_button.grid(column = 2, row = 0)

#Entry
input = Entry(width = 10)
input.grid(column=3,row=2)
#has to always be at the end of the program
window.mainloop()