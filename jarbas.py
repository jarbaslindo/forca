#O comando "import random" é utilizado para importar uma biblioteca para escolher aleatoriamente. 
import random
#Variável criada para ser a lista que contém as palavras que poderão estar presentes no jogo.
palavras = [] 
#Variável responsável por mostrar quando a letra não está contida na palavra.  
letrasErradas = ''
#Variável responsável por mostrar quando a letra está contida na palavra.
letrasCertas = ''
#Variável desenvolvida para criar uma "imagem" para o jogo, com um aspecto físico.
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def receber():
    while True:
        receber = input("Qual a palavra: ")
        palavras.append(receber)
        if receber == '':
            break
#É um comando responsável por comandar as principais funções do jogo, e é ele o comando chamado pelo comando "principal()" quando se cria o jogo. 
def principal():
    """
    Função Princial do programa
    """
    receber()
#É um comando utilizado para imprimir uma "imagem" na tela.
    print('F O R C A')
#Uma variável que tem como função escolher randomicamente qual palavra será utilizada no jogo.
    palavraSecreta = sortearPalavra()
#Variável usada para ser a letra que o jogador digitou.
    palpite = ''
#Variável utilizada para julgar a letra que o jogador digitou está certa ou errada.
    desenhaJogo(palavraSecreta,palpite)
#Comando utilizado para repetir a função enquanto a sentença for verdadeira.
    while True:
#Vai receber a letra que o jogador digitou.
        palpite = receberPalpite() 
#Vai julgar o palpite do jogador.
        desenhaJogo(palavraSecreta,palpite)
#Comando responsável por verificar se a sentença está correta ou não. Caso esteja, ou seja, caso o jogador tenha perdido o jogo, ele entra em ação.
        if perdeuJogo():
#Comando utilizado para imprimir a frase "Voce Perdeu!!!" na tela.
            print('Voce Perdeu!!!')
#Comando utilizador para parar o comando "if".
            break
#Comando responsável por verificar se a sentença está correta ou não. Caso esteja, ou seja, caso o jogador tenha ganho o jogo, ele entra em ação.
        if ganhouJogo(palavraSecreta):
#Comando utilizado para imprimir a frase "Voce Ganhou!!!" na tela. 
            print('Voce Ganhou!!!')
#Comando utilizado para parar o comando "if".
            break            
        
#Comando utilizado para "entrar em cena" caso o jogador perca.
def perdeuJogo():
#O comando "global" serve para colocar a variável "FORCAIMG" em cena mesmo que a "def perdeuJogo()" não seja acionada.
    global FORCAIMG
#Testa se a variável "letrasErradas" tem o "mesmo peso" que a variável "FORCAIMG".
    if len(letrasErradas) == len(FORCAIMG):
#Caso o comando "def perdeuJogo()" seja ativado, o "return True" será verdade. Caso contrário o comando será falso.
        return True
#Comando utilizado para caso o comando "if" não seja verdade.
    else:
#Caso o comando "def perdeuJogo()" não seja ativado, o "return False" será verdade. Caso contrário o comando será falso.
        return False
#Comando utilizado para "entrar em cena" caso o jogador vença.    
def ganhouJogo(palavraSecreta):
#O comando "global" serve para colocar a variável "letrasCertas" em cena mesmo que a "def ganhouJogo()" não seja acionada. Fazendo com que ela seja global.
    global letrasCertas
#Variável utilizada para comprovar que o jogador ganhou o jogo.
    ganhou = True
#Comando utilizado para verificar se a letra está ou não contida na palavra.
    for letra in palavraSecreta:
#Caso não esteja contida, este comando será ativado.
        if letra not in letrasCertas:
#Caso não esteja, o jogador não terá ganho jogo.
            ganhou = False 
#Comando utilizado para voltar na variável "ganhou".
    return ganhou        
        

#Comando utilizado para testar o palpite do jogador.
def receberPalpite():
#Variável utilizada para "pedir" uma letra para o jogador.    
    palpite = input("Adivinhe uma letra: ")
#Variável utilizada para deixar tudo em maiúsculo.
    palpite = palpite.upper()
#Comando utilizado para contar quantas letras tem na palavra.
    if len(palpite) != 1:
#Comando utilizado para imprimir algo na tela.
        print('Coloque um unica letra.')
#Comando utilizado para verificar se a letra está ou não contida na palavra.
    elif palpite in letrasCertas or palpite in letrasErradas:
#Comando utilizado para imprimir algo na tela.
        print('Voce ja disse esta letra.')
#Comando utilizado para testar se o jogador está escrevcendo apenas letras.
    elif not "A" <= palpite <= "Z":
#Comando utilizado para imprimir algo na tela.
        print('Por favor escolha apenas letras')
#Caso o palpite do jogador não tenha seguido as regras ele retorna e palpita novamente.
    else:
        return palpite
    
#Comando utilizado para organizar o jogo em uma ordem para que o jogador consiga entender o jogo com facilidade.     
def desenhaJogo(palavraSecreta,palpite):
#Vai fazer com que a variável se torne global.
    global letrasCertas
#Vai fazer com que a variável se torne global.
    global letrasErradas
#Vai fazer com que a variável se torne global.
    global FORCAIMG
#Comando utilizado para imprimir algo na tela.
    print(FORCAIMG[len(letrasErradas)])
    
#Variável criada para cria um "-" para cada letra da palavra.      
    vazio = len(palavraSecreta)*'-'
#Se a letra que o jogador digitou está contidada na palavra secreta, adicione uma letra a "letrasCertas".  
    if palpite in palavraSecreta:
        letrasCertas += palpite
#Caso a letra não esteja contida, a letra inserida pelo jogador vai ser adicionada a "letrasErradas".
    else:
        letrasErradas += palpite
#Caso a letra esteja inserida em letra certa.
    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):

            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     
#Comando responsável por escolher uma palavra randomicamente para o jogo.
def sortearPalavra():
#Torna a variável "palavras" global. 
    global palavras
#Comando utilizado para voltar na variável "palavras". E o ".upper" serve para corrigir a escrita do jogador.
    return random.choice(palavras).upper()

    
principal()
