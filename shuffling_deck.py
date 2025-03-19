import itertools
import random
suits=['Hearts','Diamonds','Clubs','Spades']
ranks=['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
deck=list(itertools.product(ranks,suits))
random.shuffle(deck)
def draw_card():
    return deck.pop() if deck else None

hand=[draw_card() for _ in range(5)]
print("Your hand:")
for rank,suit in hand:
    print(f"{rank} of {suit}")