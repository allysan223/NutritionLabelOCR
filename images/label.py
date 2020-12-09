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
        # put each attribute in try catch in case value is not found from search
        try:
            self.servingSize = search('Serving Size {val:w}', text)['val'] 
        except TypeError:
            self.servingSize = None

        try:
            self.servingsPer = search('Servings per container {val:d}', text)['val']
        except TypeError:
            self.servingsPer = None

        try:
            self.calories = search('Calories {val:d}', text)['val']
        except:
            self.calories = None

        try:
            self.fatCals = search('FatCal {val:d}', text)['val']
        except:
            self.fatCals = None

        self.totalFat = [None, None]
        try:
            self.totalFat[0] = search('Total Fat {:w} {:w}', text)[0]
            
        except:
            pass
        try:
            self.totalFat[1] = search('Total Fat {:w} {:w}', text)[1]+"%"
        except:
            pass

        self.satFat = [None, None]
        try:
            self.satFat[0] = search('Sat Fat {:w} {:w}', text)[0]
        except:
            pass
        try:
            self.satFat[1] = search('Sat Fat {:w} {:w}', text)[1]+"%"
        except:
            pass

        self.cholesterol = [None, None]
        try:
            self.cholesterol[0] = search('Cholesterol {:w} {:w}', text)[0]
        except:
            pass
        try:
            self.cholesterol[1] = search('Cholesterol {:w} {:w}', text)[1]+"%"
        except:
            pass

        self.sodium = [None, None]
        try:
            self.sodium[0] = search('Sodium {:w} {:w}', text)[0]
        except:
            pass
        try:
            self.sodium[1] = search('Sodium {:w} {:w}', text)[1]+"%"
        except:
            pass
        
        self.totalCarbs = [None, None]
        try:
            self.totalCarbs[0] = search('Total Carbohydrate {:w} {:w}', text)[0]
        except:
            pass
        try:
            self.totalCarbs[1] = search('Total Carbohydrate {:w} {:w}', text)[1]+"%"
        except:
            pass

        try:
            self.fiber = search('Fiber {val:w}', text)['val']
        except:
            self.fiber = None

        try:
            self.sugars = search('Sugars {val:w}', text)['val']
        except:
            self.sugars = None

        self.protien = [None, None]
        try:
            self.protien[0] = search('Protein {:w} {:w}', text)[0]
        except:
            pass
        try:
            self.protien[1] = search('Protein {:w} {:w}', text)[1]+"%"
        except:
            pass

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


    