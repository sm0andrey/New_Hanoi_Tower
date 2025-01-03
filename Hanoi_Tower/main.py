import tkinter
from tkinter import *

import time
from tkinter import simpledialog
from Tools.scripts.pindent import delete_string


from comments import *
from Exceptions import *
from Validation import *
from PIL import ImageTk, Image

class TowerInterface(Button):

    def __init__(self, img1,img2,img3,img4,poles):


        Validator(img1, img2, img3, img4, poles).validate_towerinterface()

        self.img1=img1
        self.img2=img2
        self.img3=img3
        self.img4=img4
        self.poles=poles
        self.movescount=0
        self.leaders=[]
        self.pole_1=[]
        self.pole_2=[]
        self.pole_3=[]
        self.root = Tk()
        self.canvas=None
        self.block_1=None
        self.block_2 = None
        self.block_3 = None
        self.block_4 = None
        self.moves=None
        self.time=0
        self.leader_one = None
        self.leader_two = None
        self.leader_three = None

    def main(self):
        self.root.destroy()
        self.root = Tk()
        self.root.title("tower of hanoi")
        self.root.minsize(width=1280, height=720)
        self.root.attributes("-alpha", 0.9)
        self.root.configure(background="#B4DD1E")

        title = Label(self.root, text='tower of hanoi', fg="black", font="Consolas 30", bg="#B4DD1E")
        title.pack()

        self.leaders.clear()

        self.elem_start_pos()
        self.root.mainloop()

    def put_tower_pieces(self):
        '''запускает саму игру, она создаёт изображения элементов башен (pole и img1, img2, img3, img4), заменяет кнопку start на кнопку restart, запускает счетчики времени и ходов (movescount)'''
        global enter, all_posx, all_posy, pole

        pole = ImageTk.PhotoImage(Image.open(self.poles))
        self.canvas.create_image(-20, -20, anchor=NW, image=pole)

        self.block_1 = ImageTk.PhotoImage(Image.open(self.img1))
        all_posx.append(10)
        all_posy.append(0)
        self.canvas.create_image(all_posy[0], all_posx[0], anchor=NW, image=self.block_1)

        self.block_2 = ImageTk.PhotoImage(Image.open(self.img2))
        all_posx.append(55)
        all_posy.append(0)
        self.canvas.create_image(all_posy[1], all_posx[1], anchor=NW, image=self.block_2)

        self.block_3 = ImageTk.PhotoImage(Image.open(self.img3))
        all_posx.append(100)
        all_posy.append(0)
        self.canvas.create_image(all_posy[2], all_posx[2], anchor=NW, image=self.block_3)

        self.block_4 = ImageTk.PhotoImage(Image.open(self.img4))
        all_posx.append(145)
        all_posy.append(0)
        self.canvas.create_image(all_posy[3], all_posx[3], anchor=NW, image=self.block_4)

        self.movescount=0

        # здесь первые элементы списка обозначают номер шеста (в функции move берётся остаток от деления на 10), выбраны такие числа, чтобы при удалении номера кольца не мог быть удален номер шеста
        self.pole_1 = [10, 3, 2, 1, 0]
        self.pole_2 = [11]
        self.pole_3 = [12]

        # кнопка clear закрывает текующее окно игры и открывает новое, чем полностью перезапускает игру
        clear = Button(self.root, text="clear", fg="black", font="Consolas 24 bold", bg='black', activebackground='black',
                         highlightbackground="#B4DD1E", justify=CENTER, command=lambda: self.main(),
                         width=7, bd=0)
        clear.configure(bg='#B4DD1E')
        clear.place(relx=0, rely=0.3, anchor=SW)

        enter.configure(text='restart')
        moves_number(self.movescount, self.moves)

        self.time = time.time()

        return

    @staticmethod
    def is_done(pole_3):
        '''принимает pole_3, содержащий информацию, о том, какие кольца находятся на третьем шесте и проверяет, соответствует ли этот набор собранной башне'''
        Validator(pole_3).validate_pole()
        return pole_3 == [12, 3, 2, 1, 0]

    def elem_start_pos(self):
        '''создаёт первичный интерфейс игры: фон, кнопку start и кнопки ходов, в интерфейсе может быть повторно активирована через кнопку clear, что полностью его перезапустит'''
        global enter, all_posx, all_posy

        all_posx = []
        all_posy = []
        self.pole_1 = []
        self.pole_2 = []
        self.pole_3 = []
        self.movescount=0

        self.canvas = Canvas(self.root, width=550, height=350, background="#B4DD1E", bd=0, highlightthickness=0)
        self.canvas.place(relx=0.5, rely=0.55, anchor=CENTER)
    #это кнопка start, она вызывает функцию put_tower_pieces(), чем запускает игру (после чего превращается в restart)
        enter = Button(self.root, text="start", fg="black", font="Consolas 24 bold", bg='black', activebackground='black',
                       highlightbackground="#B4DD1E", justify=CENTER, command=lambda: self.put_tower_pieces(),
                       width=7, bd=0)
        enter.configure(bg='#B4DD1E')
        enter.place(relx=0, rely=0.15, anchor=SW)
    #здесь добавляются кнопки, отвечающие за варианты ходов, кнопка 1->3, например, переносит верхнее кольцо с первого шеста на третий
        move_1 = Button(self.root, text='1->2', fg="black", font="Consolas 24 bold", bg='black', activebackground='black',
                        highlightbackground="#B4DD1E", justify=CENTER, command=lambda: self.move(self.pole_1, self.pole_2),
                        width=7, bd=0)
        move_2 = Button(self.root, text='1->3', fg="black", font="Consolas 24 bold", bg='black', activebackground='black',
                        highlightbackground="#B4DD1E", justify=CENTER, command=lambda: self.move(self.pole_1, self.pole_3),
                        width=7, bd=0)
        move_3 = Button(self.root, text='2->3', fg="black", font="Consolas 24 bold", bg='black', activebackground='black',
                        highlightbackground="#B4DD1E", justify=CENTER, command=lambda: self.move(self.pole_2, self.pole_3),
                        width=7, bd=0)
        move_4 = Button(self.root, text='2->1', fg="black", font="Consolas 24 bold", bg='black', activebackground='black',
                        highlightbackground="#B4DD1E", justify=CENTER, command=lambda: self.move(self.pole_2, self.pole_1),
                        width=7, bd=0)
        move_5 = Button(self.root, text='3->1', fg="black", font="Consolas 24 bold", bg='black', activebackground='black',
                        highlightbackground="#B4DD1E", justify=CENTER, command=lambda: self.move(self.pole_3, self.pole_1),
                        width=7, bd=0)
        move_6 = Button(self.root, text='3->2', fg="black", font="Consolas 24 bold", bg='black', activebackground='black',
                        highlightbackground="#B4DD1E", justify=CENTER, command=lambda: self.move(self.pole_3, self.pole_2),
                        width=7, bd=0)
        move_3.configure(bg='#B4DD1E')
        move_3.place(relx=0.6, rely=0.9, anchor=SW)
        move_2.configure(bg='#B4DD1E')
        move_2.place(relx=0.5, rely=0.9, anchor=S)
        move_1.configure(bg='#B4DD1E')
        move_1.place(relx=0.4, rely=0.9, anchor=SE)
        move_6.configure(bg='#B4DD1E')
        move_6.place(relx=0.6, rely=1, anchor=SW)
        move_5.configure(bg='#B4DD1E')
        move_5.place(relx=0.5, rely=1, anchor=S)
        move_4.configure(bg='#B4DD1E')
        move_4.place(relx=0.4, rely=1, anchor=SE)
        self.update_leaderboard(0)
        self.moves = Label(self.root, text=f'{self.movescount} Moves', fg="black", font="Consolas 20", bg="#B4DD1E")
        self.moves.place(relx=0.5, rely=0.12, anchor=CENTER)

    def move(self, departure_pole, destination_pole):

        '''эта функция вызывается кнопками ходов, принимая два значения: departure_pole - шест, с которого игрок хочет снять кольцо, destination_pole - шест, на которой игрок хочет переместить кольцо. Валидация аргументов здесь подразумевается в проверке: предусмотрен ли такой ход правилами. Также метод считает количество ходов и вызывает отвечает за проверку головоломки на законченность и появление поздравления'''
        Validator(departure_pole, destination_pole).validate_pole()
        try:
            item = departure_pole[1:][-1]
            # здесь задаются координаты для перемещения кольца
            if (len(destination_pole)>1) and (destination_pole[-1]<departure_pole[-1]):
                #проверка того, соответствует ли ход правилу, что кольцо можно класть только на кольцо, которое больше его
                raise RingError(self.root)
            else:

                posx = 180 * (destination_pole[0] % 10)
                posy = 145 - 45 * (len(destination_pole) - 1)


                self.movescount += 1
                moves_number(self.movescount, self.moves)

                if (item == 0):
                    # процесс перемещения происходит следующим образом: сначала перемещается изображение кольца на вычисленные ранее координаты, затем в список того шеста, на которое кольцо переместилось, с конца добавляется номер кольца (то есть в списке номера колец представлены в порядке снизу вверх), а из списка шеста, с которого кольцо сняли, номер кольца удаляется
                    self.block_1 = ImageTk.PhotoImage(Image.open("1.png"))
                    self.canvas.create_image(posx, posy, anchor=NW, image=self.block_1)
                    Tk.update(self.root)
                    destination_pole.append(item)
                    departure_pole.remove(item)

                elif (item == 1):

                    self.block_2 = ImageTk.PhotoImage(Image.open("2.png"))
                    self.canvas.create_image(posx, posy, anchor=NW, image=self.block_2)
                    Tk.update(self.root)
                    destination_pole.append(item)
                    departure_pole.remove(item)

                elif (item == 2):

                    self.block_3 = ImageTk.PhotoImage(Image.open("3.png"))
                    self.canvas.create_image(posx, posy, anchor=NW, image=self.block_3)
                    Tk.update(self.root)
                    destination_pole.append(item)
                    departure_pole.remove(item)

                elif (item == 3):
                    self.block_4 = ImageTk.PhotoImage(Image.open("4.png"))
                    self.canvas.create_image(posx, posy, anchor=NW, image=self.block_4)
                    Tk.update(self.root)
                    destination_pole.append(item)
                    departure_pole.remove(item)

                if self.is_done(self.pole_3):
                    # когда на третьем шесте удаётся собрать изначальную комбинацию (головоломка решена), выводим поздравление)
                    player_time=time.time()-self.time
                    congratulations(self.root, self.movescount, player_time)
                    # после поздравления игрока просят ввести имя для внесения результата в таблицу лидеров (если он попал в топ-3 по времени сбора башни)
                    name = simpledialog.askstring(title="Congratulations!",
                                                  prompt="What's your Name?:\n (leave empty if you don`t wanna be on the leaderboard)")
                    if name:
                        #в списке лидеров self.leaders хранятся упорядоченные 3 лучших результата за всё время
                        if len(self.leaders)<3:
                            self.leaders.append([player_time,name])
                            self.leaders.sort()
                            self.update_leaderboard(len(self.leaders))
                        elif player_time<max(self.leaders)[0]:
                            self.leaders.append([player_time, name])
                            self.leaders.sort()
                            while len(self.leaders)>3:
                                self.leaders.remove(max(self.leaders))
                            self.update_leaderboard(len(self.leaders))
                    return
        #если игрок пытается перенести кольцо с пустого шеста, на интерфейсе появится надпись, что шест пустой
        except IndexError:
            raise EmptyPoleError(self.root, departure_pole)

    def update_leaderboard(self,mode):
        '''метод обновляет таблицу лидеров в соответствии с режимом, заданным переменной mode'''
        #mode - количество записей в списке лидеров, то есть количество строк, которое нужно обновить (0 - создаётся пустая таблица, 1 - обновляется только первая строка таблицы и тд)
        Validator(mode).validate_mode()
        if mode==0:
            leaderboard = Label(self.root, text='leaderboard', fg="black", font="Consolas 28", bg="#B4DD1E")
            leaderboard.place(rely=0.06, relx=0.7)
            self.leader_one = Label(self.root, text='1.', fg="black", font="Consolas 20", bg="#B4DD1E")
            self.leader_one.place(rely=0.11, relx=0.7)
            self.leader_two = Label(self.root, text='2.', fg="black", font="Consolas 20", bg="#B4DD1E")
            self.leader_two.place(rely=0.16, relx=0.7)
            self.leader_three = Label(self.root, text='3.', fg="black", font="Consolas 20", bg="#B4DD1E")
            self.leader_three.place(rely=0.21, relx=0.7)
        if mode==1:
            self.leader_one.configure(text=f'1. {str(self.leaders[0][0])[:4]} sec - {self.leaders[0][1]}')
        if mode==2:
            self.leader_one.configure(text=f'1. {str(self.leaders[0][0])[:4]} sec - {self.leaders[0][1]}')
            self.leader_two.configure(text=f'2. {str(self.leaders[1][0])[:4]} sec - {self.leaders[1][1]}')
        if mode==3:
            self.leader_one.configure(text=f'1. {str(self.leaders[0][0])[:4]} sec - {self.leaders[0][1]}')
            self.leader_two.configure(text=f'2. {str(self.leaders[1][0])[:4]} sec - {self.leaders[1][1]}')
            self.leader_three.configure(text=f'3. {str(self.leaders[2][0])[:4]} sec - {self.leaders[2][1]}')

a=TowerInterface('1.png','2.png','3.png','4.png','poles.png')
a.main()
