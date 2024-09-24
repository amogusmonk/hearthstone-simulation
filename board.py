import random
from effects import MinionEffects

class Deck:
    def __init__(self, cards):
        self.cards = cards
    def shuffle(self):
        random.shuffle(self.cards)
    def draw_card(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            print("The deck is empty!")
            return None
        
class Hand:
    def __init__(self):
        self.cards = [] #list of cards in hand
    def add_card(self, card):
        self.cards.append(card)
    def display_hand(self, player):
        print(f"\n{player.name}'S CURRENT HAND:")
        for i in range(len(self.cards)):
            print(f" {i}. {self.cards[i]}")
        print("-------------------------------------------------------------------------")

class Battlefield:
    def __init__(self):
        self.minions = [] #list of minions on battlefield
    def add_minion(self, minion):
        self.minions.append(minion) 
        #implement charge
        if minion.description == "Charge":
            minion.awake = True
    def remove_minion(self, minion):
        self.minions.remove(minion)
    def check_attack_ability(self): #if there are any cards that are awake and can attack
        if len(self.minions) == 0:
            return False
        can_attack = False
        for m in self.minions:
            if m.attack_count > 0 and m.awake:
                can_attack = True
        return can_attack
    def minion_death(self, player, minion): #check if minion is dead; remove if dead
        if minion.health <= 0:
            print(f"{player.name}'s {minion.name} has fallen. The card will be removed from the battlefield." )
            #deactivate stormwind champion effect
            if minion.name == "Stormwind Champion":
                MinionEffects.deactivate_1(player)
            if minion in self.minions:
                self.remove_minion(minion)
    def update_minion(self): #make minions on the battlefield wake up, restore their attack count
        for minion in self.minions:
            if not minion.awake:
                minion.awake = True
            if minion.attack_count == 0:
                minion.attack_count += 1
    def display_battlefield(self, player):
        print(f"\n{player.name}'s BATTLEFIELD:")
        print(f"{player.name}'s hero\n(Health: {player.hero_health})\n")
        for i in range(len(self.minions)):
            print(f" {i}. {self.minions[i]}")
        print("-------------------------------------------------------------------------\n") 
