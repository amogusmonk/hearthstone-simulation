from player_actions import PlayerTurn
from board import Deck, Hand, Battlefield
from setup import Game


#handles player attributes

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