import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self,atc, hp, mp, df, magic, dodge):
        self.atc = atc
        self.atkl = atc-10
        self.atkh =  atc+10
        self.hp = hp
        self.mhp = hp
        self.mp = mp
        self.mmp = mp
        self.df = df
        self.magic = magic
        self.actions = ["Attack ","Magic"]
        self.dodge = dodge
    def generate_dmg(self):
        return random.randrange(self.atkl,self.atkh)
    def generate_spelldmg(self,i):
        mgl = self.magic[i]["dmg"]-5
        mgh = self.magic[i]["dmg"]+5
        return random.randrange(mgl,mgh)
    def dodge_chance(self):
        chance = random.randrange(1,100)
        if self.dodge<chance:
            return True
        else:
            return False      
    def take_dmg(self,dmg):
        self.hp-=dmg
        if self.hp<0:
            self.hp=0
        return self.hp
    def get_hp(self):
        return self.hp
    def get_mp(self):
        return self.mp
    def get_atc(self):
        return self.atc
    def reduce_mp(self,cost):
        self.mp-=cost
        if self.mp<0:
            self.mp=0
    def get_spell(self,i):
        return self.magic[i]["name"]
    def get_spell_mp_cost(self,i):
        return self.magic[i]["cost"]
    def choose_action(self):
        i=1
        print("ACTIONS")
        for item in self.actions:
            print(str(i),":",item)
            i+=1
    def choose_magic(self):
        print("MAGIC")
        i = 1 
        for spell in self.magic:
            print(str(i),":",spell["name"],"cost:",str(spell["cost"]),"damage:",str(spell["dmg"]))
            i+=1 
    def generate_information(self,atc,hp):
        print(hp , " life points","/",atc,"attack points")






