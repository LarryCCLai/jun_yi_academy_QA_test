import os
def string_reverse(s):\
	return s[::-1]\

def word_reverse(s):
	length = len(s)
	i = 0
	while i < length:
		j = i + 1
		while j < length and s[j] !=' ':
			j+=1
		new = s[i:j][::-1]
		s = s.replace(s[i:j],new,1)
		i=j+1
	return s
	
if __name__ == '__main__':
	print('[Reverse string]')
	s = "junyiacademy is great"
	reverseS = string_reverse(s)
	print('Original string:', s)
	print('Result:',reverseS,'\n')
	
	print('[Reverse the words in a string]')
	s = "flipped class room is important"
	reverseS = word_reverse(s)
	print('Original string:', s)
	print('Result:',reverseS,'\n')

	