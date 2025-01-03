import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import font
import time
'''этот модуль содержит различные комментарии, которые могут выводиться в процессе игры, функции принимают, как минимум, аргументы movescount (количество сделанных ходов) и root (или напрямую связанный с ним аргумент) для возможности вывода комментария на основной интерфейс'''
def moves_number(movescount, moves):
    '''принимает аргументы movescount, moves и пишет на экране количество сделанных игроком ходов'''
    if not (isinstance(movescount, int) and isinstance(moves, tkinter.Label)):
        raise ValueError
    else:
        moves.configure(text=f'{movescount} moves')


def congratulations(root, movescount, game_time):
    '''эта функция принимает стандартные для модуля аргументы, game_time (это время потраченное игроком на завершение головоломки), программа выводит поздравление с указанием времени при успешном выполнении головоломки (за минимальное количество ходов) и более скромное поздравление с пожеланием, если ходов было больше минимального количества'''
    if not (isinstance(root, tkinter.Tk) and isinstance(movescount,int) and isinstance(game_time, float)):
        raise ValueError
    else:
        if movescount==15:
            congrats = Label(root, text=f'congrats!!!!\nyou needed {str(game_time)[:4]} secs', fg="black", font="Consolas 78", bg="#FFFFFF")

        if movescount>15:
            congrats = Label(root, text=f'congrats!\ncould`ve use less moves though\n {str(game_time)[:4]} secs', fg="black", font="Consolas 48", bg="#FFFFFF")

        congrats.place(relx=0.5, rely=0.8, anchor=CENTER)
        congrats.after(4000, congrats.destroy)





