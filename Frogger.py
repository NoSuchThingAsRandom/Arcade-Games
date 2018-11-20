import random
import time
import pygame
class Log_Row:
	def __init__(self,y,max_num,columns):
		self.y=y
		self.num=random.randint(1,max_num)
		self.speed=float(1/random.randint(0,10))		
		
		self.dir=((-1)**(random.randint(1,2)))
		self.size=dir,random.randint(1,int(columns/self.num))
		
		self.logs=[]
		for x in range(0,self.num):
			self.logs.append(Log(self.y))

	
class Log:
	def __init__(self,y):
		self.x=random.randint(0,columns)
		self.y=y

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW=(255,255,0)
PURPLE=(255,0,255)
BROWN=(100,50,0)

#Green for frog			F
#Purple for safe		S
#Red for end 2 tiles	E

#Brown for log			L
#Black for road			R


# Dimensions
rows = 14
columns = 10
cell_width = 20
cell_height = 20
offset_height = 0.1
offset_width = 0.05
width = int(columns*cell_width*(1+offset_width))
height = int(rows*cell_height*(1+offset_height))
size = (width, height)

def createGrid():
    grid = [x[:] for x in [[""] * rows] * columns]
    print("Window size is: "+str(width)+", "+str(height))
    print(len(grid))

    for x in range(0,columns):
            grid[x][rows-1]="S"

    for y in range(2,7):
            for x in range(0,columns):
                    grid[x][rows-y]="W"
    for x in range(0,columns):
            grid[x][rows-7]="S"

    for y in range(8,13):
            for x in range(0,columns):
                    grid[x][rows-y]="W"
                    
    for y in range(13,15):
            for x in range(0,columns):
                    grid[x][rows-y]="E"
    return grid

grid=createGrid()

#Frog

frogx = int(columns/2)
frogy = int(rows-1)
grid[frogx][frogy] = "F"


#Logs
max_num=3
logs=[]
for y in range(2,7):
	logs.append(Log_Row(y,max_num,columns))
for y in range(8,13):
	logs.append(Log_Row(y,max_num,columns))



print(logs)

	
	
#User Options
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
speed=10



# Pygame Setup
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 15)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
finished = False
clock = pygame.time.Clock()
start=time.time()
while not finished:
# GRID
	#Moves blocks
	
	#Need to check if frog in way
	

	#Moves Frog
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


    #Detects if block in front
    if grid[frogx][frogy] != "":
        if grid[frogx][frogy] != "S" and grid[frogx][frogy] != "E"  and grid[frogx][frogy] != "R"  :
            finished = True
			print("You hit something!")
            continue
	if frogx >= rows or frogx < 0 or frogy >= columns or frogy < 0:
        print("Out of grid!")
        finished = True
        continue
	grid[frogx][frogy] = "H"
    # Detects end
    if (frogy >=rows-1):
		print("YOU WIN")
		finished=True
		continue



# GRAPHICS
    screen.fill(BLACK)
    # Draws Map
    # Text
    display="Score: "+str(score)+"     Length: "+str(length)+"       Time: +"+str(round((time.time()-start),2))
    textsurface = font.render(
        display, False, WHITE)
    screen.blit(textsurface, (int(width*0.5*offset_width),0))

    pygame.draw.rect(screen, WHITE, [int(width*0.5*offset_width), int(
        height*0.5*offset_height), (columns*cell_width), (rows*cell_height)])

    # rect[x,y,width,heigth]

    # Draws Grid
    for x in range(0, columns):
        for y in range(0, rows):
            if grid[x][y] != "":
                if grid[x][y] == "F":  # Frog
                    pygame.draw.rect(screen, GREEN, [int(width*0.5*offset_width+(x*cell_width)), int(
                        height*0.5*offset_height+(y*cell_height)), cell_width, cell_height])
                elif grid[x][y] == "S":  # Safe
                    pygame.draw.rect(screen, PURPLE, [int(width*0.5*offset_width+(x*cell_width)), int(
                        height*0.5*offset_height+(y*cell_height)), cell_width, cell_height])
				elif grid[x][y] == "E":  # End
                    pygame.draw.rect(screen, PURPLE, [int(width*0.5*offset_width+(x*cell_width)), int(
                        height*0.5*offset_height+(y*cell_height)), cell_width, cell_height])
				elif grid[x][y] == "L":  # Log
                    pygame.draw.rect(screen, PURPLE, [int(width*0.5*offset_width+(x*cell_width)), int(
                        height*0.5*offset_height+(y*cell_height)), cell_width, cell_height])
				elif grid[x][y] == "C":  # Car
                    pygame.draw.rect(screen, PURPLE, [int(width*0.5*offset_width+(x*cell_width)), int(
                        height*0.5*offset_height+(y*cell_height)), cell_width, cell_height])		
				elif grid[x][y] == "W":  # Water
                    pygame.draw.rect(screen, PURPLE, [int(width*0.5*offset_width+(x*cell_width)), int(
                        height*0.5*offset_height+(y*cell_height)), cell_width, cell_height])
				elif grid[x][y] == "R":  # Road
                    pygame.draw.rect(screen, PURPLE, [int(width*0.5*offset_width+(x*cell_width)), int(
                        height*0.5*offset_height+(y*cell_height)), cell_width, cell_height])
    # Updates
    pygame.display.flip()
    clock.tick(speed)