from formats import *
from memoria import *
from math_game import *
from jokenpo import *
from datetime import datetime, date
import os,shutil

now = datetime.now()
data = now.strftime('%d/%m/%Y %H:%M')

user = os.getlogin()
dir = os.getcwd()
Dpath = dir + '\Jogos\SimpleGamesPython\data'


class file:
    def __init__(self, FileName = f'{Dpath}\config.txt'):
        global file_name
        file_name = FileName
        
        if not os.path.exists(Dpath):
            os.mkdir(Dpath)
            
        if not os.path.exists(FileName):
            load = open(FileName, 'wt')
            load.close()
            
            
        self.append(f'USER: {user}\n', favLine = 0)
        self.append(f'último acesso: {data}\n', favLine = 1)
        
    def append(self, appText = '', trade = True, favLine = None):
        if trade:
            doc = open(file_name, 'r')
            lines = doc.readlines()
            doc.close()
            
            doc = open(file_name, 'w')
            
            for index,line in enumerate(lines):
                lineC = line.split(':')
                try:
                    if favLine == index: 
                        doc.write(appText)
                        trade  = False
                    else:
                        doc.write(line)
                    
                except:
                    if appText == lineC[0]:
                        doc.write(appText)
                        trade  = False

                    else:
                        doc.write(line)
            
            doc.close()
            
        if trade:
            doc = open(file_name, 'at')
            doc.write(appText)
            doc.close()

    def info(self, what):
        doc = open(file_name, 'r')
        lines = doc.readlines()
        
        for  line in lines:
            lineC = line.split(':')       
            
        if what == lineC[0]:
            return lineC[1]
    
        doc.close()        
        
file = file()
rounds = 0

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
        
    elif action == 4:
        break
    
    rounds += 1

BeforeRound = file.info('Vezes jogadas')
try:
    totalRound = int(BeforeRound) + rounds
except:
    totalRound = rounds

file.append(f'Vezes jogadas:{totalRound}\n', favLine = 2)