from formats import *
from memoria import *
from math_game import *
from jokenpo import *
import os,shutil

user = os.getlogin()
dir = os.getcwd()
Dpath = dir + '\Jogos\SimpleGamesPython\data'

class file:
    def __init__(self, FileName = f'{Dpath}\config.txt'):
        if not os.path.exists(Dpath):
            os.mkdir(Dpath)
            
        if not os.path.exists(FileName):
            load = open(FileName, 'wt')
            load.write(f'USER: {user}\n')
            load.close()


file()

while True:
    #*Cria um menu através do módulo 'formats'--------------------------------------------
    menu(txt = ['Memória','Jokênpo','Matematica','Sair'], title = f'Bem vindo {user} ao Jogos 2.0')
    action = checkNumber()
    
    if action == 1:
        memoria()
    
    elif action == 2:
        jokenpo()
        
    elif action == 3:
        math()
        continue
        
    elif action == 4:
        #!msg_sleep(txt = ['Finalizando ','1 ','2 ','3 ','4 ''.','.','.','\n'], sequence = True) Está comentado, pois desacelera o processo de saída.
        break