import pygame
import os
from player import Player
from projectTile import ProjectTile
from bot import Bot

class Main:
    def run(self):

        pygame.init()

        width = 500
        height = 480

        window = pygame.display.set_mode((width, height))

        pygame.display.set_caption("Pygon Ball")

        background = pygame.image.load(os.path.join('images/','background.jpg'))

        pygame.mixer.music.load('music.mp3')
        pygame.mixer.music.play(0)

        clock = pygame.time.Clock()

        score = 10

        def redrawGameWindow():
            
            global walkCount

            text = font.render('Score: ' + str(score), 1, (0, 0, 0))
            window.blit(text, (390, 10))
            player.draw(window)
            bot.draw(window)
            
            for bullet in bullets:
                bullet.draw(window)
                
            pygame.display.update()

        def showResult(text):
            fontGameOver = pygame.font.SysFont('comicsans', 70)
            fontPlayAgain = pygame.font.SysFont('comicsans', 25)
            textGameOver = fontGameOver.render(text, 1, (255, 0, 0))
            textPlayAgain = fontPlayAgain.render('Jogar novamente!', 1, (255, 0, 0))
            window.blit(textGameOver, (250 - (textGameOver.get_width() / 2), 200))
            window.blit(textPlayAgain, (250 - (textPlayAgain.get_width() / 2), 325))
            
            player.y = 800
            player.x = 800
            bot.x = 750
            bot.y = 750
                
            pygame.mixer.music.stop()

            posMouse = pygame.mouse.get_pos()
            pressedMouse = pygame.mouse.get_pressed()

            if posMouse[1] >= 327 and posMouse[1] <= 338 and posMouse[0] >= 181 and posMouse[0] <= 321:
                if pressedMouse[0]:
                    Main().run()

        font = pygame.font.SysFont('comicsans', 30, True)
        player = Player(320, 434, 64, 64)
        bot = Bot(10, 442, 64, 64, 480)
        shootLoop = 0

        bullets = []
        run = True
        x = 0

        while run:

            #Scrolling Background
            rel_x = x % background.get_rect().width
            window.blit(background, (rel_x - background.get_rect().width, 0))
            if rel_x < width:
                window.blit(background, (rel_x, 0))
            x -= 1
            
            clock.tick(27)

            if player.hitbox[1] < bot.hitbox[1] + bot.hitbox[3] and player.hitbox[1] + player.hitbox[3] > bot.hitbox[1]:
                if player.hitbox[0] + player.hitbox[2] > bot.hitbox[0] and player.hitbox[0] < bot.hitbox[0] + bot.hitbox[2]:
                    player.hit(window)
                    pygame.display.update()
                    score -= 1

            if shootLoop > 0:
                shootLoop += 1
            if shootLoop > 2:
                shootLoop = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            for bullet in bullets:
                if bullet.y - bullet.radius < bot.hitbox[1] + bot.hitbox[3] and bullet.y + bullet.radius > bot.hitbox[1]:
                    if bullet.x + bullet.radius > bot.hitbox[0] and bullet.x - bullet.radius < bot.hitbox[0] + bot.hitbox[2]:
                        if bot.health >= 8 and bot.health <= 10:
                            bot.vel = 10
                          
                        elif bot.health >= 5 and bot.health <= 6:
                            bot.vel = 15
                           
                        elif bot.health >= 2.4 and bot.health <= 3:
                            bot.vel = 20
                        else:
                            bot.vel = 30
                           
                        bot.hit()
                        pygame.display.update()
                        if bot.visible == False:
                            score += 1
              
                        bullets.pop(bullets.index(bullet))
                if bullet.x < 500 and bullet.x > 0:
                    bullet.x += bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))
            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LCTRL] and shootLoop == 0:
                if player.left:
                    facing = -1
                else:
                    facing = 1
                    
                if len(bullets) < 3:
                    bullets.append(ProjectTile(round(player.x+2),
                                               round(player.y + player.height // 5),
                                               15, (0,0,0), facing))
                shootLoop = 1

            if keys[pygame.K_LEFT] and player.x > player.vel:
                player.x -= player.vel
                player.left = True
                player.right = False
            
            elif keys[pygame.K_RIGHT] and player.x < 500 - player.width - player.vel:
                player.x += player.vel
                player.right = True
                player.left = False
                
            else:
                player.walkCount = 0
                
            if not(player.isJump):
                
                if keys[pygame.K_SPACE]:
                    player.isJump = True
                    player.walkCount = 0
            else:
                if player.jumpCount >= -10:
                    neg = 1
                    if player.jumpCount < 0:
                        neg = -1
                    player.y -= (player.jumpCount ** 2) * 0.5 * neg
                    player.jumpCount -= 1
                else:
                    player.isJump = False
                    player.jumpCount = 10
                    
            if score < 0:
                showResult("GAME OVER!")
            else:
                if bot.visible == False:
                    showResult("VOCÊ VENCEU!")

            redrawGameWindow()

        pygame.quit()

if __name__ == '__main__':
    Main().run()
            
