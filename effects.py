import random
from setup import Game

#classes for minion and spell effects

class MinionEffects: #class for each minion's effects (not including basic taunt, charge, stealth)
    def activate_1(player): #stormwind champion
        for m in player.battlefield.minions:
            if m.name != "Stormwind Champion":
                m.attack += 1
                m.health += 1
        print("Stormwind Champion's effect has been activated.")
    def deactivate_1(player): #deactivate stormwind champion
        for m in player.battlefield.minions:
            if m.name != "Stormwind Champion":
                m.attack -= 1
                m.health -= 1
                if m.health <= 0:
                    player.battlefield.remove_minion(m)
                    print(f"Since Stormwind Champion's effect has been deactivated, {player.name}'s {m.name} has fallen.")

class SpellEffects: #class for each spell's effects
    def fireball(player, opponent):
        opponent.battlefield.display_battlefield(opponent)
        fireball_choice = int(input("Type the index of the minion that will be attacked by the fireball, or type '-1' to attack the opponent's hero: "))
        if fireball_choice >= 0:
            opponent.battlefield.minions[fireball_choice].health -= 6
            print(f"The fireball hit {opponent.battlefield.minions[fireball_choice].name}, and it now has {opponent.battlefield.minions[fireball_choice].health} health left.")
            opponent.battlefield.minion_death(opponent, opponent.battlefield.minions[fireball_choice]) #check minion death
        else:
            opponent.hero_health -= 6
            print(f"The fireball hit {opponent.name}'s hero, and the hero now has {opponent.hero_health} health left.")
            Game.check_end_game(player, opponent) #check hero death
    def polymorph(opponent):
        opponent.battlefield.display_battlefield(opponent)
        sheep_choice = int(input("Type the index of the minion that will transtorm into a sheep: "))
        sheeped_minion = opponent.battlefield.minions[sheep_choice]
        print(f"{opponent.name}'s {sheeped_minion.name} has turned into a 1/1 Sheep.")
        sheeped_minion.transform("Sheep", 1, 1) #turn to sheep!
    def flamestrike(opponent):
        print(f"{opponent.name}'s battlefield has been hit with a flamestrike!")
        for minion in opponent.battlefield.minions[:]:
            minion.health -= 5
            opponent.battlefield.minion_death(opponent, minion)
    def arcane_intellect(player):
        print(f"{player.name} has drawn 2 cards using Arcane Intellect.")
        Game.draw_card(player.deck, player.hand)
        Game.draw_card(player.deck, player.hand)
    def holy_nova(player, opponent):
        print(f"All of {opponent.name}'s minions have been damaged, and health of {player.name}'s minions have been restored.")
        for minion in player.battlefield.minions:
            minion.health += 2
        for minion in opponent.battlefield.minions[:]:
            minion.health -= 2
            opponent.battlefield.minion_death(opponent, minion)
    def cataclysm(player, opponent):
        for m in player.battlefield.minions[:]:
            player.battlefield.remove_minion(m)
        for m in opponent.battlefield.minions[:]:
            opponent.battlefield.remove_minion(m)
        print("All minions have been destroyed.")
        player.hand.display_hand(player)
        for _ in range(0, 2):
            choice = int(input("Type the index of the card you would like to discard: "))
            print(f"{player.hand.cards[choice].name} has been discarded.")
            player.hand.cards.pop(choice)
        print("The cataclysm has destroyed all minions and two cards.")
    def deadly_shot(opponent):
        dead_minion = random.choice(opponent.battlefield.minions)
        opponent.battlefield.remove_minion(dead_minion)
        print(f"{opponent.name}'s {dead_minion.name} has been destroyed.")