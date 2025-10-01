import p1_random as p1
rng = p1.P1Random()

still_playing = True
game_number = 1
p_bank = []

# Statistics
player_wins = 0
dealer_wins = 0
ties = 0
games_played = 0


def draw_card():
    card = rng.next_int(13) + 1  # 1–13
    if card == 1:
        print("Your card is an ACE!")
        value = 1
    elif card == 11:
        print("Your card is a JACK!")
        value = 10
    elif card == 12:
        print("Your card is a QUEEN!")
        value = 10
    elif card == 13:
        print("Your card is a KING!")
        value = 10
    else:
        print(f"Your card is a {card}!")
        value = card
    p_bank.append(value)
    return value


def count_hand():
    return sum(p_bank)


def options():
    print('')
    print('1. Get another card')
    print('2. Hold hand')
    print('3. Print statistics')
    print('4. Exit')


def show_stats():
    print(f"Number of Player wins: {player_wins}")
    print(f"Number of Dealer wins: {dealer_wins}")
    print(f"Number of tie games: {ties}")
    print(f"Total # of games played is: {games_played}")
    if games_played > 0:
        win_percent = (player_wins / games_played) * 100
        print(f"Percentage of Player wins: {win_percent:.1f}%")
    print("")


def reset_game():
    """Start a new game."""
    global p_bank, game_number
    p_bank = []
    game_number += 1
    print(f"\nSTART GAME #{game_number}\n")


def choose():
    global still_playing, player_wins, dealer_wins, ties, games_played

    option = int(input('Choose an option: '))
    if option == 1:
        draw_card()
        hand = count_hand()
        print(f"Your hand is: {hand}")
        if hand > 21:
            print("You exceeded 21! You lose.")
            dealer_wins += 1
            games_played += 1
            reset_game()

    elif option == 2:
        dealer_hand = rng.next_int(11) + 16  # dealer between 16–26
        player_hand = count_hand()
        print(f"Dealer's hand: {dealer_hand}")
        print(f"Your hand is: {player_hand}")

        if player_hand > 21:
            print("You busted! Dealer wins.")
            dealer_wins += 1
        elif dealer_hand > 21:
            print("Dealer busts! You win!")
            player_wins += 1
        elif player_hand > dealer_hand:
            print("You win!")
            player_wins += 1
        elif dealer_hand > player_hand:
            print("Dealer wins!")
            dealer_wins += 1
        else:
            print("It's a tie!")
            ties += 1

        games_played += 1
        reset_game()

    elif option == 3:
        show_stats()

    elif option == 4:
        still_playing = False


print(f"START GAME #{game_number}\n")

while still_playing:
    if not p_bank:  # First draw of a new game
        draw_card()
        print(f"Your hand is: {count_hand()}")
    options()
    choose()
