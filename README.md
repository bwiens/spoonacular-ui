# spoonacular-ui

## Description:

This is a command-line user interface for the [Spoonacular API](https://spoonacular.com/food-api/). You can enter ingredients that you already have, and it will suggest recipes to you. You can then like a recipe, which will then compile a list of the missing ingredients for this recipe. After the recipe selection process, the missing ingredients, along with their aisle locations and the total cost will be shown.

## User Documentation

Run Spoonacular UI:

0. Make sure the API key has been set up (see technical documentation) 
1. Execute the file './spoonacular_ui.py' (you might have to make it executable with 'chmod +x spoonacular_ui.py')
2. Enter the number of ingredients you already have
3. Enter the ingredients 
4. Like recipes you want to later utilize 
5. Finish the recipe selection process by entering that you are satisfied

## Technical Documentation

Setup Spoonacular UI:

Install the following Python libraries:

```
sys (to check if the API Key has been set)
os (to load the API Key from the environment)
requests (to call the Spoonacular API)
```

Add your API key to your environment variables to keep it secure by entering the following command in your shell:
```
export API_KEY='<your key here>'
```
Alternatively, you can place it in a bash file so you can just execute the file when needed or after a reboot:
```
#!/bin/sh

export API_KEY='<your key here>'
```
The Spoonacular UI currently expects the API_KEY variable to be set as an environment variable. Alternatively, the API_KEY could be read from a file directly by the script, but that would require it to be added to .gitignore and be kept out of the source files.

The code has several methods:
```
select_ingredients
retrieve_recipes
determine_missing_ingredients
display_cost_location
```
The methods are de-coupled so that they can be unit tested (testability) or mocked individually, and also be reused for future purposes (reusability).

## TODO

1. Come up with a better way to check for legitimate ingredients such as "Salt" vs "Sal" in select_ingredients.
2. When liking the recipe for 4-Ingredient Dark Chocolate Fudgesicles, it seems to crash the API when calling mealplanner/shopping-list/compute for its missing ingredients -- come up with an error check for this.
3. Add Unit Tests for the de-coupled methods.
4. Add a successful API Connection test to check for Satus Code 200.
5. Add a check for sufficient quota with Spoonacular.
