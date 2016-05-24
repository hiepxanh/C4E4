class Ninja:
    def __init__(self,name,village,healthPoint,attackPoint,defensePonit):
        self.name=name
        self.village=village
        self.healthPoint=healthPoint
        self.attacPoint=attackPoint
    def attack(self,enemy):
        ninja_name = self.name
        enemy_name = enemy.name
        ninja_village = self.village
        enemy_village = enemy.village
        ninja_hp = self.healthPoint
        enemy_hp = enemy.heathPoint
        ninja_atk = self.attackPoint
        enemy_atk = enemy.attackPoint
        ninja_def = self.defensePoint
        enemy_def = enemy.defensePoint

        if ninja_atk < enemy_def:
            print (ninja_name, "can not attack", enemy_name)
            # print("\t",ninja_name,"HP =",ninja_hp)
            print("\t" + enemy_name + "'s HP is still " + str(enemy_hp))
        else:
            enemy_hp = enemy_hp - (ninja_atk - enemy_def)
            print(ninja_name, "attacks", enemy_name)
            # print("\t",ninja_name,"HP =",ninja_hp)
            print("\t" + enemy_name + "'s remaining HP is " + str(enemy_hp))
        return enemy_hp

        naruto = Ninja("Naruto", "Leaf", 11, 7, 4)
        gaara = Ninja("Gaara", "Sand", 12, 6, 8)
        zabuza = Ninja("Zubuza", "Fog", 9, 8, 3)
        deidara = Ninja("Deidara", "Rock", 8, 10, 1)

        print("Before Combat:")
        print("\t" + Naruto.name + "'s HP is " + str(Naruto.healthPoint))
        print("\t" + Gaara.name + "'s HP is " + str(Gaara.healthPoint))
        print("\t" + Zabuza.name + "'s HP is " + str(Zabuza.healthPoint))
        print("\t" + Deidara.name + "'s HP is " + str(Deidara.healthPoint))

        print("")

        print("In Combat:")
        Naruto.attack(gaara)
        Zabuza.attack(naruto)
        Gaara.attack(deidara)
        Deidara.attack(zabuza)
        Naruto.attack(zabuza)