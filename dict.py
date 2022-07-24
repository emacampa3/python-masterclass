# dictionary
vehicles = {
  'dream': 'Honda 250T',
  'er5': 'Kawasaki ER5'
}

# ways of retrieving values from a dict
my_car = vehicles['er5'] # crashes if the key does not exist
my_car = vehicles.get('er5') # returns None if the key does not exist
print(my_car)
