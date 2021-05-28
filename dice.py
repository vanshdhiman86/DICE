import random
d1="[-----------]\n[           ]\n[     0     ]\n[           ]\n[-----------]"
d2="[-----------]\n[           ]\n[  0     0  ]\n[           ]\n[-----------]"
d3="[-----------]\n[     0     ]\n[     0     ]\n[     0     ]\n[-----------]"
d4="[-----------]\n[   0   0   ]\n[           ]\n[   0   0   ]\n[-----------]"
d5="[-----------]\n[   0   0   ]\n[     0     ]\n[   0   0   ]\n[-----------]"
d6="[-----------]\n[   0   0   ]\n[   0   0   ]\n[   0   0   ]\n[-----------]"
switch = { 1 : d1, 2 : d2, 3 : d3, 4 : d4, 5 : d5, 6 : d6}
dice=random.randint(1,6)
x ="y"
while x == "y":
	dice=random.randint(1,6)
	print(switch[dice])
	x = input("press y to roll the dice ")

input()