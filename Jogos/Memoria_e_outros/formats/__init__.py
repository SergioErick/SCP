from time import sleep

def menu(txt, title = 'Olá'):
    line(title)
    
    print('\033[34m')
    
    for i,w in enumerate(txt):
        print(f'[ {i + 1} ] {w.title()}')
    
    print('\033[m')
        
def line(msg, color = '\033[1;32m'):
    print(color)
    
    print('-' * 50)
    print(f'{msg:^50}')
    print('-' * 50)
    
    print('\033[m')
    
def checkNumber(answer = 'R: '):
    while True:
        try:
            pergunta = int(input(f'\033[34m{answer.title()}\033[m'))
            
        except:
            print('Valor inválido.')
            continue
        
        else:
            return pergunta

def checkNumberFloat(answer = 'R: '):
    while True:
        try:
            pergunta = float(input(f'\033[34m{answer.title()}\033[m'))
            
        except:
            print('Valor inválido.')
            continue
        
        else:
            return pergunta

def check_not_yes(answer = 'R: '):
    while True:
        pergunta = str(input(f'{answer}[ s / n ]: '))
    
        if pergunta not in 'SsNn':
            continue
        
        if pergunta in 'Ss':
            return True
        
        else:
            return False

def msg_sleep(txt, time = 0.5, sequence = False):
    print(f"\n\033[33m{'~' * 50}\n")
    
    if sequence:
        for i in txt:
            print(i, end = '', flush = True)
            sleep(time)
    else:
        for i in txt:
            print(i)
            sleep(time)
        
    print(f"\n{'~' * 50}\033[m\n")
    