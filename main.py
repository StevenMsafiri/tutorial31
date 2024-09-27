import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
original_data = pandas.read_csv("./data/french_words.csv")

try:
    data = pandas.read_csv("./data/french_words.csv")
except FileNotFoundError:
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient='records')

def random_french_word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    if len(to_learn) < 1:
        main_card.itemconfig(card_title, text="Over", fill="black")
        main_card.itemconfig(card_word, text="You know all words", fill="black")

    else:
        current_card = random.choice(to_learn)
        main_card.itemconfig(card_title, text="French", fill="black")
        main_card.itemconfig(card_word, text=current_card["French"], fill="black")
        main_card.itemconfig(card_background, image=card_front)
        flip_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    random_french_word()

def flip_card():
    main_card.itemconfig(card_title, text="English", fill= "white")
    main_card.itemconfig(card_word, text= current_card["English"], fill="white")
    main_card.itemconfig(card_background, image=card_back)


window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_word = PhotoImage(file="./images/right.png")
wrong_word = PhotoImage(file="./images/wrong.png")

main_card = Canvas(width=800, height=526)
card_background = main_card.create_image(400, 263, image=card_front)
main_card.config(highlightthickness=0, bg = BACKGROUND_COLOR)
main_card.grid(column=0, row=0, columnspan =2)

card_title = main_card.create_text(400, 150, text="Title", fill="Black", font=("Ariel", 40, "italic"))

card_word = main_card.create_text(400, 263, text="word", fill="Black", font=("Ariel", 60, "bold"))

correct_button = Button(image=right_word, highlightthickness=0, bg = BACKGROUND_COLOR, command=is_known)
correct_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_word, highlightthickness=0, bg = BACKGROUND_COLOR, command=random_french_word)
wrong_button.grid(column=0, row=1)

random_french_word()
window.mainloop()