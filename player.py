from effects import SpellEffects, MinionEffects
from board import Deck, Hand, Battlefield
from setup import Game

class Player:
    def __init__(self, name, cards):
        self.name = name
        self.deck = Deck(cards)
        self.hand = Hand()
        self.battlefield = Battlefield()
        self.mana_crystals = 1
        self.hero_health = 30
    def draw_starting_hand(self):
        self.deck.shuffle()
        for _ in range(0,3):
            Game.draw_card(self.deck, self.hand)
    def take_turn(self, opponent):
        PlayerTurn.play_card(self, opponent)
        PlayerTurn.command_minion(self, opponent)
        PlayerTurn.end_turn(self)

class PlayerTurn: #all the actions a player can do: play card, command minion, end turn
    def play_card(player, opponent):
        player.deck.shuffle()
        Game.draw_card(player.deck, player.hand)

        while player.mana_crystals > 0:
            opponent.battlefield.display_battlefield(opponent)
            player.battlefield.display_battlefield(player)
            player.hand.display_hand(player)
            print(f"\nYou have {player.mana_crystals} mana crystals.")

            choice = int(input("\nType the index of the card you would like to play. If you don't want to play a card, type '-1': "))
            if choice == -1:
                break

            chosen_card = player.hand.cards[choice]
            if chosen_card.mana_cost <= player.mana_crystals:
                player.mana_crystals -= chosen_card.mana_cost
                player.hand.cards.remove(chosen_card)
                print(f"{player.name} has played {chosen_card.name} and now has {player.mana_crystals} mana crystals remaining.\n")
                chosen_card.play(player, opponent) #play according to minion or spell

            else: #if not enough mana crystals
                print(f"Sorry, you do not have enough mana crystals to play {chosen_card.name}. Try again.")
    
    def command_minion(player, opponent):
        while True:
            if player.battlefield.check_attack_ability() == False: #if no minions can attack this round/if there are no minions on field
                break

            opponent.battlefield.display_battlefield(opponent)
            player.battlefield.display_battlefield(player)

            print(f"{player.name},", end=" ")
            attacking = input("\nWould you like to attack using one of your minions? Type 'y' or 'n' ")
            if attacking == "n":
                break
    
            #choose minion to attack with
            attacking_minion_index = PlayerTurn.choose_attack_card(player)
            
            #check for taunt and stealth, choose opponent card/hero to attack
            attacked_minion_index = PlayerTurn.choose_attacked_card(opponent)

            player.battlefield.minions[attacking_minion_index].attacked() #-1 attack count
            player.battlefield.minions[attacking_minion_index].update_stealth(False) #toggle stealth
            #carry out attacks
            if attacked_minion_index == -1:
                PlayerTurn.attack_hero(player, opponent, attacking_minion_index)
            else:
                 #two minions attack each other
                player.battlefield.minions[attacking_minion_index].collision(opponent.battlefield.minions[attacked_minion_index])
                #remove dead minions from both battlefields
                player.battlefield.minion_death(player, player.battlefield.minions[attacking_minion_index])
                opponent.battlefield.minion_death(opponent, opponent.battlefield.minions[attacked_minion_index])
            
    def attack_hero(player, opponent, index):
        opponent.hero_health -= player.battlefield.minions[index].attack
        print(f"{player.name} has attacked {opponent.name}'s hero, and {opponent.name}'s hero now has {opponent.hero_health} health.")
        Game.check_end_game(player, opponent) #check if either hero died
    
    def use_spell(spell_card, player, opponent):
        print(f"{player.name} consumed a spell card, {spell_card.name} with effect: {spell_card.effect}.\n")
        if spell_card.name == "Fireball":
            SpellEffects.fireball(player, opponent)
        elif spell_card.name == "Polymorph":
            if len(opponent.battlefield.minions) != 0:
                SpellEffects.polymorph(opponent)
            else:
                print(f"Sorry, the spell was not effective since there are no minions on {opponent.name}'s battlefield.")
                player.hand.add_card(spell_card)
        elif spell_card.name == "Flamestrike":
            SpellEffects.flamestrike(opponent)
        elif spell_card.name == "Arcane Intellect":
            SpellEffects.arcane_intellect(player)
        elif spell_card.name == "Holy Nova":
            SpellEffects.holy_nova(player, opponent)
        elif spell_card.name == "Cataclysm":
            SpellEffects.cataclysm(player, opponent)
        elif spell_card.name == "Deadly Shot":
            SpellEffects.deadly_shot(opponent)

    def minion_effect(minion, player, opponent):
        if minion.name == "Stormwind Champion":
            MinionEffects.activate_1(player)
        else:
            pass #for future effects
        
    def choose_attack_card(player):
        while True:
            attacking_minion_index = int(input("Type the index of the minion you would like to attack with: "))
            if player.battefield.minions[attacking_minion_index].attack_count <= 0:
                print("Sorry, the minion you chose already attacked.")
            elif player.battlefield.minions[attacking_minion_index].awake == False:
                print("The minion you chose is sleeping. Try again.")
            else:
                return attacking_minion_index
    
    def choose_attacked_card(opponent):
        taunt_list = [m for m in opponent.battlefield.minions if m.description == "Taunt"]
        while True:
            attacked_minion_index = int(input("Type the index of the minion that you would like to attack, or type '-1' to attack the opponent's hero: "))
            if attacked_minion_index > len(opponent.battlefield.minions)-1:
                print("Sorry, the index you have chosen is out of bounds.")
            elif taunt_list and (opponent.battlefield.minions[attacked_minion_index].description != "Taunt" or attacked_minion_index == -1): #if there is taunt, and chosen is a hero/is not taunt effect
                print("Sorry, you must attack a minion with Taunt first.")
            elif attacked_minion_index == -1: #check if hero, otherwise stealth part is messed up
                return -1
            elif opponent.battlefield.minions[attacked_minion_index].stealth == True:
                print("Sorry, the minion you have selected is in Stealth mode, and you cannot attack it yet.")
            else:
                return attacked_minion_index

    def end_turn(player):
        print(f"\n{player.name}, your turn has ended.\n")
        player.battlefield.update_minion()   #wake up minions for the next round, reset their attack count