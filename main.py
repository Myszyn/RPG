from classes.game import Person, bcolors
from classes.magic import Spell




#dark magic(attack)
fire = Spell("fire",20,150,"dark")
zap = Spell("zap",10,50,"dark")
earthquake = Spell("earthquake",5,40,"dark")
blizzard = Spell("blizzard",13,75,"dark")
apocalipto = Spell("apocalipto",50,300,"dark")

#light magic(heal)
heal = Spell("heal",10,50,"light")
healius = Spell("healius",25,225,"light")



player = Person(50,500,75,10,[fire,zap,blizzard,heal],10)
enemy = Person(40,1200,50,30,[],3)

player_hp = player.get_hp()
enemy_hp = enemy.get_hp()
player_atc = player.get_atc()
enemy_atc = enemy.get_atc()

game = True
print("An enemy attack")
enemy.generate_information(enemy_atc,enemy_hp)
print("Your Stats:")
player.generate_information(player_atc,player_hp)


while(game):
    print("======================================")
    player.choose_action()
    choice = input("choose action")
    number = int(choice)-1
    print("you choose ",player.actions[number])

    if number == 0:
        dmg = player.generate_dmg()
        if enemy.dodge_chance():
            enemy.take_dmg(dmg)
            print("you attack for",dmg, "life points. Enemy life: ", enemy.get_hp())
        else:
            print("enemy dodge the attack")
    if number == 1:
        print("You have ",player.get_mp(),"magic points")
        player.choose_magic()
        magic_choose = int(input("choose magic: "))-1
       
       
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
    
