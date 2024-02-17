# Declare prices of coffee's as well as tax

priceCoffee = 5
priceMuffin = 4
priceScones = 6
priceMugs = 15
TAX = 0.06

# Ask for total number of item's purchased

print("*******************************************")
print("My Coffee and Muffin Shop")
totalCoffee = input("Number of coffees bought? ")
totalMuffin = input("Number of muffins bought? ")
totalScones = input("Number of scones bought? ")
totalMugs = input("Number of mugs bought? ")
print("*******************************************")

# Caclulate total's and redisplay receipt
# First convert values to proper data types

totalCoffee = int(totalCoffee)
totalMuffin = int(totalMuffin)
totalScones = int(totalScones)
totalMugs = int(totalMugs)
coffeeFinal = totalCoffee*priceCoffee
muffinFinal = totalMuffin*priceMuffin
sconesFinal = totalScones*priceScones
mugsFinal = totalMugs*priceMugs
subTotal = coffeeFinal + muffinFinal + sconesFinal + mugsFinal
currentTax = subTotal * TAX
finalTotal = currentTax+subTotal

print("\n*******************************************")
print("My Coffee and Muffin Shop Receipt")

# Add conditions to only display necessary info

if totalCoffee > 0 : 
  print(totalCoffee," Coffee at $",priceCoffee," each: $",coffeeFinal)
if totalMuffin > 0 :
  print(totalMuffin," Muffins at $",priceMuffin," each: $",muffinFinal)
if totalScones > 0 :
  print(totalScones," Scones at $",priceScones," each: $",sconesFinal)
if totalMugs > 0 :
  print(totalMugs," Mugs at $",priceMugs," each: $",mugsFinal)
#Multiply tax by 100 to display proper value
print((TAX*100),"% tax: $",currentTax)
print("--------")
print("Total: $",finalTotal)
print("Thank you for shopping with us today!")
print("*******************************************")


