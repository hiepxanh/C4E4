






from firebase import firebase
from time import sleep

fb = firebase.FirebaseApplication('https://hiepxanh.firebaseio.com/user/', None) #
while True:
    response = fb.get('/user', None)
    for key, value in response.items():
        # print(key)
        text = value['text']
        name = value['name']
        print(str.format("{0} : {1}", name, text))
        sleep(5)



class Ninja:
    def __init__(self, name, village, healthPoint, attackPoint, defensePoint):
        self.name = name
        self.village = village
        self.healthPoint = healthPoint
        self.attackPoint = attackPoint
        self.defensePoint = defensePoint

    def attack(self, enemy):
        print(str.format("{0} attacks {1}", self.name, enemy.name))
        if self.attackPoint < enemy.defensePoint:
            enemy.healthPoint = enemy.healthPoint
            print(str.format('{0} cannot hurt {1}', self.name, enemy.name))
            print('Ninja', enemy.name, 'healthPoint: ', enemy.healthPoint)
        else:
            enemy.healthPoint = enemy.healthPoint - (self.attackPoint - enemy.defensePoint)
            print(enemy.name, 'healthPoint: ', enemy.healthPoint)
        return enemy.healthPoint


Naruto = Ninja('Naruto', 'Leaf', 11, 7, 4)
Gaara = Ninja('Gaara', 'Sand', 12, 6, 8)
Zabuza = Ninja('Zabuza', 'Fog', 9, 8, 3)
Deidara = Ninja('Deidara', 'Rock', 8, 10, 1)

print('In combat:')
Naruto.attack(Gaara)
Zabuza.attack(Naruto)
Gaara.attack(Deidara)
Deidara.attack(Zabuza)