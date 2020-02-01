import json

def get_valid_recipes(ingredients: list, recipes : dict):
    valid_recipies = {} 
    for recipe, recipe_dict in recipes.items():  #goes through dict of recipes
            for recipe_attributes, value in recipe_dict.items():
                if recipe_attributes == "ingredients":  #if the key is "ingredients", the value is a list of strings containing the ingredients
                    sum = 0                             #sum of the number of ingredients in the recipe
                    for ingredient in ingredients:
                        for ingredient_string in value: #iterates through each string within the value list
                            if ingredient in ingredient_string:
                                sum += 1
                                if sum >= .7 * len(value):      #we determined 70% of the ingredients must be covered by the items the user has
                                    valid_recipies[recipe] = recipe_dict
    
    return valid_recipies


def get_all_valid_recipes(ingredients : list) -> json:

    with open('recipes/recipes_raw_nosource_ar.json') as f:     #gets data from allrecipes
        ar_recipes = json.load(f)
    
    valid_recipies = get_valid_recipes(ingredients, ar_recipes)

    with open('recipes/recipes_raw_nosource_epi.json') as f:    #gets data from epicurious
        ep_recipes = json.load(f)
    
    valid_recipies.update(get_valid_recipes(ingredients, ep_recipes))

    with open('recipes/recipes_raw_nosource_fn.json') as f:     #gets data from food network
        fn_recipes = json.load(f)
    
    valid_recipies.update(get_valid_recipes(ingredients, fn_recipes)) 
