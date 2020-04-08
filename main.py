from classes.game import Person, bcolors
from classes.magic import Spell
from classes.item import Armor, Items
import random



#dark magic(attack)█
normalius = Spell("normalius",0,random.randrange(50,100),"dark",0)
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
helmet = Armor("helmet     ",0,100,0,10,0)
sword = Armor("sword      ",15,110,5,0,0)
wand = Armor("wand       ",10,0,110,0,30)
wizard_hat = Armor("wizard hat ",0,110,5,5,10)
speed_boots = Armor("speed boots",0,210,15,5,0)
chest = Armor("chest      ",0,300,2,20,0)

items =[potion,hipotion,megaelixer,granade,glass_cannon]
enemy_speel=[fire,zap,blizzard,heal,normalius]

#persons
#antek mage
player1 = Person("Antek ",50,500,75,10,[fire,zap,blizzard,heal,healius,poison],10,[wand,wizard_hat,speed_boots],items)
#franek warior
player2= Person("Franek",20,800,40,10,[fire,zap,blizzard,heal,healius,poison],10,[wizard_hat,speed_boots],items)
#james assasin
player3 = Person("James ",70,300,20,10,[fire,zap,blizzard,heal,healius,poison],25,[wand,wizard_hat,speed_boots],items)
#clik healer
player4= Person("Clik  ",30,600,75,10,[fire,zap,blizzard,heal,healius,poison],10,[wand,wizard_hat,speed_boots],items) 

players = [player1,player2,player3,player4]


#======================ENEMIES===================
enemy1 = Person("Demon ",500,1000,50,30,enemy_speel,3,[],[])
enemy2 = Person("Imp   ",100,750,100,30,enemy_speel,3,[],[])
enemy3 = Person("devil ",100,750,100,30,enemy_speel,3,[],[])

enemies =[enemy1,enemy2,enemy3]
print("GET READY FOR THE BATTLE")
def choice_eq():
    for player in players:

        print(player.name,"\n")
        player.choose_armor()
    
        choice = int(input("Choose armor :"))-1

        check_number =len(player.armor)
        if choice>=check_number:
              print("Wrong numer")
              item_choice =1 
              choice_eq()   
        
       armor_choice = player.armor[choice]
        print("You choose ",armor_choice.name)
        player.receive_armor(armor_choice)




choice_eq()


print("==============================")


turn = 0



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
    deafeated_enemies=0
    deafeated_players=0
    if len(enemies)==0:
                print("You win")
                break
    if len(players)==0:
                print("You lose")
                break
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
            if len(enemies)==0:
                print("You win")
                break
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
            if enemies[enemy].get_hp()==0:
                 print(enemies[enemy].name.replace(" ",""),"is dead")
                 del enemies[enemy]
            for enemy in enemies:
                 if enemy.hp == 0:
                     deafeated_enemies +=1 
                     del enemy
                 if len(enemies)==0:
                    print("You win")
                    break
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
                print("You attack",enemies[enemy].name.replace(" ","") ,"enemy for",spell.dmg,"life point. Enemy Life", enemies[enemy].get_hp())
                print("===================================================== \n")
            elif spell.type=="light":
                player.reduce_mp(spell.cost)
                player.heal(spell_dmg)
                print("you heal yourself for",spell.dmg,"life point. Your Life", player.get_hp())
                print("===================================================== \n")
            elif spell.type=="poison":
                poisoned = player.choose_target(enemies)
                player.reduce_mp(spell.cost)
                print("You choose poison. Poison will deal damage to",enemies[poisoned].name.replace(" ",""),"for 5 turns")
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
            print("===================================================== \n")
            item_dmg = item.generate_item_dmg()
            enemy = player.choose_target(enemies)
            print("===================================================== \n")
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
                    print("You hit",enemies[enemy].name.replace(" ",""),"for",glass_points-300,"with glass cannon")
                    print("===================================================== \n")
                else:
                    player.take_dmg(glass_points)
                    print("You hit yourself for",glass_points,"with glass cannon")
                    print("===================================================== \n")
            if enemies[enemy].get_hp()==0:
                print(enemies[enemy].name.replace(" ",""),"is dead")
                del enemies[enemy]

            item.reduce_item_quantity()
            if item.quantity==0:
                remove = player.items
                remove.remove(item)
            if item_choice==-1:
                continue
            for enemy in enemies:
                if enemy.hp == 0:
                    deafeated_enemies +=1        
                if len(enemies)==0:
                    print("You win")
                    break

#================================POISON==========================================
#TODO add multiple number of poisoned enemy
        if turn>0:
            poison_dmg =poison.generate_damage()
            print("poison deal",poison_dmg,"damage for",enemies[poisoned].name ,". turns left: ",turn)
            print("===================================================== \n")
            enemies[poisoned].take_dmg(poison_dmg)
            turn-=1
            if enemies[poisoned].get_hp()==0:
                    print(enemies[poisoned].name.replace(" ",""),"is dead")
                    del enemies[poisoned]

#===================================ENEMY=========================================

    for enemy in enemies:
       
        choice = random.randrange(0,2)
        for player in players:
            if player.hp == 0:
                deafeated_players +=1
        if choice==0:
            if player.dodge_chance():
                if enemy.hp>0:
                    target = random.randrange(0,len(players))
                    enemy_dmg = enemy.generate_dmg()
                    players[target].take_dmg(enemy_dmg)
                    print(enemy.name.replace(" ",""),"attack",players[target].name.replace(" ","") ,"for",enemy_dmg,"life point. Your life: ",players[target].get_hp())
                    if players[target].get_hp()==0:
                        print(players[target].name.replace(" ",""),"is dead.")
                        del players[target]
                        break
            else:
                print("you dodge",enemy.name.replace(" ",""),"'s"," attack")
        elif choice ==1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            if spell.type=="dark":
                enemy.reduce_mp(spell.cost)
                target = random.randrange(0,len(players))
                players[target].take_dmg(magic_dmg)
                print(enemy.name.replace(" ",""),"attacks",players[target].name,"with",spell.name,"for",spell.dmg,)
               

                if players[target].get_hp()==0:
                    print(players[target].name.replace(" ",""),"is dead.")
                    del players[target]
            elif spell.type=="light":
                enemy.reduce_mp(spell.cost)
                enemy.heal(magic_dmg)
                print (enemy.name.replace(" ",""),"heals yourself for",spell.dmg,"life point.",enemy.name ," Life", player.get_hp())
                

        #elif choice ==2:

    if len(enemies)==deafeated_enemies:
        print("You win")
        game = False
    if len(players)==0:
        print("You lose")
        game = False
