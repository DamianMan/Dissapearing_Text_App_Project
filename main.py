from tkinter import *

window = Tk()
window.config(width=900, height=900, bg='#2B3467')
window.title('Disappearing Writing App')


#TITLE
title_label = Label(text='This is another Dangerous Writing App', fg='#EB455F', bg='#2B3467',
                    font=("Times", 35, "bold"))
title_label.place(x=130, y=50)


#SUB-TITLE
sub_title_label = Label(text="Do not stop Writing or everything's gonna be lost!", fg='#BAD7E9', bg='#2B3467',
                    font=("Times", 25, "normal"))
sub_title_label.place(x=160, y=120)

#ENTRY-WRITING

writing_text = Text()
click_label = Label()
#--------------- FUNCTION TO START WRITING -------------------
def start_writing():
    title_label.place(x=-1000, y=0)
    sub_title_label.place(x=-1000, y=0)
    start_button.place(x=-1000, y=0)
    window.config(bg='#FCFFE7')
    click_label.config(text='Click to Start Writing. \n 10 Seconds of No Writing and everything is deleted! ', fg='#FF0303', background='#FCFFE7', font=('Times', 30, 'bold'))
    click_label.place(x=100, y=10)

    writing_text.config(width=80, height=35, bg='#FCFFE7',fg='black', highlightthickness=0, font=('Times', 20, 'normal'))
    writing_text.place(x=30, y=100)

    lenght_session.place(x=-1000, y=0)





#---------FUNCTION TO GET WHEN SOME KEY IS PRESSED ON KEYBOAR--------
text_written = []
time = 1
def typing(event):
    global time, SECONDS_NO_WRITE
    if time == 1:
        time += 1
        timer()





window.bind("<Key>", typing)



#-----------TIMER-----------
MINUTES = 4
SECONDS = 60
SECONDS_NO_WRITE = 0
def timer():
    global SECONDS, MINUTES, time, text_written
    while MINUTES >= 0:
        SECONDS -= 1
        print(f'timer {MINUTES}:{SECONDS}')
        window.update()
        window.after(1000)
        text = writing_text.get("1.0", "end-1c")
        text_written.append(text)
        if text_written.count(text_written[-1]) > 4 and text != '':
            window.config(background='#E96479')
            click_label.config(bg='#E96479')
            writing_text.config(bg='#E96479')
            print(text_written)

            window.update()
            window.config(background='#FCFFE7')
            click_label.config(bg='#FCFFE7')
            writing_text.config(bg='#FCFFE7')
            window.update()
        if text_written.count(text_written[-1]) == 10 and text != '':
            print('Game over')
            text_written = []
            writing_text.delete("1.0", END)




        if SECONDS == 0:
            MINUTES -= 1
            SECONDS = 60
            time = 1




#START BUTTON
lenght_session = Label(text='Lenght session 5 minutes', fg='#FCFFE7', font=('Times', 15, 'normal'), background='#2B3467')
lenght_session.place(x=335, y=220)
start_button = Button(text='Start Writing', width=10, height=1, font=('Times', 20, 'bold'),background='#2B3467', fg='#FF0303', highlightthickness=0,
                      highlightbackground='#2B3467', command=start_writing)
start_button.place(x=350, y=250)


















window.mainloop()