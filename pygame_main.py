import pygame
import main as fn
from colors import colors


def end(screen,font):
    ''' Shows when a player has lost the game.'''
    pygame.draw.rect(screen, (234, 149, 210), pygame.Rect(0, 0, 500, 500), border_bottom_left_radius=8,
                     border_bottom_right_radius=8)

    end_surf = font.render('You Lose :( ', False, (0, 0, 0))
    screen.blit(end_surf, (10, 500))

    score_surf = font.render('Your total score is:{}'.format(fn.score), False, (0, 0, 0))
    screen.blit(score_surf, (10, 640))

    try_surf = font.render(f'Try Again? Press R', False, (0, 0, 0))
    screen.blit(try_surf, (20, 100))

    quit_surf = font.render(f'Or Press Q to Quit', False, (0, 0, 0))
    screen.blit(quit_surf, (20, 140))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    return False



def win(screen,font):
    ''' Shows when a player has won'''

    pygame.draw.rect(screen, (234, 149, 210), pygame.Rect(0, 0, 500, 500), border_bottom_left_radius=8,
                     border_bottom_right_radius=8)

    end_surf = font.render('You Win :) ', False, (0, 0, 0))
    screen.blit(end_surf, (10, 500))

    score_surf = font.render('Your total score is:{}'.format(fn.score), False, (0, 0, 0))
    screen.blit(score_surf, (10, 640))

    try_surf = font.render(f'Keep going? Press R', False, (0, 0, 0))
    screen.blit(try_surf, (20, 100))

    quit_surf = font.render(f'Or Press Q to Quit', False, (0, 0, 0))
    screen.blit(quit_surf, (20, 140))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                elif event.key == pygame.K_q:
                    return False


def player_turn(gb):
    ''' Allows the player to move tiles.'''

    global score
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    gb = fn.move_up(gb)
                    return gb
                elif event.key == pygame.K_DOWN:
                    gb = fn.move_down(gb)
                    return gb
                elif event.key == pygame.K_LEFT:
                    gb = fn.move_left(gb)
                    return gb
                elif event.key == pygame.K_RIGHT:
                    gb = fn.move_right(gb)
                    return gb


def main(gameboard):
    ''' Causes the game to run and ends it when the requirements are met'''

    pygame.init()
    pygame.font.init()
    running = True
    HEIGHT = 700
    WIDTH = 500
    pygame.display.set_caption("Yennie-48")
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    font = pygame.font.SysFont('Comic Sans', 30)
    screen.fill((227, 208, 226))
    two_win = False

    first_move = fn.random_token(gameboard)
    gameboard[first_move['row']][first_move['cell']] = first_move['value']
    while running:
        screen.fill((227, 208, 226))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if fn.win(gameboard):
            if two_win:
                pass
            else:
                final = win(screen, font)
                if final:
                    two_win = True
                    screen.fill((227, 208, 226))
                else:
                    return final
        if fn.game_over(gameboard):
            final = end(screen,font)
            return final

        ai_move = fn.random_token(gameboard)
        if ai_move == True:
            if fn.win(gameboard):
                if two_win:
                    pass
                else:
                    final = win(screen, font)
                    if final:
                        two_win = True
                        screen.fill((227, 208, 226))
                    else:
                        return final
            if fn.game_over(gameboard):
                final = end(screen,font)
                return final
        else:
            gameboard[ai_move['row']][ai_move['cell']] = ai_move['value']


        print_cells(screen, gameboard, font)

        pygame.display.update()
        move = player_turn(gameboard)
        if move == False:
            break
        gameboard = move
    return


def print_cells(surface,gb,font):
    ''' Prints all the tiles and score onto the board'''

    pygame.draw.rect(surface, (234,149,210), pygame.Rect(0,0,500,500), border_bottom_left_radius= 8, border_bottom_right_radius= 8)
    score_surf = font.render(f'Score: {fn.score}', False, (0, 0, 0))
    title_surf = font.render(f'2048', False, (0, 0, 0))

    surface.blit(title_surf, (0, 600))
    surface.blit(score_surf, (0,500))

    for i in range(4):
        for j in range(4):
            x = j * 500 // 4 + 10
            y = i * 500 // 4 + 10
            w = 500 // 4 - 2 * 10
            h = 500 // 4 - 2 * 10

            pygame.draw.rect(surface, colors[str(gb[i][j])], pygame.Rect(x,y,w,h), border_radius = 8)
            if gb[i][j] != 0:
                text_surf = font.render(str(gb[i][j]), False, (0,0,0))
                textangle = text_surf.get_rect(center = (x + w/2, y + h/2))

                surface.blit(text_surf, textangle)

if __name__ == '__main__':
    score = 0
    gameboard = fn.GB()
    while True:
        fn.score = 0
        x = main(gameboard.gb)
        if x:
            gameboard.clear()
            pass
        else:
            break
    pygame.quit