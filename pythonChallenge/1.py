#url : http://www.pythonchallenge.com/pc/def/map.html
from string import maketrans
import string
def transletter01(s):
	ret = ""
	#ascii a-z:97-122
	for letter in s:
		if ord(letter)>=97 and ord(letter) <=122:
			ret += chr(97+(ord(letter)-95)%26)
		else:
			ret += letter
	return ret

def transletter02(s):
	transtab = maketrans(string.letters[0:26],string.letters[2:26]+string.letters[0:2])
	ret = s.translate(transtab)
	return ret

if __name__ == '__main__':
	s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
	print transletter01(s),'\n'
	print transletter02(s)
	#update url
	print transletter02('map')