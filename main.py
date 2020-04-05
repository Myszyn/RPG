from classes.game import Person, bcolors
from classes.magic import Spell
from classes.item import Armor, Items
import random



#dark magic(attack)█

fire = Spell("fire",20,150,"dark",0)
zap = Spell("zap",10,50,"dark",0)
earthquake = Spell("earthquake",5,40,"dark",0)
blizzard = Spell("blizzard",13,75,"dark",0)
apocalipto = Spell("apocalipto",50,300,"dark",0)

#light magic(heal)
heal = Spell("heal",10,75,"light",0)
healius = Spell("healius",25,250,"light",0)

#poison magic(damage per turn)
poison = Spell("poison",20,40,"poison",5)


#heal items
potion = Items("potion","potion","heal for 50 hp",50,3)
hipotion = Items("hipotion","potion","heal for 100 hp",100,2)

megaelixer = Items("megaelixer","elixer","fully restores HP/MP of one party member",9999,1)
hielixer = Items("hielixer","elixer","fully restores party members HP/MP",9999,1)

#attack items
granade= Items("granade","attack","attack for 200 hp",500,2)

#attack-heal items
glass_cannon = Items("glass cannon","attheal","attack your enemy for 0-500 hp or hit you for 0-300 hp",0,2)


#items(armor)TODO
helmet = Armor("helmet",0,100,0,10,0)
sword = Armor("sword",15,0,5,0,0)
wand = Armor("wand",10,0,0,0,30)
wizard_hat = Armor("wizard hat",0,0,5,5,10)
speed_boots = Armor("speed boots",0,20,15,5,0)
chest = Armor("chest",0,300,2,20,0)

items =[potion,hipotion,megaelixer,granade,glass_cannon]

#persons
#antek mage
player1 = Person("Antek ",50,500,75,10,[fire,zap,blizzard,heal,healius,poison],10,[],items)
#franek warior
player2= Person("Franek",20,800,40,10,[fire,zap,blizzard,heal,healius,poison],10,[],items)
#james assasin
player3 = Person("James ",70,300,20,10,[fire,zap,blizzard,heal,healius,poison],25,[],items)
#clik healer
player4= Person("Clik  ",30,600,75,10,[fire,zap,blizzard,heal,healius,poison],10,[],items) 

players = [player1,player2,player3,player4]

enemy1 = Person("Demon ",40,3500,50,30,[],3,[],[])
enemy2 = Person("Imp   ",40,1500,100,30,[],3,[],[])
enemy3 = Person("devil ",40,1500,100,30,[],3,[],[])

enemies =[enemy1,enemy2,enemy3]




print("==============================")


turn = 0
"""
player_hp = player.get_hp()
enemy_hp = enemy.get_hp()
player_atc = player.get_atc()
enemy_atc = enemy.get_atc()
"""
game = True
print("An enemy attack")
for enemy in enemies:
    enemy.generate_information()
for player in players:
    player.generate_information()

"""
print("Your Stats:")
player.generate_information()
"""

while(game):
#=======================================ACTIONS=====================================
    print("==============================HEROES====================================")
    print("NAME                              HP                                 MP               ")
    for player in players:
        player.get_stats()
        print("\n")
    print("======================ENEMIES============================")
    print("\n")
    print("NAME                                               HP                                ")
    for enemy in enemies:
        enemy.get_enemy_stats()
        print("\n")

    print("===================================================== \n")
    for player in players:
        print(player.get_name()," :  \n")
        
    
        player.choose_action()
        choice = input("Choose action :")
        number = int(choice)-1
        check_number =len(player.items)
        if number+2>=check_number:
            print("Wrong number")
            continue

        print("you choose ",player.actions[number])
    
#=======================================ATTACK========================================
        if number == 0:
            enemy = player.choose_target(enemies)
            check_number =len(player.magic)
            dmg = player.generate_dmg()
            if enemies[enemy].dodge_chance():
                enemies[enemy].take_dmg(dmg)
                print("you attack",enemies[enemy].name,"for",dmg, "life points. Enemy life: ", enemies[enemy].get_hp())
                print("===================================================== \n")
            else:
                print("enemy dodge the attack")
                print("===================================================== \n")
#======================================MAGIC==========================================
        if number == 1:

            print("You have ",player.get_mp(),"magic points")
            player.choose_magic()
            magic_choose = int(input("choose magic: "))-1
            check_number =len(player.magic)
            if magic_choose>=check_number:
                print("Wrong numer")        
                continue
            if magic_choose==-1:
                continue
       
       

            spell = player.magic[magic_choose]
            spell_dmg = spell.generate_damage()

  
            if spell.cost>player.mp:
                print("not enough mp")
                continue
            if spell.type=="dark":
                player.reduce_mp(spell.cost)
                enemy = player.choose_target(enemies)
                enemies[enemy].take_dmg(spell_dmg)
                print("You attack",enemies[enemy].name ,"enemy for",spell.dmg,"life point. Enemy Life", enemies[enemy].get_hp())
                print("===================================================== \n")
            elif spell.type=="light":
                player.reduce_mp(spell.cost)
                player.heal(spell_dmg)
                print("you heal yourself for",spell.dmg,"life point. Your Life", player.get_hp())
                print("===================================================== \n")
            elif spell.type=="poison":
                poisoned = player.choose_target(enemies)
                player.reduce_mp(spell.cost)
                print("You choose poison. Poison will deal damage to",enemies[poisoned].name,"for 5 turns")
                turn = poison.get_spell_turn()
                print("===================================================== \n")
         

#===================================ITEMS=======================================

        if number==2:
            if len(player.items)==0:
                print("You dont have any item")
                continue

            player.choose_items()
            item_choice = int(input("Choose item : "))-1
            check_number =len(player.items)
            if item_choice>=check_number:
                print("Wrong numer")
                item_choice =1 
                continue
            item = player.items[item_choice]
            item_dmg = item.generate_item_dmg()
            enemy = player.choose_target(enemies)
            if item.type=="potion":
                player.heal(item_dmg)
                print("You heal yourself with", item.name,"for",item_dmg,"hp")
                print("===================================================== \n")
            if item.type=="attack":
                enemy =player.choose_target(enemies)
                enemies[enemy].take_dmg(item_dmg)
                print("You attack enemy with", item.name,"for",item_dmg)
                print("===================================================== \n")
            if item.type=="elixer":
                player.hp = player.mhp
                player.mp = player.mmp
                print("Fully restores mp/hp")
            if item.type=="attheal":
                glass_points = random.randrange(0,800)
                if glass_points>300:
                    enemies[enemy].take_dmg(glass_points-300)
                    print("You hit",enemies[enemy].name,"for",glass_points-300,"with glass cannon")
                    print("===================================================== \n")
                else:
                    player.take_dmg(glass_points)
                    print("You hit yourself for",glass_points,"with glass cannon")
                    print("===================================================== \n")

            item.reduce_item_quantity()
            if item.quantity==0:
                remove = player.items
                remove.remove(item)
            if item_choice==-1:
                continue
#================================POISON==========================================
#TODO add multiple number of poisoned enemy
        if turn>0:
            poison_dmg =poison.generate_damage()
            print("poison deal",poison_dmg,"damage for",enemies[poisoned].name ,". turns left: ",turn)
            enemies[poisoned].take_dmg(poison_dmg)
            turn-=1

#===================================ENEMY=========================================
    for enemy in enemies:

        if enemy.get_hp()==0:
            print("You win")
            break
        if player.dodge_chance():
            enemy_dmg = enemy.generate_dmg()
            player2.take_dmg(enemy_dmg)
            print(enemy.name,"attack for",enemy_dmg,"life point. Your life: ",player.get_hp())
        else:
            print("you dodge the attack")

        if player.get_hp()==0:
            print("You lose")
            break
