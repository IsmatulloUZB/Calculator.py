print('[Kalkulyator]\nSalom,')
a = float(input("Birinchi sonni yozing: "))
amal = input("Qanday amal bajaramiz?(+;-;*;/): ")
b = float(input("Ikkinchi sonni yozing: "))
d = a % b
e = int(a) / int(b)
if amal == "+":
	c = a + b
	print(int(c))
elif amal == "-":
	c = a - b
	print(int(c))
elif amal == "*":
	c = a * b
	print(int(c))
elif amal == "/":
	c = a / b
	print(c)
	if d == 0:
		print()
	else:
	    print("  ", int(d), "\n", int(e), "─\n", " ", int(b))
else:
	print("noto'gri amal tanlandi")
input()
