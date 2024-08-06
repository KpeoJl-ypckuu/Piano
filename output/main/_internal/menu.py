import pygame
import settings
import pygame.freetype
import sprite
class Menu():
    def __init__(self,game):
        self.fon = pygame.image.load('menu.png')
        self.fon = pygame.transform.scale(self.fon,settings.SIZE)
        self.game = game
        self.shrift = pygame.freetype.Font('шрифт.ttf', 16)
        self.number_song = 1
        self.color_song = [255,0,0]
        self.color_song2 = [255,202,0]
        self.color_song3 = [255,202,0]
    def event(self):
        events = pygame.event.get()
        for save in events:
            if save.type == pygame.QUIT:
                self.game.start1 = 2
            elif save.type == pygame.KEYDOWN:
                if save.key == pygame.K_DOWN:
                    if self.number_song == 1:
                        self.number_song = 2
                        self.color_song = [255,202,0]
                        self.color_song2 = [255,0,0]
                    elif self.number_song == 2:
                        self.number_song = 3
                        self.color_song2 = [255,202,0]
                        self.color_song3 = [255,0,0]
                    elif self.number_song == 3:
                        self.number_song = 1
                        self.color_song = [255,0,0]
                        self.color_song3 = [255,202,0]
                if save.key == pygame.K_UP:
                    if self.number_song == 1:
                        self.number_song = 3
                        self.color_song = [255,202,0]
                        self.color_song3 = [255,0,0]
                    elif self.number_song == 2:
                        self.number_song = 1
                        self.color_song2 = [255,202,0]
                        self.color_song = [255,0,0]
                    elif self.number_song == 3:
                        self.number_song = 2
                        self.color_song2 = [255,0,0]
                        self.color_song3 = [255,202,0]
                if save.key == pygame.K_RETURN:
                    self.game.on_off_menu = 1
                    self.game.song.number_nota = 0
                    self.game.song.notbI = []
                    if self.number_song == 1:
                        self.game.song = sprite.Song(settings.CHRISTMAS_TREE_DURATION,settings.CHRISTMAS_TREE_NOTES)
                    if self.number_song == 2:
                        self.game.song = sprite.Song(settings.BIRCH_DURATION,settings.BIRCH_NOTES)
                    if self.number_song == 3:
                        self.game.song = sprite.Song(settings.MORNING_DURATION,settings.MORNING_NOTES)


    def logic(self):
        pass
    def paint(self):
        self.game.window.blit(self.fon,[0,0])
        self.shrift.render_to(self.game.window,[100,150],'В лесу родилась ёлочка',self.color_song)
        self.shrift.render_to(self.game.window,[100,250],'Берёзка',self.color_song2)
        self.shrift.render_to(self.game.window,[100,350],'Утро',self.color_song3)
        pygame.display.update()
