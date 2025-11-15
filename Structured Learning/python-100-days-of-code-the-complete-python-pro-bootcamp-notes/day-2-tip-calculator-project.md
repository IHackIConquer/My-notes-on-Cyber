# Day 2 - Tip Calculator Project

```
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? £"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tipcalc =(tip/100)
tipvalue = (bill * tipcalc)

final_bill_per_person = ((bill + tipvalue)/people)

final_amount = round(final_bill_per_person,2)

print("Each person should pay: £" + str(final_amount))

```

{% embed url="https://trinket.io/python/fcc388e1c06f?outputOnly=true&runOption=run" %}

