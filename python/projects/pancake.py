class Pancake(self, eggs, flour, salt, milk, butter):
    self.eggs = eggs
    self.flour = flour
    self.salt = salt
    self.milk = milk
    self.butter = butter

    def portion(eggs, flour, salt, milk, butter):
        numEgg = input(int('enter numbers of eggs you got'))


ingredient_basis = {}
ingredient_basis['egg']='based on eggs?'
ingredient_basis['flour']='based on flour?'
ingredient_basis['salt']='based on salt?... lol'
ingredient_basis['milk']='based on milk?'
ingredient_basis['butter']='based on butter?'


menu = {}
menu['1']='1: Based on the availble ingredients'
menu['2']='2: Based on number of portions needed'

portion = {}
portion['1']
portion['2']
portion['3']
portion['4']
portion['5']
portion['6']
portion['7']
portion['8']
portion['9']
portion['10']

def func_menu(ingredient_basis, menu, portion):
    option1=menu.keys()
    option1.sort()
    for entry in option1:
        print (entry, menu[entry])

def selection_ingredients(menu):
    pass
def selection_portions(menu):
    pass
def main(func):
    pass

if __name__=='__main__':
    main()