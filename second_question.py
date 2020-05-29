def second_question(num):
	amount = num
	for i in range(1, num + 1):
		if((i % 3 == 0 and i % 5 != 0 ) or (i % 3 != 0 and i % 5 == 0)):
			amount -= 1
	return amount
	
if __name__ == '__main__':
	print(second_question(15))