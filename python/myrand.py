#required import
import random

#seed data
# random.seed(45)

# start, stop, step
random_int_value = random.randrange(0, 9, 2) #exclusive...0, 8
print(random_int_value)


choice_arr = [55,44,77,88]
print(random.choice(choice_arr))

# float between 0 and 1 min max
random_float_value = random.uniform(0, 1)
print(random_float_value)
print(random.random())

#shuffle deck
deck = ["ace of hearts", "2 of dimaonds", "3 of clubs", "4 of spades", "5 of diamonds", "6 of hearts"]
random.shuffle(deck)
print(deck)

# 3 random cards from deck
my_sample = random.sample(deck, k=3)
print(my_sample)
