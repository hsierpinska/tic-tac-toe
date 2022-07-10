from tkinter import *

import tictactoe as ttt
photoslist=[]
window = Tk()
window.title("Kółko i krzyżyk")
window.geometry("488x650")
window.configure(background = 'white')

for i in range(0,8):
    a=str(i) + '.png'
    photo = PhotoImage(file = a)
    photoslist.append(photo)



one = ttt.tictactoe(window, photoslist)

window.mainloop()

