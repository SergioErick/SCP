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
            
            if self.player_play in [1,2,3,4]:
                break
        
        if self.player_play == 4:
            return
        
        msg_sleep(txt = ['Jo...','kên...','po...'])
        
        line(f'\nO pc escolheu {self.computer_play} e você {self.player_play}\n', color = '\033[31m')

        self.who_is_winner()
        
    def who_is_winner(self):
        if self.computer_play == self.player_play:
            line('Empate', color = '\033[37m')
            
        elif self.computer_play - self.player_play == -2 or self.computer_play - self.player_play == 1:
            line('\nO computador ganhou\n', color = '\033[1;31m')
            
        elif self.player_play - self.computer_play == -2 or self.player_play - self.computer_play == 1:
            line('\nO player ganhou\n', color = '\033[4;32m')