import random
import time
import pygame


class Log_Row:
    def __init__(self, y, max_num, columns):
        self.columns = columns
        self.count = 0
        self.y = y
        self.num = random.randint(1, max_num)
        self.speed = float(random.randint(5, 20))

        self.dir = ((-1) ** (random.randint(1, 2)))
        self.size = random.randint(1, int((0.5 * columns) / self.num))

        self.logs = []
        for x in range(0, self.num):
            self.logs.append(Log(self.y))

    def move_logs(self):
        if self.count == self.speed:
            for log in self.logs:
                log.x += self.dir
                if log.x == self.columns:

                    log.x = 0
                elif log.x < 0:
                    log.x = self.columns - 1
            self.count = 0
        else:
            self.count += 1


class Log:
    def __init__(self, y):
        self.x = random.randint(0, columns - 1)
        self.y = y


def createGrid():
    grid = [x[:] for x in [[""] * rows] * columns]
    # print("Window size is: " + str(width) + ", " + str(height))
    # print(len(grid))

    for x in range(0, columns):
        grid[x][rows - 1] = "S"

    for y in range(2, 7):
        for x in range(0, columns):
            grid[x][rows - y] = "W"
    for x in range(0, columns):
        grid[x][rows - 7] = "S"
        grid[x][rows - 8] = "S"

    for y in range(9, 14):
        for x in range(0, columns):
            grid[x][rows - y] = "W"

    for y in range(13, 15):
        for x in range(0, columns):
            grid[x][rows - 14] = "E"
    return grid


def frogger(level):
    global columns
    global rows
    # Colours
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)
    BROWN = (100, 50, 0)

    # Green for frog			F
    # Purple for safe		S
    # Red for end 2 tiles	E

    # Brown for log			L
    # Black for road			R

    # Dimensions
    rows = 14
    columns = 15
    cell_width = 50
    cell_height = 50
    offset_height = 0.1
    offset_width = 0.05
    width = int(columns * cell_width * (1 + offset_width))
    height = int(rows * cell_height * (1 + offset_height))
    size = (width, height)

    grid = createGrid()

    # Frog

    frogx = int(columns / 2)
    frogy = int(rows - 1)
    grid[frogx][frogy] = "F"

    # Logs
    max_num = 3
    logs = []
    for y in range(1, 6):
        logs.append(Log_Row(y, max_num, columns))
    for y in range(8, 13):
        logs.append(Log_Row(y, max_num, columns))

    speed = 30

    # Pygame Setup
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 15)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Frogger")
    finished = False
    clock = pygame.time.Clock()
    start = time.time()
    while not finished:
        # GRID
        # Regenerates grid
        grid = createGrid()

        # Moves log
        for x in logs:
            x.move_logs()

        for row in logs:
            for log in row.logs:
                for dif in range(0, row.size):
                    grid[log.x - dif][log.y] = "L"
        # Need to check if frog in way

        # Moves Frog
        # Detects if block occupying current space
        if grid[frogx][frogy] != "":
            if grid[frogx][frogy] != "S" and grid[frogx][frogy] != "E" and grid[frogx][frogy] != "W":
                finished = True
                print("You got hit by something!")
                continue
        # Moves frog
        grid[frogx][frogy] = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    frogy -= 1
                if event.key == pygame.K_DOWN:
                    frogy += 1
                if event.key == pygame.K_LEFT:
                    frogx -= 1
                if event.key == pygame.K_RIGHT:
                    frogx += 1

        # Checks frog in bounds
        if frogx >= rows or frogx < 0 or frogy >= rows or frogy < 0:
            print("Out of bounds!")
            finished = True
            continue

        # Detects if block in front
        if grid[frogx][frogy] != "":
            if grid[frogx][frogy] != "S" and grid[frogx][frogy] != "E" and grid[frogx][frogy] != "W":
                finished = True
                print("You hit something!")
                continue

        # Detects if finished
        if frogy == 0:
            print("YOU WIN")
            finished = True
            pygame.display.quit()
            pygame.quit()
            return True, round(time.time()-start,2)

        grid[frogx][frogy] = "F"
        # GRAPHICS
        screen.fill(BLACK)
        # Draws Map
        # Text
        display = "     Level: " + str(level) + "       Time: +" + str(round((time.time() - start), 2))
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
                    if grid[x][y] == "F":  # Frog
                        pygame.draw.rect(screen, GREEN, [int(width * 0.5 * offset_width + (x * cell_width)), int(
                            height * 0.5 * offset_height + (y * cell_height)), cell_width, cell_height])
                    elif grid[x][y] == "S":  # Safe
                        pygame.draw.rect(screen, YELLOW, [int(width * 0.5 * offset_width + (x * cell_width)), int(
                            height * 0.5 * offset_height + (y * cell_height)), cell_width, cell_height])
                    elif grid[x][y] == "E":  # End
                        pygame.draw.rect(screen, PURPLE, [int(width * 0.5 * offset_width + (x * cell_width)), int(
                            height * 0.5 * offset_height + (y * cell_height)), cell_width, cell_height])
                    elif grid[x][y] == "L":  # Log
                        pygame.draw.rect(screen, BROWN, [int(width * 0.5 * offset_width + (x * cell_width)), int(
                            height * 0.5 * offset_height + (y * cell_height)), cell_width, cell_height])
                    elif grid[x][y] == "W":  # Water
                        pygame.draw.rect(screen, BLUE, [int(width * 0.5 * offset_width + (x * cell_width)), int(
                            height * 0.5 * offset_height + (y * cell_height)), cell_width, cell_height])

        # Updates
        pygame.display.flip()
        clock.tick(speed)
    pygame.display.quit()
    pygame.quit()
    return False, round(time.time()-start,2)


def play():
    level = 1
    loop = True
    fast_time = 100000
    while loop:
        result = frogger(level)
        loop = result[0]
        if fast_time > result[1]:
            fast_time = result[1]
        if result[0]:
            level += 1
    print("Your final level was: " + str(level))
    print("With a fastest level of : " + str(fast_time))
    return [str(level), str(fast_time)]
