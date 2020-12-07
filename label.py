from parse import *

class Label():
    """
    Serving Size cup
    Servings per container 4
    Calories 250 FatCal 120
    Total Fat 130 20%
    Sat Fat 99 40%
    Cholesterol 28mg 12%
    ‘Sodium 55mg 2%
    Total Carbohydrate 30g 12%
    Dietary Fiber 2g
    Sugars 239
    Protein 4g 8%
    Ingredients: Cream, Skim Mik, Liquid
    ‘Sugar, Water, Egg Yolks, Brown Sugar,
    Mikfat, Peanut Ol, Sugar, Butter, Salt,
    Carrageenan, Vanilla Extract.
    """
    def __init__(self, text):
        self.text = text
        self.servingSize = search('Serving Size {:w}', text)
        self.servingsPer = search('Servings per container {:d}', text)
        self.calories = search('Calories {:d}', text)
        self.fatCals = search('FatCal {:d}', text)
        self.totalFat = search('Total Fat {:d} {:w}', text)
        self.satFat = search('Sat Fat {:d} {:w}', text)
        self.cholesterol = search('Cholesterol {:d} {:w}', text)
        self.sodium = search('Sodium {:d} {:w}', text)
        self.totalCarbs = search('Total Carbohydrate {:d} {:w}', text)
        self.fiber = search('Fiber {:w}', text)
        self.sugars = search('Sugars {:d}', text)
        self.protien = search('Protein {:d} {:w}', text)
        try:
            self.ingredients = text.split("Ingredients: ")[1]
        except IndexError:
            self.ingredients = None

    