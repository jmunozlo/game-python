import pygame


# Colores
azul = (0, 0, 150)
blanco = (255, 255, 255)

# pantalla
pantalla_tamano = (800, 600)


pantalla = pygame.display.set_mode(pantalla_tamano)
reloj = pygame.time.Clock()


Termino = False

y = 200
velocidad = 0
parado = []
parado.append(pygame.image.load('parado1.png'))
parado.append(pygame.image.load('parado2.png'))
parado.append(pygame.image.load('parado3.png'))

ataque = []

ataque.append(pygame.image.load('ataque1.png'))
ataque.append(pygame.image.load('ataque2.png'))
ataque.append(pygame.image.load('ataque3.png'))

for imagen in parado:
    imagen.set_colorkey((255, 255, 255))

for imagen in ataque:
    imagen.set_colorkey((255, 255, 255))

estado = 0

cuadro_actual = 0
while not Termino:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Termino = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                velocidad = -8
            if event.key == pygame.K_DOWN:
                velocidad = 8
            if event.key == pygame.K_SPACE and estado == 0:
                cuadro_actual =0
                estado = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                velocidad = 0
            if event.key == pygame.K_DOWN:
                velocidad = 0

    # actualizacion
    cuadro_actual += 0.1
    if estado == 0:
        if cuadro_actual > 2:
            cuadro_actual = 0
    if estado == 1:
        if cuadro_actual > 1:
            cuadro_actual = 0
            estado = 0
    pantalla.fill(azul)
    y += velocidad
    if y > 500:
        y = 500
    if y < 0:
        y = 0
    # Dibujos
    if estado == 0:
        pantalla.blit(parado[int(cuadro_actual)], (50, y))
    else:
        pantalla.blit(ataque[int(cuadro_actual)], (50, y))
    pygame.display.flip()
    reloj.tick(60)
