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
            return enemy.healthpoint
        else:
            return enemy.healthpoint
        print(self.name, ": ", self.healthpoint,"\n",enemy.name, ": ", enemy.healthpoint)


Naruto = Ninja("Naruto", "Leaf", 11, 7, 4)
Gaara = Ninja("Gaara", "Sand", 12, 6, 8)
Zabuza = Ninja("Zabuza", "Fog", 9, 8, 3)
Deidara = Ninja("Deidara", "Rock", 8, 10, 1)

Naruto.attack(Gaara)
Zabuza.attack(Naruto)
Gaara.attack(Deidara)
Deidara.attack(Zabuza)

# while True:
#     Naruto.attack(Gaara)
#     if Gaara.healthpoint<=0:
#         break
#     Zabuza.attack(Naruto)
#     if Naruto.healthpoint <=0:
#         break
#     Gaara.attack(Deidara)
#     if Deidara.healthpoint <=0:
#         break
#     Deidara.attack(Zabuza)
#     if Zabuza.healthpoint <=0:
#         break
