from random import randint
from time import sleep
from formats import *

class math:
    def __init__(self):
        self.acertos = self.erros = tentativas = 0
        self.operation_math = {1: "/",2: '*', 3: '+', 4: '-'}
        
        while True:
            if tentativas == 0:
                menu(txt = ['Apenas de Divisão','Apenas Multiplicação','Apenas Soma','Apenas subtração','Aleatório','Rules','Sair'], title = 'Matemática')
                react = checkNumber()
            
            if 0 > react > 7:
                continue
               
            elif react == 7:
                return
        
            else:
                global a,b
                i = react
                
                if react == 5:
                    i = randint(1,4)
                
                op = self.operation_math[i]
                a = randint(0,1000)
                b = randint(0,1000)
                
                ab = f'{a}{op}{b}'
                
                self.player = checkNumberFloat(f'Quanto é {ab}: ')
                self.correct = eval(ab)
                
                self.check_correct()
                
            
            tentativas += 1
            
            if not check_not_yes('\nDeseja continuar'):
                break
            
            
        print(f'Você acertou {self.acertos} e errou {self.erros}. De {tentativas} tentativas.')
            
    
    def rules(self):
        pass
    
    def check_correct(self):
        if self.correct == self.player:
            print('\033[4;32mAcertou\033[m')
            self.acertos += 1
            
        else:
            print('\033[4;31mErrou\033[m')
            print(f'O correto era {self.correct:.2f}')
            self.erros += 1