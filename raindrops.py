#13-3
'''task: make grid of stars that fall down towards the bottom of the screen '''

import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

#-----------------------------Classes---------------
class Settings():
	def __init__(self):
		
		#to do with screen
		self.screen_height=1200
		self.screen_width=800
		self.bg_color=((230,230,230))
		
		#to do with star
		self.star_fall_speed=2
		
class Star(Sprite):
	
	def __init__(self,display,setting):
		super(Star, self).__init__()
		self.display=display
		
		#get the image +the rect 
		self.image=pygame.image.load('star.bmp')
		self.rect=self.image.get_rect()
		
		#set the intiatl cordinates
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height
		
		#decimal position
		self.x=float(self.rect.x)
		self.y=float(self.rect.y)
		
		
	#draw the star
	def draw_stars(self,stars,display):
		stars.draw(display)
	
	#make the star drop 
	def update(self,setting):
		self.y +=setting.star_fall_speed
		self.rect.y =self.y
			
#------------------Game functions ---------------		
def make_display(setting):
	display=pygame.display.set_mode((setting.screen_height,setting.screen_width))
	pygame.display.set_caption(('falling star'))
	display.fill((setting.bg_color))
	return display
	
def check_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
		if event.type == pygame.KEYDOWN:
			if event.key ==pygame.K_q:
				sys.exit()
					
#need to get the number of rows allowed on the screen
def get_rows(display,setting,stars,total_usable):
	#find the screen width avalable 
	star=Star(display,setting)
	usable_room=setting.screen_width-star.rect.width- star.rect.width 
	total_star_room=int( usable_room /(2*star.rect.width))
	
	return total_star_room

def get_columbs(display,setting):
	#get the usable height in the y direction
	star=Star(display,setting)
	total_usable=int((setting.screen_height) / (3*star.rect.height))
	return total_usable
				
def star_grid_code(total_usable,total_star_room,display,stars,setting):
	#loops to make it work 
	for columb in range(total_usable):
		for star_number in range(total_star_room):	
			star=Star(display,setting)
			star.x= star.rect.width + 3*star.rect.width *star_number
			star.y= 2*star.rect.height *columb
			
			#settings the cordinates into x y
			star.rect.x=star.x
			star.rect.y=star.y
			stars.add(star)
			
def update_stars(stars,display,setting):
		star=Star(display,setting)
		stars.update(setting)		

def new_row_stars(display,setting,total_star_room,stars):
	for star_number in range(total_star_room):	
		star=Star(display,setting)
		star.x= star.rect.width + 3*star.rect.width *star_number
		star.rect.x=star.x
		stars.add(star)		
			
			
#-----------------executor section---------
def run_stars():
	setting=Settings()
	
	#make screen
	display=make_display(setting)
	rect=display.get_rect()
	#star class
	star=Star(display,setting)
	stars=Group()
				
	#making the grid of stars appear 
	total_usable = get_columbs(display,setting)
	total_star_room = get_rows(display,setting,stars,total_usable)
	star_grid_code(total_usable,total_star_room,display,stars,setting)

	
	counter =0
	while counter< 10000:
		check_events()
			
		star.draw_stars(stars,display)
		update_stars(stars,display,setting)
	
		#should remove the stars from the group of stars 
		for star in stars.copy():
			if star.rect.top == rect.bottom:
				stars.remove(star)
				new_row_stars(display,setting,total_star_room,stars)
		
		pygame.display.flip()
		counter+=1
		
		
run_stars()
