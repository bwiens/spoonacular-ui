#!/usr/bin/python3

import requests
import os

class SpoonacularUI(object):

    def __init__(self):
        self.api_url = 'https://api.spoonacular.com/'
        self.headers = {"Application": "spoonacular",
                        "Content-Type": "application/x-www-form-urlencoded"}
        self.api_key = os.environ.get("API_KEY")

    def select_ingredients(self):
        """
        Gather ingredients from user input
        """
        ingredients = []
        # determine number of ingredients the user already has, must be between 1 and 20
        n = 0
        while True:
            try:
                n = int(input('How many ingredients do you have? Enter an integer between 1 and 10: '))
            except ValueError:
                print('Enter an integer between 1 and 10 ')
                continue
            if 0 < n < 11:
                break
        # retrieve ingredients the user already has
        for i in range(0, n):
            ingredient = ''
            # make sure input is alphanumeric
            while not ingredient.isalpha():
                ingredient = input(
                        "Enter Ingredient (3-10 characters), " + str(i + 1) + " out of " + str(n) + ": ")
            # add the ingredient
            ingredients.append(ingredient)
        return ingredients

    def retrieve_recipes(self, ingredients):
        """
        Search for recipes based on entered ingredients
        """
        parameters = {
            'ingredients': ingredients,
            'apiKey': self.api_key
        }
        result = requests.get(self.api_url + 'recipes/findByIngredients',
                              headers=self.headers,
                              params=parameters)
        recipes = result.json()
        return recipes

    def determine_missing_ingredients(self, user_recipes):
        """
        Select recipes that are likable
        """
        # create a dictionary for missing ingredients of "liked" recipes
        missing_ingredients = {'items': []}
        # create sets of valid input choices
        yes = {'y', 'ye', 'yes', }
        no = {'n', 'no'}
        satisfied = False
        # present recipes and see if the user likes any
        for recipe in user_recipes:
            # if the user is satisfied, exit the loop
            if satisfied:
                break
            choice = ''
            while choice not in yes and choice not in no:
                choice = input("Are you interested in " + str(recipe['title']) + "? Type 'yes' or 'no'. ").lower()
            if choice in yes:
                # add missing ingredients and their missing amounts
                for mi in recipe['missedIngredients']:
                    missing_ingredients['items'].append((mi['originalString']))
            # check if the user is satisfied
            choice = input("Are you satisfied with your recipe selection? Type 'yes' or 'no'. ").lower()
            if choice in yes:
                satisfied = True
        return missing_ingredients

    def display_cost_location(self, ingredients):
        """
        Find aisle locations and cost of missing ingredients
        """
        parameters = {
            'apiKey': self.api_key
        }
        # fetch the aisle locations and cost of each missing ingredient
        result = requests.post(self.api_url + 'mealplanner/shopping-list/compute',
                               headers=self.headers,
                               json=ingredients,
                               params=parameters)
        locations = result.json()
        print()
        print("You are missing the following ingredients: ")
        print("------------------------------------------")
        # show the aisle locations
        for ingredient in (ingredients['items']):
            print(ingredient)
        print()
        print("You can find the ingredients in the following aisles:")
        print("-----------------------------------------------------")
        for aisle in locations['aisles']:
            for item in aisle["items"]:
                print(item['name'] + ' - ' + item['aisle'])
        # convert the total cost to dollar amount
        print('Estimated Total Cost: ' + '${:,.2f}'.format(locations['cost'] / 100))

# create instance of SpoonacularUI class and call the de-coupled methods
sp = SpoonacularUI()
user_ingredients = sp.select_ingredients()
spoon_recipes = sp.retrieve_recipes(user_ingredients)
m_ingredients = sp.determine_missing_ingredients(spoon_recipes)
sp.display_cost_location(m_ingredients)
