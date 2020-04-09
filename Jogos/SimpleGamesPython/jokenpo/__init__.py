from random import randint
from time import sleep
from formats import *

class jokenpo:
    def __init__(self):
        game = {
            1: 'pedra',
            2: 'papel',
            3: 'tesoura'
        }
        
        self.computer_play = randint(1,3)
        
        while True:
            menu(txt = ['Pedra', 'Papel', 'Tesoura', 'Sair'], title = 'Jokênpo')
            self.player_play = checkNumber()
            
            if 0 < self.player_play <= 4:
                break
        
        if self.player_play == 4:
            return
        
        msg_sleep(txt = ['Jo...','kên...','po...'])
        
        line(f'\nO pc escolheu {game[self.computer_play]} e você {game[self.player_play]}\n', color = '\033[31m')

        self.who_is_winner()
        
    def who_is_winner(self):
        '''
        Essa função decide quem ganhou, ela usa um príncipio matemático para decidir quem ganhou. :)
        '''
        
        pc = self.computer_play
        us = self.player_play
        
        if pc == us:
            line('Empate', color = '\033[37m')
            
        elif pc - us == -2 or pc - us == 1:
            line('\nO computador ganhou\n', color = '\033[1;31m')
            
        else:
            line('\nO player ganhou\n', color = '\033[4;32m')