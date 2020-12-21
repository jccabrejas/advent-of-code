from collections import defaultdict
# import numpy as np
# import re
import os, sys

def read_input(filename='test.txt'):
    with open(os.path.join(os.getcwd(),filename)) as f:
        result = list()
        for line in f.readlines():
            result.append(line.rstrip())
        return result

if len(sys.argv) == 2:
    inputText = read_input(sys.argv[1])
else:
    inputText = read_input()

def part_1():
    # parse file {allergen1: [[possible foods], [possible foods], ... ],
    #             allergen2: [[f1, f3], ...],
    #               ...}
    # count allergens and foods
    # For each allergen find the intersection
    # if len == 1 => result = {allergen:food}
    # remove that food from the list
    # repeat until all determined
    # count foods with allergens and count foods without allergens

    ingredients = defaultdict(list)

    foodSet = set()

    for line in inputText:
        line = line.replace('contains ', '').replace(')', '').replace(' (', '(')
        foodTemp, allergenTemp = line.split('(')
        foods = foodTemp.split(' ')
        allergens = allergenTemp.replace(' ','').split(',')
        foodSet.update(foods)

        for a in allergens:
            ingredients[a].append(set(foods))

    result = defaultdict(str)
    temp = defaultdict(set)
    while len(ingredients) > 0:
        iteration = ingredients.copy()
        for a, possibleFoods in iteration.items():
            intersection = set.intersection(*possibleFoods)
            if len(intersection) == 1: 
                temp[a] = list(intersection)[0]
                del ingredients[a]
                for k, v in ingredients.items():
                    [s.discard(temp[a]) for s in ingredients[k]]
                continue

    allergenicFoods = set()
    allergenicFoods.update(temp.values())
    nonAllergenicFoods = foodSet - allergenicFoods

    counter = 0
    for line in inputText:
       for t in nonAllergenicFoods:
           if t in line.split(' '):
               counter += 1
    

    return counter, temp

result, allergens = part_1()
print('Part 1: ',result)

print('Part 2: ', ','.join([allergens[a] for a in sorted(allergens.keys())])) 