class Ninja:
  def __init__(self, name, village, healthPoint,attackPoint, defensePoint):
    self.name = name
    self.village = village
    self.healthPoint = healthPoint
    self.attackPoint = attackPoint
    self.defensePoint = defensePoint
  def attack(self,enemy):
    ninja_name = self.name
    enemy_name = enemy.name
    ninja_village = self.village
    enemy_village = enemy.village
    ninja_hp = self.healthPoint
    enemy_hp = enemy.healthPoint
    ninja_atk = self.attackPoint
    enemy_atk = enemy.attackPoint
    ninja_def = self.defensePoint
    enemy_def = enemy.defensePoint

    if ninja_atk < enemy_def:
             print(ninja_name, "can not attack", enemy_name)
             print("\t" + enemy_name + "'s HP is still " + str(enemy_hp))
    else:
             enemy_hp = enemy_hp - (ninja_atk - enemy_def)
             print(ninja_name, "attacks", enemy_name)
  # print("\t",ninja_name,"HP =",ninja_hp)
             print("\t" + enemy_name + "'s remaining HP is " + str(enemy_hp))
    return enemy_hp

naruto = Ninja("Naruto","Leaf",11,7,4)
gaara = Ninja("Gaara","Sand",12,6,8)
zabuza = Ninja("Zabuza", "Fog", 9,8,3)
deidara = Ninja("Deidara", "Rock", 8,10,1)
naruto.attack(gaara)
print("")
zabuza.attack(naruto)
print("")
# print("Before Combat:")
# print("\t" + naruto.name + "'s HP is " + str(naruto.healthPoint))
# print("\t" + gaara.name + "'s HP is " + str(gaara.healthPoint))
# print("\t" + zabuza.name + "'s HP is " + str(zabuza.healthPoint))
# print("\t" + deidara.name + "'s HP is " + str(deidara.healthPoint))
# print("")
#
# print("In Combat:")
# naruto.attack(gaara)
# zabuza.attack(naruto)
# gaara.attack(deidara)
# deidara.attack(zabuza)
# naruto.attack(zabuza)
#
