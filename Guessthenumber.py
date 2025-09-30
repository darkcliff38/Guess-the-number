import pygame
import random

def reiniciar_juego(): 
    global num_secreto, suposicion, intentos, mensaje_texto
    num_secreto = random.randint(1, 100)
    suposicion = ""
    mensaje_texto = "Escribe un número en el teclado"
    intentos = 0
    print("El número secreto es:", num_secreto)

#Crear los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
GRIS = (128, 128, 128)
VERDE = (0, 255, 0)


pygame.init()


fuente_grande = pygame.font.Font(None, 48) #Crea la fuente
fuente_peque = pygame.font.Font(None, 30)

alto_pantalla = 800
ancho_pantalla = 600
pantalla = pygame.display.set_mode((alto_pantalla, ancho_pantalla))
pygame.display.set_caption("Guess the number")


reiniciar_juego()
titulo_juego = "Adivina un número entre 1 y 100."
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r: # Reinicia el juego si se presiona 'R'
                reiniciar_juego()
            elif evento.unicode.isdigit(): # Verifica si es un dígito
                suposicion += evento.unicode
            elif evento.key == pygame.K_BACKSPACE: # Maneja la tecla de retroceso
                suposicion = suposicion[:-1] # Borra el último caracter
            elif evento.key == pygame.K_RETURN: # Maneja la tecla Enter
                try: # Lógica para comparar la suposición con el número secreto
                    intento = int(suposicion)
                    intentos += 1  # Contador de intentos
                    if intento < num_secreto:
                        mensaje_texto  = "El número es más alto."

                    elif intento > num_secreto:
                        mensaje_texto  = "El número es más bajo."

                    else:
                        mensaje_texto = f"¡Correcto! El número era {num_secreto}.\n"
                        mensaje_texto += "Presiona R para jugar de nuevo."                 
                    suposicion = ""           
                except ValueError:
                # Si el usuario no ingresó un número (aunque ya lo filtramos)
                    mensaje_texto  = "Por favor, ingresa un número válido."
                pass


 
    pantalla.fill(GRIS)

    titulo_renderizado = fuente_grande.render(titulo_juego, True, NEGRO)
    pantalla.blit(titulo_renderizado, (50, 50))

    suposicion_renderizada = fuente_peque.render(suposicion, True, NEGRO)
    pantalla.blit(suposicion_renderizada, (50, 100))

    mensaje_renderizado = fuente_peque.render(mensaje_texto, True, NEGRO)
    pantalla.blit(mensaje_renderizado, (50, 150))

    texto_intentos = fuente_peque.render(f"Intentos: {intentos}", True, NEGRO)
    pantalla.blit(texto_intentos, (50, 180))



    pygame.display.flip()
pygame.quit()
