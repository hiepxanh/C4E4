
from firebase import firebase
from time import sleep
fb = firebase.FirebaseApplication('https://hiepxanh.firebaseio.com/user/',None)
while True:
    response = fb.get('/user', None)
    print(response)
    sleep(10)


# class Ninja:
#     def __init__(self, name, village, healthPoint,attackPoint, defensePoint):
#         self.name = name
#         self.village = village
#         self.healthPoint = healthPoint
#         self.attackPoint = attackPoint
#         self.defensePoint = defensePoint
#     def attack(self,enemy):
#         HPa = self.healthPoint
#         ATKb = enemy.attackPoint
#         DEFa = self.defensePoint
#         return (HPa - (ATKb - DEFa))
#
# Naruto = Ninja("Naruto","Leaf",11,7,4)
# Gaara = Ninja("Gaara","Sand",12,6,8)
# Zabuza = Ninja("Zabuza", "Fog", 9,8,3)
# Deidara = Ninja("Deidara", "Rock", 8,10,1)
#
# after_combat = Gaara.attack(Naruto)
# print ("HP Gaara: ",after_combat)
# after_combat = Naruto.attack(Zabuza)
# print ("HP Naruto: ", after_combat)
# after_combat = Deidara.attack(Gaara)
# print ("HP Deidara: ", after_combat)
# after_combat = Zabuza.attack(Deidara)
# print ("HP Zabuza: ", after_combat)