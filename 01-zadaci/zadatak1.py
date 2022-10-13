def four(listOfNumbers):
	return [num if num%4==0 else round(num**0.5, 2) for num in listOfNumbers]

print(four([213, 14, 12, 6543, 232]))
print(four([16, 100, 50]))