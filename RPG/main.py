from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 12, 120, "black")
blizzard = Spell("Blizzard", 11, 110, "black")
meteor = Spell("Meteor", 20, 200, "black")

# create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# create items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one member", 9999)
# hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_item = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
               {"item": superpotion, "quantity": 1},
               {"item": elixer, "quantity": 10},
              # {"item": hielixer, "quantity": 2},
               {"item": grenade, "quantity": 1}, ]

player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura],
                player_item)
enemy = Person(1200, 65, 45, 25, [], [])

running = True

print(bcolors.FAIL + "An Enemy Attacks!!" + bcolors.ENDC)
while running:

    print("\n")

    player.player_stats()

    print("=================================================")
    player.choose_action()
    choice = input("Choose Action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_dmg(dmg)
        print(bcolors.OKGREEN + "You have attacked for ", str(dmg), " points of damage." + bcolors.ENDC)

    # if player chose Magic option
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic: ")) - 1

        # allows us to go back if we choose the wrong menu
        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_spell_dmg()

        if spell.cost > player.get_mp():
            print(bcolors.FAIL + "Sorry! You're out of magic points." + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)
        if spell.type is "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "You used " + spell.name, str(magic_dmg),
                  " healed" + bcolors.ENDC)
        elif spell.type is "black":
            enemy.take_dmg(magic_dmg)
            print(bcolors.OKGREEN + "You used spell and attacked for ", str(magic_dmg),
                  " points of damage." + bcolors.ENDC)

    # if player chose Item option
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose an Item: ")) - 1
        # allows us to go back
        if item_choice == -1:
            continue

        item = player.items[item_choice]["item"]

        if player.items[item_choice]["quantity"] == 0:
            print(bcolors.FAIL + "None left!" + bcolors.ENDC)
            continue

        if item.type is "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + item.name + " heals for " + str(item.prop), "HP" + bcolors.ENDC)
        elif item.type is "elixer":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN + "Fully Restored HP/MP" + bcolors.ENDC)

        elif item.type == "attack":
            enemy.take_dmg(item.prop)
            print(bcolors.FAIL + item.name + " deals", str(item.prop), "points of damage" + bcolors.ENDC)

        player.items[item_choice]["quantity"] -= 1

    enemy_choice = 1
    enemey_dmg = enemy.generate_damage()
    player.take_dmg(enemey_dmg)
    print(bcolors.FAIL + "Enemy attacked for ", str(enemey_dmg), " points of damage." + bcolors.ENDC)

    print("--------------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC)

    print("Your HP:", bcolors.FAIL + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC)
    print("Your MP:", bcolors.FAIL + str(player.get_mp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You Win" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You were defeated" + bcolors.ENDC)
        running = False
