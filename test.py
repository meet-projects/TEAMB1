
words=["ssd","dsds","aaina","sasasdd"]


e_word = raw_input("search for a word in the list 'words': ")
check = False
for word in words:
	if e_word in word or word in e_word:
		if check==False:
			check=True
			print "Results: "
		print " :" + word

if check==False:
	print "Sorry, no results found."


	
