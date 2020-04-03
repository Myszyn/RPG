import random

class Spell:
    def __init__(self,name,cost,dmg,type):
        self.name=name
        self.cost = cost
        self.dmg = dmg
        self.hdmg  = dmg + 20
        self.ldmg = dmg - 20
        self.type = type
    def generate_damage(self):
        return random.randrange(self.ldmg,self.hdmg)


    




