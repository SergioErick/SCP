from time import sleep

def menu(txt, title = 'Olá'):
    """Cria a interface de um menu, onde as opções são numeradas. O usúario somente tem que ser passar dentro de uma list, dict ou tuple para que seja feito um menu com mais de uma opção
    
    Arguments:
        txt (type: str/tuple/dict/list) --> São as opções que o usuário tem que passar
    
    Keyword Arguments:
        title (type: str) --> É o título do menu (default: 'Olá')
    """    
    
    line(title)
    
    print('\033[34m')
    
    for i,w in enumerate(txt):
        print(f'[ {i + 1} ] {w.title()}')
    
    print('\033[m')
        
def line(msg, color = '\033[1;32m'):
    """
    Coloca um texto centralizado entre duas linhas traçadas(EX: "------")
    
    Arguments:
        msg (type: string) --> É o texto que vai ser colocado
    
    Keyword Arguments:
        color (type: string) --> A cor do texto e linha (default: '\033[1;32m')
    """    
    
    print(color)
    
    print('-' * 50)
    print(f'{msg:^50}')
    print('-' * 50)
    
    print('\033[m')
    
def checkNumber(answer = 'R: '):
    """Cria um loop que só pode sair quando o usuário digita um valor válido - int(EX: 17).
    
    Keyword Arguments:
        answer (type: string) --> É a pergunta que será feita ao user (default: 'R: ')
    
    Returns:
        (type: int) --> Retorna o número digitado pelo user
    """    
    
    while True:
        try:
            pergunta = int(input(f'\033[34m{answer.title()}\033[m'))
            
        except:
            print('Valor inválido.')
            continue
        
        else:
            return pergunta

def checkNumberFloat(answer = 'R: '):
    """Cria um loop que só pode sair quando o usuário digita um valor válido - float(EX: 7.5).
    
    Keyword Arguments:
        answer (type: string) --> A pergunta que será feita ao user (default: 'R: ')
    
    Returns:
        (type: FLoat) --> Retorn o valor digitado pelo user
    """    
    
    
    while True:
        try:
            pergunta = float(input(f'\033[34m{answer.title()}\033[m'))
            
        except:
            print('Valor inválido.')
            continue
        
        else:
            return pergunta

def check_not_yes(answer = 'R: '):
    """Verifica se o valor digitado corresponde á: s(sim), n(não).
    
    Keyword Arguments:
        answer (type: string) --> Pergunta que será feita ao usuário (default: 'R: ')
    
    Returns:
        Boolean --> Retorna false para n e True para s.
    """    
    
    while True:
        pergunta = str(input(f'{answer}[ s / n ]: '))
    
        if pergunta not in 'SsNn':
            continue
        
        if pergunta in 'Ss':
            return True
        
        else:
            return False

def msg_sleep(txt, time = 0.5, sequence = False):
    """Exibe mensagens em sequência com um certo tempo
    
    Arguments:
        txt (type: string/tuple/dict/tuple) --> São as mensagens que serão exibidas em uma sequência
    
    Keyword Arguments:
        time (type: int/float) --> Tempo de intervalo de uma mensagem a outra (default: 0.5)
        sequence (type: boolean) --> Define-se que, cada mensagem será mostrada ou não na mesma linha. True para sim e False para não(default: False)
    """    
    
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
    
class ColorHelp:
    def open(color = 'branco', color_background = '', style = ''):
        colors = {
            
            'branco':30,
            'vermelho':31,
            'verde':32,
            'amarelo':33,
            'azul':34,
            'roxo':35,
            'azul_claro':36,
            'cinza':37,
            
        }
        style = {
            
                

        }
        
        color = color.lower()
        
        if color_background == '': 
            print(f'\033[{colors[color]}m')
            
        elif style == '':
            print(f'\033[{colors[color]};{colors[color] + 10}m')
        
        else:
            print(f'\033[{colors[color]};{colors[color] + 10};{colors[color] - 30}m')