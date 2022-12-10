def getnumline(filename):
	""" THIS MODULE WILL HELP YOU TO COUNT TOTAL NUMBER OF LINE IN A FILE """
	with open(f'/storage/emulated/0/{filename}','r') as d:#you just have to replace the diractory name according to your device
		Counter = 0
		Content = d.read() 
		CoList = Content.split("\n") 
		for i in CoList: 
		    if i:
		    	Counter += 1
	return Counter#the total number of line
if __name__=="__main__":
#	gh=getnumline("trainBOOK.py")
	#print(gh)
#	print(getnumline.__doc__)