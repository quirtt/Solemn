import numpy as np

import random
def riffle_shuffle(deck):
    cut_index = int(np.random.normal(25.78, 2.3046))
    cut_index = max(1, min(cut_index, 51))
    left_hand = deck[:cut_index]
    right_hand = deck[cut_index:]
    shuffled_deck = []
    while left_hand or right_hand:
        if len(right_hand) > 0 and np.random.rand() <= len(right_hand) / (len(left_hand) + len(right_hand)):
            shuffled_deck.append(right_hand.pop(0))
        else:
            shuffled_deck.append(left_hand.pop(0))
    return shuffled_deck

def swap_first_card(deck):
    index = int(list(np.random.binomial(52, 0.5, 1))[0])
    index = min(index, 52)
    deck[0]=deck.pop(0)
    deck.insert(index,deck[0])
def rising_singleton(array):
    # Create an index array to store the positions of values in the input array
    index = [0] * 52

    # Populate the index array with the positions of values in the input array
    for i in range(52):
        index[array[i] - 1] = i

    Sum = 0
    SingletonCard = 0

    # Check if there is a unique Rising Singleton
    for i in range(52):
        if (index[i] >= index[min(i + 1, 51)]) and (index[i] <= index[max(i - 1, 0)]):
            Sum += 1
            SingletonCard = i + 1

    return [Sum == 1, SingletonCard]

unique_singleton_count = 0

# Repeat the process 10,000 times
for x in range(10000):
    deck = list(range(1,53))
    for y in range(3):
        deck = riffle_shuffle(deck)
    swap_first_card(deck)
    is_unique_singleton,z = rising_singleton(deck)
    if is_unique_singleton:
        unique_singleton_count += 1

# Percentage of unique singletons
print("Percentage: ", unique_singleton_count/100)import numpy as np

import random
def riffle_shuffle(deck):
    cut_index = int(np.random.normal(25.78, 2.3046))
    cut_index = max(1, min(cut_index, 51))
    left_hand = deck[:cut_index]
    right_hand = deck[cut_index:]
    shuffled_deck = []
    while left_hand or right_hand:
        if len(right_hand) > 0 and np.random.rand() <= len(right_hand) / (len(left_hand) + len(right_hand)):
            shuffled_deck.append(right_hand.pop(0))
        else:
            shuffled_deck.append(left_hand.pop(0))
    return shuffled_deck

def swap_first_card(deck):
    index = int(list(np.random.binomial(52, 0.5, 1))[0])
    index = min(index, 52)
    deck[0]=deck.pop(0)
    deck.insert(index,deck[0])
def rising_singleton(array):
    # Create an index array to store the positions of values in the input array
    index = [0] * 52

    # Populate the index array with the positions of values in the input array
    for i in range(52):
        index[array[i] - 1] = i

    Sum = 0
    SingletonCard = 0

    # Check if there is a unique Rising Singleton
    for i in range(52):
        if (index[i] >= index[min(i + 1, 51)]) and (index[i] <= index[max(i - 1, 0)]):
            Sum += 1
            SingletonCard = i + 1

    return [Sum == 1, SingletonCard]

unique_singleton_count = 0

# Repeat the process 10,000 times
for x in range(10000):
    deck = list(range(1,53))
    for y in range(3):
        deck = riffle_shuffle(deck)
    swap_first_card(deck)
    is_unique_singleton,z = rising_singleton(deck)
    if is_unique_singleton:
        unique_singleton_count += 1

# Percentage of unique singletons
print("Percentage: ", unique_singleton_count/100)