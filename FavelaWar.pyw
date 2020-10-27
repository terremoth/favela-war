import pygame
import sys
import time
from PIL import Image
import os

pygame.mixer.pre_init()
pygame.mixer.init(buffer=2048)
pygame.mixer.set_num_channels(50)
this_path = os.path.dirname(os.path.realpath(__file__));
LOOP_SOUND_FOREVER = -1
pygame.init()
pygame.display.init()
pygame.display.set_caption('Favela War')

def make_sprite(filename, posX, posY, width, height):
	sprite_file_with_location = os.path.join(this_path, "sprites", filename)
	open_file = Image.open(sprite_file_with_location)
	crop_rectangle = (posX, posY, width, height)
	cropped_im = open_file.crop(crop_rectangle)
	
	mode = cropped_im.mode
	size = cropped_im.size
	data = cropped_im.tobytes()

	rendered_img = pygame.image.fromstring(data, size, mode)
	return rendered_img

def get_audio_file (filename):
	return os.path.join(this_path, "audio", filename)
	 
scenario = os.path.join(this_path, "", "favela.jpg")
img = Image.open(scenario)
width, height = img.size

# Load sounds
shot_sound 		= get_audio_file('shot.wav')
ambient_sound 	= get_audio_file('ambient.wav')
cops 			= get_audio_file('cops.wav')
shell_falling 	= get_audio_file('shell_falling.wav')

gun1 = make_sprite("pistola.png", 0,0,135,135)


	
screen = pygame.display.set_mode((width, height))
bg = pygame.image.load(scenario)

pygame.mouse.set_visible(0)


pygame.mixer.find_channel().play(pygame.mixer.Sound(ambient_sound), loops = LOOP_SOUND_FOREVER)
pygame.mixer.find_channel().play(pygame.mixer.Sound(cops), loops = LOOP_SOUND_FOREVER)

gun_position_adjust_to_center_mouse_x = 30
gun_position_adjust_to_center_mouse_y = 10

while True:
	screen.blit(bg,(0,0))
	mx, my = pygame.mouse.get_pos()
	gun_position_x = mx - gun_position_adjust_to_center_mouse_x
	gun_position_y = my - gun_position_adjust_to_center_mouse_y
	screen.blit(gun1, (gun_position_x, gun_position_y))
				
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif ev.type == pygame.MOUSEBUTTONDOWN:
			if ev.button == 1:
				channel = pygame.mixer.find_channel()
				channel.play(pygame.mixer.Sound(shot_sound), maxtime=1350)
				channel.queue(pygame.mixer.Sound(shell_falling))			
	time.sleep(0.01)
	pygame.display.update()
