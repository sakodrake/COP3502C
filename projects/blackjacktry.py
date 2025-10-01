import p1_random as p1
rng = p1.P1Random()

still_playing = True
game_number = 1
p_bank = []
player_card = ''
p_card = player_card


def cards(p_card):
    player_card = rng.next_int(13) + 1
    p_card = player_card
    if player_card == 11:
        p_card = "JACK!"
    elif player_card == 12:
        p_card = "QUEEN!"
    elif player_card == 13:
        p_card ="KING!"
    p_bank.append(p_card)
    return p_card

def count(p_card):
    hand = 0
    for i in p_bank:
        hand += i
    return hand

def options():
    print('')
    print('1. Get another card')
    print('2. Hold hand')
    print('3. Print statistics')
    print('4. Exit')
    return ''

def choose():
     option = input('Choose an option: ')
     if option == 1:
         cards(p_card)


print('START GAME #1')
print('')

while still_playing:
    print(f"Your card is a {cards(p_card)}!")
    print(f"Your hand is: {count(p_card)}")
    print(options())
    print(choose())
    

    