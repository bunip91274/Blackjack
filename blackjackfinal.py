'''
Blackjack.
Maksym Pronin, ICS3U1, June 13th, 2025
'''
# import random functions
import random
# create the variables for player score, dealer score, the amount of aces the player has and the amount of aces the dealer has
playerscore = 0
dealerscore = 0
acecount = 0
dealeracecount = 0
# set the ace and dealer ace to false
ace = False
dealerace = False
def playerhit(card):
# turn the ace count and player score into global, can be changed and used inside and outside of the functions. so basically they are "global" to the entire program
    global acecount, playerscore
# if the card is an ace, add 11 to player score, and 1 to the ace count
    if card == "Ace":
        playerscore = playerscore + 11
        acecount = acecount + 1
# if its any of the face cards, add 10 to the player score
    elif card == "King" or card == "Queen" or card == "Jack":
        playerscore = playerscore + 10
# if it's a number card, turn into integer and add to player score
    else:
        card = int(card)
        playerscore = playerscore + card
# while score is above 21 and ace count is above zero, remove 10 from the player score (turn the ace into a 1) and remove 1 from the ace count. it does this for any aces in the hand when the score is above 21
    while playerscore > 21 and acecount > 0:
        playerscore = playerscore - 10
        acecount = acecount - 1
# return the card
    return card
# dealer gets a card, same logic as player just with different variables
def dealerhit(card):
    global dealeracecount, dealerscore
    if card == "Ace":
        dealerscore = dealerscore + 11
        dealeracecount = dealeracecount + 1
    elif card == "King" or card == "Queen" or card == "Jack":
        dealerscore = dealerscore + 10
    else:
        card = int(card)
        dealerscore = dealerscore + card
    while dealerscore > 21 and dealeracecount > 0:
        dealerscore = dealerscore - 10
        dealeracecount = dealeracecount - 1
    return card
# create the list with all the cards and load the cards from the text file
allcards = []
for i in range(16):
    file = open("cards.txt", "r")
# open the card file and load all cards into the list
    for i in range(13):
        card = file.readline().strip()
        allcards.append(card)
    file.close()
# shuffle the deck 300 times by popping a random card and adding it onto the end of the deck
for i in range(300):
    cardspot = random.randint(0, len(allcards)-1)
    shuffle = allcards[cardspot]
    allcards.pop(cardspot)
    allcards.append(shuffle)
# greetings and name
print("Welcome to Blackjack")
name = input("What is your name?:")
# ask how much money they are playing with
money = int(input("Enter the amount of money you're bringing: "))
# main game loop - player must have at least $5
while money >= 5:
    playerscore = 0
    dealerscore = 0
    acecount = 0
    dealeracecount = 0
# reload deck if less than 20 cards left
    if len(allcards) < 20:
        for i in range(16):
            file = open("cards.txt", "r")
            for i in range(13):
                card = file.readline().strip()
                allcards.append(card)
            file.close()
# ask how much they want to bet
    betamount = int(input("Enter the bet amount (Minimum bet is $5, whole amounts only): "))
# turns bet into a integer if a float or anything else is entered
    betamount = float(betamount)
    betamount = int(betamount)
# keeps prompting the user if they enter an amount that's more than the amount of money they brought
    while betamount > money:
        betamount = int(input("Enter the bet amount (Minimum bet is $5, whole amounts only): "))
    while betamount < 5:
        betamount = int(input("Enter the bet amount (Minimum bet is $5, whole amounts only: "))
        betamount = float(betamount)
        betamount = int(betamount)
# subtract bet from player's money
    money = money - betamount
    print("You have", money, "dollars left")
# player draws 2 cards
    print("Your cards are:")
    print(playerhit(allcards[0]))
    allcards.pop(0)
    print(playerhit(allcards[0]))
    allcards.pop(0)
# tells the player their cards and their total score
    print("Your score is", playerscore)
# dealer shows one card, keeps one hidden. tells the dealer's score off the first card only, for now
    print("The dealer's card is ", dealerhit(allcards[0]))
    print("The dealer's score is", dealerscore)
    allcards.pop(0)
    hidden = dealerhit(allcards[0])
    allcards.pop(0)
    move = input("Would you like to stand (s), hit (h) or double (d)?: ")
# ask what the player wants to do (hit, stand, double)
    while playerscore <= 21 and move != "s":
# hit - player takes another card
        if move == "h":
            print("Your new card is", playerhit(allcards[0]))
            allcards.pop(0)
            print("Your score is", playerscore)
# player busted - breaks loop
            if playerscore > 21:
                print("You bust.")
                break
# if player doesn't bust, rounds keeps going
            else:
                move = input("Would you like to stand (s), hit (h) or double (d)?: ")
# if player chooses double, checks if player has enough money to double
        elif move == "d":
# if player doesn't have enough money, prompts him to pick something else
            if betamount > money:
                print("Balance is too low to double")
                move = input("Would you like to stand (s), hit (h) or double (d)?: ")
# if player has enough to double, goes ahead with the round
            else:
# subtract bet from player's money and double the player bet
                money = money - betamount
                betamount = betamount * 2
# player gets his final card
                print("Your new card is ", playerhit(allcards[0]))
                allcards.pop(0)
# dealer plays and reveals his hidden card and score
                print("Your score is ", playerscore)
                print("The dealer's hidden card is", hidden)
                print("The dealer's score is", dealerscore)
# dealer keeps hitting until score is at least 17
                while dealerscore <= 16:
                    print("Dealer must hit. His new card is", dealerhit(allcards[0]))
                    print("Dealer score is", dealerscore)
                    allcards.pop(0)
# player busted
                if playerscore > 21:
                    print("Your score is over 21. You lose.")
                    break
# dealer busted, player wins, winnings doubled + double, round ends
                elif dealerscore > 21 and playerscore <= 21:
                    print("Dealer bust. You win!")
                    betamount = betamount * 2
                    money = money + betamount
                    print("Your new balance is", money)
                    break
# player score higher than dealer score, player wins, winnings doubled, round ends
                elif playerscore > dealerscore:
                    print("You win!")
                    betamount = betamount * 2
                    money = money + betamount
                    print("Your new balance is", money)
                    break
# dealer score is higher, player loses, round ends
                elif dealerscore > playerscore:
                    print("You lose.")
                    break
# tie - player loses (house rules)
                elif playerscore == dealerscore:
                    print("You lose.")
                    break
# stand - dealer reveals hidden card and plays their turn
    if move == "s":
        print("The dealer's hidden card is", hidden)
        print("The dealer's score is", dealerscore)
# dealer keeps hitting until score is at least 17
        while dealerscore <= 16:
            print("Dealer must hit. His new card is", dealerhit(allcards[0]))
            print("Dealer score is", dealerscore)
            allcards.pop(0)
# player busted
        if playerscore > 21:
            print("Your score is over 21. You lose.")
# dealer busted, player wins
        elif dealerscore > 21 and playerscore <= 21:
            print("Dealer bust. You win!")
            betamount = betamount * 2
            money = money + betamount
            print("Your new balance is", money)
# player score is higher than dealer score, player wins, winnings doubled, round ends
        elif playerscore > dealerscore:
            print("You win!")
            betamount = betamount * 2
            money = money + betamount
            print("Your new balance is", money)
# dealer wins, round ends
        elif dealerscore > playerscore:
            print("You lose.")
# tie - player loses (house rules)
        elif playerscore == dealerscore:
            print("You lose.")
# not enough money to keep playing
    if money < 5:
        print("You don't have enough money to play. Game over")
        break
# ask if the player wants to play again
    else:
        again = input("Do you want to play again? (y/n): ").lower()
        if again != "y":
            break

