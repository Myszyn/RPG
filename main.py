from classes.game import Postac, bcolors



magic = [{"name":"fire","cost":10,"dmg":50},
         {"name":"zap","cost":20,"dmg":150},
         {"name":"earthquake","cost":13,"dmg":75}]

player = Postac(50,500,75,10,magic)
enemy = Postac(40,2000,50,30,magic)


gra = True
print("wróg atakuje")

while(gra):
    print("======================================")
    player.choose_action()
    choice = input("wybierz akcje")
    liczba = int(choice)-1
    print("wybrales ",player.actions[liczba])

    if liczba == 0:
        dmg = player.generate_dmg()
        enemy.take_dmg(dmg)
        print("zaatakowales za",dmg, "punktow zycia. Zycie wroga: ", enemy.get_hp())

    enemy_choice = 1

    enemy_dmg = enemy.generate_dmg()
    player.take_dmg(enemy_dmg)
    print("wrog zaatakowal za",enemy_dmg,"punktow zycia. Twoje życie: ",player.get_hp())