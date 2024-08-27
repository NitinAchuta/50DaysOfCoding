from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
LAGNUAGE_FONT = ('Ariel', 40, 'italic')
WORD_FONT =  ('Ariel', 60, 'bold')

try:
    data = pd.read_csv('data/word_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')

to_learn = data
word_index = -1

# ------------------------ Button Functions ------------------#

def next_card():
    global word_index, flip_timer, to_learn
    window.after_cancel(flip_timer)
    word_index = random.randint(0, len(to_learn) - 1)
    french_word = to_learn.French[word_index]
    canvas.itemconfig(card_word, text=french_word, fill = 'black')
    canvas.itemconfig(card_title, text = 'French', fill = 'black')
    canvas.itemconfig(card_background, image = front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill = 'white')
    english_word = to_learn.English[word_index]    
    canvas.itemconfig(card_word, text=english_word, fill = 'white')
    canvas.itemconfig(card_background, image = back_img)

def is_known():
    global to_learn, word_index
    to_learn = to_learn.drop(word_index)
    new_data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv')
    next_card()




# ------------------------------ UI -------------------------- #
window = Tk()
window.title('Flashcard Game')
window.config(padx=50,pady=50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#Canvas config
canvas = Canvas(height = 526, width= 800, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file = 'images/card_front.png')
card_background = canvas.create_image(400, 263, image = front_img)
card_title = canvas.create_text(400, 150, text='', fill='black', font=LAGNUAGE_FONT)
card_word = canvas.create_text(400, 263, text = '', fill='black', font = WORD_FONT)

canvas.grid(row=0, column = 0, columnspan= 2)

#Back image
back_img = PhotoImage(file = 'images/card_back.png')

#Right and wrong buttons
known_img = PhotoImage(file = 'images/right.png')
known_button = Button(image = known_img, highlightthickness=0, command=is_known)
known_button.grid(row=1,column=1)

unknown_img = PhotoImage(file = "images/wrong.png")
unknown_button = Button(image = unknown_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

next_card()

#end loop
window.mainloop()