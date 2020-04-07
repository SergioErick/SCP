from formats import *
from random import randint
from time import sleep


class memoria:
    
    def __init__(self):
        self.rodadas = 1
        self.acertos = self.erros = 0
        self.computer_numbers = list()
        self.player_numbers = list()
        
        while True:
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
            
            self.rodadas += 1
            
            self.computer_numbers.clear()
            self.player_numbers.clear()
        
        line('Muito Bem')
        print(f'\nVocê acertou \033[4;32m{self.acertos}\033[m e errou \033[1;31m{self.erros}\033[m de um total de {self.acertos + self.erros} rodadas\n')
        
    def start(self, difficulty):
        if difficulty == 1:
            velocity = 0.8
        
        elif difficulty == 2:
            velocity = 0.6
            
        elif difficulty == 3:
            velocity = 0.4
        
        elif difficulty == 4:
            return False
         
        print('\033[1;36m')   
        print('\n','-=-' * 16)
        
        for i in range(0, self.rodadas):
        
            number = randint(0,100)
            print(f'\b\b\b{number}', end = '', flush = True)
            sleep(velocity)
            print('\b\b\b?', end = '')
            
            self.computer_numbers.append([number][:])
            
        print('\n','-=-' * 16,'\n')
        print('\033[m')
        
        self.player_time()
        
    def player_time(self):
        for i in range(0, self.rodadas):
            print('\033[33m')
            
            print(f'\nDigite o {i + 1}º que apareceu.')
            n = checkNumber()
            
            print('\033[m')
            
            self.player_numbers.append([n][:])
            
        for check in self.player_numbers:
            if check not in self.computer_numbers:
                self.erros += 1
            
            else:
                self.acertos += 1
