import random


class Armor:
    def __init__(self,name,atc,hp,dodge,df,mp):
        self.atc = atc
        self.hp = hp
        self.dodge = dodge
        self.df = df
        self.mp = mp
        self.name = name

 

   
class Items:
    def __init__(self,name,type,description,prop,quantity):
        self.type= type
        self.name = name
        self.description=description
        self.prop= prop
        self.quantity=quantity

    def generate_item_dmg(self):
        return self.prop

    def reduce_item_quantity(self):
         self.quantity-=1
