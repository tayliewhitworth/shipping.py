groundPremium = 125.00
weight = 4.8
weight2 = 41.5

def groundShipping(weight):
  flatCharge = 20
  if weight <= 2:
    cost = weight * 1.5 + flatCharge
  elif weight > 2 and weight <= 6:
    cost = weight * 3 + flatCharge
  elif weight >= 6 and weight <= 10:
    cost = weight * 4 + flatCharge
  else:
    cost = weight * 4.75 + flatCharge
  return cost

def droneShipping(weight):
  if weight <= 2:
    cost = weight * 4.5
  elif weight > 2 and weight <= 6:
    cost = weight * 9
  elif weight >= 6 and weight <= 10:
    cost = weight * 12
  else:
    cost = weight * 14.25
  return cost

def cheapestOption(weight):
  if groundShipping(weight) < groundPremium and groundShipping(weight) < droneShipping(weight):
    print('The cheapest option is Ground Shipping')
  elif droneShipping(weight) < groundShipping(weight) and droneShipping(weight) < groundPremium:
    print('The cheapest option is Drone Shipping')
  else:
    print('The cheapest option is Premium Shipping')


print(f'The price for ground shipping is: ${groundShipping(weight):.2f} ')
print(f'The price for premium shipping is: ${groundPremium:.2f}')
print(f'The price for drone shipping is: ${droneShipping(weight):.2f}')
cheapestOption(weight)

print()

print(f'The price for ground shipping is: ${groundShipping(weight2):.2f} ')
print(f'The price for premium shipping is: ${groundPremium:.2f}')
print(f'The price for drone shipping is: ${droneShipping(weight2):.2f}')
cheapestOption(weight2)
