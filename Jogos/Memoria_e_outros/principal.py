from formats import *
from memoria import *
from math_game import *
from jokenpo import *

jogar_novamente = False

while True:
    
    if not jogar_novamente:    
        # print('\n\033[7;37m','=-=' * 50,'\033[m\n')
        
        menu(txt = ['Memória','Jokênpo','Matematica','Sair'], title = 'Bem vindo ao Jogos 2.0')
        action = checkNumber()
        
    # print('\n\033[7;37m','=-=' * 50,'\033[m\n')
    
    if action == 1:
        memoria()
    
    elif action == 2:
        jokenpo()
        
    elif action == 3:
        math()
        continue
        
    elif action == 4:
        # msg_sleep(txt = ['Finalizando ','1 ','2 ','3 ','4 ''.','.','.','\n'], sequence = True)
        break
    
    jogar_novamente = check_not_yes('Deseja jogar novamente')
    