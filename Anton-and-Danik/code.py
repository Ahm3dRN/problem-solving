
def main(n, s):
	a = 0
	d = 0
	for letter in s:
		if letter == "A":
			a+=1
		elif letter == "D":
			d+=1
		else:
			pass
	return "Anton" if a > d else "Danik" if d > a else "Friendship"