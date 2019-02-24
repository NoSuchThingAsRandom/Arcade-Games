import random
import time
import pygame


def play(increase_speed):
    # Colours
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # Dimensions
    rows = 25
    columns = 25
    cell_width = 20
    cell_height = 20
    offset_height = 0.1
    offset_width = 0.05
    width = int(columns * cell_width * (1 + offset_width))
    height = int(rows * cell_height * (1 + offset_height))
    size = (width, height)

    grid = [x[:] for x in [[""] * columns] * rows]

    # Snake
    length = 1
    bearing = "N"
    preserve_tail = False
    headx = int(columns / 2)
    heady = int(rows / 2)
    tailx = int(columns / 2)
    taily = int(rows / 2)
    grid[headx][heady] = "H"

    # Food
    foodx = random.randint(0, rows - 1)
    foody = random.randint(0, columns - 1)
    grid[foodx][foody] = "F"

    # User Options
    """
    print("Please select your difficulty:")
    print("Easy (E)")
    print("Medium (M)")
    print("Hard (H)")
    diff = "M"
    if diff == "E":
        speed = 1
    elif diff == "M":
        speed = 5
    elif diff == "H":
        speed = 10
    else:
        speed = 5
    """
    if increase_speed:
        speed=5
    else:
        speed = 10

    # Scoring
    score = 0
    previous_time = time.time()

    # Pygame Setup
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 15)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Snake")
    finished = False
    clock = pygame.time.Clock()
    start = time.time()
    start_game = False
    while not finished:
        # User Input
        while not start_game:
            text_start = font.render(
                "Press any key to start", False, RED)
            screen.blit(text_start, (int(width * 0.5 * offset_width), 0))
            pygame.draw.rect(screen, WHITE, [int(width * 0.5 * offset_width), int(
                height * 0.5 * offset_height), (columns * cell_width), (rows * cell_height)])
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    start_game = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bearing = "N"
                if event.key == pygame.K_DOWN:
                    bearing = "S"
                if event.key == pygame.K_LEFT:
                    bearing = "W"
                if event.key == pygame.K_RIGHT:
                    bearing = "E"

        # GRID
        # Moves head
        grid[headx][heady] = bearing
        if bearing == "N":
            heady -= 1
        elif bearing == "E":
            headx += 1
        elif bearing == "S":
            heady += 1
        elif bearing == "W":
            headx -= 1
        if headx >= rows or headx < 0 or heady >= columns or heady < 0:
            print("Out of grid!")
            finished = True
            continue
        if grid[headx][heady] != "":
            if grid[headx][heady] != "F":
                finished = True
                continue
        grid[headx][heady] = "H"
        # Detects food
        if (headx == foodx) and (heady == foody):
            time_scored = time.time()
            score += round((100 * ((time_scored - previous_time) ** -0.8) + 1), None)
            # print(str(round((time_scored - previous_time), 2)) + " : " + str(
            #   round((100 * ((time_scored - previous_time) ** -0.8) + 1), None)))
            previous_time = time_scored
            length += 1
            preserve_tail = True
            while grid[foodx][foody] != "":
                foodx = random.randint(0, rows - 1)
                foody = random.randint(0, columns - 1)
            grid[foodx][foody] = "F"
            if increase_speed:
                speed+=2
        if preserve_tail:
            preserve_tail = False
        else:
            tail_bearing = grid[tailx][taily]
            grid[tailx][taily] = ""
            if tail_bearing == "N":
                taily -= 1
            elif tail_bearing == "E":
                tailx += 1
            elif tail_bearing == "S":
                taily += 1
            elif tail_bearing == "W":
                tailx -= 1

        # GRAPHICS
        screen.fill(BLACK)
        # Draws Map
        # Text
        display = "Score: " + str(score) + "     Length: " + str(length) + "       Time: +" + str(
            round((time.time() - start), 2))+"       Speed: "+str(speed)
        textsurface = font.render(
            display, False, WHITE)
        screen.blit(textsurface, (int(width * 0.5 * offset_width), 0))

        pygame.draw.rect(screen, WHITE, [int(width * 0.5 * offset_width), int(
            height * 0.5 * offset_height), (columns * cell_width), (rows * cell_height)])

        # rect[x,y,width,heigth]

        # Draws Grid
        for x in range(0, columns):
            for y in range(0, rows):
                if grid[x][y] != "":
                    if grid[x][y] == "F":  # Food
                        pygame.draw.rect(screen, RED, [int(width * 0.5 * offset_width + (x * cell_width)), int(
                            height * 0.5 * offset_height + (y * cell_height)), cell_width, cell_height])
                    elif grid[x][y] == "H":  # Food
                        pygame.draw.rect(screen, BLUE, [int(width * 0.5 * offset_width + (x * cell_width)), int(
                            height * 0.5 * offset_height + (y * cell_height)), cell_width, cell_height])
                    else:  # Snake
                        pygame.draw.rect(screen, GREEN, [int(width * 0.5 * offset_width + (x * cell_width)), int(
                            height * 0.5 * offset_height + (y * cell_height)), cell_width, cell_height])

        # Updates
        pygame.display.flip()
        clock.tick(speed)
    pygame.display.quit()
    pygame.quit()
    print("\n"*3)
    print("Score: " + str(score) + "\nLength: " + str(length) + "\nTime: +" + str(
        round((time.time() - start), 2)) + "\nSpeed: " + str(speed))
    return [str(score), str(length), str(round((time.time() - start), 2)), str(speed)]
# play()
def standard():
    return play(False)

def speed():
    return play(True)
