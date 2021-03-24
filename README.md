# spoonacular-ui
Command line user interface for the [Spoonacular API](https://spoonacular.com/food-api/)

Description:

This is a command-line user interface for the Spoonacular API. You can enter ingredients that you already have, 
and it will suggest recipes to you. You can then like a recipe, which will then compile a list of the missing ingredients for this recipe. After the recipe selection process, the missing ingredients, along with their aisle locations and total cost will be shown.

## User Documentation

Run Spoonacular UI:

0. Make sure the API key has been setup (see technical documentation) 
1. Execute the file './spoonacular_ui.py' (you might have to make it executable with 'chmod +x spoonacular_ui.py')
2. Enter the number of ingredients you already have
3. Enter the ingredients 
4. Like recipes you want to later utilize 
5. Finish the recipe selection process by entering that you are satisfied

## Technical Documentation

Setup Spoonacular UI:

Add your API key to your environment variables to keep it secure by entering the following command in your shell:
```
export API_KEY='<your key here>'
```
Alternatively you can place it in a bash file so you can just execute the file when needed or after a reboot:
```
#!/bin/sh

export API_KEY='<your key here>'
```
The Spoonacular UI currently expects the API_KEY variable to be set as a environment variable. Alternatively, the API_KEY could be read from a file directly by the script, but that would require it to be added to .gitignore and be kept out of the source files.

The code has several methods:
```
select_ingredients
retrieve_recipes
determine_missing_ingredients
display_cost_location
```
The methods are de-coupled so that they can be unit tested (testability) or mocked individually, and also be reused for future purposes (reusability).

## TODO

1. Come up with a better way to check for legitamite ingredients such as "Salt" vs "Sal" in select_ingredients
2. When liking the recipe for 4-Ingredient Dark Chocolate Fudgesicles, it seems to crash the API when retrieving the missing ingredients
