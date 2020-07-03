import pandas as pd

chips = {'Chips':  ['Simba', 'Lays']}
cooldrinks={'Cooldrinks': ['Coke', 'Fanta']}
chocolates ={'Chocolates': ['Cadbury', 'Tex']}
pies = {'Pies':['Pepper Steak', 'Chicken']}
fruit = {'Fruit':['Pear', 'Apple', 'Orange']}
cupcakes = {'Cupcakes':['vanilla', 'Chocolate']}
veggies = {'Veggies':['spinach', 'cabbage']}

dfChips = pd.DataFrame(chips)
dfCooldrinks = pd.DataFrame(cooldrinks)
dfChocolates = pd.DataFrame(chocolates)
dfPies = pd.DataFrame(pies)
dfFruit = pd.DataFrame(fruit)
dfCupcakes = pd.DataFrame(cupcakes)
dfVeggies = pd.DataFrame(veggies)

dvList = [dfChips, dfCooldrinks, dfChocolates, dfPies, dfFruit, dfCupcakes, dfVeggies]
for i in range(len(dvList)):
    print(dvList[i])

