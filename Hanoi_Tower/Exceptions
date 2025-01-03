import tkinter
from tkinter import *

'''классы исключений, которые помимо обработки ошибок так же оставляют комментари на самом интерфейсе игры'''
class EmptyPoleError(Exception):
    def __init__(self, root, pole):
        self.root=root
        self.pole=pole
        self.message()
    def message(self):
        '''вызывается при попытке перенести кольцо с пустого шеста. есть два применения: если игра еще не началась или если на шесте просто сейчас нет колец. выдаёт сообщение в самом интерфейсе игры'''
        if len(self.pole)>0:
            message = Label(self.root, text=f'pole {self.pole[0]%10+1} \nhas no rings', fg="red", font="Consolas 20", bg="#B4DD1E")
            message.place(rely=0.5, relx=0.75)
            message.after(2000, message.destroy)
        else:
            message = Label(self.root, text=f'press start', fg="red",
                            font="Consolas 20", bg="#B4DD1E")
            message.place(rely=0.5, relx=0.75)
            message.after(2000, message.destroy)

class RingError(Exception):
    def __init__(self,root):
        self.root=root
        self.message()

    def __str__(self):
        return 'RingError Exception raised'

    def message(self):
        '''выводит на интерфейс игры сообщение о том, игрок пытается переместить кольцо, которое для этого слишком большое'''
        message = Label(self.root, text=f'the ring you`re trying to move \nis too big', fg="red", font="Consolas 18",
                        bg="#B4DD1E")
        message.place(rely=0.5, relx=0.65)
        message.after(2000, message.destroy)
class FileError(Exception):
    '''исключение, вызываемое валидатором, проверяющим формат файлов'''
    def __init__(self,file):
        self.file=file
    def __str__(self):
        return f'File {self.file} has wrong format'
