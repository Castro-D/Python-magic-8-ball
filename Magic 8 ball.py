import random
import tkinter as tk
import sys
responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes – definitely.', 'You may rely on it.',
             'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.',
              'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.',
              'Dont count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=500)
canvas.pack()


def label_change():
    label['text'] = 'Thinking...'
    label.after(2000, ask_question)


def ask_question():
    label['text'] = random.choice(responses)


def clear_txt():
    entry.delete(0, 'end')


def clear_label(widget):
    widget['text'] = ''


def exit_app():
    sys.exit()


background_image = tk.PhotoImage(file='magicball.gif')
background_label= tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='black', bd=4)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, bg='white', font=('Times new roman', 25))
entry.place(relwidth=1, relheight=1)

button1 = tk.Button(root, text='Ask', bg='gray', font=('Times new roman', 25), command=lambda: label_change())
button1.place(relx=0.14, rely=0.2, relwidth= 0.2, relheight=0.19, anchor='n')

button2 = tk.Button(root, text='Clear', bg='gray', font=('Times new roman', 25), command=clear_txt)
button2.place(relx=0.39, rely=0.2, relwidth= 0.2, relheight=0.19, anchor='n')

button3 = tk.Button(root, text='Retry', bg='gray', font=('Times new roman', 25), command=lambda: clear_label(label))
button3.place(relx=0.64, rely=0.2, relwidth= 0.2, relheight=0.19, anchor='n')

button4 = tk.Button(root, text='Quit', bg='gray', font=('Times new roman', 25), command=exit_app)
button4.place(relx=0.89, rely=0.2, relwidth= 0.2, relheight=0.19, anchor='n')

frame2 = tk.Frame(root, bg='black', bd=5)
frame2.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.5, anchor='n')
label = tk.Label(frame2, bg='violet', font=('Times new roman', 25))
label.place(relwidth=1, relheight=1)

root.mainloop()
