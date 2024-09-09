import character.character
import item.item
import math
day = 0
waterCount = 0
foodCount = 0
inventory = []

John = character("John", "fine", [], 20, 20, 99, 99)
John.dialogue = ["Hey there, hows it goin'?", "What's up?", "What's the plan?", "Could I get some water?", "We got any water in the back", "I could go for a cheeseburger right now", "Could we stop for food on the way?", "I feel like I'm 'bouta pass out", "Need.. Water..", "My stomach is turning inside out", "John stares at the wildlife, with his mouth watering", "Aghh, I'm bleeding!", "it hurts! It hurts!", "I don't feel so good", "I'm dying...", "John has passed"]

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
    elif character.thirst < 10 and character.thirst <= character.hunger:
        character.status = "thirsty"
    elif character.hunger < 10 and character.hunger < character.thirst:
        character.status = "hungry"
    elif character.thirst < 4 and character.thirst <= character.hunger:
        character.status = "parched"
    elif character.hunger < 4 and character.hunger < character.thirst:
        character.status = "starved"
    elif character.injuryTimer > 50 and character.sicknessTimer > 50:
        character.status = "fine"

def passTime(character, hours):
    # Decrease thirst and hunger
    character.thirst -= 1
    character.hunger -= 1

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

