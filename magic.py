import random

class Spell:
    def __init__(self,name,cost,dmg,type,turn):
        self.name=name
        self.cost = cost
        self.dmg = dmg
        self.hdmg  = dmg + 20
        self.ldmg = dmg - 20
        self.type = type
        self.turn = turn
    def generate_damage(self):
        return random.randrange(self.ldmg,self.hdmg)
    def get_spell_dmg(self):
        return self.dmg
    def get_spell_turn(self):
        return self.turnself.hdmg)


    




