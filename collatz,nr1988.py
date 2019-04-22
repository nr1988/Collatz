def collatz(num):
	if num%2==0:
		print(num//2)
		return (num//2)
	elif num %2==1:
		print(3*num+1)
		return(3*num+1)


print("give a number:")
try:
	n=input(int())
except:
	print("That's not a valid answer, please enter a valid number")
	exit()

while n!=1:
	n=collatz(int(n))





		

