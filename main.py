import pygame
from pygame.locals import *
from sys import exit 
from random import randint
pygame.init()

largura = 640
altura = 480

velocidade = 10

x_snake = largura/2 - 20
y_snake = altura/2 - 30
x_const_snake = 5
y_const_snake = 0
lista_Corpo_Snake = []


morreu = False
x_apple = randint(40, 600)
y_apple = randint(50, 400)

crescimento_snake = 10
pontos = 0
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('minigame')
#Variáveis
def cresce_snake(lista_Corpo_Snake):
       for XeY in lista_Corpo_Snake:
        pygame.draw.rect(tela, (0,255,0), (XeY[0],XeY[1],20,20))

def reiniciar_jogo():
    global largura, altura, velocidade, x_snake, y_snake, crescimento_snake, pontos, lista_Corpo_Snake, lista_Cabeca_Snake, x_apple, y_apple, morreu

    largura = 640
    altura = 480
    velocidade = 10
    x_snake = largura/2 - 20
    y_snake = altura/2 - 30
    crescimento_snake = 5
    pontos = 0
    lista_Corpo_Snake = []
    lista_Cabeca_Snake = []
    x_apple = randint(40, 600)
    y_apple = randint(50, 400)
    morreu = False
while True:
    pygame.time.Clock().tick(30)
    tela.fill((0,0,0))
    fonte = pygame.font.SysFont('arial',40 ,True,True)
    mensagem = f'Pontos: {pontos}'
    msg_formatada = fonte.render(mensagem, True, (255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_const_snake == velocidade:
                    pass
                else:
                    x_const_snake = -velocidade
                    y_const_snake = 0
            if event.key == K_d:
                if x_const_snake == -velocidade:
                    pass
                else:
                    x_const_snake = velocidade
                    y_const_snake = 0
            if event.key == K_w:
                if y_const_snake == velocidade:
                    pass
                else:
                    y_const_snake = -velocidade
                    x_const_snake = 0
            if event.key == K_s:
                if y_const_snake == -velocidade:
                    pass
                else: 
                    y_const_snake = velocidade
                    x_const_snake = 0

    x_snake = x_snake + x_const_snake
    y_snake = y_snake + y_const_snake

    if x_snake == largura:
        x_snake = 0
    elif x_snake == 0:

    
        x_snake = largura

    if y_snake == altura:
        y_snake = 0
    elif y_snake == 0:
        y_snake = altura


    snake = pygame.draw.rect(tela, (0,255,0), (x_snake, y_snake, 20, 20))
    apple = pygame.draw.rect(tela, (255,0,0), (x_apple,y_apple,20,20))

    if snake.colliderect(apple):
        x_apple = randint(40, 600)
        y_apple = randint(50, 400)
        pontos = pontos +1
        crescimento_snake = crescimento_snake +1

    lista_Cabeca_Snake = []
    lista_Cabeca_Snake.append(x_snake)
    lista_Cabeca_Snake.append(y_snake)
    lista_Corpo_Snake.append(lista_Cabeca_Snake)
    
    cresce_snake(lista_Corpo_Snake)

    if len(lista_Corpo_Snake) > crescimento_snake:
        del lista_Corpo_Snake[0]

    if lista_Corpo_Snake.count(lista_Cabeca_Snake) > 1:

        morreu = True
        while morreu:
            tela.fill((0,0,0))
            fonte2 = pygame.font.SysFont('arial', 20 ,True, True)
            mensagem_rein = f'Aperte a tecla P para reiniciar'
            mensagem_pontos_rein = f'Total de pontos: {pontos}'
            mensagem_formatada_pontos_rein = fonte2.render(mensagem_pontos_rein, True, (255,255,255))
            mensagem_formatada_rein = fonte2.render(mensagem_rein, True, (255,255,255))
            cent_msg = mensagem_formatada_rein.get_rect()
            cent_ponto_msg = mensagem_formatada_pontos_rein.get_rect()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_p:
                        print('oo')
                        reiniciar_jogo()
            cent_ponto_msg.center = (largura/2, altura/2 + 60)
            cent_msg.center = (largura/2, altura/2)
            tela.blit(mensagem_formatada_pontos_rein, (cent_ponto_msg))
            tela.blit(mensagem_formatada_rein, (cent_msg))            
            pygame.display.update()


    tela.blit(msg_formatada, (420, 40))
    pygame.display.update()