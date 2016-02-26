# blackjack
import numpy as np


# Create deck class
class deck(object):
    
    def __init__(self):
        
        # want to incorporate suits and J, Q, K, A
        # maybe consider a dictionary instead of a list
        # key = JS (jack of spades): value of 11
        card_names = ['2','3','4','5','6','7','8','9','10', 'Jack', 'Queen', 'King', 'Ace']

        self.deck = card_names * 4
        
    def shuffle(self):
        print "The deck has been shuffled"
        return np.random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()
    
    def show(self):
        print('\n'.join('{}: {}'.format(*k) for k in enumerate(self.deck)))
        
# Create player class       
class player(object):
    
    def __init__(self):
        self.hand = []
        self.bank = 500.0
    
    def addCard(self,new_card):
        self.hand.append(new_card)
        return self.hand
    
    def showBank(self):
        return self.bank
        
# Create dealer class 
class dealer(object):
    
    def __init__(self):
        self.hand = []
        
    def addCard(self,new_card):
        self.hand.append(new_card)
        return self.hand
        
# place bet function
def place_bet(bank):
    
    while True:
        try:
            response = bank * 2
            while response > bank:
                string = "You have $%s to spend.  How much would you like to bet?  " % bank
                response = int(raw_input(string))
        except:
            print "Please enter an integer"
            continue
        else:
            bank -= response
            print "You have $%s left in the bank!" % bank
            break
            
    return response, bank
    
# ask for bet, hold, split choice
def ask_choice(hand):
    choice = ""
    
    if hand[0] == hand[1] and len(hand) == 2:   
        while choice not in ('hit', 'hold', 'split'):
            choice = raw_input("Hit, Hold, or Split?  ").lower()
    else:
        while choice not in ('hit', 'hold'):
            choice = raw_input("Hit or Hold?").lower()
    return choice

# calculate hand value
def calc_score(hand):
    aces = [x for x in hand if x == 'Ace']
    hand2 = [x for x in hand if x <> 'Ace']
    hand = hand2 + aces
        
    value = 0
    for card in hand:
        if card == '2':
            value += 2
        elif card == '3':
            value += 3
        elif card == '4':
            value += 4
        elif card == '5':
            value += 5
        elif card == '6':
            value += 6
        elif card == '7':
            value += 7
        elif card == '8':
            value += 8
        elif card == '9':
            value += 9
        elif card == '10' or card == 'Jack' or card == 'Queen' or card == 'King':
            value += 10
        elif card == 'Ace':
            if value >= 11:
                value += 1
            else:
                value += 11
    return value
    
def restart():
    restart = ''
    while restart <> 'Y' and restart <> 'N':
        restart = str(raw_input("Do you want to play again? (Y)es or (N)o:  ").upper())
    
    if restart == 'Y':
        return True
    else:
        return False
        
    

# Code
    
# Introduce game
player1 = player()
dealer1 = dealer()

play = True

while play == True:
    # Create a new deck and shuffle it
    new_deck = deck()
    new_deck.shuffle()
    
    # Take bet and adjust bank value
    bet,bank = place_bet(player1.bank)
    player1.bank = bank
    
    # Deal two cards each to player and dealer
    dealer1.hand = []
    player1.hand = []
    
    for i in (0,1):
        dealer1.addCard(new_deck.deal())
        player1.addCard(new_deck.deal())
     
    # show player's cards 
    print "Your cards are: "
    print player1.hand
    
    # reveal one of dealer's cards to player
    print "The dealer has: "
    print dealer1.hand[0] + " and ???"
    

    # ask what the player wants to do
    move = ''
    while move <> 'hold':
        player1_score = calc_score(player1.hand)
        dealer_score = calc_score(dealer1.hand)
        
        if player1_score > dealer_score and player1_score == 21 and len(player1.hand) == 2:
            print "Blackjack!"
            player1.bank += bet * 2.5
            print "You have %s in the bank!" % player1.bank
        
        move = ask_choice(player1.hand)
        
        if move == 'hold':
            player1_score = calc_score(player1.hand)
            dealer_score = calc_score(dealer1.hand)
            
            print "Your hand: "
            print player1.hand
            
            print "Dealer's hand: "
            print dealer1.hand
            
            # while dealer has less than a 17, they get more cards
            while dealer_score < 17:
                print "The dealer gets another card"
                dealer1.addCard(new_deck.deal())
                print "Dealer's hand: "
                print dealer1.hand
                dealer_score = calc_score(dealer1.hand)
                print dealer_score
                
            #player score = 18 dealer score= 17
            if player1_score > dealer_score and player1_score == 21 and len(player1.hand) == 2:
                print "Blackjack!"
                player1.bank += bet * 2.5
                print "You have %s in the bank!" % player1.bank
            elif player1_score > dealer_score and player1_score <= 21 and len(player1.hand) >= 2:
                print "You won!"
                player1.bank += bet * 2.0
                print "You have %s in the bank!" % player1.bank

            elif player1_score > 21:  # if both player and dealer bust, the dealer wins
                print "Bust!"
                print "You have %s in the bank!" % player1.bank
            elif player1_score < dealer_score and dealer_score <= 21:
                print "You lose!"
                print "You have %s in the bank!" % player1.bank
            elif player1_score < dealer_score and dealer_score > 21:
                print "You win!  Dealer bust!"
                player1.bank += bet * 2.0
                print "You have %s in the bank!" % player1.bank
            elif player1_score == dealer_score:
                print "Same score, you get your bet back"
                player1.bank += bet
                print "You have %s in the bank!" % player1.bank
                
        elif move == 'hit':
            player1.addCard(new_deck.deal())
            
            print "Your cards are: "
            print player1.hand
            
            if calc_score(player1.hand) == 21 and calc_score(dealer1.hand) <> 21:
                print "The dealer has: "
                print dealer1.hand
                
                print "You win!!"
                player1.bank += bet * 2.0
                print "You have %s in the bank!" % player1.bank
                break
            elif calc_score(player1.hand) == 21 and calc_score(dealer1.hand) == 21:
                print "Sam score, you get your money back"
                player1.bank += bet
                print "You have %s in the bank!" % player1.bank
                break
            elif calc_score(player1.hand) > 21:
                print "Bust!"
                print "You have %s in the bank!" % player1.bank
                break
            
            print "The dealer has: "
            print dealer1.hand[0] + " and ???"
            
        elif move == 'split':
            pass
    
    if player1.bank <= 0:
        print "Sorry, you're out!"
        play = False
        break
    else:
        play = restart()

    
            