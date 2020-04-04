from classes.game import Person, bcolors
from classes.magic import Spell
from classes.item import Armor, Items

"""
print("\n\n")
print("NAME                        HP                             MP")
print("                             _________________________     __________")
print("Gopis:     500/500          [                         ]   [          ]")

print("                             _________________________     __________")
print("Gopis:     500/500          [                         ]   [          ]")

print("                             _________________________     __________")
print("Gopis:     500/500          [████████████             ]   [          ]")
"""
#dark magic(attack)██████████
fire = Spell("fire",20,150,"dark")
zap = Spell("zap",10,50,"dark")
earthquake = Spell("earthquake",5,40,"dark")
blizzard = Spell("blizzard",13,75,"dark")
apocalipto = Spell("apocalipto",50,300,"dark")

#light magic(heal)
heal = Spell("heal",10,75,"light")
healius = Spell("healius",25,250,"light")


#heal items
potion = Items("potion","potion","heal for 50 hp",50,3)
hipotion = Items("hipotion","potion","heal for 100 hp",100,2)

megaelixer = Items("megaelixer","elixer","fully restores HP/MP of one party member",9999,1)
hielixer = Items("hielixer","elixer","fully restores party members HP/MP",9999,1)

#attack items
granade= Items("granade","attack","attack for 500 hp",500,2)




#items(armor)TODO
helmet = Armor("helmet",0,100,0,10,0)
sword = Armor("sword",15,0,5,0,0)
wand = Armor("wand",10,0,0,0,30)
wizard_hat = Armor("wizard hat",0,0,5,5,10)
speed_boots = Armor("speed boots",0,20,15,5,0)
chest = Armor("chest",0,300,2,20,0)

items =[potion,hipotion,megaelixer,granade]

#persons
player = Person(50,500,75,10,[fire,zap,blizzard,heal,healius],10,[],items) 
enemy = Person(40,1200,50,30,[],3,[],[])


print("==============================")



player_hp = player.get_hp()
enemy_hp = enemy.get_hp()
player_atc = player.get_atc()
enemy_atc = enemy.get_atc()

game = True
print("An enemy attack")
enemy.generate_information()
print("Your Stats:")
player.generate_information()


while(game):
    print("======================================")
    player.choose_action()
    choice = input("Choose action :")
    number = int(choice)-1
    print("you choose ",player.actions[number])
#=======================================ATTACK========================================
    if number == 0:
        dmg = player.generate_dmg()
        if enemy.dodge_chance():
            enemy.take_dmg(dmg)
            print("you attack for",dmg, "life points. Enemy life: ", enemy.get_hp())
        else:
            print("enemy dodge the attack")
#======================================MAGIC==========================================
    if number == 1:
        print("You have ",player.get_mp(),"magic points")
        player.choose_magic()
        magic_choose = int(input("choose magic: "))-1
        if magic_choose==-1:
            continue
       
       
        spell = player.magic[magic_choose]
        spell_dmg = spell.generate_damage()

  
        if spell.cost>player.mp:
            print("not enough mp")
            continue
        if spell.type=="dark":
            player.reduce_mp(spell.cost)
            enemy.take_dmg(spell_dmg)
            print("You attack enemy for",spell.dmg,"life point. Enemy Life", enemy.get_hp())
        elif spell.type=="light":
            player.reduce_mp(spell.cost)
            player.heal(spell_dmg)
            print("you heal yourself for",spell.dmg,"life point. Your Life", player.get_hp())

#===================================ITEMS=======================================

    if number==2:
        if len(player.items)==0:
            print("You dont have any item")
            continue
        player.choose_items()
        item_choice = int(input("Choose item : "))-1
        item = player.items[item_choice]
        item_dmg = item.generate_item_dmg()
        if item.type=="potion":
            player.heal(item_dmg)
            print("You heal yourself with", item.name,"for",item_dmg,"hp")
        if item.type=="attack":
            enemy.take_dmg(item_dmg)
            print("You attack enemy with", item.name,"for",item_dmg)
        if item.type=="elixer":
            player.hp = player.mhp
            player.mp = player.mmp
            print("Fully restores mp/hp")
        item.reduce_item_quantity()
        if item.quantity==0:
            remove = player.items
            remove.remove(item)
        if item_choice==-1:
            continue

#===================================ENEMY=========================================
    enemy_choice = 1

    if player.dodge_chance():
        enemy_dmg = enemy.generate_dmg()
        player.take_dmg(enemy_dmg)
        print("Enemy attack for",enemy_dmg,"life point. Your life: ",player.get_hp())
    else:
        print("you dodge the attack")

    print("===========================================")
    print("Your hp: ",player.get_hp(),"/",player.mhp)
    print("Enemy hp: ",enemy.get_hp(),"/",enemy.mhp)

    if player.get_hp()==0:
        print("You lose")
        break
    if enemy.get_hp()==0:
        print("You win")
        break
    
    
