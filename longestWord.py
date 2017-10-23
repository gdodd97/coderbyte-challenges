def LongestWord(sen):

	word =max(sen.split(), key = len)
	sen = word
	return sen

print LongestWord(raw_input())