# Blackjack — Python (ICS3U1 Final Project)

A complete text-based Blackjack game written in Python as my final project for ICS3U1 (June 2025).
This program features full game logic, betting, dealer behaviour, and a .txt deck-loading system.

# Features
**Full Blackjack Game Logic**

-Player and dealer turns

-Hit, Stand, and Double options

-Automatic bust detection

-Dealer hits until 17 or higher

-Tie results in a house win (project rules)

**Accurate Scoring System**

-Aces automatically adjust between 11 and 1

-Face cards = 10

-Player and dealer ace counts are tracked separately

-.txt Deck System

-Loads cards from cards.txt

-Deck contains 16 copies of a 13-card list (standard for assignment)

-Reloads the deck when low on cards

-Randomized shuffling (300-pass shuffle)

**Betting + Money Tracking**

-User chooses the bet amount each round

-Minimum bet of $5

-Double-down option handled correctly

-Balance updates every round

**Replay System**

-Game continues until player chooses to stop

-Auto-stops if balance drops below $5

