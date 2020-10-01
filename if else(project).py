# python
sub = ("This is just for pratice")
bus = ("My name is Surya")
print(bus  + ". i am learning python and " + sub)

def water(water,money):
	if water >= 200 and money >= 20:
		return ("thank you very much")
	elif water < 200 and money >= 20:
		return ("sorry we dont have stock")
	elif water >=200 and money < 20:
		return ("not enough money")
	else:
		return("not enough money plus we dont have stock")
print(water(0,0))
print(water(200,19))
print(water(180,20))
print(water(200,20))
print(water(10,0))
print(water(203,192))
print(water(18023,2032))
print(water(54200,2530))
