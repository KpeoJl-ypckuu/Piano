import time
import settings
import pygame 
import random
import sprite
import menu
import pygame.freetype

pygame.init()
pygame.mixer.init(channels=4)


class Game():
    def __init__(self):
        self.start1 = 1
        self.on_off_menu = 2
        self.window = pygame.display.set_mode(settings.SIZE)
        self.pm = pygame.time.Clock()
        self.song = sprite.Song(settings.MORNING_DURATION,settings.MORNING_NOTES)
        self.menu = menu.Menu(self)
        self.game_over = False
        self.shrift = pygame.freetype.Font('шрифт.ttf', 16)
    def paint(self):
        self.window.fill([255,255,255])
        stolb = 0
        while stolb < settings.LINES:
            pygame.draw.line(self.window,[0,0,0],[settings.SHIRINA_LINES * stolb,0],[settings.SHIRINA_LINES * stolb,600])
            stolb = stolb + 1
        if self.game_over == False:
            self.song.paint(self.window)
        else:
            self.shrift.render_to(self.window,[100,150],'Вы проиграли !')
        if self.song.number_nota == len(self.song.names) and self.song.notbl[-1].rect.top > settings.SIZE[1]:
            self.shrift.render_to(self.window,[100,150],'Вы победили !')
        pygame.display.update()
    def logic(self):
        self.song.controller()
        self.song.spawn_not()
        for save_nota in self.song.notbl:
            if save_nota.rect.y > 600 and save_nota.pressed == 0:
                self.game_over = True
    def event(self):
        events = pygame.event.get()
        for save in events:
            if save.type == pygame.QUIT:
                self.start1 = 2
            if save.type == pygame.MOUSEBUTTONDOWN:
                for save_nota in self.song.notbl:
                    if save_nota.rect.collidepoint(save.pos):
                        true_or_false = self.song.pressure_nota(save_nota.number)
                        if true_or_false == True:
                            print('всё норм')
                        else:
                            print('что то не так')
                            self.game_over = True
                        save_nota.click()
                        print(save_nota.name)
            if save.type == pygame.KEYDOWN:
                if save.key == pygame.K_RETURN:
                    self.on_off_menu = 2
                    self.game_over = False 
            
                
    def start(self):
        while self.start1 == 1:
            if self.on_off_menu == 1:
                self.paint()
                self.logic()
                self.event()
            else:
                self.menu.paint()
                self.menu.logic()
                self.menu.event()
            self.pm.tick(100)
game = Game()
game.start()




