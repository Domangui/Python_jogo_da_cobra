import pygame
from pygame import *
from sys import exit
from random import randint
pygame.init()

#screen
height = 640
width = 480

#Variaveis uteis
velocidade = 10
pontos = 0

#snake
x_length_snake = 20
y_length_snake = 20
x_position_snake = height/2 - x_length_snake/2
y_position_snake = width/2 - y_length_snake/2
x_control_snake = 5
y_control_snake = 0
body_snake_list = []
length_body_snake = 20
death_snake = False
#apple
x_length_apple = 20
y_length_apple = 20
x_position_apple = randint(40,600)
y_position_apple = randint(50, 400)

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('Snake')

#Funções
def mov_snake(body_snake_list):
    for XeY in body_snake_list:
        pygame.draw.rect(screen, (0,255,0), (XeY[0],XeY[1],20,20))

def reiniciar_jogo():
    global x_length_snake,death_snake,body_snake_list,head_snake_list, y_length_snake, x_position_snake, y_position_snake, length_body_snake, velocidade, pontos, x_position_apple, y_position_apple
    x_length_snake = 20
    y_length_snake = 20
    x_position_snake = height/2 - x_length_snake/2
    y_position_snake = width/2 - y_length_snake/2
    length_body_snake = 20
    velocidade = 10
    pontos = 0
    body_snake_list = []
    head_snake_list = []
    x_position_apple = randint(40,600)
    y_position_apple = randint(50, 400)
    death_snake = False

while True:
        
    pygame.time.Clock().tick(30)
    screen.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    fonte = pygame.font.SysFont('arial', 40, True, True)
    msg_formatada = fonte.render(mensagem, True,(255,255,255))
    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_control_snake == velocidade:
                    pass
                else:
                    x_control_snake = -velocidade
                    y_control_snake = 0
            if event.key == K_d:
                if x_control_snake == -velocidade:
                    pass
                else:
                    x_control_snake = velocidade
                    y_control_snake = 0
            if event.key == K_w:
                if y_control_snake == velocidade:
                    pass
                else:
                    y_control_snake = -velocidade
                    x_control_snake = 0
            if event.key == K_s:
                if y_control_snake == -velocidade:
                    pass
                else:
                    y_control_snake = velocidade
                    x_control_snake = 0

    x_position_snake = x_position_snake + x_control_snake
    y_position_snake = y_position_snake + y_control_snake

    snake = pygame.draw.rect(screen, (0,255,0), (x_position_snake,y_position_snake,x_length_snake,y_length_snake) )
    apple = pygame.draw.rect(screen, (255,0,0), (x_position_apple,y_position_apple,x_length_apple,y_length_apple))

    if snake.colliderect(apple):
        x_position_apple = randint(40, 600)
        y_position_apple = randint(50, 400)
        pontos = pontos + 1
        length_body_snake = length_body_snake + 1
        velocidade = velocidade + float(0.03)

    head_snake_list = []
    head_snake_list.append(x_position_snake)
    head_snake_list.append(y_position_snake)
    body_snake_list.append(head_snake_list)

    if len(body_snake_list) > length_body_snake:
        del body_snake_list[0]

    
            
    if body_snake_list.count(head_snake_list) > 1:
        msg_snake = f'Digite R para reiniciar o jogo.'
        fonte_snake = pygame.font.SysFont('arial',20,True,True)
        msg_formatada_snake = fonte_snake.render(msg_snake, True, (255,255,255)) 
        ret_text = msg_formatada_snake.get_rect()
        msg_pontos_snake = f' Total de pontos {pontos}'
        fonte_pontos_snake = pygame.font.SysFont('arial', 20, True, True)
        msg_ponto_formatada_snake = fonte_pontos_snake.render(msg_pontos_snake, True, (255,255,255))
        ret_pontos_text = msg_ponto_formatada_snake.get_rect()
        death_snake = True

        while death_snake:
            screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_pontos_text.center = (height/2,width/2 + 60)
            ret_text.center = (height/2, width/2)
            screen.blit(msg_formatada_snake, ret_text)
            screen.blit(msg_ponto_formatada_snake, ret_pontos_text)
            pygame.display.update()

    if x_position_snake > height:
        x_position_snake = 0
    if x_position_snake < 0:
        x_position_snake = 640
    if y_position_snake > width:
        y_position_snake = 0
    if y_position_snake < 0:
        y_position_snake = 480
    

    mov_snake(body_snake_list)
    screen.blit(msg_formatada, (450,40))

    pygame.display.update()
