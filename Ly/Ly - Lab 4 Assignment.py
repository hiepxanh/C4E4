class Ninja:
    def __init__(self, name, village, healthPoint, attackPoint, defensePoint):
        self.name = name
        self.village = village
        self.healthPoint = healthPoint
        self.attackPoint = attackPoint
        self.defensePoint = defensePoint

    def attack(self, enemy):
        nameA = self.name
        nameB = enemy.name
        HPa = self.healthPoint
        HPb = enemy.healthPoint
        ATKa = self.attackPoint
        ATKb = enemy.attackPoint
        DEFa = self.defensePoint
        DEFb = enemy.defensePoint

        if ATKa < DEFb:
            print(nameA, "could not attack", nameB)
            HPb = HPb
        else:
            HPb = HPb - (ATKa - DEFb)
            print(nameA, "attacked", nameB)
        return HPb

Naruto = Ninja("Naruto", "Leaf", 11, 7, 4)
Gaara = Ninja("Gaara", "Sand", 12, 6, 8)
Zabuza = Ninja("Zabuza", "Fog", 9, 8, 3)
Deidara = Ninja("Deidara", "Rock", 8, 10, 1)

print("Before battle: ")
print("Gaara's HP: ", Gaara.healthPoint)
print("Naruto's HP: ", Naruto.healthPoint)
print("Deidara's HP: ", Deidara.healthPoint)
print("Zabuza's HP: ", Zabuza.healthPoint)

print("")

print("After battle: ")
print("Gaara's new HP: ", Naruto.attack(Gaara))
print("Naruto's new HP: ", Zabuza.attack(Naruto))
print("Deidara's new HP: ", Gaara.attack(Deidara))
print("Zabuza's new HP: ", Deidara.attack(Zabuza))
