import pygame
from pygame.locals import *
from sys import exit
import pygame
from pygame.locals import *
from sys import exit
import time

pygame.init()

tela = pygame.display.set_mode((740, 480))
pygame.display.set_caption('Star - Basquete e Matemática')
fundo_inicio = pygame.transform.scale(pygame.image.load('telastart.jfif'), (740, 480))
fundo_jogo = pygame.transform.scale(pygame.image.load('graficojogo.jfif'), (740, 480))
botao_inicio = pygame.transform.scale(pygame.image.load('botaostart.jfif'), (150, 50))
jogador = pygame.transform.scale(pygame.image.load('jogador-Photoroom.png'), (100, 120))
botao_rect = botao_inicio.get_rect(center=(370, 330))
jogador_rect = jogador.get_rect(center=(600, 230))

sprite_sheet = pygame.image.load('com-effects-1--unscreen-ezgif.com-gif-to-sprite-converter.png')
quadro_largura = sprite_sheet.get_width() // 5
quadro_altura = sprite_sheet.get_height() // 10
quadros_bola = []

for j in range(10):
    for i in range(5):
        quadro = sprite_sheet.subsurface((i * quadro_largura, j * quadro_altura, quadro_largura, quadro_altura))
        quadro_redimensionado = pygame.transform.scale(quadro, (700, 300))
        quadros_bola.append(quadro_redimensionado)

perguntas = [
    {"pergunta": " Qual é o valor de (-2/4)^4", "opcoes": ["A) 4/2", "B)16/81", "C) 0,5", "D) 0"], "resposta": "B"},
    {"pergunta": "A soma das raízes quadradas de 1024 + 625 ", "opcoes": ["A) 7", "B) 97", "C) 37", "D) 57"],
     "resposta": "D"},
    {"pergunta": "O resultado de 7^4 . 7^9 é: ", "opcoes": ["A) 7^-5", "B)7^24", "C) 7^9", "D) 7^5"], "resposta": "A"},
    {"pergunta": "Qual o resultado da soma dos ângulos internos de um triângulo?",
     "opcoes": ["A) 180°", "B) 90°", "C)30°", "D)60°"], "resposta": "A"},
    {"pergunta": "A formula da lei dos senos e cossenos é: a/senA = b/senB = c/senC; a² + b² + c² - 2.b.c. cos a",
     "opcoes": ["A) Verdadeiro", "B) Falso", ], "resposta": "A"},
    {"pergunta": "O valor de 2^5 / 2^3 é", "opcoes": ["A) 2¹", "B) 2^10", "C) 2^7", "D)2²"], "resposta": "D"},
    {"pergunta": " Qual é o valor de (-2/4)^4", "opcoes": ["A) 4/2", "B)16/81", "C) 0,5", "D) 0"], "resposta": "B"},
    {"pergunta": "O resultado de 4x + 2 = 10 é: ", "opcoes": ["A) 2,5", "B)10/4", "C)2", "D)0"], "resposta": "C"},
    {"pergunta": "O resultado da inequação 2(x + 3) > 3(1-x) é: ", "opcoes": ["A) 0.6", "B)5/3", "C)3/5", "D)-3/5"],
     "resposta": "D"},
    {"pergunta": "O resultado de 3x - 9 = 12 é: ", "opcoes": ["A) 7", "B) 32", "C) 1", "D) 3"], "resposta": "A"},
    {"pergunta": "As raízes da equação x² - x - 20 = 0 são:",
     "opcoes": ["A) x¹ = x² = 7", "B)x¹ = -4 e x² = 5", "C) x¹ = 5 e x² = -4", "D) x¹ = 9 e x²= 3"], "resposta": "C"},
    {"pergunta": "A soma da raiz quadrada ", "opcoes": ["A) x", "B) xx", "C) xxx", "D) xxxx"], "resposta": "D"},
    {
        "pergunta": "Uma funçaõ afim é definida pela seguinte lei de formação: y = 4x + 7, qual será seu valor se a imagem for igual a -3",
        "opcoes": ["A) -3", "B) -5", "C) 15", "D) 3"], "resposta": "B"},
    {"pergunta": "O gráfico de uma função do segundo grau é:  ",
     "opcoes": ["A) uma parábula", "B) uma reta", "C) Formado por segmentos de diferentes direções", ],
     "resposta": "A"},
    {"pergunta": " Dada a dizima periódica, qual é sua fração correspondente?",
     "opcoes": ["A) 4/9", "B) 4/90", "C) 4/900", "D) 4/9000"], "resposta": "A"},
    {"pergunta": "O que representa o seno em um triângulo retângulo? ",
     "opcoes": ["A)cateto oposto/hipotenusa", "B)CA/CO", "C)Nenhuma das anteriores"], "resposta": "A"},
    {"pergunta": "Sendo A = {0,11,12,13,14} e B = {11,12}, a intercecção e união das duas é igual:",
     "opcoes": ["A) Intersecção: {0,11,12,13,14}; União: {11,12}", "B)Intersecção e União: {0}",
                "C)Intersecção: {0}; União:{0,11,12,13,14} ",
                "D) Intersecção: {11,12}; União: {0,11,12,13,14}"], "resposta": "D"},
    ]


def texto(msg, pos, tam=30, cor=(0, 0, 0)):
    tela.blit(pygame.font.Font(None, tam).render(msg, True, cor), pos)


def contagem_regressiva():
    for contador in range(3, 0, -1):
        tela.blit(fundo_jogo, (0, 0))
        texto(f"O jogo vai começar em {contador}...", (210, 140), 50, (0, 0, 0))
        pygame.display.update()
        time.sleep(1)


def animacao_bola():
    x, y = 0, 0
    for quadro in quadros_bola:
        tela.blit(fundo_jogo, (0, 0))
        tela.blit(jogador, jogador_rect)
        tela.blit(quadro, (x, y))
        pygame.display.update()
        time.sleep(0.05)


def jogo():
    while True:
        tela.blit(fundo_inicio, (0, 0))
        tela.blit(botao_inicio, botao_rect)
        if any(e.type == MOUSEBUTTONDOWN and botao_rect.collidepoint(e.pos) for e in pygame.event.get() if
               e.type != QUIT):
            contagem_regressiva()
            break
        pygame.display.update()

    indice, pontos, resultado, nivel, acertos_consecutivos, erros_consecutivos = 0, 0, "", 1, 0, 0
    while True:
        if erros_consecutivos >= 5:
            tela.fill((0, 0, 0))
            texto("Fim de Jogo", (300, 50), 50, (255, 0, 0))
            texto("Você cometeu 5 erros seguidos!", (270, 120), 40, (255, 255, 0))
            texto(f"Pontuação final: {pontos}", (250, 100), 40, (255, 255, 0))
            texto(f"Nível alcançado: {nivel}", (220, 80), 40, (255, 255, 0))
            pygame.display.update()
            time.sleep(3)
            return

        if indice >= len(perguntas):
            tela.fill((0, 0, 0))
            texto("Fim de Jogo", (300, 200), 50, (255, 255, 255))
            texto(f"Pontuação final: {pontos}", (270, 260), 40, (255, 255, 0))
            pygame.display.update()
            time.sleep(3)
            return

        tela.blit(fundo_jogo, (0, 0))
        tela.blit(jogador, jogador_rect)
        pygame.draw.rect(tela, (255, 165, 0), (10, 330, 720, 150))
        texto(perguntas[indice]["pergunta"], (20, 340))
        for i, opcao in enumerate(perguntas[indice]["opcoes"]):
            texto(opcao, (20 + i * 150, 400))
        texto(f"Pontos: {pontos}", (540, 20))
        texto(f"Nível: {nivel}", (540, 60))
        texto(resultado, (300, 150), 40, (0, 255, 0) if resultado == "Correto!" else (255, 0, 0))

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit(), exit()
            elif evento.type == KEYDOWN:
                resposta = {K_a: "A", K_b: "B", K_c: "C", K_d: "D"}.get(evento.key)
                if resposta == perguntas[indice]["resposta"]:
                    pontos += 10
                    resultado = "Correto!"
                    acertos_consecutivos += 1
                    erros_consecutivos = 0
                    if acertos_consecutivos == 5:
                        nivel += 1
                        acertos_consecutivos = 0
                    animacao_bola()

                else:
                    resultado = "Incorreto!"
                    acertos_consecutivos = 0
                    erros_consecutivos += 1
                indice = (indice + 1) % len(perguntas)
        pygame.display.update()


jogo()
