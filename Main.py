import character.character
import item.item
import math
day = 0
waterCount = 0
foodCount = 0
money = 0
inventory = []

char1 = character("John", "fine", [], 20, 20, 99, 99)
char1.dialogue = ["Hey there, hows it goin'?", "What's up?", "What's the plan?", "Could I get some water?", "We got any water in the back", "I could go for a cheeseburger right now", "Could we stop for food on the way?", "I feel like I'm 'bouta pass out", "Need.. Water..", "My stomach is turning inside out", "John stares at the wildlife, with his mouth watering", "Aghh, I'm bleeding!", "It hurts! it hurts!", "I don't feel so good", "I'm dying...", char1.name + " has passed"]

char2 = character("Beatrice", "fine", [], 20, 20, 99, 99)
char2.dialogue = ["Hey! How are you?", "Hey there!", "What's next?", "Could I have something to drink?", "I could use some water right now", "Lets go hunting soon", "Could you spare some extra food?", "I feel really light headed", "You think that brown river is safe to drink?", "Please give me food, just anything", "Beatrice munches on her hair in the corner", "Aghh, I't hurts!", "There's blood everywhere!", "I feel really nauseous", "Beatrice is throwing up constantly", char2.name + " has passed"]

char3 = character("Neil", "fine", [], 20, 20, 99, 99)
char3.dialogue = ["Hi! How are you?", "What's up?", "What's next?", "Man, I'm thirsty", "You got something to drink?", "Lets hunt something, I'm hungry", "You got something to eat?", "The world feels like its spinning", "I feel feint", "That bear over there looks delicious right now", "I haven't eaten for days...", "Aghh, I need something for this cut", "It won't stop bleeding!", "I feel really ill", "Please tell me you brought medicine", char3.name + " has passed"]
def characterInteract(character, status):
    if status == "fine":
        rand = math.random(0,3)
        if rand < 1:
            print(character.dialogue[0])
        elif rand < 2:
            print(character.dialogue[1])
        else:
            print(character.dialogue[2])
    elif status == "thirsty":
        rand = math.random(0, 2)
        if rand < 1:
            print(character.dialogue[3])
        else:
            print(character.dialogue[4])
    elif status == "hungry":
        rand = math.random(0, 2)
        if rand < 1:
            print(character.dialogue[5])
        else:
            print(character.dialogue[6])
    elif status == "parched":
        rand = math.random(0, 2)
        if rand < 1:
            print(character.dialogue[7])
        else:
            print(character.dialogue[8])
    elif status == "starved":
        rand = math.random(0, 2)
        if rand < 1:
            print(character.dialogue[9])
        else:
            print(character.dialogue[10])
    elif status == "sick":
        rand = math.random(0, 2)
        if rand < 1:
            print(character.dialogue[11])
        else:
            print(character.dialogue[12])
    elif status == "injured":
        rand = math.random(0, 2)
        if rand < 1:
            print(character.dialogue[13])
        else:
            print(character.dialogue[14])
    elif status == "dead":
        print(character.dialogue[15])

def updateStatus(character):
    #Checks the character's stats and updates the status accordingly
    if character.thirst <= 0 or character.hunger <= 0 or character.injuryTimer <= 0 or character.sicknessTimer <= 0:
        character.status = "dead"
    elif character.thirst < 12 and character.thirst <= character.hunger:
        character.status = "thirsty"
    elif character.hunger < 12 and character.hunger < character.thirst:
        character.status = "hungry"
    elif character.thirst < 4 and character.thirst <= character.hunger:
        character.status = "parched"
    elif character.hunger < 4 and character.hunger < character.thirst:
        character.status = "starved"
    elif character.injuryTimer > 50 and character.sicknessTimer > 50:
        character.status = "fine"

def passTime(character):
    # Decrease thirst and hunger
    character.thirst -= 4
    character.hunger -= 2

    # Handle injury and sickness
    if character.injuryTimer < 50:
        character.injuryTimer -= 1
    if character.sicknessTimer < 50:
        character.sicknessTimer -= 1

    # Random chance of getting sick
    if math.random(0, 100) < 5:  # 5% chance of getting sick
        randSickness = math.random(0, 100)
        if randSickness < 40:  # Chances per illness
            character.sicknessTimer = 3
            character.status = "sick"
            print(character, " caught smallpox")
        elif randSickness < 5:
            character.sicknessTimer = 2
            character.status = "sick"
            print(character, " caught the black plague")
        else:
            character.sicknessTimer = 5
            character.status = "sick"
            print(character, " caught the flu")

    # Update character status
    character.status = updateStatus(character)

def playGame():

    print("Welcome to the Oregon Trail(Temu Edition)!")
    print("Your goal is to survive the 30 day trip to oregon")
    print("You are the leader of your group, and you need to manage your group's resources and make decisions to ensure the survival of your group.")
    print("Good luck!")
    
    if input("Would you like to change your character's name? (Y/N): ").lower() == "y":
        char1.name = input("Give your first character a name: ")
        char2.name = input("Give your second character a name: ")
        char3.name = input("Give your third character a name: ")

