class Ninja:
    def __init__(self,name,village,healthPoint,attackPoint,defensePoint):
        self.name=name
        self.village=village
        self.healthPoint = healthPoint
        self.attackPoint = attackPoint
        self.defensePoint = defensePoint
    def attack(self,enemy):
        HPb = enemy.healthPoint
        DEFb = enemy.defensePoint
        ATKa = self.attackPoint
        return(HPb-(ATKa - DEFb))
naruto = Ninja("Naruto","Leaf",11,7,4)
gaara = Ninja("Gaara","Sand",12,6,8)
zabuza = Ninja("Zabuza","Fog",9,8,3)
deidara = Ninja("Deidara","Rock",8,10,1)

print(naruto.attack(gaara))
# Naruto danh gaara tang mau 