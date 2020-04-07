import random
from classes.magic import Spell
from classes.item import Armor, Items


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
    def __init__(self,name,atc, hp, mp, df, magic, dodge,armor,items):
        self.atc = atc
        self.atkl = atc-10
        self.atkh =  atc+10
        self.hp = hp
        self.mhp = hp
        self.mp = mp
        self.mmp = mp
        self.df = df
        self.magic = magic
        self.armor = armor
        self.actions = ["Attack ","Magic","Items"]
        self.dodge = dodge
        self.items = items
        self.name = name

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

    def heal(self,dmg):
        self.hp+=dmg
        if self.mhp<self.hp:
            self.hp=self.mhp
        
    def take_dmg(self,dmg):
        self.hp-=dmg
        if self.hp<0:
            self.hp=0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_name(self):
        return self.name

    def get_mp(self):
        return self.mp

    def get_atc(self):
        return self.atc

    def reduce_mp(self,cost):
        self.mp-=cost
        if self.mp<0:
            self.mp=0

    def choose_action(self):
        i=1
        print("ACTIONS")
        for item in self.actions:
            print(str(i),":",item)
            i+=1
#==========================CHOOSE_STH=============================================================
    def choose_magic(self):
        print("===================================================== \n")
        print("MAGIC")
        i = 1 
        for spell in self.magic:
            print(str(i),":",spell.name,"cost:",str(spell.cost),"damage:",str(spell.dmg))
            i+=1 

    def choose_armor(self):
        print("Choose armor")
        i=1
        for item in self.armor:
            print(str(i),":",armor.name,"attack:",str(armor.atc),"health points:",str(armor.hp))
            i+=1
    def choose_items(self):
        print("===================================================== \n")
        print("Choose items")
        i=1
        for items in self.items:
            print(str(i),":",items.name,"  :",str(items.description),"(x",items.quantity,")")
            i+=1
    def choose_target(self,enemies):
        print("===================================================== \n")
        print("Target")
        i=1
        for enemy in enemies:
            if enemy.hp!=0:
                print(str(i),": ",enemy.name)
                i+=1

        choice = int(input("choose target :"))-1

        return choice

   
#==========================================================================================================
    def generate_information(self):
        print(self.name, self.hp , " life points","/",self.atc,"attack points")
    def get_stats(self):
        hp_bar  = ""
        mp_bar  = ""
        hp_bar_ticks = (self.hp/self.mhp)*100/4
        mp_bar_ticks = (self.mp/self.mmp)*100/10
        while hp_bar_ticks>0:
            hp_bar+="█"
            hp_bar_ticks -=1
        while len(hp_bar)<25:
            hp_bar+=" "
        while mp_bar_ticks>0:
            mp_bar+="█"
            mp_bar_ticks -=1
        while len(mp_bar)<10:
            mp_bar+=" "

        hp_string= str(self.hp)+"/"+str(self.mhp)
        mp_string= str(self.mp)+"/"+str(self.mmp)
        current_hp = ''
        current_mp = ''
        if len(hp_string)<9:
            decreased = 9-len(hp_string)
            while decreased>0:
                hp_string+=" "
                decreased-=1
            #hp_string+=current_hp


        if len(hp_string)<9:
            decreased = 9-len(mp_string)
            while decreased>0:
                mp_string+=" "
                decreased-=1
            #mp_string+=current_mp


        print(self.name,":     ",hp_string,"[",hp_bar,"]  ", mp_string," [",mp_bar,"]","\n")


    def endturn_stats(self):
        print(self.name,"health points :", self.hp ,"/",self.mhp,"mana points :",self.mp,"/",self.mmp)

    def generate_information(self):
        print(self.name, self.hp , " life points","/",self.atc,"attack points")
    def get_enemy_stats(self):
        hp_bar  = ""
        mp_bar  = ""
        hp_bar_ticks = (self.hp/self.mhp)*100/2
        while hp_bar_ticks>0:
            hp_bar+="█"
            hp_bar_ticks -=1
        while len(hp_bar)<50:
            hp_bar+=" "

        hp_string= str(self.hp)+"/"+str(self.mhp)
        current_hp = ''
        if len(hp_string)<11:
            decreased = 11-len(hp_string)
            while decreased>0:
                hp_string+=" "
                decreased-=1
            #hp_string+=current_hp


        print(self.name,":     ",hp_string,"[",hp_bar,"]  ")
        def check_enemy_hp(self,enemy):
            if enemy.hp==0:
                return False
            if enemy.hp>0:
                return True
    def choose_enemy_spell(self):
        
        magic_choice = random.randrange(0,len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg  = spell.generate_damage()
        percent = self.hp/self.mhp * 100
        if self.mp < spell.cost or spell.type == "light" and percent>50 :
            spell = self.magic[4]
            magic_dmg  = spell.generate_damage()
            return spell, magic_dmg
            
        else:
            return spell, magic_dmg
        
