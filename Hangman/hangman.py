import random
import http
import urllib.request
hangman = [
'''
       
      
      
      
      
=========''',
'''
  
      |
      |
      |
      |
      |
=========''',
'''
  +---+
      |
      |
      |
      |
      |
=========''',
    
'''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
animals = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
items="""
white out
coasters
washing machine
cup
air freshener
cork
plate
house
bag
thermometer
floor
table
mirror
nail clippers
sailboat
television
bow
rusty nail
headphones
piano
perfume
face wash
greeting card
stockings
keys
pencil
rubber band
beef
money
sharpie
apple
brocolli
candy wrapper
remote
newspaper
button
eraser
toilet
shirt
soda can
doll
playing card
thread
stop sign
slipper
pool stick
tree
glow stick
spring
blouse
scotch tape
cinder block
hanger
tire swing
cell phone
bracelet
toe ring
watch
knife
boom box
carrots
ipod
keyboard
sand paper
credit card
monitor
bananas
clay pot
paint brush
leg warmers
toothbrush
shoe lace
sticky note
milk
tooth picks
key chain
fridge
charger
video games
sofa
teddies
lip gloss
bottle cap
clamp
radio
spoon
mop
car
cat
lamp shade
ring
packing peanuts
ice cube tray
phone
soap
sidewalk
eye liner
bookmark
bed
purse
hanger
boom box
greeting card
perfume
shoes
face wash
bread
stockings
clamp
model car
floor
lamp
tv
bananas
plate
buckel
eraser
sandal
pencil
mp3 player
thermometer
water bottle
watch
button
credit card
socks
helmet
sharpie
balloon
candy wrapper
rusty nail
magnet
knife
monitor
sailboat
street lights
blanket
CD
canvas
chair
pillow
tooth picks
blouse
table
cinder block
vase
soy sauce packet
cookie jar
thread
carrots
beef
radio
milk
tomato
spring
washing machine
sponge
mouse pad
checkbook
purse
bookmark
fake flowers
air freshener
car
window
sticky note
glass
bracelet
USB drive
lip gloss
photo album
food
thermostat
lamp shade
cup
key chain
chocolate
newspaper
soda can
outlet
video games
bottle cap
truck
pen
rubber duck
controller
box
clothes
plastic fork
rubber band
eye liner
mop
glasses
drawer
tree
twezzers
shawl
television
keyboard
clock
clock
glasses
wallet
sailboat
outlet
clay pot
shovel
doll
twister
video games
shampoo
clamp
buckel
lamp shade
glow stick
bow
phone
twezzers
plate
thread
playing card
sponge
paper
chocolate
car
balloon
nail clippers
photo album
sandal
computer
chalk
purse
bookmark
picture frame
shawl
pool stick
plastic fork
cell phone
tooth picks
couch
button
spring
soy sauce packet
beef
towel
sharpie
tissue box
television
USB drive
food
spoon
scotch tape
vase
rusty nail
ipod
cup
wagon
candle
remote
grid paper
socks
tree
mop
sidewalk
drawer
seat belt
water bottle
candy wrapper
deodorant
coasters
door
teddies
cat
blouse
sticky note
needle
boom box
apple
cookie jar
bananas
white out
milk
packing peanuts
shirt
key chain
lip gloss
hair brush
pen
controller
mouse pad
glass
bed
toothpaste
money
charger
ring
tv
pillow
screw
drill press
bed
chalk
lace
speakers
desk
mop
sharpie
charger
sun glasses
shoes
slipper
lotion
video games
couch
television
pool stick
rusty nail
window
table
shovel
camera
air freshener
glasses
paper
perfume
teddies
shampoo
plastic fork
outlet
toe ring
twezzers
bananas
milk
vase
lip gloss
door
checkbook
rubber duck
bowl
phone
clamp
cup
computer
keys
paint brush
balloon
toilet
keyboard
magnet
photo album
CD
conditioner
tomato
money
lamp
tree
tissue box
blanket
socks
hanger
ipod
thermometer
candle
bottle
purse
bread
wagon
beef
watch
car
picture frame
hair tie
face wash
chair
blouse
packing peanuts
toothbrush
sandal
ring
radio
mirror
bottle cap
greeting card
playing card
flowers
sticky note
grid paper
chocolate
bag
helmet
tv
toothpaste
zipper
screw
eye liner
monitor
needle
bookmark
thermostat
towel
ice cube tray
tree
outlet
blouse
pencil
floor
candle
truck
shovel
car
hanger
glass
thermometer
stop sign
twezzers
bananas
glasses
ipod
pants
charger
water bottle
canvas
computer
tv
shirt
soap
socks
desk
rusty nail
beef
purse
towel
twister
chair
deodorant
bed
boom box
eye liner
shoes
remote
doll
headphones
bag
sharpie
buckel
vase
cork
air freshener
pillow
nail file
clothes
washing machine
keys
piano
fridge
drill press
cell phone
shawl
cinder block
puddle
sun glasses
television
lace
chalk
CD
toothpaste
magnet
rubber duck
paint brush
bottle cap
lotion
hair brush
hair tie
needle
soy sauce packet
tissue box
monitor
eraser
carrots
spoon
book
clock
paper
shoe lace
fork
lip gloss
window
pool stick
chocolate
sofa
rubber band
clay pot
cat
playing card
watch
lamp
grid paper
sidewalk
toothbrush
soda can"""


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = (word_file.read().split())

    return valid_words
words=load_words()
hangman=hangman[::-1]
temp=items.split("\n")
for a in animals:
    words.append(a)
for t in temp:
    words.append(t)




def game():
    global hangman
    global words
    word = words[random.randint(0,len(words)-1)]
    letters=list(word)
    letters_remaining=list(letters)
    guessed=[]
    lives=len(hangman)-1
    
    try:
        letters_remaining.remove(" ")
    except ValueError:
        None
    while len(letters_remaining)>0 and lives>0:
        current=""
        for l in letters:
            if l in guessed:
                current+=l
            elif " " ==l:
                current+=" "
            else:
                current+="-"
        print(hangman[lives])
        print()
        print(current)
        print("You have "+str(lives)+" lives left.")
        letter=list(input("Enter a letter: ").lower())
        if len(letter)==0:
            print("Enter a value!")
            lives-=1
            continue
        letter=letter[0]
        if letter in guessed:
            print("You have already guessed that letter!")
            continue
        guessed.append(letter)
        if letter in letters_remaining:
            while letter in letters_remaining:
                letters_remaining.remove(letter)
        else:
            print("Letter rejeceted")
            lives-=1
    print()
    print(hangman[lives])
    if lives==0:
        print("You died!")
    else:
        print("You win")
    print("The word was: "+str(word))
    #https://wordsapiv1.p.mashape.com/words/example/definitions
    URL="https://www.collinsdictionary.com/dictionary/english/"+word
    proxy = urllib.request.ProxyHandler({})
    auth = urllib.request.HTTPBasicAuthHandler()
    opener = urllib.request.build_opener(proxy, auth, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    conn = urllib.request.urlopen(URL)
    with urllib.request.urlopen(URL) as response:
        html = response.read().decode("utf-8")
        print(html)

    
play=True
while play:
    game()
    if "y" not in input("Do you want to play again?").lower() :
        play=False
