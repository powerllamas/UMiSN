curr = 0
while(curr <= 275):
	i = 0
	curr += 25
	newf = open('VOTE %3d .DAT' %(curr), 'w')
	for line in open('VOTE300.DAT', 'r'):
		i += 1
		newf.write(line)
		if(i%25 == 0 and i >= curr):
			newf.close()
			break