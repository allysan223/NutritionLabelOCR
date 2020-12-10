from parse import *
import re

def find_between(s, start, end):
    try:
        s = s.lower()
        start = start.lower()
        end = end.lower()
        # get text inbetween start and end
        text = (s.split(start))[1].split(end)[0].strip()
        # remove ':' if exists
        text = text.replace(":", "")
    #return if not found
    except IndexError:
        text = "Not Found"
    return text.strip()

class Label():
    """
    This is a Label class to extract and run functions on nutrition labels.
    """
    def __init__(self, text):
        self.text = text
        # put each attribute in try catch in case value is not found from search
        # try:
        #     self.servingSize = search('Serving Size {val:w}', text)['val'] 
        # except TypeError:
        #     self.servingSize = "Not Found"
        self.servingSize = find_between(text, "Serving Size", "\n")
        self.servingsPer = find_between(text, "Servings Per Container", "\n") 
        self.calories = find_between(text, "Calories", "cal")
        self.calories = find_between(text, "Calories", "\n") 
        self.fatCals = find_between(text, "calories from fat", "\n")
        if "fatcal" in self.calories:
            self.calories = find_between(text, "Calories", "fatcal") 
            self.fatCals = find_between(text, "fatcal", "\n")
        self.totalFat = find_between(text, "total fat", "\n")
        self.satFat = find_between(text, "Sat Fat", "\n")
        if self.satFat == "Not Found":
            self.satFat = find_between(text, "Sat. Fat", "\n")
        if self.satFat == "Not Found":
            self.satFat = find_between(text, "Saturated Fat", "\n")
        self.cholesterol = find_between(text, "cholesterol", "\n")
        self.sodium = find_between(text, "sodium", "\n")
        self.totalCarbs = find_between(text, "Total Carbohydrate", "\n")
        self.fiber = find_between(text, "Fiber", "\n")
        self.sugars = find_between(text, "sugars", "\n")
        self.protein = find_between(text, "protein", "\n")

        try:
            self.ingredients = re.split("Ingredients:", text, flags=re.IGNORECASE)[1]
            # self.ingredients = text.split("Ingredients: ")[1]
        except IndexError:
            self.ingredients = "Not Found"
        if self.ingredients == "Not Found":
            try:
                self.ingredients = re.split("GREDIENTS:", text, flags=re.IGNORECASE)[1]
                # self.ingredients = text.split("Ingredients: ")[1]
            except IndexError:
                self.ingredients = "Not Found"
            
    def labelPrint(self):
        print("serving size:", self.servingSize)
        print("servings per container:", self.servingsPer)
        print("calories:", self.calories)
        print("fat calories:", self.fatCals)
        print("total fat:", self.totalFat)
        print("saturated fats:", self.satFat)
        print("cholesterol:", self.cholesterol)
        print("sodium:", self.sodium)
        print("total carbohydrates:", self.totalCarbs)
        print("fiber:", self.fiber)
        print("sugars:", self.sugars)
        print("protein:", self.protein)
        print("ingredients:", self.ingredients)

    def labelString(self):
        s = ("serving size:"+ self.servingSize + "\nservings per container:" + self.servingsPer +
                "\ncalories:"+ self.calories + "\nfat calories:" + self.fatCals + "\ntotal fat:" + 
                self.totalFat + "\nsaturated fats:" + self.satFat + "\ncholesterol:" + self.cholesterol +
                "\nsodium:" + self.sodium + "\ntotal carbohydrates:" + self.totalCarbs + "\nfiber:"+ self.fiber +
                "\nsugars:" + self.sugars + "\nprotein:" + self.protein + "\ningredients:" + self.ingredients)
        return s
    
    def containsSugar(self):
        sugars = ["syrup", "ose", "sugar", "honey", "molasses", "caramel", "agave"]
        if self.ingredients == "Not Found":
            return None
        else:
            for sugar in sugars:
                if sugar in self.ingredients.lower():
                    return True
        return False

    