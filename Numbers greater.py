num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
num3 = int(input("Enter the number3: "))
if((num1>num2)& (num1>num3)):
	print(num1,"IS THE GREATES")
elif((num1>num2)& (num1>num3)):
	print(num2, "Is the greates among the three")
else:
	print(num3,"Is the greated among the three")
input()