# Read wordlists
filename1=open("Words.txt","r")
Netgear1=filename1.read().splitlines()
filename2=open("Numbers.txt","r")
Netgear2=filename2.read().splitlines()
#Create the mix wordlist
Netgear3=open("Dictionary.txt","a")

#counters
x=0
a=0
loop=True

while loop:
	wordlist =Netgear1[x]+Netgear2[a]
	a+=1
	dictionary=Netgear3.write(wordlist+"\n")
	if wordlist==Netgear1[x]+Netgear2[999]:
		x+=1
		a=0
		pass
	pass


