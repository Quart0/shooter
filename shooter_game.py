#Создай собственный Шутер!

from pygame import *
from random import randint

window = display.set_mode((700,500))
display.set_caption("Синяя бибра Люся 228")

background = transform.scale(image.load("background.png") , (700,500))



clock = time.Clock()
FPS = 60

x1 = 100


font.init()
font1 = font.SysFont('Arial',30)
font2 = font.SysFont('Arial',80)


chet = 0
jizni = 10

finish = False

mixer.init()
mixer.music.load("wahapp.mp3")
mixer.music.set_volume(0.01)
mixer.music.play()



class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect  =self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class pylya(GameSprite):
    def update(self):
        self.rect.y -= self.speed

        if self.rect.y < 0:
            self.kill()
            


class player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
    
        if keys_pressed[K_RIGHT] and self.rect.x < 600:
            self.rect.x += self.speed
    def fire(self):
        bullet = pylya("rename2.png", self.rect.centerx,self.rect.top, 15)
        puli.add(bullet)




            


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(0,700)

#enemys = sprite.group()
#enemys.add.enemy()

TheRealBibra = player("wiber.png",350,370,14) 
vrag1 = Enemy("rename.jpg",150,0,8) 
vrag2 = Enemy("700-nw.jpg",40,0,5) 
vrag3 = Enemy("700-nw.jpg",200,0,5) 
vrag4 = Enemy("hart.png",0,0,12) 

vragi = sprite.Group()
vragi.add(vrag1)
vragi.add(vrag2)
vragi.add(vrag3)
vragi.add(vrag4)

puli = sprite.Group()


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
           if e.key == K_SPACE:
               TheRealBibra.fire()
    
            
            
            
    if finish  !=  True:
        window.blit(background,(0,0))
        TheRealBibra.update()
        TheRealBibra.reset()
        vragi.update()
        puli.update()
        puli.draw(window)
        vragi.draw(window)


        vivod = font1.render('Счет:'  + str(chet),True , (255,255,255))
        window.blit(vivod,(0,0))

        sprite_list = sprite.spritecollide(TheRealBibra,vragi, False)
        for a in sprite_list:
            a.rect.y = 0
            jizni = jizni - 1
        
        jiv = font1.render('Жизни:'  + str(jizni),True , (255,255,255))
        window.blit(jiv,(0,30))

        sprite_list = sprite.groupcollide(vragi,puli, True, True)
        for a in sprite_list:
            
            vrag5 = Enemy("hart.png",0,0,12) 
            vragi.add(vrag5)
            chet = chet+1
        
        if chet > 12:
            finish = True
            jiv = font2.render('ВЫйиграалыьы',True , (77,77,255))
            window.blit(jiv,(200,200))
        if jizni < 1:
            finish = True
            jiv = font2.render('Проиграл(',True , (100,33,88))
            window.blit(jiv,(200,200))

            


    display.update()
    clock.tick(FPS)

   
    
    


