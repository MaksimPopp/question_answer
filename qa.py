#Подключение нужных модулей
import pygame
from random import randint

class TextArea():
    def __init__(self,x=0,y=0,width=10,height=10,color=None):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = color
    def set_text(self,text,fsize=12,text_color=(0,0,0)):
        self.text = text
        self.image = pygame.font.Font(None,fsize).render(text,True,text_color)
    def draw(self, shift_x=0,shift_y=0):
        pygame.draw.rect(mw, self.fill_color,self.rect)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


pygame.init()


#создание окна игры
back = (0, 255,255) #цвет фона (background)
mw = pygame.display.set_mode((500, 500)) #окно программы (main window)
mw.fill(back)


quest_card = TextArea(120, 100, 290, 70, (200,200,255))
quest_card.set_text("Вопрос", 75)


ans_card = TextArea(120, 240, 290, 70, (200,200,255))
ans_card.set_text("Ответ", 75)



quest_card.draw(10,10)
ans_card.draw(10,10)


clock = pygame.time.Clock()
while True:
    pygame.display.update()
    for event in pygame.event.get():
       if event.type == pygame.KEYDOWN:


           if event.key == pygame.K_q:
               num = randint(1,3)
               if num == 1:
                   quest_card.set_text('Что изучаешь в Алгоритмике?', 25)
               if num == 2:
                   quest_card.set_text('На каком языке говорят во Франции?', 25)
               if num == 3:
                   quest_card.set_text('Что растёт на яблоне?', 35)      


               quest_card.draw(10,25)


           if event.key == pygame.K_a:
               num = randint(1,3)
               if num == 1:
                   ans_card.set_text('Python', 35)
               if num == 2:
                   ans_card.set_text('Французский', 35)
               if num == 3:
                   ans_card.set_text('Яблоки', 35)      


               ans_card.draw(10, 25)
    clock.tick(40)