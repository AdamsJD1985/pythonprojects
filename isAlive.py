"""We are improving our game and need to add an isAlive property, which returns
 True if the lives count is greater than 0.
Complete the code by adding the isAlive property."""


class Player:
    def __init__(self, name, lives):
        self.name = name
        self._lives = lives

    def hit(self):
        self._lives -= 1

    # your code goes here
    def isAlive(self, lives):
        self._lives = lives
        if self._lives > 0:
            return True
        elif self._lives <= 0:
            return False

p = Player("Cyberpunk77", int(input()))
i = 1

while True:
    p.hit()
    print("Hit # " + str(i))
    i += 1
    if not p.isAlive:
        print("Game Over")
        break