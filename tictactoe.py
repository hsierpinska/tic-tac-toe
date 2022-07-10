from tkinter import *

class tictactoe:




    def __init__(self, window, photos):
        '''Klasa reprezentująca grę w kółko i krzyżyk'''
        #deklarowanie zmiennych
        self.__photos = photos
        self.__window = window
        self.reset()

    def reset(self):

        self.remove_widgets()
        self.__buttons = []
        self.__buttons2 = []
        self.__button = None
        self.__round = 0
        self.__won = None
        self.__index = 0
        self.__board = [i for i in range(0,9)]
        self.__winners=[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        self.startAppear()

#funkcja generująca ekran startowy
    def startAppear(self):
        start = Button(self.__window, image = self.__photos[0], font="-weight bold", borderwidth=1, command=lambda: self.startPressed())
        title = Label(self.__window, image = self.__photos[1])
        space1 = Label(self.__window, bg = 'white', padx=25, pady=10)
        space2 = Label(self.__window, bg = 'white', padx=25, pady=40)
        space1.pack()
        title.pack()
        space2.pack()
        start.pack()

#funkcja usuwająca widgety
    def remove_widgets(self):
        for widget in self.__window.winfo_children():
            widget.grid_forget()
            widget.pack_forget()
            widget.place_forget()


    #generuje planszę
    def startPressed(self):

        self.remove_widgets()
        self.__round = 0
        # pętla tworząca przyciski

        for x in range(3):

            for y in range(3):
                l1 = Button(self.__window, text=" ", font="-weight bold", padx=70, pady=70, borderwidth=1, bg="pink", command=lambda x=x, y=y: self.pressButton(x, y))

                l1.grid(column=x, row=y, sticky = N + S + E + W)
                list=[x, y]
                self.__buttons.append(list)
                self.__buttons2.append(l1)



        self.__button = Label(self.__window, image = self.__photos[4])

        textround=str(self.__round)
        roundtext = Button(self.__window, text=textround, font="-weight bold", padx=68, pady=40, borderwidth=1, bg="#99d1dd", state=DISABLED)

        round2 = Label(self.__window, image = self.__photos[5])

        self.__button.grid(column=0, row=4)
        roundtext.grid(column=1, row=4)
        round2.grid(column=2, row=4)

        self.__buttons2.append(roundtext)
        self.__buttons2.append(round2)


    def pressButton(self, x, y):


        #wyłącza przycisk po naciśnięciu
        #stawia grafike kolka

        list1=[x, y]


        for i in range(len(self.__buttons)):

            if self.__buttons[i] == list1:
                self.__index=i
                break

        self.__buttons2[self.__index].config(state=DISABLED, bg='white')
        self.__round+=1
        textround=str(self.__round)
        self.__buttons2[9].config(text=textround)
        self.checkIfWon()



#sprawdza kto wygrał
#wpisuje x  lub  o na listę, w momencie gdy pętla znajduje x na liście, to zwraca do listy pozycję czyli jego i do innej listy ktora jest potem czytana i porównywana czy zawiera
# się w liście self.__winners
    def checkIfWon(self):
        if self.__round % 2 == 0:
            self.__buttons2[self.__index].config(image = self.__photos[7])
            self.__board[self.__index] = 'X'
        else:
            self.__buttons2[self.__index].config(image = self.__photos[6])
            self.__board[self.__index] = 'O'
        indexlist_1=[]
        indexlist_2=[]
        for i in range(len(self.__board)):
            if self.__board[i] == 'X':
                indexlist_1.append(i)
            elif self.__board[i] == 'O':
                indexlist_2.append(i)

        for i in range(len(self.__winners)):
            a = set(self.__winners[i]).issubset(indexlist_1)
            if a == True and len(indexlist_1)>=3:
                self.__won = 'O'

        for i in range(len(self.__winners)):
            a = set(self.__winners[i]).issubset(indexlist_2)
            if a == True and len(indexlist_2)>=3:
                self.__won = 'X'

        if self.__won != None:

            self.__buttons2[9].config(text=self.__won + ' won the game')
            self.__buttons2[9].grid(columnspan = 2)
            self.__buttons2[10].grid_forget()
            self.__button.grid_forget()
            nextbutton = Button(self.__window, text='Next', font="-weight bold", padx=60, pady=40, borderwidth=1, bg="#99d1dd", command = lambda: self.displayEnd())
            nextbutton.grid(column=0, row=4)
            for i in range(0,9):
                self.__buttons2[i].config(state=DISABLED)


        if self.__round == 9 and self.__won == None:

            self.__button.grid_forget()
            nextbutton = Button(self.__window, text='Next', font="-weight bold", padx=60, pady=40, borderwidth=1, bg="#99d1dd", command = lambda: self.displayEnd())
            nextbutton.grid(column=0, row=4)

            self.__buttons2[9].config(text = 'Remis')
            self.__buttons2[9].grid(columnspan = 2)
            self.__buttons2[10].grid_forget()




#ekran końcowy z możliwością restartu/wyjścia
    def displayEnd(self):

        self.remove_widgets()
        space1 = Label(self.__window, bg = 'white', padx=25, pady=40)
        space2 = Label(self.__window, bg = 'white', padx=25, pady=40)
        restart = Button(self.__window, image = self.__photos[2], font="-weight bold", borderwidth=1, command=lambda: self.reset())
        quit = Button(self.__window, image = self.__photos[3], font="-weight bold", borderwidth=1, command=lambda: self.__window.destroy())
        space1.pack()
        restart.pack()
        space2.pack()
        quit.pack()






