# import statements
from random import shuffle, randrange

def get_user_input(question):
    '''asks the user to input the name of a card that they want to use for their turn. Takes a string as a question for the parameter.
    Returns the user input as a lower case string.'''
    user_input = ''
    #continues to ask the user the input question until they enter an input of length greater then 0
    while len(user_input) == 0:
        #stores the user input as a variable and strips away the whitespace before and after the input
        user_input = input(question).strip()
    #trys to cast the user input to an integer. If its possible to case the input as an integer, then the input is returned.
    try:
        user_input = int(user_input)
        return(int(user_input))
    #If the input is not able to be cast as an integer, then it checks to see if the input is equal to one of the power card names.
    except:
        if user_input.upper() == 'SOH' or user_input.upper() == 'DOT' or user_input.upper() == 'DMT':
            #if the input is equal to one of the power card names, then it is returned as an uppercase string.
            return(user_input.upper())
        else:
            #if the input is not equal to one of the power card names, then it is returned as a lowercase string.
            return(user_input.lower())

def setup_water_cards():
    '''sets up the water card pile.Then shuffles it to create a random order of cards.
    Takes no parameters.
    Returns the setup water card pile as a list. '''
    #sets the inital pile of water cards.
    list_of_water_cards = []
    #for each type of water card (1,5,& 8), the appropriate number of cards is added to the pile of cards.
    for i in range(0,30):
        list_of_water_cards.append(1)
    for i in range(0,15):
        list_of_water_cards.append(5)
    for i in range(0,8):
        list_of_water_cards.append(10)
    #the cards are shuffled.
    shuffle(list_of_water_cards)
    #the pile of cards is returned
    return(list_of_water_cards)

def setup_power_cards():
    '''sets up the power cards pile. Then shuffles it to create a random order of cards.
    Takes no parameters.
    Returns the setup pwoer cards pile as a list.'''
    #sets the inital pile of power cards.
    list_of_power_cards = []
    #for each type of power card (SOH,DOT,& DMT), the appropriate number of cards is added to the pile of cards.
    for i in range(0,10):
        list_of_power_cards.append('SOH')
    for i in range(0,2):
        list_of_power_cards.append('DOT')
    for i in range(0,3):
        list_of_power_cards.append('DMT')
    #the cards are shuffled.
    shuffle(list_of_power_cards)
    #the pile of cards is returned
    return(list_of_power_cards)

def setup_cards():
    '''runs both the setup functions for the water and power cards, then returns both piles of cards as a two-tuple.
    takes no parameters.'''
    cards = (setup_water_cards(), setup_power_cards())
    return(cards)

def get_card_from_pile(pile, index):
    '''removes a given card from a pile of cards based on the index.
    Takes the relevent pile (power or water) as a list, and the index of the card to be removed as parameters.
    Returns the card removed from the pile.'''
    return(pile.pop(index))

def arrange_cards(cards_list):
    '''arranges the cards in each players hand so that each type is in the correct order.
    Takes the cards in the player's hand as a list.
    Returns nothing.'''
    #sets the intial list of water and power cards
    water_list = []
    power_list = []
    #goes through each card in the card list passed to the function, and determines if the card is a power or water type.
    for each in cards_list:
        if type(each) == int:
            #if the card is a water type, then it gets placed into the water list.
            water_list += [each]
        else:
            #if a card is the power type, then it gets placed into the power list.
            power_list += [each]
    #removes all values from the card list passed to the function so it can be re-ordered.
    cards_list.clear()
    #sorts the cards in the water_list
    water_list.sort()
    #adds the water_list to the cards_list
    cards_list.extend(water_list)
    #sorts the cards in the power_list
    power_list.sort()
    #adds the power_list to the cards_list
    cards_list.extend(power_list)

def deal_cards(water_cards_pile, power_cards_pile):
    '''takes cards from the water pile and the power piles and deals the appropriate number of cards to each player.
    Takes the water and power cards piles as lists for the parameters.
    Returns a two-tuple of the hands of both players as lists.'''
    #sets the list of cards for each player.
    player_1_cards = []
    player_2_cards = []
    #for three iterations, deals a water card to player 1 and player 2 alternatively.
    for i in range(0,3):
        #adds a card to player 1's hand from the water cards pile
        player_1_cards.append(water_cards_pile[0])
        #removes the same card from the water cards pile.
        water_cards_pile.pop(0)
        #adds the next card to player 2's hand from the water cards pile
        player_2_cards.append(water_cards_pile[0])
        #removes the same card from the water cards pile.
        water_cards_pile.pop(0)
    #for three iterations, deals a power card to player 1 and player 2 alternatively.
    for i in range(0,2):
        #adds a card to player 1's hand from the power cards pile
        player_1_cards.append(power_cards_pile[0])
        #removes the same card from the power cards pile.
        power_cards_pile.pop(0)
        #adds the next card to player 2's hand from the power cards pile
        player_2_cards.append(power_cards_pile[0])
        #removes the same card from the power cards pile.
        power_cards_pile.pop(0)
    #calls the arrange_cards function to organize the cards in wach player's hand.
    arrange_cards(player_1_cards)
    arrange_cards(player_2_cards)
    return(player_1_cards, player_2_cards)

def apply_overflow(tank_level):
    '''determines if the tank has overflowed or not. Then returns the new value opf the tank if it has overflowed.
    Takes the given players tank as a integer for the parameter.'''
    #sets the max fill value
    max_fill_value = 80
    overflow = 0
    #calculates if the tank has overflowed or not
    overflow = int(tank_level - max_fill_value)
    #checks if the tank has overflowed or not
    if overflow > 0:
        #if the tank has overflowed, then the new value of the tank is calculated and returned.
        return(int(max_fill_value - overflow))
    else:
        #if the tank has not overflowed, then the tank value is returned without an deductions.
        return(tank_level)

def use_card(player_tank, card_to_use, player_cards, opponent_tank):
    '''determines what action should take place depending on what card the player wants to use.
    Takes the value of the player's tanks as an integer, the player's cards as a list, and the value of the opponent's tank as an integer for the parameters.
    Returns the new value of both the player's and opponent's tank.'''
    #checks if the card is a water card or not.
    if type(card_to_use) == int:
        #if the card is a water card, the value of the water card is added to the player's tank.
        player_tank += player_cards[player_cards.index(card_to_use)]
    #check if the card is SOH
    elif card_to_use == 'SOH':
        #Determines what the value of half of the opponent tank is, and subtracts the value from the opponent's tank. 
        #Also, adds half the value of the opponent's tank to the player's tank.
        half_tank = int(opponent_tank/2)
        opponent_tank -= half_tank
        player_tank += half_tank
    #check if the card is DOT
    elif card_to_use == 'DOT':
        #drains the opponent's tank
        opponent_tank = 0
    #check if the card is DMT
    elif card_to_use == 'DMT':
        #doubles the value of the player's tank
        player_tank = int(player_tank*2)
    #removes the card the player selected from their hand
    player_cards.pop(player_cards.index(card_to_use))
    #checks if the player's tank has overflowed and if so returns the new tank value.
    player_tank = apply_overflow(player_tank)
    return(player_tank, opponent_tank)

def discard_card(card_to_discard, player_cards, water_cards_pile, power_cards_pile):
    '''runs if the user wants to discard a card from their hand.
    Takes the card to discard, the list of the player's cards, the power card pile, and the water card pile as parameters.
    Returns nothing.'''
    #removes the card from the player's hand at a given index
    player_cards.pop(player_cards.index(card_to_discard))
    #checks if the card to discard is a water or power card
    if type(card_to_discard) == int:
        #if the card is a water card, it is added to the bottom of the water card pile
        water_cards_pile.append(card_to_discard)
    else:
        #if the card is a power card, it is added to the bottom of the power card pile
        power_cards_pile.append(card_to_discard)

def filled_tank(tank):
    '''checks if the tank is question had reached the level that determines the winner.
    Takes the value of the given take as a parameter.
    Returns a boolean.'''
    #checks if the value of tank is between 75 and 80
    if tank >= 75 and tank <= 80:
        #returns true if the tank level is between 75 and 80
        return True
    else:
        #returns false if the tank level is not between 75 and 80
        return False

def check_pile(pile, pile_type):
    '''checks to see if the given pile of cards is depleted, if so the pile of cards is refreshed.
    Takes the given pile as a list, and the pile type as parameters.
    Returns nothing.'''
    #checks if the length of the pile of cards is 0
    if len(pile) == 0:
        #if the card pile is empty, then checks to see if the card pile is a water or power card pile.
        if pile_type == 'water':
            #if the pile is a water pile, then the given pile is refreshed
            pile.extend(setup_water_cards())
        elif pile_type == 'power':
            #if the pile is a power pile, then the given pile is refreshed
            pile.extend(setup_power_cards())

def append_and_arrange_cards(cards_to_arrange, card_to_add):
    '''used to add a card that is drawn to a list of cards, and organize the given list of cards.
    Takes the given list of cards to arrange, and the card to add as inputs.
    Returns nothing.'''
    cards_to_arrange.append(card_to_add)
    arrange_cards(cards_to_arrange)

def take_a_new_card_from_pile (card_to_draw, water_cards_pile, power_cards_pile):
    '''to be used at the end of each turn, checks if the player used a water or power card, checks if the given pile is empty and replenishes it if needed
    then draws a new card from the given pile.
    Takes the card the user played during their turn as card_to_draw, and the power and water cards piles as lists respectively as parameters.
    Rturns the new card taken from the top of the given pile.'''
    if type(card_to_draw) == int:
        check_pile(water_cards_pile, 'water')
        #if they used or discarded a water card, then a card is drawn from the water card pile and stored as a variable
        new_card = int(get_card_from_pile(water_cards_pile, 0))
        
    else:
        #if they used or discarded a power card, then a card is drawn from the power card pile and stored as a variable
        check_pile(power_cards_pile, 'power')
        new_card = get_card_from_pile(power_cards_pile, 0)

    return(new_card)
    

def human_play(human_tank, human_cards, water_cards_pile, power_cards_pile, opponent_tank):
    '''contains all the functions required to start and complete the human turn.
    Takes the value of the player's tank, the player's list of cards, the water cards pile list, the power cards pile list, and the value of the opponent's tank as parameters.
    Returns the new values of the player's and opponent's tank after the turn.'''
    #prints the intro section for the player's turn
    print('\n')
    print('''=== Human Player's turn ===''')
    print('Your water level is at:', human_tank)
    print('''Computer's water level is at:''', opponent_tank)

    print('''Your cards are:''', human_cards)
    #sets the use_or_discard value as an empty string to initiate the while loop
    use_or_discard = ''
    #while the user's input to use or discard a card is not u or d, then the user will be continuously asked if they want to use or discard a card.
    while use_or_discard.lower() != 'u' and use_or_discard.lower() != 'd':
        #stores the value of the user's selection to use or discard a card
        use_or_discard = input('Do you want to use a card or discard a card? (u / d): ').strip()
    
    #sets the card_to_draw value as an empty string to initiate the while loop
    card_to_draw = ''

    #if the user wants to use a card, then they are asked what card they want to use, and the use_card function is called.
    if use_or_discard.lower() == 'u':
        while card_to_draw not in human_cards:
            card_to_draw = get_user_input('which card do you want to use? ')
        print('Using card:', card_to_draw)
        human_tank, opponent_tank = use_card(human_tank, card_to_draw, human_cards, opponent_tank)
    #if the user wants to discard a card, then they are asked what card they want to discard, and the discard_card function is called.
    else:
        while card_to_draw not in human_cards:
            card_to_draw = get_user_input('which card do you want to discard? ')
        print('Discarding card:', card_to_draw)
        discard_card(card_to_draw, human_cards, water_cards_pile, power_cards_pile)

    #checks if the user used or discarded a water card or power power card
    #if they used or discarded a water card, then a card is drawn from the water card pile and stored as a variable
    #if they used or discarded a power card, then a card is drawn from the power card pile and stored as a variable
    new_card = take_a_new_card_from_pile(card_to_draw, water_cards_pile, power_cards_pile)

    if type(new_card) == int:
        print('Drawing water card: ', new_card)
    else:
        print('Drawing power card: ', new_card)

    #takes the card that was drawn from the given pile and adds it to the players hand, then organizes the hand.
    append_and_arrange_cards(human_cards, new_card)

    #prints the closing comments for the user's turn.
    print('Your water level is now at:', round(human_tank,2))
    print('''Computer's water level is now at:''', round(opponent_tank,2))
    print('''Your cards are now:''', human_cards)
    return(human_tank, opponent_tank)


def computer_play(computer_tank, computer_cards, water_cards_pile, power_cards_pile, opponent_tank):
    '''contains all functions to start and complete the computer's turn.
    Takes the value of the computer's tank, the computer's list of cards, the water cards pile list, the power cards pile list, and the value of the opponent's tank as parameters.
    Returns the new values of the computer's and opponent's tank after the turn.'''
    #prints the intro messages for the computer's turn
    print('\n')
    print('''=== Computer Player's turn ===''')
    print('''Computer's water level is at: ''',  computer_tank)
    print('''Your water level is at: ''',  opponent_tank)

    water_cards_in_hand = []
    #finds water cards the computer has in hand
    for each in computer_cards:
      if type(each) == int:
          water_cards_in_hand.append(each)

    #finds the largest water card in hand
    max_water_card_in_hand = max(water_cards_in_hand)
    
    computer_card_to_draw = ''

    #If the computer is able to win on the turn it will check and win if possible
    if 10 in computer_cards and computer_tank >= 65 and computer_tank <= 70:
        computer_card_to_draw = 10
    elif 5 in computer_cards and computer_tank >= 70 and computer_tank <= 75:
        computer_card_to_draw = 5
    elif 1 in computer_cards and computer_tank >= 74 and computer_tank <= 79:
        computer_card_to_draw = 1
    elif 'DMT' in computer_cards and ((computer_tank*2) <= 80) and ((computer_tank*2) >= 75):
        computer_card_to_draw = 'DMT'
    elif 'SOH' in computer_cards and opponent_tank != 0 and (int(opponent_tank/2) + computer_tank) >= 75 and (int(opponent_tank/2) + computer_tank) <= 80:
        computer_card_to_draw = 'SOH'

    #checks if the computer can get further with a water card or DMT
    elif 'DMT' in computer_cards and (computer_tank*2) > max_water_card_in_hand:
      computer_card_to_draw = 'DMT'

    #if the computer cannot win it will check if the opponents tank is 0, and if more of a lead can be gained by draining the opponent_tank vs playing a water card.
    elif opponent_tank != 0 and 'DOT' in computer_cards and opponent_tank > max_water_card_in_hand:
        computer_card_to_draw = 'DOT'

    #if all else fails it trys to pick the largest water card it has in hand
    elif 10 in computer_cards:
        computer_card_to_draw = 10
    elif 5 in computer_cards:
        computer_card_to_draw = 5
    elif 1 in computer_cards:
        computer_card_to_draw = 1
    
    #other things the computer will try if the previous moves didn't execute
    elif 'DOT' in computer_cards:
        computer_card_to_draw = 'DOT'
    elif 'SOH' in computer_cards:
        computer_card_to_draw = 'SOH'
    elif 'DMT' in computer_cards:
        computer_card_to_draw = 'DMT'

    print('''Computer playing with card: ''', computer_card_to_draw)

    #calls the use_card function with the card the computer chose
    computer_tank, opponent_tank = use_card(computer_tank, computer_card_to_draw, computer_cards, opponent_tank)

    #checks if the computer used or discarded a water card or power power card
    #if they used or discarded a water card, then a card is drawn from the water card pile and stored as a variable
    #if they used or discarded a power card, then a card is drawn from the power card pile and stored as a variable
    new_card = take_a_new_card_from_pile(computer_card_to_draw, water_cards_pile, power_cards_pile)

    #takes the card that was drawn from the given pile and adds it to the computer's hand, then organizes the hand.
    append_and_arrange_cards(computer_cards, new_card)

    print('''Computer's water level is now at: ''',  computer_tank)
    print('''Your water level is now at: ''',  opponent_tank)

    return(computer_tank, opponent_tank)

def main():
    '''main function that ties all of the other functions together and runs the game.
    Takes no parameters.
    Returns nothing.'''
    print('\n')
    print('''Welcome to the WATER TANK game and play against the computer!
The first player to fill their tank wins the game.
On your turn select one of the cards in your hand to play.
The number cards add the given number of water units to your tank.
The card 'SOH' steals half of the opponent's tank value.
The card 'DOT' drains the opponent's tank.
The card 'DMT' doubles your tank value.
Good luck!''')
    human_tank = 0
    computer_tank = 0

    #setup the cards
    cards = setup_cards()

    #stores the card piles from each type as variables
    water_cards_pile = cards[0]
    power_cards_pile = cards[1]

    #deal the cards
    human_cards, computer_cards = deal_cards(water_cards_pile, power_cards_pile)

    #picks a random number 1 or 2, in order to determine who goes first the computer or human
    random_num = randrange(1,3)
    print('\n')
    #if the random number is 1, then the human goes first
    if random_num == 1:
        print('The Human Player has been selected to go first.')
        while filled_tank(human_tank) == False and filled_tank(computer_tank) == False:
            #alternates between the human and computer's turn while there is no winner of the game
            human_tank, computer_tank = human_play(human_tank, human_cards, water_cards_pile, power_cards_pile, computer_tank)
            #ends the loop if the human wins
            if filled_tank(human_tank) == True:
                break
            computer_tank, human_tank = computer_play(computer_tank, computer_cards, water_cards_pile, power_cards_pile, human_tank)
          
    #if the random number is 2, then the computer goes first
    else:
        print('The Computer Player has been selected to go first.')
        while filled_tank(human_tank) == False and filled_tank(computer_tank) == False:
            #alternates between the human and computer's turn while there is no winner of the game
            computer_tank, human_tank = computer_play(computer_tank, computer_cards, water_cards_pile, power_cards_pile,human_tank)
            #ends the loop if the computer wins
            if filled_tank(computer_tank) == True:
                break
            human_tank, computer_tank = human_play(human_tank, human_cards, water_cards_pile, power_cards_pile, computer_tank)
        

    print('\n')
    print("=== Game Over ===")
    #checks who won the game, and prints who the winner is
    if filled_tank(human_tank) == True:
        print('Human Player won')
    else:
        print('Computer Player won')
    print('\n')

if __name__ == '__main__':
    main()
