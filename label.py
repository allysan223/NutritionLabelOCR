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
        self.servingSize = search('Serving Size {val:w}', text)['val']
        self.servingsPer = search('Servings per container {val:d}', text)['val']
        self.calories = search('Calories {val:d}', text)['val']
        self.fatCals = search('FatCal {val:d}', text)['val']
        self.totalFat = search('Total Fat {:w} {:w}', text)[0], search('Total Fat {:w} {:w}', text)[1]+"%"
        self.satFat = search('Sat Fat {:w} {:w}', text)[0], search('Sat Fat {:w} {:w}', text)[1]+"%"
        self.cholesterol = search('Cholesterol {:w} {:w}', text)[0], search('Cholesterol {:w} {:w}', text)[1]+"%"
        self.sodium = search('Sodium {:w} {:w}', text)[0], search('Sodium {:w} {:w}', text)[1]+"%"
        self.totalCarbs = search('Total Carbohydrate {:w} {:w}', text)[0], search('Total Carbohydrate {:w} {:w}', text)[1]+"%"
        self.fiber = search('Fiber {val:w}', text)['val']
        self.sugars = search('Sugars {val:w}', text)['val']
        self.protien = search('Protein {:w} {:w}', text)[0], search('Protein {:w} {:w}', text)[1]+"%"
        try:
            self.ingredients = text.split("Ingredients: ")[1]
        except IndexError:
            self.ingredients = None
            
    def labelPrint(self):
        print("serving size:", self.servingSize)
        print("servings per container:", self.servingsPer)
        print("calories:", self.calories)
        print("fat calories:", self.fatCals)
        print("total fat:", self.totalFat)
        print("saturated fats:", self.satFat)
        print("cholesterol:", self.cholesterol)
        print("sodium:", self.sodium)
        print("fiber:", self.fiber)
        print("sugars:", self.sugars)
        print("protien:", self.protien)
        print("ingredients:", self.ingredients)


    