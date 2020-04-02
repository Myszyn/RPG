from classes.game import Person, bcolors



magic = [{"name":"fire","cost":10,"dmg":50},
         {"name":"zap","cost":20,"dmg":150},
         {"name":"earthquake","cost":13,"dmg":75}]

player = Postac(50,500,75,10,magic)
enemy = Postac(40,2000,50,30,magic)


game = True
print("An enemy attack")

while(game):
    print("======================================")
    player.choose_action()
    choice = input("choose action")
    number = int(choice)-1
    print("you choose ",player.actions[number])

    if number == 0:
        dmg = player.generate_dmg()
        enemy.take_dmg(dmg)
        print("you attack for",dmg, "life points. Enemy life: ", enemy.get_hp())

    enemy_choice = 1

    enemy_dmg = enemy.generate_dmg()
    player.take_dmg(enemy_dmg)
    print("Enemy attack for",enemy_dmg,"life point. Your life: ",player.get_hp())
