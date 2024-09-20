from cards import Spell, Minion
from player import Player
from setup import Game

def main():
    print("Welcome to HearthStone, text version.\n")
    turn = 1
    
    cards_list_1 = [
        Spell("Fireball", 4, "Fire", "Deal 6 damage"),
        Spell("Polymorph", 4, "Arcane", "Transform a minion into a 1/1 Sheep"),
        Spell("Flamestrike", 7, "Fire", "Deal 5 damage to all enemy minions"),
        Spell("Arcane Intellect", 3, "Arcane", "Draw 2 cards"),
        Spell("Holy Nova", 3, "Holy", "Deal 2 damage to all enemy minions. Restore 2 Health to all friendly characters"),
        Spell("Cataclysm", 5, "Fire", "Destroy all minions. Discard 2 cards"),
        Spell("Deadly Shot", 3, "Spell", "Destroy a random enemy minion"),
        Minion("Stormwind Champion", 7, 6, 6, "Your other minions have +1/+1", False),
        Minion("Chillwind Yeti", 4, 4, 5, "n/a", False),
        Minion("Bloodfen Raptor", 2, 3, 2, "n/a", False),
        Minion("Boulderfirst Ogre", 6, 6, 7, "n/a", False),
        Minion("Booty Bay Bodyguard", 5, 5, 4, "Taunt", False),
        Minion("Wolfrider", 3, 3, 1, "Charge", False),
        Minion("Spymistress", 1, 3, 1, "Stealth", True)
        ]
    cards_list_2 = [
        Spell("Fireball", 4, "Fire", "Deal 6 damage"),
        Spell("Polymorph", 4, "Arcane", "Transform a minion into a 1/1 Sheep"),
        Spell("Flamestrike", 7, "Fire", "Deal 5 damage to all enemy minions"),
        Spell("Arcane Intellect", 3, "Arcane", "Draw 2 cards"),
        Spell("Holy Nova", 3, "Holy", "Deal 2 damage to all enemy minions. Restore 2 Health to all friendly characters"),
        Spell("Cataclysm", 5, "Fire", "Destroy all minions. Discard 2 cards"),
        Spell("Deadly Shot", 3, "Spell", "Destroy a random enemy minion"),
        Minion("Stormwind Champion", 7, 6, 6, "Your other minions have +1/+1", False),
        Minion("Chillwind Yeti", 4, 4, 5, "n/a", False),
        Minion("Bloodfen Raptor", 2, 3, 2, "n/a", False),
        Minion("Boulderfirst Ogre", 6, 6, 7, "n/a", False),
        Minion("Booty Bay Bodyguard", 5, 5, 4, "Taunt", False),
        Minion("Wolfrider", 3, 3, 1, "Charge", False),
        Minion("Spymistress", 1, 3, 1, "Stealth", True)
        ]
    
    player_1_name = input("First player name: ")
    player_2_name = input("Second player name: ")
    print("\n Drawing cards...\n")

    player_1 = Player(player_1_name, cards_list_1)
    player_2 = Player(player_2_name, cards_list_2)

    print(f"{player_1_name}'s starting hand: ")
    player_1.draw_starting_hand()
    print()
    print(f"{player_2_name}'s starting hand: ")
    player_2.draw_starting_hand()

    print(f"\n{player_2.name}'s extra card: ")
    Game.draw_card(player_2.deck, player_2.hand)

    while True:
        Game.set_mana_crystals(player_1, player_2, turn) #set mana crystals based on turn
        print(f"\nIT IS NOW TURN {turn}.")
        print ('{:-^72}'.format(" " + player_1.name + '\'s TURN '))
        print()
        player_1.take_turn(player_2)
        print ('{:-^72}'.format(" " + player_2.name + '\'s TURN '))
        print()
        player_2.take_turn(player_1)
        turn += 1
    
if __name__ == "__main__":
    main()