from formats import *
from random import randint
from time import sleep


class memoria:
    
    def __init__(self):
        self.rodadas = self.acertos = self.erros = 0
        self.computer_numbers = list()
        self.player_numbers = list()
        
        while True:
            self.rodadas += 1
            
            if self.rodadas == 1:
                menu(txt = ['Facíl', 'Médio', 'Difícil', 'Sair'], title = 'Jogo da Memória')
                difficulty = checkNumber()

                if difficulty not in [1,2,3,4]:
                    continue
                
                elif difficulty == 4:
                    break
            
            
            self.start(difficulty)
            
            if self.erros > 0:
                break
            
            self.computer_numbers.clear()
            self.player_numbers.clear()
        
        line('Muito Bem')
        print(f'\nVocê acertou \033[4;32m{self.acertos}\033[m e errou \033[1;31m{self.erros}\033[m de um total de {self.acertos + self.erros} rodadas\n')
        
    def start(self, difficulty):
        #*Um dicionário com as velocidades ligadas com as opções do menu.
        dict_velocity = {1: 0.8, 2: 0.6, 3: 0.4}
        velocity = dict_velocity[difficulty]
         
        ColorH.open('azul_claro', style = 'bold')
        print('\n','-=-' * 16)
        
        for i in range(0, self.rodadas):
        
            number = randint(0,100)
            print(f'\b\b\b{number}', end = '', flush = True)
            sleep(velocity)
            print('\b\b\b?', end = '')
            
            self.computer_numbers.append([number][:])
            
        print('\n','-=-' * 16,'\n')
        ColorH.close()
        
        self.player_time()
        
    def player_time(self):
        for i in range(1, self.rodadas +1):
            print('\033[33m')
            
            print(f'\nDigite o {i}º que apareceu.')
            n = checkNumber()
            
            print('\033[m')
            
            self.player_numbers.append([n][:])
        
        #*Verifica se o player acertou ;)
        for i in range(0, len(self.computer_numbers)):
            if self.player_numbers[i] == self.computer_numbers[i]:
                self.acertos += 1
                
            else:
                self.erros += 1
