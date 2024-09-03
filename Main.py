import character.character
import item.item
import math

John = character("John", "Alive", [], "None", 20, 20)
John.dialogue = ["Hey there, hows it goin'?", "What's up?", "What's the plan?", "Could I get some water?", "We got any water in the back", "I could go for a cheeseburger right now", "Could we stop for food on the way?", "I feel like I'm 'bouta pass out", "Need.. Water..", "My stomach is turning inside out", "John stares at the wildlife, with his mouth watering", "Aghh, I'm bleeding!", "it hurts! It hurts!", "I don't feel so good", "I'm dying...", "John has passed"]

def characterInteract(status, dialogue):
    if status == "fine":
        rand = math.random(0,3)
        if rand < 1:
            print(John.dialogue[0])
        elif rand < 2:
            print(John.dialogue[1])
        else:
            print(John.dialogue[2])
