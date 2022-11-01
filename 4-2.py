small = True # array[0]
green = True # array[1]

cherry = [True,False,"Cherry"]
pea = [True,True,"Pea"]
watermelon = [False,True,"Watermelon"]
pumpkin = [False,False,"Pumpkin"]

def test(obj):
	if(obj[0] == small & obj[1] == green):
		print(obj[2])

test(cherry)
test(pea)
test(watermelon)
test(pumpkin)