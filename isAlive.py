"""We are improving our game and need to add an isAlive property, which returns
 True if the lives count is greater than 0.
Complete the code by adding the isAlive property."""


class Enemy:
    name = ""
    lives = 0

    def __init__(self, name, lives):
        self.name = name
        self.lives = lives

    def hit(self):
        self.lives -= 1
        if self.lives <= 0:
            print(self.name + ' killed')
        else:
            print(self.name + ' has ' + str(self.lives) + ' lives')


class Monster(Enemy):
    def __init__(self):
        super().__init__('Monster', 3)


class Alien(Enemy):
    def __init__(self):
        super().__init__('Alien', 5)


m = Monster()
a = Alien()

while True:
    x = input()
    if x == "laser":
        a.hit()
    elif x == "gun":
        m.hit()
    elif x == 'exit':
        break