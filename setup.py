
class Game: #misc. game managing thingies
    def draw_card(deck, hand): #draws card from deck; adds it to hand
        card = deck.draw_card()
        if card:
            hand.add_card(card)
            print(f"Drawn card: {card}")
    def set_mana_crystals(player, opponent, turn):
        if turn <= 10:
            player.mana_crystals = turn
            opponent.mana_crystals = turn
        else:
            player.mana_crystals = 10
            opponent.mana_crystals = 10
    def check_end_game(player1, player2):
        if(player1.hero_health <= 0):
            print(f"{player1.name} has fallen. {player2.name} wins!")
            quit()
        elif (player2.hero_health <= 0):
            print(f"{player2.name} has fallen. {player1.name} wins!")
            quit()
        else:
            pass
    






