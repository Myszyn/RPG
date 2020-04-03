from classes.game import Person, bcolors



magic = [{"name":"fire","cost":10,"dmg":50},
         {"name":"zap","cost":20,"dmg":150},
         {"name":"earthquake","cost":13,"dmg":75}]

player = Person(50,500,75,10,magic,10)
enemy = Person(40,1200,50,30,magic,3)

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
        magic_dmg = player.generate_spelldmg(magic_choose)
        enemy.take_dmg(magic_dmg)
        mp_cost = player.get_spell_mp_cost(magic_choose)
        player.reduce_mp(mp_cost)
        print("You attack enemy for",magic_dmg,"life point. Enemy Life", enemy.get_hp())
    enemy_choice = 1

    if player.dodge_chance():
        enemy_dmg = enemy.generate_dmg()
        player.take_dmg(enemy_dmg)
        print("Enemy attack for",enemy_dmg,"life point. Your life: ",player.get_hp())
    else:
        print("you dodge the attack")

    if player.get_hp()==0:
        print("You lose")
        break
    if enemy.get_hp()==0:
        print("You win")
        break
    
