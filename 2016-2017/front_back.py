
def front_back(str):
	lengthstr = len(str) - 1
	front = str[:1]
	back = str[lengthstr:]
	if len(str) < 2:
		return str
	else:
		return back + str[1:lengthstr] + front

str = raw_input("Please Enter a string Tathagat: ")

print front_back(str)
