from recipes.models import IngredientRating

ratings = (
    ('Beef', 365),
    ('Fish', 301),
    ('Prawns', 227),
    ('Cheese', 98),
    ('Lamb', 97),
    ('Pork', 76),
    ('Chicken', 49),
    ('Rice', 35),
    ('Egg', 22),
    ('Nuts', 19),
    ('Milk', 11),
    ('Peas', 8),
    ('Tomatoes', 8),
    ('Flour', 7),
    ('Banana', 3),
    ('Citrus', 2),
    ('Apple', 1)
               )

for rating in ratings:
    i = IngredientRating(ingredient = rating[0], rating = rating[1])
    i.save()