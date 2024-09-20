from player import PlayerTurn

class Card:
    def __init__(self, name, mana_cost, description):
        self.name = name
        self.mana_cost = mana_cost
        self.description = description
    def __str__(self):
        return f"{self.name} (Mana Cost: {self.mana_cost}) - {self.description}"

class Minion(Card):
    def __init__(self, name, mana_cost, attack, health, description, stealth):
        super().__init__(name, mana_cost, description)
        self.attack = attack
        self.health = health
        self.awake = False
        self.attack_count = 1
        self.stealth = stealth
    def update_stealth(self, new_bool):
        self.stealth = new_bool
    def attacked(self):
        self.attack_count -= 1
    def transform(self, name, attack, health):
        self.name = name
        self.attack = attack
        self.health = health
    def collision(self, other_minion):
        other_minion.health -= self.attack
        self.health -= other_minion.attack
        print(f"Attacked!!! Your {self.name} attacked {other_minion.name}. Your {self.name} now has {self.health} health left, and your opponent's {other_minion.name} has {other_minion.health} health left.\n")
    def play(self, player, opponent):
        player.battlefield.add_minion(self)
        PlayerTurn.minion_effect(self, player, opponent)
    def __str__(self):
        return f"{self.name} (Minion)\n(Mana Cost: {self.mana_cost}) (Attack: {self.attack}) (Health: {self.health}) (Awake: {self.awake}) - Description: {self.description}"

class Spell(Card): 
    def __init__(self, name, mana_cost, description, effect):
        super().__init__(name, mana_cost, description)
        self.effect = effect
    def play(self, player, opponent):
        PlayerTurn.use_spell(self, player, opponent)
    def __str__(self):
        return f"{self.name} (Spell)\n(Mana Cost: {self.mana_cost}) - Effect: {self.effect}"


