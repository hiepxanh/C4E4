class Ninja:
    def __init__(self,name, village, healthpoint, attackpoint, defensepoint):
        self.name = name
        self.village = village
        self.healthpoint=healthpoint
        self.attackpoint=attackpoint
        self.defensepoint=defensepoint
    def attack(self,enemy):
        if self.attackpoint > enemy.defensepoint:
            enemy.healthpoint = enemy.healthpoint -(self.attackpoint - enemy.defensepoint)
            print(self.name, ": ", self.healthpoint, "\n", enemy.name, ": ", enemy.healthpoint)
            return enemy.healthpoint

        else:
            print(self.name, ": ", self.healthpoint, "\n", enemy.name, ": ", enemy.healthpoint)



Naruto = Ninja("Naruto", "Leaf", 11, 7, 4)
Gaara = Ninja("Gaara", "Sand", 12, 6, 8)
Zabuza = Ninja("Zabuza", "Fog", 9, 8, 3)
Deidara = Ninja("Deidara", "Rock", 8, 10, 1)

# Naruto.attack(Gaara)
#
# Zabuza.attack(Naruto)
#
# Gaara.attack(Deidara)
#
# Deidara.attack(Zabuza)

for x in range (4):
    Naruto.attack(Gaara)
    Zabuza.attack(Naruto)
    Gaara.attack(Deidara)
    Deidara.attack(Zabuza)

