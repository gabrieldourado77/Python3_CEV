
# Não consegui fazer o pygame funcionar.

import pygame

pygame.mixer.init()
pygame.mixer.music.load('C:\\Users\\gabri\\Documents\\PythonMP3\\Respirar.mp3')
pygame.mixer.music.play()

e = 'Tocando um MP3'

print('='*45)
print('{:^45}'.format(e))
print('='*45)

print('Canção: Respirar (Playback)\nBanda: Diante do Trono')
print('Álbum: DT 20 - Respirar')
print('='*60)

