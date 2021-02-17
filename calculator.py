import math

print("                            CALCULATOR")
print("ОПЕРАЦИИ")
print("Сложенте: +\nВычитание: -\nУмножение: *\nДеление: / \nВозведение в степень: **\nИзвлечение квадратного корня: √\n")

print("Введите числа, над которыми хотите провести операцию -->")


firstNum = int(input("Первое число: "))

do = input("Операция: ")

tooNum = int(input("Второе число: "))


#сложение

if do == "+":
	sum = firstNum + tooNum
	print("Ответ: " + str(float(sum)))
	
#вычитание

elif do == "-":
	if firstNum > tooNum:
		razn = firstNum - tooNum
		print(razn)
	else:
		razn = tooNum - firstNum
		print("Ответ: " + str(float(razn)))

#умножение

elif do == "*":
	umn = firstNum * tooNum
	print("Ответ: " + str(float(umn)))
	
#деление

elif do == "/":
	div = firstNum / tooNum
	print("Ответ: " + str(float(div)))
	
#возведение в степень

elif do == "**":
	step = firstNum ** tooNum
	print("Ответ: " + str(float(step)))
	
#извлечение квадратного корня

elif (firstNum == 0 and do =="√"):
	print(math.sqrt(tooNum))
