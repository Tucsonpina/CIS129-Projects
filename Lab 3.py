# Declare prices of coffee's as well as tax

priceCoffee = 5
priceMuffin = 4
TAX = 0.06

# Ask for total number of item's purchased

print("*******************************************")
print("My Coffee and Muffin Shop")
totalCoffee = input("Number of coffee's bought? ")
totalMuffin = input("Number of Muffins bought? ")
print("*******************************************")

# Caclulate total's and redisplay receipt
# First convert values to proper data types

totalCoffee = int(totalCoffee)
totalMuffin = int(totalMuffin)
coffeeFinal = totalCoffee*priceCoffee
muffinFinal = totalMuffin*priceMuffin
subTotal = coffeeFinal + muffinFinal
currentTax = subTotal * TAX
finalTotal = currentTax+subTotal

print("\n*******************************************")
print("My Coffee and Muffin Shop Receipt")
print(totalCoffee," Coffee at $",priceCoffee," each: $",coffeeFinal)
print(totalMuffin," Muffins at $",priceMuffin," each: $",muffinFinal)
#Multiply tax by 100 to display proper value
print((TAX*100),"% tax: $",currentTax)
print("--------")
print("Total: $",finalTotal)
print("*******************************************")


