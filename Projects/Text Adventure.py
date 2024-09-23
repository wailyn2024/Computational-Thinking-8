import random

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] # Remember to assign number values! 
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def card_value(card):
    rank = card[0]
    if rank in ['Jack', 'Queen', 'King']:
        return 10
    elif rank == 'Ace':
        return 11  # Count as 11, will adjust later
    return int(rank)

def hand_value(hand):
    total = sum(card_value(card) for card in hand)
    aces = sum(1 for card in hand if card[0] == 'Ace')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total # Works for now not the problem

def blackjack_game():
    balance = 100
    print("Welcome to the casino! Your starting balance is $100.")
    
    while 0 < balance < 1000:
        bet = int(input(f"You have ${balance}. How much do you want to bet? "))
        
        if bet <= 0 or bet > balance:
            print("Invalid bet amount. Try again.")
            continue

        deck = create_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]
        
        print(f"Your hand: {player_hand} (Total: {hand_value(player_hand)})")
        print(f"Dealer's showing card: {dealer_hand[0]}")

        while True:
            choice = input("Do you want to hit or stay? (h/s) ").lower() #could add a or statement here 
            if choice == 'h':
                player_hand.append(deck.pop())
                print(f"You drew: {player_hand[-1]} (Total: {hand_value(player_hand)})")
                if hand_value(player_hand) > 21:
                    print("You busted! You lose your bet.")
                    balance -= bet
                    break
            elif choice == 's':
                break
            else:
                print("Invalid choice. Please choose 'h' or 's'.") #Need to do this with the amount your betting as well it keeps crashing

        if hand_value(player_hand) <= 21:
            while hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
            print(f"Dealer's hand: {dealer_hand} (Total: {hand_value(dealer_hand)})")

            player_total = hand_value(player_hand)
            dealer_total = hand_value(dealer_hand)

            if dealer_total > 21 or player_total > dealer_total:
                print("You win! You get your bet back plus winnings.")
                balance += bet
            elif player_total < dealer_total:
                print("Dealer wins! You lose your bet.")
                balance -= bet
            else:
                print("It's a push! You get your bet back.")

        if balance >= 1000:
            print("Congratulations! You've reached $1000! You win!")
        elif balance <= 0:
            print("You have lost all your money. Game over.")

if __name__ == "__main__":
    blackjack_game()