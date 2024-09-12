import character.character
import item.item
import math
money = 100
foodCount = 0
waterCount = 0
inventory = []

char1 = character("John", "fine", [], 20, 20, 99, 99)
char1.dialogue = ["Hey there, hows it goin'?", "What's up?", "What's the plan?", "Could I get some water?", "We got any water in the back", "I could go for a cheeseburger right now", "Could we stop for food on the way?", "I feel like I'm 'bouta pass out", "Need.. Water..", "My stomach is turning inside out", "John stares at the wildlife, with his mouth watering", "Aghh, I'm bleeding!", "It hurts! it hurts!", "I don't feel so good", "I'm dying...", char1.name + " has passed"]

char2 = character("Beatrice", "fine", [], 20, 20, 99, 99)
char2.dialogue = ["Hey! How are you?", "Hey there!", "What's next?", "Could I have something to drink?", "I could use some water right now", "Lets go hunting soon", "Could you spare some extra food?", "I feel really light headed", "You think that brown river is safe to drink?", "Please give me food, just anything", "Beatrice munches on her hair in the corner", "Aghh, I't hurts!", "There's blood everywhere!", "I feel really nauseous", "Beatrice is throwing up constantly", char2.name + " has passed"]

char3 = character("Neil", "fine", [], 20, 20, 99, 99)
char3.dialogue = ["Hi! How are you?", "What's up?", "What's next?", "Man, I'm thirsty", "You got something to drink?", "Lets hunt something, I'm hungry", "You got something to eat?", "The world feels like its spinning", "I feel feint", "That bear over there looks delicious right now", "I haven't eaten for days...", "Aghh, I need something for this cut", "It won't stop bleeding!", "I feel really ill", "Please tell me you brought medicine", char3.name + " has passed"]

char4 = character("Anne", "fine", [], 20, 20, 99, 99)
char4.dialogue = ["Hey, what's up?", "Hows it going?", "Yeah?", "I could use something to drink", "Could I get a water?", "We got some extra food?", "I'm hungry", "I'm seeing stars", "I.. Need.. Water..", "My stomach hurts... so... bad", "I could literally eat anything right now", "Aghh, I'm bleeding!", "Oh my gosh this hurts", "I'm so fatigued'", "I think I'm dying...", char4.name + " has passed"]

medicine = item("consumable", "medicine", 10)
medkit = item("consumable", "medkit", 15)
artifact = item("artifact", "artifact", 30)

def characterInteract(character, status):
    if status == "fine":
        rand = math.random(0,3)
        if rand < 1:
            print(f"{character.name}: {character.dialogue[0]}")
        elif rand < 2:
            print(f"{character.name}: {character.dialogue[1]}")
        else:
            print(f"{character.name}: {character.dialogue[2]}")
    elif status == "thirsty":
        rand = math.random(0, 2)
        if rand < 1:
            print(f"{character.name}: {character.dialogue[3]}")
        else:
            print(f"{character.name}: {character.dialogue[4]}")
    elif status == "hungry":
        rand = math.random(0, 2)
        if rand < 1:
            print(f"{character.name}: {character.dialogue[5]}")
        else:
            print(f"{character.name}: {character.dialogue[6]}")
    elif status == "parched":
        rand = math.random(0, 2)
        if rand < 1:
            print(f"{character.name}: {character.dialogue[7]}")
        else:
            print(f"{character.name}: {character.dialogue[8]}")
    elif status == "starved":
        rand = math.random(0, 2)
        if rand < 1:
            print(f"{character.name}: {character.dialogue[9]}")
        else:
            print(f"{character.name}: {character.dialogue[10]}")
    elif status == "sick":
        rand = math.random(0, 2)
        if rand < 1:
            print(f"{character.name}: {character.dialogue[11]}")
        else:
            print(f"{character.name}: {character.dialogue[12]}")
    elif status == "injured":
        rand = math.random(0, 2)
        if rand < 1:
            print(f"{character.name}: {character.dialogue[13]}")
        else:
            print(f"{character.name}: {character.dialogue[14]}")
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

def distributeResources(char):
    characterInteract(char, char.status)
    if char.status != "dead":
        res = input(f"What would you like to give to {char.name}? 1. Water 2. Food 3. Medicine 4. Medkit")


def playGame():

    print("Welcome to the Oregon Trail(Temu Edition)!")
    print("Your goal is to survive the 30 day trip to oregon")
    print("You are the leader of your group, and you need to manage your group's resources and make decisions to ensure the survival of your group.")
    print("Good luck!")
    
    if input("Would you like to change your characters' names? (Y/N): ").lower() == "y":
        char1.name = input("Give your first character a name: ")
        char2.name = input("Give your second character a name: ")
        char3.name = input("Give your third character a name: ")
        char4.name = input("Give your fourth character a name: ")
    alive = True
    day = 0
    while day <= 30 and alive:
        print("Day: "+ day)
        if day == 0:
            print("Today is the day before your trip! You have 100 dollars to spend on supplies.")
            exitShop = "n"
            while exitShop.lower() != "y":
                print("You have $" + money + " left.")
                print("What would you like to buy?")
                print("1. Water ($2)")
                print("2. Food ($3)")
                print("3. Medicine ($10)")
                print("4. Medkit ($15)")
                print("5. Exit")
                choice = input("Enter the number of your choice: ")
                if choice == "1":
                    if money >= 2:
                        waterCount += 5
                        money -= 2
                        print("Water purchased.")
                    else:
                        print("You don't have enough money.")
                elif choice == "2":
                    if money >= 3:
                        foodCount += 5
                        money -= 3
                        print("Food purchased.")
                    else:
                        print("You don't have enough money.")
                elif choice == "3":
                    if money >= 10:
                        inventory.append(medicine)
                        money -= 10
                        print("Medicine purchased.")
                    else:
                        print("You don't have enough money.")
                elif choice == "4":
                    if money >= 15:
                        inventory.append(medkit)
                        money -= 15
                elif  choice == "5":
                    if input("Are you sure you want to exit? (Y/N): ").lower() == "y":
                        exitShop = "y"
        
        elif day % 5 == 0:
            print("You've reached a town and can visit the shop!")
            exitShop = "n"
            while exitShop.lower() != "y":
                print("You have $" + str(money) + " left.")
                print("What would you like to do?")
                print("1. Water ($3)")
                print("2. Food ($5)")
                print("3. Medicine ($15)")
                print("4. Medkit ($20)")
                print("5. Sell Water ($1.5)")
                print("6. Sell Food ($2.5)")
                print("7. Sell Medicine ($7.5)")
                print("8. Sell Medkit ($10)")
                print("9. Sell Artifact ($20)")
                print("0. Exit")
                choice = input("Enter the number of your choice: ")
                if choice == "1":
                    if money >= 2:
                        waterCount += 5
                        money -= 2
                        print("Water purchased.")
                    else:
                        print("You don't have enough money.")
                elif choice == "2":
                    if money >= 3:
                        foodCount += 5
                        money -= 3
                        print("Food purchased.")
                    else:
                        print("You don't have enough money.")
                elif choice == "3":
                    if money >= 10:
                        inventory.append(medicine)
                        money -= 10
                        print("Medicine purchased.")
                    else:
                        print("You don't have enough money.")
                elif choice == "4":
                    if money >= 15:
                        inventory.append(medkit)
                        money -= 15
                        print("Medkit purchased.")
                    else:
                        print("You don't have enough money.")
                elif choice == "5":
                    if waterCount >= 5:
                        waterCount -= 5
                        money += 1.5
                        print("Water sold.")
                    else:
                        print("You don't have enough water to sell.")
                elif choice == "6":
                    if foodCount >= 5:
                        foodCount -= 5
                        money += 2.5
                        print("Food sold.")
                    else:
                        print("You don't have enough food to sell.")
                elif choice == "7":
                    if medicine in inventory:
                        inventory.remove(medicine)
                        money += 7.5
                        print("Medicine sold.")
                    else:
                        print("You don't have any medicine to sell.")
                elif choice == "8":
                    if medkit in inventory:
                        inventory.remove(medkit)
                        money += 10
                        print("Medkit sold.")
                    else:
                        print("You don't have any medkit to sell.")
                elif choice == "9":
                    if artifact in inventory:
                        inventory.remove(artifact)
                        money += 20
                        print("Artifact sold.")
                    else:
                        print("You don't have any artifacts to sell.")
                elif choice == "0":
                    if input("Are you sure you want to exit? (Y/N): ").lower() == "y":
                        exitShop = "y"
                else:
                    print("Invalid choice. Please try again.")
            nextDay = "n"
            while nextDay.lower() != "y":
                print("Distribute resources to your team")
                charToDistribute = input(f"Who would you like to distribute resources to? 1. {char1.name}  2. {char2.name}  3. {char3.name}  4. {char4.name}")

            
        
        

