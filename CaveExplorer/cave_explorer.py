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


class Wall:
    def __init__(self, x,height,gap):
        self.x = x
		self.height=height
		self.gap=gap
		
def createGrid():
    grid = [x[:] for x in [[""] * rows] * columns]
    return grid


def cave(level):
    global columns
    global rows
    # Colours
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

	#Black empty
	#White wall
	#Red player
	
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
	
	speed=30
    grid = createGrid()

    #Player

    playerx = int(columns / 2)
    playery = int(rows - 1)
    grid[playerx][playery] = "p"
	
	
	#Wall gen
	walls=[]
	gap=playery
	for c in range(0,columns):
		walls.append(Wall(c,rows,gap)
		gap+=(random.randint(-1,1))
		if gap>= rows:
			gap-=1
		elif gap<0:
			gap+=1
	wall_speed=5
    # Pygame Setup
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 15)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Cave Explorer")
    finished = False
    clock = pygame.time.Clock()
    start = time.time()
    while not finished:
        # GRID
		# Regenerates grid
        grid = createGrid()
		#Generates next wall
		if count=wall_speed:
			walls.pop()
			gap+=(random.randint(-1,1))
			if gap>= rows:
				gap-=1
			elif gap<0:
				gap+=1
			walls.append(Wall(c,rows,gap)
			count=0
		else:
			count+=1
       
		for x in range(0,columns):
			for y in range(0,x.y):
				if gap!=y:
					grid[x][y]="w"
        # Moves player
        # Detects if block occupying current space
        if grid[playerx][playery] != "":
            if grid[playerx][playery] != "W":
                finished = True
                print("You got hit by something!")
                continue
        # Moves player
        grid[playerx][playery] = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    playery -= 1
                if event.key == pygame.K_DOWN:
                    playery += 1
        # Checks player in bounds
        if playerx >= rows or playerx < 0 or playery >= rows or playery < 0:
            print("Out of bounds!")
            finished = True
            continue

        # Detects if block in front
        if grid[playerx][playery] != "":
            if grid[playerx][playery] != "W":
                finished = True
                print("You hit something!")
                continue

        # Detects if finished
        if playery == 0:
            print("YOU WIN")
            finished = True
            pygame.display.quit()
            pygame.quit()
            return True, round(time.time()-start,2)

        grid[playerx][playery] = "F"
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
                    if grid[x][y] == "P":  # Player
                        pygame.draw.rect(screen, RED, [int(width * 0.5 * offset_width + (x * cell_width)), int(
                            height * 0.5 * offset_height + (y * cell_height)), cell_width, cell_height])
                    elif grid[x][y] == "W":  # Wall
                        pygame.draw.rect(screen, WHITE, [int(width * 0.5 * offset_width + (x * cell_width)), int(
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
        result = cave(level)
        loop = result[0]
        if fast_time > result[1]:
            fast_time = result[1]
        if result[0]:
            level += 1
    print("Your final level was: " + str(level))
    print("With a fastest level of : " + str(fast_time))
    return [str(level), str(fast_time)]