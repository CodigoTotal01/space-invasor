import pygame, random, math

# inicializar pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# titulo e icono
pygame.display.set_caption("Space Invasor")
icono = pygame.image.load('shaders/nave-espacial-tittle.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('shaders\space.png')

# Jugador
img_jugador = pygame.image.load('shaders\\transbordador-espacial.png')
jugador_x = 368
jugador_y = 526
# para el cambio de posicion del personaje
jugador_x_cambio = 0

# varaibles de la vala
img_bala = pygame.image.load('shaders\\bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1
# bala invisible 🏹

bala_visible = False


#Puntaje
puntaje = 0

# Alien
img_enemigo = pygame.image.load('shaders\\ufo.png')
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
# para el cambio de posicion del personaje
enemigo_x_cambio = 0.1
enemigo_y_cambio = 50


def jugador(x, y):
    # blit - arrojar
    pantalla.blit(img_jugador, (x, y))


def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))


def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    return False

# todo lo que ocurra en la ventana de pygame y otras interacciones de juego son "Eventos"
se_ejecuta = True
while se_ejecuta:

    # Background RGB
    # pantalla.fill((205, 144, 228))
    pantalla.blit(fondo, (0, 0))
    # Revisara todos los eventos que exista en pygame
    for evento in pygame.event.get():
        # evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        # evento presionar flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)
        # evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # modificar ubicacion
    jugador_x += jugador_x_cambio

    # mantener nave dentor de los bordes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # modificar ubicacion
    enemigo_x += enemigo_x_cambio

    # mantener nave dentor de los bordes
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.1
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:
        enemigo_x_cambio = -0.1
        enemigo_y += enemigo_y_cambio
    # movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio


    # Colision
    colision = hay_colision(enemigo_x, enemigo_y, bala_x, bala_y)
    if colision:
        bala_y = 500
        bala_visible = False
        puntaje += 1
        print(puntaje)
        enemigo_x = random.randint(0, 736)
        enemigo_y = random.randint(50, 200)

    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)
    # Actualizar la pantalla
    pygame.display.update()
