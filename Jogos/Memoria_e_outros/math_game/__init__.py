from random import randint
from time import sleep
from formats import *

class math:
    def __init__(self):
        self.acertos = self.erros = tentativas = 0
        contas = ['//','*','+','-']
        
        while True:
            if tentativas == 0:
                menu(txt = ['Apenas de Divisão','Apenas Multiplicação','Apenas Soma','Apenas subtração','Aleatório','Rules','Sair'], title = 'Matemática')
                react = checkNumber()
            
            if react not in [1,2,3,4,5,6,7]:
                continue
            
            if react == 7:
                break
            
            elif react == 1:
                self.divisao()
            
            elif react == 2:
                self.vezes()
            
            elif react == 3:
                self.soma()
            
            elif react == 4:
                self.menos()
            
            elif react == 5:
                self.aletory()
                
            elif react == 6:
                self.rules()
            
            tentativas += 1
            self.check_correct()
            
            if not check_not_yes('Deseja continuar'):
                break
            
            
        print(f'Você acertou {self.acertos} e errou {self.erros}. De {tentativas} tentaivas.')
            
                
    def divisao(self):
        global a,b
        
        a = randint(0,1000)
        b = randint(0,1000)
        
        self.player = checkNumberFloat(f'Quanto é {a} / {b}: ')
        self.correct = a / b
        
    def vezes(self):
        pass
    
    def soma(self):
        pass
   
    def menos(self):
        pass
   
    def aletory(self):
        pass
    
    def rules(self):
        pass
    
    def check_correct(self):
        if f"{self.correct:.2f}" == f"{self.player:.2f}":
            print('\033[4;32mAcertou\033[m')
            self.acertos += 1
            
        else:
            print('\033[4;31mErrou\033[m')
            print(f'O correto era {self.correct:.2f}')
            self.erros += 1