import random

random_card_type = random.choice(("♣", "♦", "♥", "♠"))
random_card_value = random.choice(("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"))

print(random_card_type)
print(random_card_value)

print(random_card_value, random_card_type)