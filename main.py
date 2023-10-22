import random
from logo import logo
from itertools import product

SYMBOL = ['♣', '♦', '♥', '♠']
CARD_VAL = {'A': 11,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 10,
            'Q': 10,
            'K': 10,
            }
CARDS = []

total_deck = list(product(SYMBOL, CARD_VAL)) * 8
for i in total_deck:
    new_card = i[0] + i[1]
    CARDS.append(new_card)

cards = []
cards.extend(CARDS)


def deal_card():
    rand_card = random.choice(cards)
    cards.remove(rand_card)
    return rand_card


def calculate_score(rcard, cval):
    card_num = []
    for card in rcard:
        for key in cval:
            if len(card) == 2:
                if card[1] == key:
                    card_num.append(cval[key])
            else:
                if card[1]+card[2] == key:
                    card_num.append(cval[key])

    if sum(card_num) == 21:
        return 0

    if sum(card_num) > 21 and 11 in card_num:
        card_num.remove(11)
        card_num.append(1)
    return sum(card_num)


def who_wins(u_score, c_score):
    if u_score > 21 and c_score > 21:
       return "You went over. You lose 😤"

    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You Win 😁"
    else:
        return "You Lose 😤"
def play_game():
    print(logo)
    usr_cards = []
    comp_cards = []
    for _ in range(2):
        usr_cards.append(deal_card())
        comp_cards.append(deal_card())

    game_over = False
    while not game_over:
        usr_score = calculate_score(usr_cards, CARD_VAL)
        comp_score = calculate_score(comp_cards, CARD_VAL)
        print(f"Your cards: {usr_cards}, current score: {usr_score}")
        print(f"Computer's first card: {comp_cards[0]}")

        if usr_score == 0 or comp_score == 0 or usr_score > 21:
            game_over = True
        else:
            if input("Do you want to draw more cards? Type 'y' to draw or 'n' to pass: ") == 'y':
                usr_cards.append(deal_card())
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards, CARD_VAL)

    print(f"Your final hand: {usr_cards}, final score: {usr_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(who_wins(usr_score, comp_score))


while (input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == 'y'):
    play_game()
