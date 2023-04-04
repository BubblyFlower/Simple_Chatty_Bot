pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

food = {"pasta": pasta, "apple pie": apple_pie, "ratatouille": ratatouille, "chocolate cake": chocolate_cake, "omelette": omelette}
ing = input()

for item in food.keys():
    if ing in food.get(item):
        print(item, 'time!')