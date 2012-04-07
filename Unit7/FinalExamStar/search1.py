def search(n, mylist):
	for num in mylist:
		if num == n:
			return True
	return False

a_list = [2,4,5,8]
print search(6, a_list)

