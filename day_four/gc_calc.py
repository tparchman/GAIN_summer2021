import sys
import re

IN = open(sys.argv[1], 'r')
OUT = open('gc_length_out.txt', 'w')

Nlist=[] # initializing Nlist
TotalC=0
TotalG=0
CumLength=0
LineNumber = 0  ## setting to 0 to count line numbers while looping through the file. 
CumLength = 0 # initializing cum length
for Line in IN:
	LineNumber += 1
	Line = Line.strip('\n')
	if re.search("^>", Line):# matches ID
		ID = Line
		OUT.write("%s, " %(ID))
	elif re.search("[ATCG]", Line):
		Ccount=Line.count('C')
		Gcount=Line.count('G')
		SeqLength=float(len(Line))
		GC=(Gcount + Ccount)/SeqLength
		print(TotalC, TotalG)
		OUT.write("Sequence length: %d, GC content: %.2f \n" %(SeqLength, GC))
		TotalC += Ccount
		TotalG += Gcount
		CumLength += SeqLength
		LineNumber += 1

print(TotalC, TotalG, CumLength)
TotalGC = (TotalC + TotalG)/CumLength



#print("Number of sequences: %d, Total GC fraction: %f" % (TotalGC,LineNumber)) 
