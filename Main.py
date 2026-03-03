import pygame
import random

# 1. Inicialização do Pygame
pygame.init()

# 2. Configurações de Cores (Cores que aparecem na sua tela)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (213, 50, 80)
CINZA = (50, 50, 50)
AZUL = (50, 153, 213)

# 3. Configuração da Tela (Ajustada para o seu celular)
LARGURA, ALTURA = 600, 900 
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Snake Game Jakare')

# 4. Fontes
fonte_ponto = pygame.font.SysFont("arial", 35)
fonte_aviso = pygame.font.SysFont("arial", 50)

def mostrar_texto(msg, cor, x, y, fonte):
    tela.blit(fonte.render(msg, True, cor), [x, y])

def desenhar_botoes():
    # Desenha os botões cinzas de controle que aparecem na sua imagem
    pygame.draw.rect(tela, CINZA, (250, 650, 100, 80)) # Cima
    pygame.draw.rect(tela, CINZA, (250, 750, 100, 80)) # Baixo
    pygame.draw.rect(tela, CINZA, (130, 700, 100, 80)) # Esquerda
    pygame.draw.rect(tela, CINZA, (370, 700, 100, 80)) # Direita

def jogo():
    tamanho = 20
    pontos = 0
    cobra = [[300, 300]]
    direcao = 'CIMA'
    # Comida em posição aleatória
    comida = [random.randrange(0, 29)*20, random.randrange(0, 25)*20]
    relogio = pygame.time.Clock()
    fim_jogo = False

    while True:
        # TELA DE GAME OVER
        while fim_jogo:
            tela.fill(PRETO)
            mostrar_texto("GAME OVER!", VERMELHO, 160, 250, fonte_aviso)
            mostrar_texto(f"Pontos: {pontos}", BRANCO, 230, 320, fonte_ponto)
            mostrar_texto("Toque para Reiniciar", AZUL, 130, 450, fonte_ponto)
            pygame.display.update()
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT: return
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    jogo() # Reinicia o loop
                    return

        # LOGICA DOS CONTROLES TOUCH
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: return
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                # Detecta clique nos botões desenhados
                if 250<mx<350 and 650<my<730 and direcao!='BAIXO': direcao='CIMA'
                elif 250<mx<350 and 750<my<830 and direcao!='CIMA': direcao='BAIXO'
                elif 130<mx<230 and 700<my<780 and direcao!='DIREITA': direcao='ESQUERDA'
                elif 370<mx<470 and 700<my<780 and direcao!='ESQUERDA': direcao='DIREITA'

        # MOVIMENTAÇÃO
        cabeca = list(cobra[0])
        if direcao == 'CIMA': cabeca[1] -= tamanho
        elif direcao == 'BAIXO': cabeca[1] += tamanho
        elif direcao == 'ESQUERDA': cabeca[0] -= tamanho
        elif direcao == 'DIREITA': cabeca[0] += tamanho
        
        cobra.insert(0, cabeca)
        
        # SISTEMA DE PONTOS
        if cabeca == comida:
            pontos += 1
            comida = [random.randrange(0, 29)*20, random.randrange(0, 25)*20]
        else:
            cobra.pop()

        # COLISÕES (Paredes ou próprio corpo)
        if cabeca[0]<0 or cabeca[0]>=LARGURA or cabeca[1]<0 or cabeca[1]>=600 or cabeca in cobra[1:]:
            fim_jogo = True

        # DESENHO DOS ELEMENTOS NA TELA
        tela.fill(PRETO)
        for p in cobra: 
            pygame.draw.rect(tela, VERDE, (p[0], p[1], tamanho, tamanho))
        
        pygame.draw.rect(tela, VERMELHO, (comida[0], comida[1], tamanho, tamanho))
        
        # Linha divisória entre jogo e botões
        pygame.draw.line(tela, BRANCO, (0, 600), (LARGURA, 600), 2)
        
        mostrar_texto(f"PONTOS: {pontos}", BRANCO, 20, 610, fonte_ponto)
        desenhar_botoes()
        
        pygame.display.update()
        relogio.tick(10) # Velocidade do jogo

# Inicia o jogo
jogo()
