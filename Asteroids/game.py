import pygame
from menu import *
from player import *
from ctypes import windll

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        #self.DISPLAY_W, self.DISPLAY_H = 1920, 1080
        #self.DISPLAY_W, self.DISPLAY_H = 1080, 720
        #self.DISPLAY_W, self.DISPLAY_H = 480, 360
        #self.DISPLAY_W, self.DISPLAY_H = 240, 180
        self.user32 = windll.user32
        self.DISPLAY_W, self.DISPLAY_H = self.user32.GetSystemMetrics(0), self.user32.GetSystemMetrics(1)
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        pygame.display.set_caption("Asteroids")
        #pygame.window.set_icon(self.icon_image)
        self.font_name = 'Century Gothic'
        self.BLACK, self.WHITE = (15, 15, 15), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)

        self.game_loop()

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.BACK_KEY:
                self.playing = False
            self.update()
            self.draw()
            
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
    
    def update(self):
        # Game loop - Update
        self.all_sprites.update()
    
    def draw(self):
        self.display.fill(self.BLACK)
        self.all_sprites.draw(self.display)

    def draw_text(self, text, size, x, y ):
        font = pygame.font.SysFont(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)