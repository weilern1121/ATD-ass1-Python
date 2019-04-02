import gzip
import json
from urllib.request import urlopen
recipe_book = urlopen('https://s3.amazonaws.com/openrecipes/20170107-061401-recipeitems.json.gz')
recipe_book = gzip.open(recipe_book)

def parseInput(list_of_words):
    keywords, ingredientsToInclude, ingredientsToExclude = [], [], []
    for word in list_of_words:
        if word[0] == '+':
            ingredientsToInclude.append(word[1:])
        elif word[0] == '-':
            ingredientsToExclude.append(word[1:])
        else:
            keywords.append(word)
    return keywords, ingredientsToInclude, ingredientsToExclude

def getWithoutNone(recipe, field):
    if recipe[field]:
        return recipe[field]
    else:
        return []

def search():
    searchResult = []
    input = "dinner +chicken -nuts"
    keywords, ingredientsToInclude, ingredientsToExclude = parseInput(input.split())
    for recipe in recipe_book:
        recipe = json.loads(recipe.decode('utf8'))
        if not all([keyword in getWithoutNone(recipe,'description') for keyword in keywords]):
            continue
        if not all([ingredient in getWithoutNone(recipe,'ingredients') for ingredient in ingredientsToInclude]):
            continue
        if any([ingredient in getWithoutNone(recipe, 'ingredients') for ingredient in ingredientsToExclude]):
            continue
        searchResult.append(recipe)
    return searchResult

print(search())
# input = "dinner +chicken"
# if input == 'search':
#     searchResults = search()