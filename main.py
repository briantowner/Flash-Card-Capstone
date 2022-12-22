from tkinter import *
import pandas
from random import choice

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT1 = ("Ariel", 40, "italic")
FONT2 = ("Ariel", 60, "bold")
french_word = ""
english_word = ""
try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("./data/french_words.csv")

dict = df.to_dict(orient="records")
current_card = {}


# ---------------------------- NEW WORD ------------------------------- #
def new_word_check():
    dict.remove(current_card)
    new_word_cross()



def new_word_cross():
    global english_word, french_word, flip_timer, current_card
    current_card = choice(dict)
    window.after_cancel(flip_timer)
    french_word = current_card['French']
    english_word = current_card['English']
    canvas.itemconfig(word_txt, text=french_word, fill="black")
    canvas.itemconfig(title_txt, text="French", fill="black")
    canvas.itemconfig(img, image=front)
    flip_timer = window.after(3000, flip)
    print(len(dict))


def flip():
    canvas.itemconfig(img, image=back)
    canvas.itemconfig(title_txt, text="English", fill="white")
    canvas.itemconfig(word_txt, text=english_word, fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(file="./images/card_front.png")
back = PhotoImage(file="./images/card_back.png")
img = canvas.create_image(400, 263, image=front)
title_txt = canvas.create_text(400, 150, text="French", font=FONT1)
word_txt = canvas.create_text(400, 263, font=FONT2)
canvas.grid(row=0, column=0, columnspan=2)

check_image = PhotoImage(file="./images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=new_word_check)
check_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_word_cross)
wrong_button.grid(row=1, column=1)

new_word_cross()

window.mainloop()


# ---------------------------- CREATING NEW WORD BANK ------------------------------- #
new_df = pandas.DataFrame(dict)
new_csv = new_df.to_csv("./data/words_to_learn.csv", index=False)
