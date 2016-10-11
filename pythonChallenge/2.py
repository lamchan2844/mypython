#-*-coding:utf-8-*-
#url： http://www.pythonchallenge.com/pc/def/ocr.html
def find_rare_characters(fn):
	mydict = dict()
	ret = ""
	file_input = open(fn,'r')
	for line in file_input.readlines():
		for letter in line:
			if letter not in mydict:
				mydict[letter] = 1
			else:
				mydict[letter] += 1
	#print
	file_input.close()
	file_input = open(fn,'r')
	for line in file_input.readlines():
		for letter in line:
			if mydict[letter]<=3:
				ret += letter
	file_input.close()
	return ret
if __name__ == '__main__':
	file_input_name = '2.txt'
	print find_rare_characters(file_input_name)