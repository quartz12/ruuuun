
import pygame
import random
import os
from pygame.locals import *
import sys


game_flo=os.path.dirname(__file__)

def load(name, r):
	img_flo=os.path.join(game_flo, 'img')
	img=pygame.image.load(os.path.join(img_flo, name))
	x = pygame.transform.scale(img, (round(int(img.get_width())*r), round(int(img.get_height())*r)))
	return x
pygame.mixer.init()
def load_m(name, n):
	m_dir = os.path.join(game_flo, 'Music')
	shoot_sound = pygame.mixer.Sound(os.path.join(m_dir, name))
	pygame.mixer.music.set_volume(n)
	return shoot_sound

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)



img_plyer=[load('p3_walk01.png', 2), load('p3_walk02.png', 2), load('p3_walk03.png', 2), load('p3_walk04.png', 2), load('p3_walk05.png',2), load('p3_walk06.png', 2), load('p3_walk07.png', 2), load('p3_walk08.png', 2), load('p3_walk09.png', 2), load('p3_walk10.png',2), load('p3_walk11.png', 2)]
img_kill=load('ladder_mid.png', 2)
img_kill2=load('spikes.png', 2)
img_kill3=load('signRight.png', 2)
img_start=load('1613552696852.png', 1)
img_start1=load('1613554635848.png', 1)
img_o=load('cloud3.png', 2)
img_coinG=load('coinGold.png', 2)
img_coinS=load('coinSilver.png', 2)
img_button=load('Button.png', 1)
img_button_press=load('Button_press.png', 1)
k=img_button
img_setting=load('Setting.png', 0.2)
img_shop=load('Shop.png', 0.4)
img_music=load('Music.png', 0.2)
img_music_off=load('Music_off.png', 0.2)
imd_grass=load('grass.png', 4)
img_shapka_santy=load('shapka-santy.png', 0.5)
skin_shapkasanty=load('shapka-santy.png', 2)
m_coin=load_m('coins.ogg', 0.5)
m_jump=load_m('jump.ogg', 1)
m_gameover=load_m('game_ower.ogg', 0.5)
m_button=load_m('button.ogg', 0.1)
m_start=load_m('start.ogg', 0.5)
m_menu=load_m('menu.ogg', 0.2)

WIDTH = 1000
HEIGHT = 2000
WIDTH_1=int(WIDTH/2)-100
HEIGHT_1=int(HEIGHT/2)
FPS = 60
jump=17
j=False
menu=True
running=False
tt=True
hh=1400
ko=img_start
v=True
u=2
coin=0
try:
	with open("save.txt", "r") as fi:
		coin = int(fi.readline())
except:
	with open("save.txt", "w") as fi:
		file.write("0")
set_menu=False
shop_menu=False
anim=0
MUSIC=True
m=img_music
m_z=True
m_v=False
x=1400
p=0
x1=2200
p1=0
get_grass=0
i=img_start1
all_grass_clon=[1500, 1220, 940, 660, 420, 180, -60]

#цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (100, 255, 100)
BLUE = (200, 200, 255)

def GetGlass ():
	global all_grass_clon
	global get_grass
	get_grass+=1
	if get_grass>=14:
		all_grass_clon.append(1500)
		get_grass=0

#классы
class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=img_plyer[0]
		self.rect=self.image.get_rect()
		self.rect.center=(300, HEIGHT_1)
	def update(self):
		global anim
		self.rect.x=WIDTH_1
		self.rect.y=HEIGHT_1
		if anim+2>30:
			anim=0
		if j!=True:
			self.image=img_plyer[anim // 3]
			anim +=1
		else:
			self.image=img_plyer[0]
			#anim=0

class Kill(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = img_kill
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center=(1400, 1100)
	def update(self):
		all_coin.update()
		global hh
		self.rect.x=hh
		hh-=20
		if self.rect.left<=-140:
			hh=1000+random.randint(100, 200)
			a=random.randint(1, 3)
			if a==1:
				self.image=img_kill
			elif a==2:
				self.image=img_kill2
			elif a==3:
				self.image=img_kill3
		
class Coin(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=img_coinG
		self.rect=self.image.get_rect()
		self.rect.center=(-20, 1100)
	def update(self):
			self.rect.x-=20
			if self.rect.x<10:
				global u
				u=random.randint(1, 2)
				self.rect.x=1800
			if u!=1:
					self.rect.y=HEIGHT+1000
			else:
					self.rect.y=1000

class Grass(pygame.sprite.Sprite):
				def __init__(self):
					pygame.sprite.Sprite.__init__(self)
					self.image=imd_grass
					self.rect=self.image.get_rect()
					self.add(grass_clon)
					self.rect.center=(1400, 1300)
				def update(self):
					self.rect.x-=20
					if self.rect.x==-100:
						self.kill()
				
#окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Run")
clock = pygame.time.Clock()
all_spritr=pygame.sprite.Group()
plyer=Player()
all_spritr.add(plyer)
all_kill=pygame.sprite.Group()
kill=Kill()
all_kill.add(kill)
c=Coin()
all_coin=pygame.sprite.Group()
all_coin.add(c)
m_menu.play(loops=-1)
grass_clon=pygame.sprite.Group()
grass=Grass()

# Цикл игры
while tt:
	
	while menu:
		clock.tick(FPS)
		start=pygame.Rect(300, 1000, 500, 200)
		set_rect=img_setting.get_rect(bottomright=(1050, 250))
		shop_rect=img_setting.get_rect(bottomright=(200, 250))
		for event in pygame.event.get():
	 	        	 if event.type == pygame.QUIT:
	 	        	 	tt = False
	 	        	 if event.type==pygame.	MOUSEBUTTONDOWN:
	 	        	 	mouse_pos=event.pos
	 	        	 	if dog_rect.collidepoint(mouse_pos):
	 	        	 		if MUSIC:
	 	        	 		 m_start.play()
	 	        	 		ko=img_start1
	 	        	 		menu=False
	 	        	 		running=True
	 	        	 	if set_rect.collidepoint(mouse_pos):
	 	        	 		if MUSIC:
	 	        	 		 m_button.play()
	 	        	 		menu=False
	 	        	 		set_menu=True
	 	        	 	if shop_rect.collidepoint(mouse_pos):
	 	        	 		if MUSIC:
	 	        	 		 m_button.play()
	 	        	 		menu=False
	 	        	 		shop_menu=True
		screen.fill(GREEN)
		dog_rect = ko.get_rect(bottomright=(800, 1000))
		screen.blit(img_shop, shop_rect)
		screen.blit(img_setting, set_rect)
		screen.blit(ko, dog_rect)
		pygame.display.flip()
	
	while set_menu:
		clock.tick(FPS)
		if m_z:
			m_menu.play(loops=-1)
			m_z=False
		if m_v:
			m_menu.stop()
			m_v=False
		set_rect=img_setting.get_rect(bottomright=(1050, 250))
		button_music=m.get_rect(bottomright=(250, 250))
		if MUSIC==False:
			m=img_music_off
		else:
			m=img_music
		for event in pygame.event.get():
	 	        	 if event.type == pygame.QUIT:
	 	        	 	tt = False
	 	        	 if event.type==pygame.	MOUSEBUTTONDOWN:
	 	        	 	mouse_pos=event.pos
	 	        	 	if set_rect.collidepoint(mouse_pos):
	 	        	 		if MUSIC:
	 	        	 		 m_button.play()
	 	        	 		set_menu=False
	 	        	 		menu=True
	 	        	 	if button_music.collidepoint(mouse_pos):
	 	        	 		if MUSIC==False:
	 	        	 			m_z=True
	 	        	 			m_button.play()
	 	        	 			MUSIC=True
	 	        	 		else:
	 	        	 			m_v=True
	 	        	 			MUSIC=False
		screen.fill(GREEN)
		screen.blit(m, button_music)
		screen.blit(img_setting, set_rect)
		pygame.display.flip()
		
	while shop_menu:
		clock.tick(FPS)
		shop_rect=img_setting.get_rect(bottomright=(200, 250))
		for event in pygame.event.get():
			if event.type==pygame.MOUSEBUTTONDOWN:
				mouse_pos=event.pos
				if shop_rect.collidepoint(mouse_pos):
				       	 		if MUSIC:
				       	 			m_button.play()
				       	 		menu=True
				       	 		shop_menu=False
		screen.fill(GREEN)
		screen.blit(img_shop, shop_rect)
		pygame.display.flip()
		
		
	while running:
	 	   clock.tick(FPS)
	 	   GetGlass()
	 	   x-=5
	 	   if x<-100:
	 	   	p=random.randint(-400, 500)
	 	   	x=1400
	 	   x1-=5
	 	   if x<-100:
	 	   	p1=random.randint(-400, 500)
	 	   	x1=1400
	 	   obl=img_o.get_rect(bottomright=(x, 500+p))
	 	   obl1=img_o.get_rect(bottomright=(x1, 500+p1))
	 	   button=k.get_rect(bottomright=(700, 1900))
	 	   y=500+random.randint(-500, 500)
	 	   
	 	   for event in pygame.event.get():
	 	        	 if event.type == pygame.QUIT:
	 	        	 	tt = False
	 	        	 if event.type==MOUSEBUTTONDOWN:
	 	        	 	mouse_po=(mouse_pos)
	 	        	 if pygame.mouse.get_pressed()[0] and button.collidepoint(pygame.mouse.get_pos()):
	 	        	 		k=img_button_press
	 	        	 		j=True
	 	        	 else:
	 	        	 	k=img_button
	 	   if j==True:
	 	        	 		if jump==17:
	 	        	 			if MUSIC:
	 	        	 				m_jump.play()
	 	        	 		if jump>-18:
	 	        	 				if jump<=0:
	 	        	 					HEIGHT_1+=(jump**2)/5
	 	        	 					jump-=1
	 	        	 				else:
	 	        	 					HEIGHT_1-=(jump**2)/5
	 	        	 					jump-=1
	 	        	 		else:
	 	        	 			jump=17
	 	        	 			j=False
	 	   this=pygame.sprite.spritecollide(plyer, 		all_kill, False)
	 	   if this:
	 	     					if MUSIC:
	 	     						m_gameover.play()
	 	     					menu=True
	 	     					running=False
	 	     					hh=1400
	 	     					i=img_start
	 	   cc=pygame.sprite.spritecollide(plyer, all_coin, False)
	 	   if cc:
	 	   	if MUSIC:
	 	   		m_coin.play()
	 	   	u=5
	 	   	coin+=1
	 	   	with open("save.txt", "w") as file:
	 	   		file.write(str(coin))
	 	   for b in range(len(all_grass_clon)):
	 	   	all_grass_clon[b] -= 20
	 	   for bullet in all_grass_clon:
	 	     if bullet < -600:
	 	     	all_grass_clon.remove(bullet)
	 	   grass_clon.update()
	 	   all_kill.update()
	 	   all_spritr.update()
	 	   screen.fill(BLUE)
	 	   pygame.draw.rect(screen, (96, 115, 114), (0, 1300, 1100, 2300))
	 	   screen.blit(img_o, obl)
	 	   screen.blit(img_o, obl1)
	 	   for clon in all_grass_clon:
	 	   	screen.blit(imd_grass, pygame.Rect(clon, 1150, 0, 0))
	 	   
	 	   draw_text(screen, str(coin)+'coins', 100, 200, 10)
	 	   
	 	   screen.blit(k, button)
	 	   all_coin.draw(screen)
	 	   all_kill.draw(screen)
	 	   all_spritr.draw(screen)
	 	   pygame.display.flip()