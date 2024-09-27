from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)


card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_word = PhotoImage(file="./images/right.png")
wrong_word = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_front)
canvas.config(highlightthickness=0, bg = BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan =2)

canvas.create_text(400, 150, text="Title", fill="Black", font=("Ariel", 40, "italic"))

canvas.create_text(400, 263, text="word", fill="Black", font=("Ariel", 60, "bold"))

correct_button = Button(image=right_word, highlightthickness=0, bg = BACKGROUND_COLOR)
correct_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_word, highlightthickness=0, bg = BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)




window.mainloop()