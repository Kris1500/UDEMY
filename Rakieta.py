from random import randint

class Rocket:
    def __init__(self,speed):
        self.alt = 1
        self.speed = 4

    def moveUp(self):
        self.alt += self.speed

rockets = [Rocket(4) for _ in range(5)]
#print(rockets)

for i in range (10):
    rocketMove = randint(0,4)
    rockets[rocketMove].moveUp()

for rocket in rockets:
    print(rocket.alt)