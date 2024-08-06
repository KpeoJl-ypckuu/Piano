import pygame 
import settings
import random
nota1 = pygame.image.load('long_tile_pressed.png')
nota1 = pygame.transform.scale(nota1,[settings.SHIRINA_LINES,280])
nota2 = pygame.image.load('long_tile.png')
nota2 = pygame.transform.scale(nota2,[settings.SHIRINA_LINES,280])
nota3 = pygame.image.load('short_tile_pressed.png')
nota3 = pygame.transform.scale(nota3,[settings.SHIRINA_LINES,200])
nota4 = pygame.image.load('short_tile.png')
nota4 = pygame.transform.scale(nota4,[settings.SHIRINA_LINES,200])


class Nota():
    def __init__(self,dlitelnost,name,number):
        self.name = name
        self.dlitelnost = dlitelnost
        if dlitelnost == 1:
            self.pic = nota4
        elif dlitelnost == 2:
            self.pic = nota2 
        self.dlina = self.pic.get_width()
        self.shirina = self.pic.get_height()
        self.rect = pygame.rect.Rect([settings.SHIRINA_LINES * random.randint(0,settings.LINES -1),-200],[self.dlina,self.shirina])
        self.speedY = 5
        self.sound = pygame.mixer.Sound('Sounds/' + name + '.ogg')
        self.sound.set_volume(0.1)
        self.pressed = 0
        self.number = number
    def controller(self):
        self.rect.y = self.rect.y + self.speedY
    def paint(self,window):
        window.blit(self.pic, self.rect)
    def click(self):
        if self.pic == nota2:
            self.pic = nota1
        if self.pic == nota4:
            self.pic = nota3
        channel = pygame.mixer.find_channel()
        if channel != None:
            channel.queue(self.sound)
        else:
            pygame.mixer.stop()
        self.sound.play()
        self.pressed = 1

    

class Song():
    def __init__(self,dlitelnosty,names):
        self.dlitelnosty = dlitelnosty
        self.names = names
        self.notbl = []  
        self.clock = 0
        self.clock_moment_spawn = 0 
        self.number_nota = 0
    def spawn_not(self):
        self.clock = pygame.time.get_ticks()
        if self.clock - self.clock_moment_spawn >= 500 and self.number_nota < len(self.names):
            self.clock_moment_spawn = pygame.time.get_ticks()
            nota = Nota(self.dlitelnosty[self.number_nota],self.names[self.number_nota],self.number_nota)
            self.number_nota = self.number_nota + 1
            self.notbl.append(nota)
    def paint(self,window):
        for save in self.notbl:
            save.paint(window)
    def controller(self):
        for save in self.notbl:
            save.controller()
    def pressure_nota(self,number_pressed_nota):
        notbI_no_pressed = self.notbl[0:number_pressed_nota]
        notbI_amount_pressed = 0
        amount_notbI_no_pressed = len(notbI_no_pressed)
        for nota in notbI_no_pressed:
            if nota.pressed == 0:
                return False
            if nota.pressed == 1:
                notbI_amount_pressed = notbI_amount_pressed + 1
        if amount_notbI_no_pressed == notbI_amount_pressed:
            return True
            
                
        
            


    
            