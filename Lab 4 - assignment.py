class Ninja:
    def __init__(self,name,village,healthPoint,attackPoint,defensePoint):
        self.name = name
        self.village = village
        self.healthPoint = healthPoint
        self.attackPoint = attackPoint
        self.defensePoint = defensePoint
    def attack(self,enemy):
        if self.attackPoint >= enemy.defensePoint:
            enemy.healthPoint = enemy.healthPoint - (self.attackPoint - enemy.defensePoint)
        print('After being attacked by {0}, {1} has a remaining healthPoint of {2}'.format(self.name,enemy.name,enemy.healthPoint))
        return enemy.healthPoint
Naruto = Ninja('Naruto','Leaf',11,7,4)
Gaara = Ninja('Gaara','Sand',12,6,8)
Zabura = Ninja('Zabura','Fog',9,8,3)
Deidara = Ninja('Deidara','Rock',8,10,1)

# Turn 1:
Naruto.attack(Gaara)
Zabura.attack(Naruto)
Gaara.attack(Deidara)
Deidara.attack(Zabura)


