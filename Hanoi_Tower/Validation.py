import tkinter
from tkinter import *
import filetype
from Exceptions import *
'''класс осуществляющий валидацию аргументов для методов класса TowerInterface, принимающий список аргументов для проверки'''
class Validator():
    def __init__(self, *args):
        self.objects=[*args]
    def validate_towerinterface(self):
        '''проверяет, правильный ли формат имеют передаваемые конструктору класса TowerInterface файлы (они должны быть изображениями)'''
        for file in self.objects:
            try:
                if not filetype.is_image(file):
                    raise FileError(file)
            except FileNotFoundError:
                raise FileNotFoundError
    def validate_pole(self):
        '''для методов принимающих списки, обозначающие наборы колец на шестах, проверяет на то, что переданы списки возможной в рамках логики программы длины'''
        for object in self.objects:
            if not (isinstance(object,list)) or len(object)==0 or len(object)>5:
                raise ValueError(f'something wrong with a pole {object}')
    def validate_mode(self):
        '''проверяет укладывается ли значение "режима" метода в допустимый диапозон'''
        for object in self.objects:
            if not (object in [0,1,2,3]):
                raise ValueError('wrong mode')
